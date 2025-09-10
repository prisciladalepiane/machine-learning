# Projeto 5 - Construção de Feature Store e Aplicação de Engenharia de Atributos 
# Módulo de Criação da Feature Store

# Imports
import numpy as np
import pandas as pd


# Criação dos dados aleatórios
n_samples = 100
n_features = 20
n_features_grupo1 = 2
n_features_grupo2 = 10
n_random = n_features - (n_features_grupo1 + n_features_grupo2)

# Gerar primeiro grupo de features
features_grupo1 = np.random.randn(n_samples, n_features_grupo1)

# Gerar segundo grupo de features (combinações lineares das informativas)
features_grupo2 = np.dot(features_grupo1, np.random.rand(n_features_grupo1, n_features_grupo2))

# Gerar features aleatórias
features_grupo3 = np.random.randn(n_samples, n_random)

# Combinar todos os tipos de features
X = np.hstack([features_grupo1, features_grupo2, features_grupo3])

# Gerar o vetor de target simulando uma classificação binária
y = (features_grupo1[:, 0] + features_grupo1[:, 1] > 0).astype(int)  

# Criar um DataFrame
df = pd.DataFrame(X, columns = [f'feature_{i}' for i in range(X.shape[1])])
df['target'] = y

print("DataFrame criado com sucesso!")
print(df.head())


