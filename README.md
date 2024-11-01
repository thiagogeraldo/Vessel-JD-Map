# JD MAP by Vessel
[JD_UBER_Compressed 1.pdf](https://github.com/user-attachments/files/17198326/JD_UBER_Compressed.1.pdf)

## Introdução
A John Deere enfrenta desafios na gestão da logística interna, especialmente no transporte de peças e materiais entre diferentes setores da fábrica. A falta de visibilidade em tempo real sobre a localização dos veículos de reboque e o status dos pedidos pode levar a atrasos, ineficiências e aumento de custos operacionais. Este projeto visa desenvolver uma solução integrada para melhorar a eficiência logística, fornecendo rastreamento em tempo real dos veículos de reboque e uma plataforma centralizada para gestão de pedidos e monitoramento da carga transportada.

## Desenvolvimento
A arquitetura do projeto inclui:
- Uma interface web para login, gestão de pedidos e visualização de mapas.
- Um servidor Flask para gerenciar autenticação, processamento de dados e comunicação em tempo real.
- Futuramente, um banco de dados para armazenamento de informações de usuários.
- Dispositivos ESP32 para rastreamento de veículos de reboque e medição de carga, com comunicação em tempo real via Flask-SocketIO.

O frontend rodará nos navegadores dos usuários, acessível via rede interna da John Deere, enquanto o backend será hospedado em um servidor local ou na nuvem, disponível temporariamente em https://thiag0.pythonanywhere.com. Os dispositivos ESP32 serão instalados nos veículos de reboque, comunicando-se com o servidor via Wi-Fi.

Os usuários farão login para acessar a plataforma, onde poderão criar e gerenciar pedidos de peças e materiais. A localização dos veículos de reboque será atualizada em tempo real no mapa, permitindo melhor planejamento e resposta rápida a mudanças. Os dispositivos ESP32 medirão a carga transportada pelos veículos de reboque e atualizarão essa informação em tempo real no sistema, com informações sobre o status dos pedidos, localização dos veículos e carga transportada.

As tecnologias envolvidas incluem:
- Python com Flask para o backend.
- Jinja2 para templates HTML.
- Flask-SocketIO para comunicação em tempo real do ESP32 com o site.
- Leaflet para mapas interativos.
- Algoritmo A* para encontrar rotas otimizadas dentro da fábrica.
- Estrutura de dados Grid para representar o mapa da fábrica.
- ESP32 para rastreamento de veículos e medição de carga, utilizando triangulação para calcular a posição com base em sinais Wi-Fi e células de carga para medir o peso transportado.

Os dispositivos ESP32 instalados nos veículos de reboque utilizam sinais Wi-Fi para calcular a posição dos veículos dentro da fábrica, com triangulação baseada na intensidade do sinal (RSSI) de vários pontos de acesso. Além disso, os ESP32 estão equipados com células de carga que medem o peso dos itens transportados. Essas informações são enviadas para o servidor, que atualiza a posição dos veículos no mapa e os ícones de carga em tempo real.
![Diagrama sem nome drawio](https://github.com/user-attachments/assets/cc61332e-639a-41ca-a056-0c9572591048)


## Resultados
A aplicação fornece uma plataforma centralizada para gestão de pedidos e rastreamento de veículos de reboque. Os principais resultados incluem:
- Eficiência operacional, com rastreamento contínuo dos veículos de reboque e monitoramento da carga transportada, permitindo melhor planejamento e resposta rápida.
- Visibilidade em tempo real e gestão centralizada, melhorando a organização e comunicação interna.
- Alta escalabilidade do código, permitindo que a solução cresça conforme a demanda, suportando um número crescente de veículos e pedidos sem perda de desempenho.

Essa solução integrada melhora significativamente a logística interna da John Deere, proporcionando uma operação mais eficiente e transparente.

## Testes de Desempenho

### Definição da Ferramenta de Teste
Para realizar os testes de desempenho, utilizamos uma combinação de dispositivos e navegadores, especificamente:
- **Dispositivos:** Celular e notebook.
- **Navegadores:** Firefox e Chrome.
- **Ferramentas de Medição:** Um cronômetro foi utilizado para medir o tempo de resposta com precisão.

**Objetivo:** Avaliar a eficiência do site em termos de tempo de resposta e capacidade de suportar múltiplos dispositivos simultaneamente.

### Evidências de Testes
Os testes foram realizados sob duas condições distintas:
1. **IP Local:**
   - **Procedimento:** Acessamos o site hospedado localmente utilizando o IP da rede interna.
   - **Resultados:** O tempo de resposta foi praticamente instantâneo para todas as operações, incluindo login e navegação entre páginas.

2. **Site Hospedado Gratuitamente:**
   - **Procedimento:** Acessamos o site hospedado em um servidor gratuito, temporariamente disponível em https://thiag0.pythonanywhere.com.
   - **Resultados:** 
     - **Login:** Tempo de resposta variou em média 15 segundos, chegando até em 22 segundos.
     - **Navegação:** Tempo de resposta após o login também variou significativamente, impactando a experiência do usuário.

3. **Teste de Multi-Dispositivos:**
   - **Procedimento:** Dois usuários acessaram e interagiram com o sistema simultaneamente em diferentes dispositivos (um no celular e outro no notebook).
   - **Resultados:** A interação foi bem-sucedida sem quaisquer problemas de desempenho, demonstrando a capacidade do sistema de suportar múltiplos dispositivos simultâneos.

https://github.com/user-attachments/assets/6d3542a8-fe4e-4cb1-834e-7cb928ac0a96
[Testes.pptx](https://github.com/user-attachments/files/17603375/Testes.pptx)


### Discussão dos Resultados
Os resultados indicam uma clara diferença de desempenho entre o site hospedado localmente e o hospedado gratuitamente:
- **Desempenho Local:** Excelente, com tempos de resposta instantâneos, proporcionando uma experiência de usuário fluida e eficiente.
- **Desempenho Hospedado Gratuitamente:** Significativamente inferior, com tempos de resposta de até 22 segundos, o que pode afetar negativamente a usabilidade do site.

O teste de multi-dispositivos foi bem-sucedido, demonstrando que o sistema pode suportar múltiplos usuários interagindo simultaneamente sem degradação de desempenho, o que é um ponto positivo para a escalabilidade futura do projeto.

### Soluções Futuras
Para melhorar o desempenho do site e reduzir os tempos de resposta, as seguintes ações serão consideradas para garantir que o site ofereça uma experiência de usuário mais rápida e eficiente, mesmo sob carga de múltiplos usuários e dispositivos:
- **Migrar para um servidor pago:** Servidores pagos oferecem melhor desempenho e tempos de resposta mais rápidos em comparação com hospedagem gratuita.
- **Otimização do Código Backend:** Melhorar a eficiência do processamento de dados no servidor Flask para reduzir tempos de resposta.
- **Implementação de Cache:** Utilizar técnicas de cache para armazenar dados frequentemente acessados, reduzindo o tempo de carregamento de páginas e recursos.
- **Uso de Banco de Dados:** Implementar um banco de dados adequado para a organização e acesso eficiente das informações pode melhorar significativamente o desempenho em aplicações com grande volume de dados.
