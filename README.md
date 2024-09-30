# JD MAP by Vessel

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

## Resultados
A aplicação fornece uma plataforma centralizada para gestão de pedidos e rastreamento de veículos de reboque. Os principais resultados incluem:
- Eficiência operacional, com rastreamento contínuo dos veículos de reboque e monitoramento da carga transportada, permitindo melhor planejamento e resposta rápida.
- Visibilidade em tempo real e gestão centralizada, melhorando a organização e comunicação interna.
- Alta escalabilidade do código, permitindo que a solução cresça conforme a demanda, suportando um número crescente de veículos e pedidos sem perda de desempenho.

Essa solução integrada melhora significativamente a logística interna da John Deere, proporcionando uma operação mais eficiente e transparente.
