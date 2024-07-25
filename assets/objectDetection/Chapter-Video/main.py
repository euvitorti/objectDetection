# main.py

from colorDetection.color_detection import detect_traffic_light_color, describe_traffic_light_color
from textToSpeech.text_to_speech import speak

import cv2
import cvzone
from ultralytics import YOLO
import time
import threading

# Inicializar a câmera e o modelo YOLO
cap = cv2.VideoCapture("videos/semaforo.mp4")
model = YOLO("../Yolo-Weights/yolov8n.pt")

# Dicionário para traduzir os nomes das classes para português
class_translation = {
    # (Dicionário omitido para brevidade)
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

# Variável para armazenar o estado anterior do semáforo
last_traffic_light_color = None
last_speech_time = time.time()
speech_interval = 5  # intervalo de 5 segundos entre falas

while cap.isOpened():
    success, img = cap.read()  # Capturar um frame da câmera
    if not success:
        break

    results = model(img)  # Realizar detecção de objetos no frame capturado
    detected_objects = []  # Lista para armazenar as descrições dos objetos detectados

    height, width, _ = img.shape  # Obter a altura e largura do frame

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Extrair e converter coordenadas para inteiros
            w, h = x2 - x1, y2 - y1
            area = w * h

            cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2)  # Desenhar um retângulo nos cantos da imagem

            conf = round(float(box.conf[0]), 2)  # Calcular o nível de confiança e arredondar para duas casas decimais
            cls = int(box.cls[0])  # Obter o índice da classe do objeto detectado
            class_name = model.names[cls]  # Obter o nome da classe usando o índice da classe

            if class_name in relevant_objects:
                class_name_pt = class_translation.get(class_name, class_name)  # Traduzir o nome da classe para português

                if x1 < width // 3:
                    position = "à esquerda"
                elif x2 > 2 * width // 3:
                    position = "à direita"
                else:
                    position = "à frente"

                detected_objects.append(f'{class_name_pt} {position}')

                if class_name == 'traffic light':
                    roi = img[y1:y2, x1:x2]  # Extrair a região de interesse (ROI) do semáforo
                    traffic_light_color = detect_traffic_light_color(roi)  # Detectar a cor do semáforo

                    # Descreve a cor do semáforo e a posição
                    description = describe_traffic_light_color(traffic_light_color, position)

                    # Atualiza a fala apenas se a cor do semáforo mudou
                    if traffic_light_color != last_traffic_light_color:
                        if traffic_light_color == 'verde':
                            message = 'Semáforo com sinal verde.'
                        elif traffic_light_color == 'vermelho':
                            message = 'Semáforo com sinal vermelho.'
                        else:
                            message = description

                        if time.time() - last_speech_time > speech_interval:
                            speak_thread = threading.Thread(target=speak, args=(message,))
                            speak_thread.start()
                            last_speech_time = time.time()

                        last_traffic_light_color = traffic_light_color

    cv2.imshow("Imagem", img)  # Exibir a imagem
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
