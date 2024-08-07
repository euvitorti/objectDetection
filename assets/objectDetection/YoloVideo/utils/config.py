# utils/config.py

import cv2
from ultralytics import YOLO

# Inicializar a câmera e o modelo YOLO
# def initialize_camera_and_model(video_path, weights_path):
#     cap = cv2.VideoCapture(video_path)
#     model = YOLO(weights_path)
#     return cap, model

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

# Inicializar tempo para controle de falas
# speech_interval = 5  # intervalo de 5 segundos entre falas
