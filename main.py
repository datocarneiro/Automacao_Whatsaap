import pyautogui
import time
import argparse
                                              # Automação  V0.0.1 
    # Configurar o parser de argumentos
parser = argparse.ArgumentParser(description='Exemplo de script com argumentos.')
parser.add_argument('--mensagem', type=str, help='Mensagem a ser enviada')
    # Obter os argumentos da linha de comando
args = parser.parse_args()

pyautogui.hotkey("win", "s")
time.sleep(1)
pyautogui.write("Whatsapp")
time.sleep(2) 
pyautogui.press("enter") 
time.sleep(3) 

def enviar_mensagem(usuario, mensagem):

    # Digitar na barra de pesquisa do software o nome do usuário
    pyautogui.write(usuario)
    time.sleep(1)
    
    # Clicar no resultado da pesquisa
    pyautogui.click(x=205, y=199)  # Ajuste as coordenadas (x, y) conforme necessário
    time.sleep(3)
    
    # Enviar mensagem para o contato específico
    pyautogui.write(mensagem)
    time.sleep(5)
    pyautogui.press("enter")
  
usuarios_alvo = ['ANOTAÇÕES FACULDADE', 'Anotações']
# usuarios_alvo2 =["Minha empresa"]
for usuario in usuarios_alvo:
    enviar_mensagem(usuario, args.mensagem)
    time.sleep(2) 
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(2) 
    print("Envidado para :"+usuario)

print("Todas as mensagens foram enviadas!")
'''
 python main3.py --mensagem "Tem video novo no canal! Se inscreva e não perca os cursos de Python e Javascrip. https://youtu.be/JM0x2xPll94?si=_HXqVRBj8QZ4OS-w "

'''