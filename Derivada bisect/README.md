# Método da Bissecção

Este projeto implementa o método da bissecção para encontrar raízes de uma função polinomial de segundo grau.

## Função Implementada

A função polinomial utilizada é:
\[
f(x) = ax^2 + bx + c
\]
Onde:
- \(a = 1\)
- \(b = -2\)
- \(c = -3\)

## Método da Bissecção

O método da bissecção encontra uma raiz de uma função contínua \(f(x)\) no intervalo \([a, b]\), onde \(f(a)\) e \(f(b)\) têm sinais opostos. O intervalo é dividido ao meio repetidamente até que a raiz seja encontrada com uma tolerância \(\epsilon\).

### Algoritmo

1. Verifique se \(f(a) \cdot f(b) < 0\).
2. Calcule o ponto médio \(x_{\text{med}} = \frac{a + b}{2}\).
3. Se \(f(x_{\text{med}}) \cdot f(a) \leq 0\), a raiz está no intervalo \([a, x_{\text{med}}]\).
4. Caso contrário, a raiz está no intervalo \([x_{\text{med}}, b]\).
5. Repita até que o intervalo seja menor que \(\epsilon\).

## Como Executar

1. **Requisitos**:
   - Python 3.x
   - Bibliotecas: `numpy`, `matplotlib`

2. **Instalação das Dependências**:
   ```bash
   pip install numpy matplotlib

3. **Execução**:

Execute o script bisseccao.py:

bash
Copy
python bisseccao.py
Resultados
Gráfico da Função: Mostra a função 
f(x)
f(x) e a raiz encontrada.

Intervalo da Raiz: O intervalo onde a raiz foi encontrada é exibido no terminal.

Autor
[Yasmin Rosa Selois de Moura]
[yasminselois2112@outlook.com]
[https://github.com/yasminrsdm-hub]

