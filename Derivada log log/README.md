# Análise de Derivadas Numéricas

Este projeto tem como objetivo calcular e visualizar derivadas numéricas de funções trigonométricas (seno e cosseno) utilizando três métodos diferentes: derivada central, derivada adiantada e derivada atrasada. Além disso, o código calcula e plota os erros associados a cada método em função do passo `h`.

## Métodos de Derivada Numérica

1. **Derivada Central**: 
   \[
   f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}
   \]
   
2. **Derivada Adiantada**:
   \[
   f'(x) \approx \frac{f(x+h) - f(x)}{h}
   \]
   
3. **Derivada Atrasada**:
   \[
   f'(x) \approx \frac{f(x) - f(x-h)}{h}
   \]

## Funcionalidades do Código

- **Cálculo das Derivadas**: O código calcula as derivadas central, adiantada e atrasada para a função seno em um intervalo de ângulos de 0 a \(2\pi\).
- **Visualização Gráfica**: Plota as derivadas calculadas e as compara com a função cosseno (derivada analítica do seno).
- **Análise de Erros**: Calcula e plota os erros absolutos das derivadas central e adiantada em função do passo `h` usando um gráfico log-log.

## Como Executar o Código

1. **Requisitos**:
   - Python 3.x
   - Bibliotecas: `numpy`, `matplotlib`

2. **Instalação das Dependências**:
   ```bash
   pip install numpy matplotlib

Explicação do Código
O código está dividido em várias células, cada uma com uma funcionalidade específica:

Importação de Bibliotecas: Importa numpy para cálculos numéricos e matplotlib para visualização gráfica.

Função derivada: Implementa os três métodos de derivada numérica.

Cálculo das Derivadas: Calcula as derivadas da função seno em um intervalo de ângulos.

Visualização Gráfica: Plota as derivadas calculadas e as compara com a função cosseno.

Análise de Erros: Calcula e plota os erros das derivadas central e adiantada em função do passo h.

Resultados
Gráfico das Derivadas: Mostra a comparação entre as derivadas numéricas e a derivada analítica (cosseno).

Gráfico de Erros: Mostra como os erros das derivadas central e adiantada variam com o passo h.

Melhorias Sugeridas
Documentação: Adicione comentários no código para explicar cada passo.

Função de Erro: Melhore a função de cálculo de erro para evitar divisão por zero.

Testes: Adicione testes para verificar a precisão dos métodos de derivada.

Interatividade: Transforme o código em uma função interativa onde o usuário pode escolher a função e o passo h.

Autor
[Yasmin Rosa Selois de Moura]
[yasminselois2112@outlook.com]
[https://github.com/yasminrsdm-hub]