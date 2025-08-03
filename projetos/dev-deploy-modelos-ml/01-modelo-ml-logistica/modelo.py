# Imports
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# Dados de de produtos
dsa_dados = {
    'Peso_Embalagem_Gr': [212, 215, 890, 700, 230, 240, 730, 780, 218, 750, 202, 680],
    'Tipo_Embalagem': ['Caixa de Papelão', 'Caixa de Papelão', 'Plástico Bolha', 'Plástico Bolha', 'Caixa de Papelão', 'Caixa de Papelão', 'Plástico Bolha', 'Plástico Bolha', 'Caixa de Papelão', 'Plástico Bolha', 'Caixa de Papelão', 'Plástico Bolha'],
    'Tipo_Produto': ['Smartphone', 'Tablet', 'Tablet', 'Tablet', 'Smartphone', 'Smartphone', 'Tablet', 'Smartphone', 'Smartphone', 'Tablet', 'Smartphone', 'Tablet']  # Alterei o segundo e o oitavo rótulo
}


df = pd.DataFrame(dsa_dados)

# Separa X (entrada) e Y (saída)
X = df[['Peso_Embalagem_Gr', 'Tipo_Embalagem']]
y = df['Tipo_Produto']

# Divide os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)  

# Criado os codificadores para as variáveis categóricas
le_tipo_embalagem = LabelEncoder()
le_tipo_produto = LabelEncoder()

# Ajuste do codificador aos dados
le_tipo_embalagem.fit(X_train['Tipo_Embalagem'])
le_tipo_produto.fit(y_train)

# Aplica a transformação nos dados de treinamento e teste 
X_train['Tipo_Embalagem'] = le_tipo_embalagem.transform(X_train['Tipo_Embalagem'])
X_test['Tipo_Embalagem'] = le_tipo_embalagem.transform(X_test['Tipo_Embalagem'])
y_train = le_tipo_produto.transform(y_train)
y_test = le_tipo_produto.transform(y_test)

# Cria o modelo
modelo = DecisionTreeClassifier()

# Treina o modelo
modelo.fit(X_train, y_train)

# Faz previsão com o modelo
y_pred = modelo.predict(X_test)

# Calcula a acurácia
acc_modelo = accuracy_score(y_test, y_pred)

# Print
print(f"\nAcurácia: ", round(acc_modelo,2))

print("\nRelatório de Classificação:\n")

# Obtém o classification report
report = classification_report(y_test, y_pred)

# Imprimir o report
print(report)