# Documentação para Automatização de Mensagens no WhatsApp
Este é um script simples escrito em Python usando a biblioteca tkinter para criar uma interface gráfica e a biblioteca pyautogui para automatizar o envio de mensagens em lote para grupos de WhatsApp. O script foi projetado para funcionar em sistemas Windows.

# Instalação das Bibliotecas
Certifique-se de ter as bibliotecas necessárias instaladas antes de executar o script. Você pode instalar as bibliotecas usando o seguinte comando no terminal ou prompt de comando:
bashCopy code

    pip install tkinter pyautogui 

# Como Utilizar
    * é necessario instalar o whatsapp para desktop (aplicativo)

    1.	Execute o script Python.python main.py 
    2.	A interface gráfica será exibida com uma caixa de texto para você digitar sua mensagem.
    3.	Digite a mensagem desejada na caixa de texto.
    4.	Clique no botão "Enviar Mensagens".
    5.	O script automatizará a abertura do WhatsApp, procurará os usuários especificados e enviará a mensagem.
    6.	O processo será repetido para cada usuário alvo.
    7.	Ao final, o console exibirá a mensagem "Todas as mensagens foram enviadas!".

# Observações
•	Certifique-se de que o WhatsApp Web esteja aberto antes de iniciar o script.
•	O código usa coordenadas específicas para clicar em elementos na tela. Certifique-se de que essas coordenadas são válidas para a resolução do seu monitor. Se necessário, ajuste as coordenadas no código.
•	O script foi projetado para funcionar em sistemas Windows e pode não funcionar corretamente em outros sistemas operacionais.


