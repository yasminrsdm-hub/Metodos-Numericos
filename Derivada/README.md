# Trabalho de Cálculo de Derivadas

Este repositório contém um Jupyter Notebook que implementa métodos numéricos e simbólicos para o cálculo de derivadas de funções. O notebook é dividido em três partes principais:

1. **Implementação de Métodos Numéricos para Cálculo de Derivadas**:
   - Funções para construir matrizes e deltas usados no cálculo de derivadas.
   - Implementação do método de Newton-Raphson para calcular derivadas de qualquer ordem.

2. **Comparação com a Biblioteca SciPy**:
   - Comparação dos resultados obtidos com a implementação própria e a função `derivative` da biblioteca `scipy.misc`.

3. **Cálculo de Derivadas Simbólicas com SymPy**:
   - Uso da biblioteca `sympy` para calcular derivadas simbólicas de funções matemáticas.

## Descrição

### 1. Implementação de Métodos Numéricos

O notebook contém três funções principais:

- **`construir_matriz(n, h=0.001, impar=True)`**: Constrói uma matriz usada para cálculos de derivadas, dependendo se a derivada é par ou ímpar.
- **`construir_deltas(n, func, x0, h=0.001, par=True)`**: Calcula os deltas necessários para o cálculo das derivadas.
- **`calcular_derivada(orde, func, x0, n, h=0.001)`**: Calcula a derivada de uma função em um ponto específico, dada a ordem da derivada.

### 2. Comparação com SciPy

O código compara os resultados das derivadas calculadas pela implementação própria com os resultados obtidos usando a função `derivative` da biblioteca `scipy.misc`. A comparação é feita para a função \( f(x) = x^3 + x^2 - 3x + 2 \) no intervalo \([-2, 2]\).

### 3. Cálculo de Derivadas Simbólicas com SymPy

O notebook também utiliza a biblioteca `sympy` para calcular derivadas simbólicas de três funções:

- \( y = a \cdot x^n + b \)
- \( y = e^{-x} \cdot \cos(2x) \)
- \( y = x^3 + x^2 - 3x \)

