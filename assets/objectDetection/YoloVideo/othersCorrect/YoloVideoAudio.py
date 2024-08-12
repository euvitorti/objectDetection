# CÓDIGO PRINCIPAL

threadingimport
import time

import cv2
import cvzone
import pyttsx3
from ultralytics import YOLO

# Inicializar motor de texto-para-fala
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Ajustar a velocidade da fala se necessário

# Função para falar o texto
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize camera object
cap = cv2.VideoCapture("videos/omg.mp4")

# Carregar modelo YOLO com pesos especificados
model = YOLO("../models/yolov8n.pt")

# Dicionário para traduzir os nomes das classes para português
class_translation = {
    'person': 'pessoa',
    'bicycle': 'bicicleta',
    'car': 'carro',
    'motorbike': 'moto',
    'aeroplane': 'avião',
    'bus': 'ônibus',
    'train': 'trem',
    'truck': 'caminhão',
    'boat': 'barco',
    'traffic light': 'semáforo',
    'fire hydrant': 'hidrante',
    'stop sign': 'placa de pare',
    'parking meter': 'parquímetro',
    'bench': 'banco',
    'bird': 'pássaro',
    'cat': 'gato',
    'dog': 'cachorro',
    'horse': 'cavalo',
    'sheep': 'ovelha',
    'cow': 'vaca',
    'elephant': 'elefante',
    'bear': 'urso',
    'zebra': 'zebra',
    'giraffe': 'girafa',
    'backpack': 'mochila',
    'umbrella': 'guarda-chuva',
    'handbag': 'bolsa',
    'tie': 'gravata',
    'suitcase': 'mala',
    'frisbee': 'frisbee',
    'skis': 'esquis',
    'snowboard': 'snowboard',
    'sports ball': 'bola de esportes',
    'kite': 'pipa',
    'baseball bat': 'taco de beisebol',
    'baseball glove': 'luva de beisebol',
    'skateboard': 'skate',
    'surfboard': 'prancha de surf',
    'tennis racket': 'raquete de tênis',
    'bottle': 'garrafa',
    'wine glass': 'taça de vinho',
    'cup': 'copo',
    'fork': 'garfo',
    'knife': 'faca',
    'spoon': 'colher',
    'bowl': 'tigela',
    'banana': 'banana',
    'apple': 'maçã',
    'sandwich': 'sanduíche',
    'orange': 'laranja',
    'broccoli': 'brócolis',
    'carrot': 'cenoura',
    'hot dog': 'cachorro-quente',
    'pizza': 'pizza',
    'donut': 'rosquinha',
    'cake': 'bolo',
    'chair': 'cadeira',
    'sofa': 'sofá',
    'potted plant': 'planta em vaso',
    'bed': 'cama',
    'dining table': 'mesa de jantar',
    'toilet': 'banheiro',
    'TV': 'TV',
    'laptop': 'laptop',
    'mouse': 'mouse',
    'remote': 'controle remoto',
    'keyboard': 'teclado',
    'cell phone': 'celular',
    'microwave': 'microondas',
    'oven': 'forno',
    'toaster': 'torradeira',
    'sink': 'pia',
    'refrigerator': 'geladeira',
    'book': 'livro',
    'clock': 'relógio',
    'vase': 'vaso',
    'scissors': 'tesoura',
    'teddy bear': 'ursinho de pelúcia',
    'hair drier': 'secador de cabelo',
    'toothbrush': 'escova de dentes'
}

# Lista de objetos relevantes para descrever
relevant_objects = {
    'person': 'pessoa',
    'car': 'carro',
    'motorbike': 'moto',
    'bus': 'ônibus',
    'train': 'trem',
    'truck': 'caminhão',
    'traffic light': 'semáforo',
    'stop sign': 'placa de pare'
}

# Definir limite para objetos de curta distância
distance_threshold = 1  # Você pode ajustar esse valor conforme necessário

# Inicializar tempo para controle de falas
last_speech_time = time.time()
speech_interval = 5  # intervalo de 5 segundos entre falas

while cap.isOpened():
    success, img = cap.read()  # Capturar um frame da câmera
    if not success:  # Se o frame não for capturado com sucesso, pular a iteração
        break

    results = model(img)  # Realizar detecção de objetos no frame capturado
    detected_objects = []  # Lista para armazenar as descrições dos objetos detectados

    height, width, _ = img.shape  # Obter a altura e largura do frame

    for r in results:
        boxes = r.boxes  # Obter caixas delimitadoras dos resultados
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Extrair e converter coordenadas para inteiros
            w, h = x2 - x1, y2 - y1  # Calcular largura e altura da caixa delimitadora
            area = w * h  # Área da caixa delimitadora para estimar a distância

            # Estimar a distância com base na área
            if area > distance_threshold * (width * height):
                # Se a área estiver acima do limiar, considerar o objeto como próximo
                cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2)  # Desenhar um retângulo nos cantos da imagem

                conf = round(float(box.conf[0]), 2)  # Calcular o nível de confiança e arredondar para duas casas decimais
                cls = int(box.cls[0])  # Obter o índice da classe do objeto detectado
                class_name = model.names[cls]  # Obter o nome da classe usando o índice da classe

                # Verificar se o objeto é relevante
                if class_name in relevant_objects:
                    class_name_pt = class_translation.get(class_name, class_name)  # Traduzir o nome da classe para português

                    # Descrever a posição do objeto com base em sua coordenada x
                    if x1 < width // 3:
                        position = "à esquerda"
                    elif x2 > 2 * width // 3:
                        position = "à direita"
                    else:
                        position = "à frente"

                    # Adicionar a descrição do objeto e sua posição
                    detected_objects.append(f'{class_name_pt} {position}')

    # Converter a lista de objetos detectados em uma string
    if detected_objects and (time.time() - last_speech_time > speech_interval):
        objects_description = ', '.join(detected_objects)
        # Executar a fala em um thread separado
        speak_thread = threading.Thread(target=speak, args=(f'Há: {objects_description}',))
        speak_thread.start()

        last_speech_time = time.time()  # Atualizar o tempo da última fala

    cv2.imshow("Imagem", img)  # Exibir a imagem
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Sair do loop se a tecla 'q' for pressionada
        break

# Liberar a câmera e destruir todas as janelas do OpenCV
cap.release()
cv2.destroyAllWindows()
