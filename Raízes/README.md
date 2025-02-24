# Trabalho Raízes de Polinômios

Este repositório contém uma implementação de métodos numéricos para encontrar as raízes de polinômios e visualizar o comportamento desses polinômios.

## Descrição

O notebook implementa as seguintes funcionalidades:

1. **Cálculo de Polinômios e Derivadas**:
   - `polinomio(x, coeffs)`: Calcula o valor de um polinômio para um dado `x` e seus coeficientes.
   - `derivada(x, coeffs)`: Calcula a derivada do polinômio para um dado `x` e seus coeficientes.

2. **Método de Newton-Raphson**:
   - `metodo_newton(polinomio, derivada, x0, max_iter=100, tol=1e-6)`: Implementa o método de Newton-Raphson para encontrar uma raiz do polinômio.

3. **Encontrar Raízes**:
   - `encontrar_raizes(coefficients)`: Encontra todas as raízes reais e complexas de um polinômio dados seus coeficientes, utilizando `numpy.roots` e refinando as raízes com o método de Newton-Raphson.

4. **Entrada do Usuário**:
   - O usuário é solicitado a inserir o grau do polinômio e seus coeficientes.

5. **Cálculo das Raízes**:
   - As raízes do polinômio são calculadas e impressas.

6. **Visualização**:
   - O polinômio \( y = x^3 - 3x^2 + 4x - 2 \) é plotado no intervalo \([-2, 4]\) usando `matplotlib`.

## Exemplo de Saída

- O usuário insere um polinômio de grau 3 com coeficientes 1, -3, 4 e -2.
- As raízes encontradas são \(1 + i\), \(1 - i\) e aproximadamente 1.
- O polinômio é plotado, mostrando seu comportamento no intervalo especificado.

## Visualização

- O gráfico é criado usando `matplotlib` com uma cor rosa forte para a curva do polinômio.
- O título, rótulos e legenda são adicionados ao gráfico para maior clareza.

