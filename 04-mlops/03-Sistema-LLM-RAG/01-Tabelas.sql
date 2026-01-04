-- Projeto 2 - MLOps da Concepção ao Deploy - Sistema de LLM/RAG
-- SQL - Criação do Banco de Dados

-- Deleta o schema se já existir
DROP SCHEMA IF EXISTS projeto2 CASCADE;

-- Cria o schema
CREATE SCHEMA projeto2 AUTHORIZATION priscila;

-- Cria as tabelas

CREATE TABLE projeto2.clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INTEGER NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefone VARCHAR(20) NOT NULL,
    cidade VARCHAR(100) NOT NULL
);


CREATE TABLE projeto2.produtos_eletronicos (
    id SERIAL PRIMARY KEY,
    produto VARCHAR(100) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    quantidade_em_estoque INTEGER NOT NULL,
    categoria VARCHAR(50) NOT NULL
);

CREATE TABLE projeto2.vendas (
    id_venda SERIAL PRIMARY KEY,
    id_cliente INTEGER NOT NULL REFERENCES projeto2.clientes(id),
    id_produto INTEGER NOT NULL REFERENCES projeto2.produtos_eletronicos(id),
    data_venda DATE NOT NULL,
    quantidade INTEGER NOT NULL,
    valor_total DECIMAL(10, 2) NOT NULL
);
