# Projeto Visão Guiada Em Desenvolvimento 👓
 
## Descrição do Projeto
Este projeto visa desenvolver um software que guie pessoas cegas utilizando técnicas de detecção de objetos. O software utiliza a YOLO (You Only Look Once) para a detecção de objetos em tempo real através da câmera, e então fornecerá orientações auditivas para ajudar os usuários a navegar com segurança em diferentes ambientes.

### Tecnologias Utilizadas 👨‍💻
- Python
- OpenCV
- YOLO
- cvzone

## Estrutura do Projeto
### Detecção de Objetos 🕵️‍♀️
A parte de detecção de objetos já está implementada. O código inicializa a câmera, carrega o modelo YOLO com modelos pré-treinados, e exibe os objetos detectados em tempo real:

## Implementação da Orientação
A próxima etapa é implementar a parte do software que guiará as pessoas cegas. Essa funcionalidade incluirá:
- Análise do Ambiente: Utilizar os dados da detecção de objetos para entender o ambiente ao redor.
- Geração de Instruções Auditivas: Criar mensagens de áudio que descrevam os objetos detectados e forneçam orientações sobre como navegar em torno deles.
- Integração com Hardware de Áudio: Implementar a funcionalidade para reproduzir as mensagens de áudio através de fones de ouvido ou outro dispositivo de saída de som.
