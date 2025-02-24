# Método de Newton-Raphson

Este projeto implementa o método de Newton-Raphson para encontrar raízes de uma função polinomial de segundo grau.

## Função Implementada

A função polinomial utilizada é:
\[
f(x) = ax^2 + bx + c
\]
Onde:
- \(a = 1\)
- \(b = -2\)
- \(c = -3\)

## Método de Newton-Raphson

O método de Newton-Raphson é um método iterativo para encontrar raízes de uma função. Ele usa a derivada da função para aproximar a raiz.

### Algoritmo

1. Escolha um valor inicial \(x_0\).
2. Calcule a próxima aproximação:
   \[
   x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
   \]
3. Repita até que a diferença entre \(x_{n+1}\) e \(x_n\) seja menor que \(\epsilon\).

## Como Executar

1. **Requisitos**:
   - Python 3.x
   - Bibliotecas: `numpy`, `matplotlib`

2. **Instalação das Dependências**:
   ```bash
   pip install numpy matplotlib
Execução:

Execute o script newton_raphson.py:

bash
Copy
python newton_raphson.py
Resultados
Gráfico da Função: Mostra a função f(x)
f(x) e a raiz encontrada.

Raiz Encontrada: A raiz é exibida no terminal.

Autor
[Yasmin Rosa Selois de Moura]
[yasminselois2112@outlook.com]
[https://github.com/yasminrsdm-hub]