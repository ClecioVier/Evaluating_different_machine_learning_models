# Importando o load do joblib
import numpy
import pandas as pd
from joblib import load
import sklearn
import openpyxl

# Carregando o modelo que havíamos exportado
reg = load('/Users/USER/Desktop/Code/Projetos/Machine Learning/Deploy/Producao/Modelo/regressor.joblib')

# Importando a base
baseNova = pd.read_excel(
    '/Users/USER/Desktop/Code/Projetos/Machine Learning/Deploy/Producao/Entradas/dadosVenda_producao.xlsx')

# Tratando os valores vazios do Desconto
baseNova.loc[baseNova.Desconto.isnull(), 'Desconto'] = 0

# Separando X e y
X = baseNova[['PrecoOriginal', 'Desconto']]

# Fazendo essa previsão
y_pred = reg.predict(X)

# Podemos deixar com 1 única
y_pred = numpy.around(y_pred, 1)

# Podemos substituir essa previsão na base inicial
baseNova['VendaQtd'] = y_pred

# Exportando para o Excel
baseNova.to_excel('/Users/USER/Desktop/Code/Projetos/Machine Learning/Deploy/Producao/Saidas/resultado.xlsx',
                  index=False)
