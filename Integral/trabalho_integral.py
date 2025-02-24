# -*- coding: utf-8 -*-
"""Trabalho integral.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IfopDNUaSeeTmlmQ6TBdtEO0URV7zB_N
"""

import numpy as np

# Define a função que representa o integrando e^(-u)
def funcao_original(u):
    return np.exp(-u)

# Define a função que implementa o método do trapézio adaptativo
def trapezio_adaptativo(func, a, b, epsilon):
    integral_anterior = 0.0  # Inicializa a integral anterior como 0
    erro_anterior = float('inf')  # Inicializa o erro anterior como infinito
    n = 1  # Inicializa o número de subintervalos como 1

    while True:  # Loop para refinamento iterativo da integral
        h = (b - a) / n  # Calcula o tamanho de cada subintervalo (largura)
        x = np.linspace(a, b, n + 1)  # Gera pontos igualmente espaçados no intervalo
        y = func(x)  # Calcula os valores da função nos pontos x
        extremos = (y[0] + y[n]) / 2.0  # Calcula a média dos valores nos extremos dos subintervalos
        integral_atual = extremos * h  # Calcula a contribuição dos extremos para a integral

        for i in range(1, n):  # Loop para somar as contribuições do interior dos subintervalos
            integral_atual += y[i] * h

        erro = abs(integral_atual - integral_anterior) / 3.0  # Calcula o erro estimado

        if erro < epsilon or erro >= erro_anterior:  # Verifica se o erro é aceitável ou se está piorando
            return integral_atual, erro  # Retorna a integral aproximada e o erro estimado

        integral_anterior = integral_atual  # Atualiza a integral anterior
        erro_anterior = erro  # Atualiza o erro anterior
        n *= 2  # Dobra o número de subintervalos para a próxima iteração

# Define o parâmetro de erro desejado
epsilon = 1e-5

# Define um valor para "a"
a = 1.0

# Define um limite superior finito para a integração
limite_superior = 10

# Calcula a integral usando o método do trapézio adaptativo
integral_aproximada, erro_estimado = trapezio_adaptativo(funcao_original, 0, limite_superior, epsilon)

print("Integral Aproximada:", integral_aproximada)
print("Erro Estimado:", erro_estimado)