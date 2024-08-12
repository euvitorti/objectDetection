import math
import cv2
import cvzone
from ultralytics import YOLO

# Initialize camera object
cap = cv2.VideoCapture("../videos/bike.mp4")

# Load YOLO model with specified weights
model = YOLO("../models/yolov8n.pt")

while True:
    success, img = cap.read()  # Capture a frame from the camera
    if not success:  # If frame is not captured successfully, skip the iteration
        continue

    results = model(img, stream=True)  # Perform object detection on the captured frame
    for r in results:
        boxes = r.boxes  # Get bounding boxes from the results
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]  # Extract coordinates of the bounding box

            # Convert coordinates to integers
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1  # Calculate width and height of the bounding box
            cvzone.cornerRect(img, (x1, y1, w, h))  # Draw a corner rectangle on the image

            conf = math.ceil((box.conf[0] * 100)) / 100  # Calculate confidence level and round it to two decimal places
            cls = int(box.cls[0])  # Get the class index of the detected object
            class_name = model.names[cls]  # Get the class name using the class index

            # Put text on the image with the class name and confidence level
            cvzone.putTextRect(img, f'{class_name} {conf}', (max(0, x1), max(35, y1)), scale=3, thickness=3)

    # Resize the image to make the window smaller
    img_resized = cv2.resize(img, (640, 480))

    cv2.imshow("Image", img_resized)  # Display the resized image
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Break the loop if 'q' key is pressed
        break

# Release the camera and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()


# import cv2
# import cvzone
# from ultralytics import YOLO
# import pyttsx3
# import time
# import threading
# import numpy as np
#
# # Inicializar motor de texto-para-fala
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)  # Ajustar a velocidade da fala se necessário
#
# # Função para falar o texto
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
#
# # Função para detectar a cor do semáforo
# def detect_traffic_light_color(roi):
#     hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
#
#     red_lower1 = np.array([0, 70, 50])
#     red_upper1 = np.array([10, 255, 255])
#     red_lower2 = np.array([170, 70, 50])
#     red_upper2 = np.array([180, 255, 255])
#
#     yellow_lower = np.array([20, 100, 100])
#     yellow_upper = np.array([30, 255, 255])
#
#     green_lower = np.array([40, 50, 50])
#     green_upper = np.array([90, 255, 255])
#
#     mask_red1 = cv2.inRange(hsv, red_lower1, red_upper1)
#     mask_red2 = cv2.inRange(hsv, red_lower2, red_upper2)
#     mask_red = cv2.add(mask_red1, mask_red2)
#
#     mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
#     mask_green = cv2.inRange(hsv, green_lower, green_upper)
#
#     red_count = cv2.countNonZero(mask_red)
#     yellow_count = cv2.countNonZero(mask_yellow)
#     green_count = cv2.countNonZero(mask_green)
#
#     if red_count > yellow_count and red_count > green_count:
#         return "vermelho"
#     elif yellow_count > red_count and yellow_count > green_count:
#         return "amarelo"
#     elif green_count > red_count and green_count > yellow_count:
#         return "verde"
#     else:
#         return "indefinido"
#
# # Initialize camera object
# cap = cv2.VideoCapture("videos/semaforo.mp4")
#
# # Carregar modelo YOLO com pesos especificados
# model = YOLO("../models/yolov8n.pt")
#
# # Dicionário para traduzir os nomes das classes para português
# class_translation = {
#     'person': 'pessoa',
#     'bicycle': 'bicicleta',
#     'car': 'carro',
#     'motorbike': 'moto',
#     'aeroplane': 'avião',
#     'bus': 'ônibus',
#     'train': 'trem',
#     'truck': 'caminhão',
#     'boat': 'barco',
#     'traffic light': 'semáforo',
#     'fire hydrant': 'hidrante',
#     'stop sign': 'placa de pare',
#     'parking meter': 'parquímetro',
#     'bench': 'banco',
#     'bird': 'pássaro',
#     'cat': 'gato',
#     'dog': 'cachorro',
#     'horse': 'cavalo',
#     'sheep': 'ovelha',
#     'cow': 'vaca',
#     'elephant': 'elefante',
#     'bear': 'urso',
#     'zebra': 'zebra',
#     'giraffe': 'girafa',
#     'backpack': 'mochila',
#     'umbrella': 'guarda-chuva',
#     'handbag': 'bolsa',
#     'tie': 'gravata',
#     'suitcase': 'mala',
#     'frisbee': 'frisbee',
#     'skis': 'esquis',
#     'snowboard': 'snowboard',
#     'sports ball': 'bola de esportes',
#     'kite': 'pipa',
#     'baseball bat': 'taco de beisebol',
#     'baseball glove': 'luva de beisebol',
#     'skateboard': 'skate',
#     'surfboard': 'prancha de surf',
#     'tennis racket': 'raquete de tênis',
#     'bottle': 'garrafa',
#     'wine glass': 'taça de vinho',
#     'cup': 'copo',
#     'fork': 'garfo',
#     'knife': 'faca',
#     'spoon': 'colher',
#     'bowl': 'tigela',
#     'banana': 'banana',
#     'apple': 'maçã',
#     'sandwich': 'sanduíche',
#     'orange': 'laranja',
#     'broccoli': 'brócolis',
#     'carrot': 'cenoura',
#     'hot dog': 'cachorro-quente',
#     'pizza': 'pizza',
#     'donut': 'rosquinha',
#     'cake': 'bolo',
#     'chair': 'cadeira',
#     'sofa': 'sofá',
#     'potted plant': 'planta em vaso',
#     'bed': 'cama',
#     'dining table': 'mesa de jantar',
#     'toilet': 'banheiro',
#     'TV': 'TV',
#     'laptop': 'laptop',
#     'mouse': 'mouse',
#     'remote': 'controle remoto',
#     'keyboard': 'teclado',
#     'cell phone': 'celular',
#     'microwave': 'microondas',
#     'oven': 'forno',
#     'toaster': 'torradeira',
#     'sink': 'pia',
#     'refrigerator': 'geladeira',
#     'book': 'livro',
#     'clock': 'relógio',
#     'vase': 'vaso',
#     'scissors': 'tesoura',
#     'teddy bear': 'ursinho de pelúcia',
#     'hair drier': 'secador de cabelo',
#     'toothbrush': 'escova de dentes'
# }
#
# # Lista de objetos relevantes para descrever
# relevant_objects = {
#     'person': 'pessoa',
#     'car': 'carro',
#     'motorbike': 'moto',
#     'bus': 'ônibus',
#     'train': 'trem',
#     'truck': 'caminhão',
#     'traffic light': 'semáforo',
#     'stop sign': 'placa de pare'
# }
#
# # Definir limite para objetos de curta distância
# # distance_threshold = 1  # Você pode ajustar esse valor conforme necessário
#
# # Inicializar tempo para controle de falas
# last_speech_time = time.time()
# speech_interval = 5  # intervalo de 5 segundos entre falas
#
# while cap.isOpened():
#     success, img = cap.read()  # Capturar um frame da câmera
#     if not success:  # Se o frame não for capturado com sucesso, pular a iteração
#         break
#
#     results = model(img)  # Realizar detecção de objetos no frame capturado
#     detected_objects = []  # Lista para armazenar as descrições dos objetos detectados
#
#     height, width, _ = img.shape  # Obter a altura e largura do frame
#
#     for r in results:
#         boxes = r.boxes  # Obter caixas delimitadoras dos resultados
#         for box in boxes:
#             x1, y1, x2, y2 = map(int, box.xyxy[0])  # Extrair e converter coordenadas para inteiros
#             w, h = x2 - x1, y2 - y1  # Calcular largura e altura da caixa delimitadora
#             area = w * h  # Área da caixa delimitadora para estimar a distância
#
#             # Estimar a distância com base na área
#             # if area > distance_threshold * (width * height):
#             # Se a área estiver acima do limiar, considerar o objeto como próximo
#             cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2)  # Desenhar um retângulo nos cantos da imagem
#
#             conf = round(float(box.conf[0]), 2)  # Calcular o nível de confiança e arredondar para duas casas decimais
#             cls = int(box.cls[0])  # Obter o índice da classe do objeto detectado
#             class_name = model.names[cls]  # Obter o nome da classe usando o índice da classe
#
#             # Verificar se o objeto é relevante
#             if class_name in relevant_objects:
#                 class_name_pt = class_translation.get(class_name, class_name)  # Traduzir o nome da classe para português
#
#                 # Descrever a posição do objeto com base em sua coordenada x
#                 if x1 < width // 3:
#                     position = "à esquerda"
#                 elif x2 > 2 * width // 3:
#                     position = "à direita"
#                 else:
#                     position = "à frente"
#
#                 # Adicionar a descrição do objeto e sua posição
#                 detected_objects.append(f'{class_name_pt} {position}')
#
#                 # Se o objeto detectado for um semáforo, detectar sua cor
#                 if class_name == 'traffic light':
#                     roi = img[y1:y2, x1:x2]  # Extrair a região de interesse (ROI) do semáforo
#                     traffic_light_color = detect_traffic_light_color(roi)  # Detectar a cor do semáforo
#                     detected_objects.append(f'semáforo {traffic_light_color} {position}')
#
#     # Converter a lista de objetos detectados em uma string
#     if detected_objects and (time.time() - last_speech_time > speech_interval):
#         objects_description = ', '.join(detected_objects)
#         # Executar a fala em um thread separado
#         speak_thread = threading.Thread(target=speak, args=(f'Há: {objects_description}',))
#         speak_thread.start()
#
#         last_speech_time = time.time()  # Atualizar o tempo da última fala
#
#     cv2.imshow("Imagem", img)  # Exibir a imagem
#     if cv2.waitKey(1) & 0xFF == ord('q'):  # Sair do loop se a tecla 'q' for pressionada
#         break
#
# # Liberar a câmera e destruir todas as janelas do OpenCV
# cap.release()
# cv2.destroyAllWindows()