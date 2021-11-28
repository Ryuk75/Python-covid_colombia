# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 14:05:52 2021

@author: m1vhs
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

#1 Número de casos de Contagiados en el País.

num_pais = len(data)
print("Punto 1")
print(num_pais)
print()

#2 Número de Municipios Afectados

num_muni = len(data.groupby('Nombre municipio').size())
print("Punto 2")
print(num_muni)
print()

#3 Liste los municipios afectados (sin repetirlos)

list_muni = data.groupby('Nombre municipio').size().sort_values(ascending = False)
print("Punto 3")
print(list_muni)
print()