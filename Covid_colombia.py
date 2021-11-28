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