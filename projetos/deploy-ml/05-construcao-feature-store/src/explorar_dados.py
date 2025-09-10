# Projeto 5 - Construção de Feature Store e Aplicação de Engenharia de Atributos 
# Exploração e Visualização dos Dados

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_features = pd.read_csv('feature_store.csv')

def plot_histograms(df_features):
    # Histogrmas das Features
    num_features = len(df_features.columns) - 1  
    cols = 3  
    rows = (num_features + cols - 1) // cols  
    fig, axes = plt.subplots(nrows = rows, ncols = cols, figsize = (15, rows * 3))
    axes = axes.flatten()

    for i, col in enumerate(df_features.columns[:-1]):  

        sns.histplot(df_features[col], ax = axes[i], kde = True)
        axes[i].set_title(col)
        axes[i].set_ylabel('Count')


    for i in range(num_features, len(axes)):
        axes[i].set_visible(False)  

    plt.tight_layout()
    plt.show()

def plot_correlations(df_features):
    correlation_matrix = df_features.corr()
    plt.figure(figsize = (8, 6))
    sns.heatmap(correlation_matrix, annot = True, cmap = 'coolwarm')
    plt.title('Matriz Correlação')
    plt.show()

def analisa_dados(df_features):
    print("Primeiras linhas do DataFrame:")
    print(df_features.head())
    print("\nInformações do DataFrame:")
    print(df_features.info())
    print("\nEstatísticas descritivas:")
    print(df_features.describe())
    
    print("\nGráfico de Histogramas das Features:")
    plot_histograms(df_features)
    print("\nMatriz de Correlação:")
    plot_correlations(df_features)