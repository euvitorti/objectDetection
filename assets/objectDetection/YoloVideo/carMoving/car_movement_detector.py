import cv2

# Inicializa o vídeo (pode ser uma captura de câmera ou um arquivo de vídeo)
video = cv2.VideoCapture('../videos/carros.mp4')  # ajuste o caminho se necessário

if not video.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

# Captura o primeiro frame
ret, frame1 = video.read()
if not ret:
    print("Erro ao capturar o primeiro frame.")
    video.release()
    cv2.destroyAllWindows()
    exit()

# Converte o primeiro frame para escala de cinza
prev_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

# Define o nome da janela e o tamanho
window_name = 'Frame'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 800, 600)  # Ajuste o tamanho da janela conforme necessário

while True:
    # Captura o próximo frame
    ret, frame2 = video.read()
    if not ret:
        break

    # Converte o frame para escala de cinza
    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Calcula a diferença absoluta entre o frame atual e o anterior
    diff = cv2.absdiff(prev_gray, gray)

    # Aplica uma limiarização para obter uma imagem binária
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    # Encontra os contornos na imagem binária
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Se houver contornos, desenha caixas delimitadoras
    if contours:
        for contour in contours:
            # Desenha uma caixa delimitadora ao redor do contorno
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Atualiza o frame anterior
    prev_gray = gray

    # Redimensiona o frame para ajustar à janela
    frame_resized = cv2.resize(frame2, (800, 600))  # Ajuste o tamanho conforme necessário

    # Mostra o frame com caixas delimitadoras
    cv2.imshow(window_name, frame_resized)

    # Aguarda 10 ms e verifica se a tecla 'q' foi pressionada
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Libera o vídeo e fecha todas as janelas
video.release()
cv2.destroyAllWindows()
