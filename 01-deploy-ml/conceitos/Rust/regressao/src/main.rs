// Construindo Um Modelo de Regressão com Linguagem Rust

// Imports
use linfa::traits::{Fit, Predict};
use linfa::dataset::DatasetBase;
use linfa_linear::LinearRegression;
use ndarray::array;

// Define uma função chamada `mean_squared_error` que calcula o erro quadrático médio (MSE).
// A função recebe duas referências a vetores de uma dimensão (Array1<f64>), `y_true` e `y_pred`, e retorna um valor `f64`.
fn mean_squared_error(y_true: &ndarray::Array1<f64>, y_pred: &ndarray::Array1<f64>) -> f64 {
    
    // Calcula a diferença entre os valores verdadeiros (`y_true`) e os valores preditos (`y_pred`).
    let diff = y_true - y_pred;
    
    // Aplica a função de mapeamento `mapv` a cada elemento do vetor `diff`, elevando-o ao quadrado.
    // Em seguida, calcula a média dos valores resultantes usando `mean()` e desempacota o valor com `unwrap()`.
    diff.mapv(|x| x.powi(2)).mean().unwrap()
}


fn main() {

    // Dados de entrada
    let x = array![[1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [4.0, 5.0]];

    // Dados de saída
    let y = array![3.0, 5.0, 7.0, 9.0];

    let dataset = DatasetBase::new(x.clone(), y.clone());

    let modelo = LinearRegression::default();

    // Treinando o modelo com os dados
    let modelo = modelo.fit(&dataset).expect("Erro ao treinar o modelo");

    // Testando o modelo com novos dados
    let x_test = array![[5.2, 6.1], [6.3, 7.4]];
    let y_test_real = array![11.0, 13.0];  // Valores reais para comparação
    let y_test_pred = modelo.predict(&x_test);

    // Arredondando as previsões
    let y_test_pred_rounded = y_test_pred.mapv(|x: f64| x.round());

    // Imprimindo os resultados
    println!("Previsões do Modelo: {:?}", y_test_pred_rounded);

    // Calculando o erro quadrático médio
    let mse = mean_squared_error(&y_test_real, &y_test_pred_rounded);
    println!("Erro Quadrático Médio (MSE): {}", mse);
}

// Execute: cargo run --quiet
// Execute: cargo build --quiet --release