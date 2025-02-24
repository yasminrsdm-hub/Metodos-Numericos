# Método do Trapézio Adaptativo

Este repositório contém uma implementação do método do trapézio adaptativo para calcular integrais numéricas em Python. O método do trapézio adaptativo ajusta o número de intervalos para garantir que o erro seja menor que uma tolerância especificada.

## Requisitos

- Python 3.x
- Bibliotecas: `numpy`, `matplotlib`

## Instalação

Para instalar as dependências, execute:

```bash
pip install numpy matplotlib
Uso
O código pode ser executado como um script Python. Ele calcula a integral de uma função usando o método do trapézio adaptativo e imprime o resultado, o erro estimado e o número de intervalos usados.

Exemplo
python
Copy
# Função polinomial de exemplo
def poly(x, a=0, b=1, c=0):
    return a * x**2 + b * x + c

# Cálculo da integral usando o método do trapézio adaptativo
integral, erro, N = trapezio_adaptativo(poly, 0, 1)
print(f"Integral: {integral}, Erro: {erro}, N: {N}")
Resultados
O código imprime o valor da integral, o erro estimado e o número de intervalos usados.