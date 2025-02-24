Simulação de Sistema Massa-Mola com Método de Euler Explícito
Este script implementa o Método de Euler Explícito para simular o comportamento de um sistema massa-mola. O método de Euler é um método numérico simples para resolver equações diferenciais ordinárias (EDOs), e neste caso, é aplicado para modelar a dinâmica de um sistema massa-mola.

Descrição do Projeto
O sistema massa-mola é um dos sistemas físicos mais básicos e é descrito por uma equação diferencial de segunda ordem. Neste projeto, o método de Euler explícito é utilizado para resolver numericamente as equações do movimento, gerando gráficos de posição e velocidade em função do tempo, além de um gráfico de espaço de fase (posição vs. velocidade).

Equações do Sistema
As equações do sistema são:


dt/dx=v (velocidade)
dv/dt=−ω0**2x (aceleração, onde ω0**2 é a constante da mola)

O método de Euler explícito é aplicado para atualizar a posição e a velocidade a cada passo de tempo.

Como Executar o Projeto
Pré-requisitos
Python 3.x instalado.

Bibliotecas Python: numpy e matplotlib.