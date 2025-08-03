# Deploy do modelo de Machine Learning na Nuvem AWS 

import pickle
import pandas as pd
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

def carregar_arquivo(path):
    with open(path, 'rb') as file:
        return pickle.load(file)

#modelo = carregar_arquivo('modelo_final.pkl')
#scaler = carregar_arquivo('scaler_final.pkl')