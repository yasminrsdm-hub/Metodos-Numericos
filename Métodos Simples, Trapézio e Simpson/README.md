# Integração Numérica: Métodos Simples, Trapézio e Simpson

Este repositório contém implementações de métodos de integração numérica em Python, incluindo:

1. **Método Simples (Soma de Retângulos)**: Aproxima a integral usando a soma de áreas de retângulos.
2. **Método do Trapézio**: Aproxima a integral usando a soma de áreas de trapézios.
3. **Método de Simpson**: Aproxima a integral usando parábolas para maior precisão.

## Requisitos

- Python 3.x
- Bibliotecas: `numpy`, `matplotlib`

## Instalação

Para instalar as dependências, execute:

```bash
pip install numpy matplotlib
Uso
O código pode ser executado em um ambiente Jupyter Notebook ou como um script Python. Ele calcula a integral de funções de exemplo usando os três métodos e compara os resultados com os valores exatos.

Exemplos de Funções
func_1(x) = x^2

func_2(x) = sin(x)

func_3(x) = exp(-x)

Resultados
O código imprime os resultados das integrais calculadas pelos três métodos e compara com os valores exatos.