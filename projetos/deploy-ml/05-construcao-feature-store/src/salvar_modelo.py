# Projeto 5
# Salvar o Modelo e as Previsões

# Imports
import json
import pandas as pd
from joblib import dump

def salvar_modelo(model, model_path):

    dump(model, model_path)

def salvar_previsoes(predictions, y_test, predictions_path):

    predictions_df = pd.DataFrame({'ValorReal': y_test, 'ValorPrevisto': predictions})
    
    predictions_df.to_csv(predictions_path, index = False)

def salvar_info(run_info, run_info_path):

    with open(run_info_path, 'w') as f:
        
        json.dump(run_info, f)
