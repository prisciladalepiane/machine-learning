// Importações de bibliotecas
use linfa::prelude::*;
use linfa_logistic::LogisticRegression;
use ndarray::{Array1, Array2};
use rocket::{post, serde::json::Json, serde::Deserialize, serde::Serialize, routes};
use std::fs::{File, OpenOptions};
use std::io::{BufReader, BufWriter};
use bincode::{deserialize_from, serialize_into};
use csv::ReaderBuilder;


// Estruturas para requisição e resposta da API

// Deserialize: para desserializar dados JSON recebidos
#[derive(Deserialize)]
struct PredictRequest {
    features: Vec<f64>,
}
// Serialize: para serializar dados JSON de resposta
#[derive(Serialize)]
struct PredictResponse {
    class: usize,
}

fn carrega_csv(filename: &str) -> (Array2<f64>, Array1<usize>) {
 
    let mut rdr = ReaderBuilder::new() // Configura o leitor CSV
        .has_headers(true) // Indica que o CSV tem cabeçalho
        .delimiter(b',') // Define o delimitador como vírgula
        .from_path(filename) 
        .expect("Erro ao abrir o arquivo CSV");
    let mut features_vec = Vec::new();
    let mut targets_vec = Vec::new();

    for result in rdr.records() {
        let record = result.expect("Erro ao ler o registro");
        let mut row_features = Vec::new();

        for (i, field) in record.iter().enumerate() {
            if i == record.len() - 1 {
                // Última coluna é o alvo - converte para usize
                let target: usize = field.parse().expect("Erro ao converter alvo");
                targets_vec.push(target);
            } else {
                // Outras colunas são características (features) - converte para f64
                let feature: f64 = field.parse().expect("Erro ao converter característica");
                row_features.push(feature);
            }
        }
     features_vec.push(row_features);
    }

    let n_samples = targets_vec.len();
    let n_features = features_vec[0].len();
    let features = Array2::from_shape_vec(
        (n_samples, n_features),
        features_vec.into_iter().flatten().collect(),
    ).expect("Erro ao criar Array2 de características");
    let targets = Array1::from_vec(targets_vec);
    (features, targets)
}

fn treina_salva_modelo(){

    let (features, targets) = carrega_csv("dados.csv");

    let dataset = linfa::Dataset::new(features, targets);

    // Treina o modelo de regressão logística
    let fitted_model = LogisticRegression::default()
        .fit(&dataset)
        .expect("Erro ao treinar o modelo");

    // Cria o arquivo para salvar o modelo treinado
    let file = File::create("modelo.bin").expect("Erro ao criar o arquivo do modelo");
    let mut writer = BufWriter::new(file);

    serialize_into(&mut writer, &fitted_model).expect("Erro ao salvar o modelo");

}

fn carrega_modelo() ->  Result<linfa_logistic::FittedLogisticRegression<f64, usize>, String> {

    let file = OpenOptions::new()
        .read(true)
        .open("modelo.bin")
        .map_err(|e| format!("Erro ao abrir o arquivo do modelo: {}", e))?;

    let reader = BufReader::new(file);

    let fitted_model: linfa_logistic::FittedLogisticRegression<f64, usize> =
        deserialize_from(reader).map_err(|e| format!("Erro ao carregar o modelo: {}", e))?;

    Ok(fitted_model)

}

#[post("/predict", format = "json", data = "<input>")]
fn predict(input: Json<PredictRequest>) -> Result<Json<PredictResponse>, String> {
  
    // Tenta carregar o modelo treinado
    match carrega_modelo() {
        
        Ok(fitted_model) => {

            // Converte as características recebidas em um array 2D para a previsão
            let features_array: Array2<f64> = Array2::from_shape_vec((1, input.features.len()), input.features.clone()).unwrap();
            
            // Faz a previsão usando o modelo carregado
            let prediction = fitted_model.predict(&features_array);
            
            // Retorna a classe prevista como resposta em JSON
            Ok(Json(PredictResponse {
                class: prediction[0],
            }))
        },
        Err(e) => {
            // Em caso de erro ao carregar o modelo, exibe mensagem de erro
            eprintln!("Erro ao carregar o modelo: {}", e);
            panic!("Falha ao carregar o modelo!");
        }
    }
}

#[rocket::main]
async fn main() {
    treina_salva_modelo();

        rocket::build()

            // Define as rotas disponíveis na API
            .mount("/", routes![predict]) 
            .launch()
            .await

            // Inicia o servidor Rocket
            .unwrap(); 
}


