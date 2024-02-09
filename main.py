import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui
import time

class WhatsappAutomacaoApp:
    def __init__(self, root):
        self.root = root
        root.title("automação Dato... Mensagens em lote para grupos de Whatsapp")

        self.mensagem_label = ttk.Label(root, text="Digite sua Mensagem:")
        self.mensagem_label.grid(row=0, column=50, padx=60, pady=80, sticky="W")

        self.mensagem_text = tk.Text(root, wrap="word", width=80, height=20)
        self.mensagem_text.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="W")

        self.enviar_button = ttk.Button(root, text="Enviar Mensagens", command=self.enviar_mensagens)
        self.enviar_button.grid(row=1, column=0, columnspan=3, pady=10)

    def enviar_mensagens(self):
        mensagem = self.mensagem_text.get("1.0", "end-1c")

        if not mensagem.strip():
            messagebox.showwarning("Aviso", "Por favor, digite uma mensagem.")
            return

        pyautogui.hotkey("win", "s")
        time.sleep(1)
        pyautogui.write("Whatsapp")
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)

        usuarios_alvo = ['ANOTACOES FACULDADE', 'Anotacoes Dato']

        for usuario in usuarios_alvo:
            self.enviar_mensagem(usuario, mensagem)
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'f')
            time.sleep(2)
            print("Enviado para: " + usuario)

        print("Todas as mensagens foram enviadas!")

    def enviar_mensagem(self, usuario, mensagem):
        pyautogui.write(usuario)
        time.sleep(1)
        pyautogui.click(x=205, y=199)
        time.sleep(1)
        pyautogui.write(mensagem)
        time.sleep(2)
        pyautogui.press("enter")

if __name__ == "__main__":
    root = tk.Tk()
    app = WhatsappAutomacaoApp(root)
    root.mainloop()
