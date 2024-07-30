import time

last_speech_time = time.time()
speech_interval = 5  # Intervalo de 5 segundos entre falas

def should_speak():
    global last_speech_time
    if time.time() - last_speech_time > speech_interval:
        last_speech_time = time.time()
        return True
    return False
