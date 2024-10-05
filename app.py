import pyautogui
import time

from pynput.mouse import Listener

# Definir uma função que contém as ações a serem executadas


def rotina_automatica():
    # Mover o mouse e realizar os cliques em pontos específicos
    pyautogui.click(x=776, y=100, button='left', duration=10)
    pyautogui.click(x=1317, y=101, button='left', duration=10)
    pyautogui.click(x=1016, y=562, button='left', duration=10)
    pyautogui.click(x=768, y=504, button='left', duration=10)
    pyautogui.click(x=1075, y=693, button='left', duration=10)
    pyautogui.click(x=994, y=659, button='left', duration=10)
    pyautogui.click(x=1171, y=431, button='left', duration=10)
    #pyautogui.click(x=1138, y=670, button='left', duration=10)
    print(f"Rotina executada às {time.strftime('%H:%M:%S')}")  # Mostrar no terminal o horário da execução


# Esperar alguns segundos para se preparar antes da primeira execução
time.sleep(9)

# Loop infinito para executar a função a cada 1 minuto
while True:
    rotina_automatica()  # Executa a função de cliques
    time.sleep(100)  # Aguarda 60 segundos antes de repetir

# Passo 2: Realizar um clique no ponto atual
#pyautogui.click()  # Clicar na posição atual do mouse

# Clique com mais controle
# pyautogui.click(x=500, y=500, button='left')  # Também é possível definir diretamente a posição e o botão (esquerdo ou direito)

#print("Mouse movido e clique realizado.")

# Mostra a posição atual do mouse na tela


#while True:
#    x, y = pyautogui.position()
#    print(f"Posição atual do mouse: X = {x}, Y = {y}")
#    time.sleep(1)  # Aguarda 1 segundo para facilitar a leitura


# captura posição do clique

# Função que será chamada quando houver um clique do mouse
"""
def on_click(x, y, button, pressed):
    if pressed:  # Se houver um clique (pressão do botão do mouse)
        print(f"Mouse clicado na posição: X = {x}, Y = {y}")


# Iniciar o listener para monitorar cliques
with Listener(on_click=on_click) as listener:
    listener.join()
"""