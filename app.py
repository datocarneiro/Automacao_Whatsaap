import pyautogui
import time

# Aqui está um exemplo simples de como você pode capturar a posição do mouse:
# Este código cria um loop infinito que imprime continuamente a posição do mouse 
# até que seja interrompido pelo usuário pressionando Ctrl+C.
try:
    while True:
        x, y = pyautogui.position()
        print(f'Posição do mouse: x={x} y={y}')
        time.sleep(3)
except KeyboardInterrupt:
    print('\nCaptura de posição do mouse encerrada.')