# Projeto 2 - MLOps da Concepção ao Deploy - Sistema de LLM/RAG
# Python - Pipeline de Extração de Análises com LLM

# Imports
import csv
import psycopg2
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama

# Instanciação do LLM através do Ollama
llm = Ollama(model = "llama3.1")

# Criação do parser para a saída do modelo de linguagem
output_parser = StrOutputParser()

# Função para gerar texto baseado nos dados do PostgreSQL
def gera_analises():

    # Conecta ao banco de dados PostgreSQL com as credenciais fornecidas
    conn = psycopg2.connect(
        dbname="pridb",
        user="priscila",
        password="pri1010",
        host="localhost",
        port="5222"
    )

    # Cria um cursor para executar comandos SQL
    cursor = conn.cursor()
    
    # Define a consulta SQL 
    query = """
        SELECT
            c.nome AS nome_cliente,
            CASE 
                WHEN c.idade BETWEEN 0 AND 18 THEN '0-18'
                WHEN c.idade BETWEEN 19 AND 25 THEN '19-25'
                WHEN c.idade BETWEEN 26 AND 35 THEN '26-35'
                WHEN c.idade BETWEEN 36 AND 45 THEN '36-45'
                WHEN c.idade BETWEEN 46 AND 55 THEN '46-55'
                WHEN c.idade > 55 THEN '55+'
            END AS faixa_etaria,
            c.cidade AS cidade_cliente,
            p.produto AS nome_produto,
            p.marca AS marca_produto,
            p.categoria AS categoria_produto,
            SUM(v.valor_total) AS total_venda,
            SUM(v.quantidade) AS total_quantidade_vendida
        FROM
            projeto2.vendas v
        JOIN
            projeto2.clientes c ON v.id_cliente = c.id
        JOIN
            projeto2.produtos_eletronicos p ON v.id_produto = p.id
        GROUP BY
            c.nome, faixa_etaria, c.cidade, p.produto, p.marca, p.categoria
        HAVING
            SUM(v.valor_total) > 2000
        ORDER BY
            c.nome;
    """
    
    # Executa a consulta SQL
    cursor.execute(query)

    # Obtém todos os resultados da consulta
    rows = cursor.fetchall()
    
    # Inicializa uma lista para armazenar os analises
    analises = []

    # Criação do template de prompt 
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Você é um analista especializado. Analise os dados e forneça feedback em português do Brasil sobre os padrões de vendas dos produtos."),
            ("user", "question: {question}")
        ]
    )

    # Definição da cadeia de execução: prompt -> LLM -> output_parser
    chain = prompt | llm | output_parser

    # Itera sobre as linhas de resultados
    for row in rows:
        
        # Desempacota os valores de cada linha
        nome_cliente, faixa_etaria, cidade_cliente, nome_produto, marca_produto, categoria_produto, total_venda, total_quantidade_vendida = row
        
        # Cria o prompt para o LLM com base nos dados 
        consulta = f"Nome do Cliente {nome_cliente} Faixa Etária do Cliente {faixa_etaria} Cidade do Cliente {cidade_cliente} Nome do Produto {nome_produto} Marca do Produto {marca_produto} Categoria do Produto {categoria_produto} Total de Venda ${total_venda:.2f} Quantidade Vendida {total_quantidade_vendida}."
        
        # Gera o texto de análise usando o LLM
        response = chain.invoke({'question': consulta})
        
        # Adiciona o texto gerado à lista de analises
        analises.append(response)
    
    # Fecha a conexão com o banco de dados
    conn.close()

    # Salva as análises em um arquivo CSV
    with open('analise.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Análise"])
        for analise in analises:
            writer.writerow([analise])

    # Retorna a lista de análises
    return analises

# Gera análises chamando a função definida
analises = gera_analises()

# Imprime cada insight gerado
for analise in analises:
    print(analise)





