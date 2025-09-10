import os
import json
import time
import cria_feature_store
import explorar_dados
import treinar_modelo
import salvar_modelo

if __name__ == "__main__":
    print("\nIniciando a execução do pipeline...\n")

    time.sleep(2)

    os.makedirs('feature_store', exist_ok = True)
    os.makedirs('pipeline_runs', exist_ok = True)

    feature_df = cria_feature_store.criar_feature_store()

    feature_path = os.path.join('feature_store', 'feature_store.csv')
    feature_df.to_csv(feature_path, index = False)

    time.sleep(2)

    explorar_dados.analisa_dados(feature_df)

    model, X_test, y_test, predictions, accuracy, class_report = treinar_modelo.treina_avalia_modelo(feature_df)

    model_path = os.path.join('pipeline_runs', 'random_forest_model.joblib')

    predictions_path = os.path.join('pipeline_runs', 'predictions.csv')

    salvar_modelo.salvar_modelo(model, model_path)
    salvar_modelo.salvar_previsoes(predictions, y_test, predictions_path)

    pipeline_info = {
        'tipo_modelo': 'RandomForestClassifier',
        'caminho_modelo': model_path,
        'caminho_feature_store': feature_path,
        'caminho_previsoes': predictions_path,
        'acuracia': accuracy
    }

    salvar_modelo.salvar_info(pipeline_info, os.path.join('pipeline_runs', 'run_info.json'))

    print("\nAcurácia do modelo: {:.2f}".format(accuracy))
    print("\nRelatório de Classificação:\n", class_report)

    print("\nResumo da execução do pipeline salvo em 'pipeline_runs/run_info.json':\n")
    print(json.dumps(pipeline_info, indent = 4))

    print("\nExecução do pipeline concluída.\n")
