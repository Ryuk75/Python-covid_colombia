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

data['Sexo'].replace('f','F',inplace=True)
data['Sexo'].replace('m','M',inplace=True)
data['Estado'].replace('leve','Leve',inplace=True)
data['Estado'].replace('LEVE','Leve',inplace=True)

#1 Número de casos de Contagiados en el País.
num_pais = len(data)
print("Punto 1")
print(num_pais)
print()

#2 Número de Municipios Afectados
data['Nombre municipio'].replace('puerto colombia','PUERTO COLOMBIA',inplace=True)
data['Nombre municipio'].replace('puerto COLOMBIA','PUERTO COLOMBIA',inplace=True)
data['Nombre municipio'].replace('MEDELLiN','MEDELLIN',inplace=True)
data['Nombre municipio'].replace('Galapa','GALAPA',inplace=True)
data['Nombre municipio'].replace('momil','MOMIL',inplace=True)
data['Nombre municipio'].replace('Guepsa','GUEPSA',inplace=True)
data['Nombre municipio'].replace('barrancabermeja','BARRANCABERMEJA',inplace=True)
data['Nombre municipio'].replace('Pensilvania','PENSILVANIA',inplace=True)
data['Nombre municipio'].replace('Anserma','ANSERMA',inplace=True)
num_muni = len(data.groupby('Nombre municipio').size())
print("Punto 2")
print(num_muni)
print()

#3 Liste los municipios afectados (sin repetirlos)
list_muni = data.groupby('Nombre municipio').size().sort_values(ascending = False)
print("Punto 3")
print(list_muni)
print()

#4 Número de personas que se encuentran en atención en casa
data['Ubicación del caso'].replace('casa','Casa',inplace=True)
data['Ubicación del caso'].replace('CASA','Casa',inplace=True)
num_encasa = len(data[data['Ubicación del caso'] == 'Casa'])
print("Punto 4")
print(num_encasa)
print()

#5 Número de personas que se encuentran recuperados
data['Recuperado'].replace('fallecido','Fallecido',inplace=True)
num_recu = len(data[data['Recuperado'] == 'Recuperado'])
print("Punto 5")
print(num_recu)
print()

#6 Número de personas que ha fallecido
num_fall = len(data[data['Ubicación del caso'] == 'Fallecido'])
print("Punto 6")
print(num_fall)
print()

#7 Ordenar de Mayor a menor por tipo de caso (Importado, en estudio, Relacionado)
tipoContagio = data.groupby('Tipo de contagio').size().sort_values(ascending = False)
print("Punto 7")
print(tipoContagio)
print()

#8 Número de departamentos afectados
data['Nombre departamento'].replace('Tolima','TOLIMA',inplace=True)
data['Nombre departamento'].replace('Caldas','CALDAS',inplace=True)
num_dept = len(data.groupby('Nombre departamento').size().sort_values(ascending = False))
print("Punto 8")
print(num_dept)
print()

#9 Liste los departamentos afectados(sin repetirlos)
list_dept= data.groupby('Nombre departamento').size().sort_values(ascending = False)
print("Punto 9")
print(list_dept)
print()

#10 Ordene de mayor a menor por tipo de atención
tipoAtencion = data.groupby('Ubicación del caso').size().sort_values(ascending = False)
print("Punto 10")
print(tipoAtencion)
print()

#11 Liste de mayor a menor los 10 departamentos con mas casos de contagiados
topDeptCo = data.groupby('Nombre departamento').size().sort_values(ascending = False).head(10)
print("Punto 11")
print(topDeptCo)
print()

#12 Liste de mayor a menor los 10 departamentos con mas casos de fallecidos
topDeptFa = data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre departamento').size().sort_values(ascending = False).head(10)
print("Punto 12")
print(topDeptFa)
print()

#13 Liste de mayor a menor los 10 departamentos con mas casos de recuperados
topDeptRe = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending = False).head(10)
print("Punto 13")
print(topDeptRe)
print()

#14 Liste de mayor a menor los 10 municipios con mas casos de contagiados
topMunCo = data.groupby('Nombre municipio').size().sort_values(ascending = False).head(10)
print("Punto 14")
print(topMunCo)
print()

#15 Liste de mayor a menor los 10 municipios con mas casos de fallecidos
topMunFa = data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre municipio').size().sort_values(ascending = False).head(10)
print("Punto 15")
print(topMunFa)
print()

#16 Liste de mayor a menor los 10 municipios con mas casos de recuperados
topMunRe = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending = False).head(10)
print("Punto 16")
print(topMunRe)
print()

#17 Liste agrupado por departamento y en orden de Mayor a menor las ciudades con mas casos de contagiados
ciudadesCont = data.groupby(['Nombre departamento','Nombre municipio']).size().sort_values(ascending = False)
print("Punto 17")
print(ciudadesCont)
print()

#18 Número de Mujeres y hombres contagiados por ciudad por departamento
genCiudad = data.groupby(['Nombre departamento','Nombre municipio','Sexo']).size()
print("Punto 18")
print(genCiudad)
print()

#19 Liste el promedio de edad de contagiados por hombre y mujeres por ciudad por departamento
promCiudad = data.groupby(['Nombre departamento','Nombre municipio','Sexo']).Edad.mean()
print("Punto 19")
print(promCiudad)
print()

#20 Liste de mayor a menor el número de contagiados por país de procedencia
data['Nombre del país'].replace('ESTADOS UNIDOS','ESTADOS UNIDOS DE AMÉRICA',inplace=True)
data['Nombre del país'].replace('VENEUELA','VENEZUELA',inplace=True)
data['Nombre del país'].replace('MEXICO','MÉXICO',inplace=True)
paisProc = data.groupby('Nombre del país').size().sort_values(ascending = False)
print("Punto 20")
print(paisProc)
print()

#21 Liste de mayor a menor las fechas donde se presentaron mas contagios
fechaContagios = data.groupby('Fecha de diagnóstico').size().sort_values(ascending = False)
print("Punto 21")
print(fechaContagios)
print()

#22 Diga cual es la tasa de mortalidad y recuperación que tiene toda Colombia
tasaMor = (len(data[data['Ubicación del caso'] == 'Fallecido']) / len(data)) * 100
tasaRec = (len(data[data['Recuperado'] == 'Recuperado']) / len(data)) * 100
print("Punto 22")
print(tasaMor)
print(tasaRec)
print()

#23 Liste la tasa de mortalidad y recuperación que tiene cada departamento
tasaMorDept = (data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre departamento').size().sort_values(ascending = False) / data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre departamento').size().sort_values(ascending = False).sum()) * 100
tasaRecDept = (data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending = False) / data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending = False).sum()) * 100
print("Punto 23")
print(tasaMorDept)
print(tasaRecDept)
print()

#24 Liste la tasa de mortalidad y recuperación que tiene cada ciudad
tasaMorCiu = (data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre municipio').size().sort_values(ascending = False) / data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre municipio').size().sort_values(ascending = False).sum()) * 100
tasaRecCiu = (data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending = False) / data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending = False).sum()) * 100
print("Punto 24")
print(tasaMorCiu)
print(tasaRecCiu)
print()