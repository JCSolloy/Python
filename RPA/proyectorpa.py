
import platform
import pyautogui as rpa
import time

wait = rpa.PAUSE = 1

# Funcion para detectar el sistema operativo
def detect_os():
    if platform.system() == 'Windows':
        os = 'Windows'
    elif platform.system() == 'Darwin':
        os = 'MacOS'
    elif platform.system() == 'Linux':
        os = 'Linux'
    else:   
        os = 'Unknown OS'
    return os

# Funcion para abrir excel
def open_excel():
    wait = 1
    if os == 'Windows':
        rpa.press('winleft')
        time.sleep(wait)
        rpa.write('excel')
        time.sleep(wait)
        rpa.press('enter')
    elif os == 'MacOS':
        rpa.hotkey('command', 'space')
        time.sleep(wait)
        rpa.write('excel')
        time.sleep(wait)
        rpa.press('enter')
    elif os == 'Linux':
        rpa.hotkey('ctrl', 'alt', 't')
        rpa.write('excel')
        rpa.press('enter')
    else:
        print('Unknown OS')

# Funcion para abrir edge
def open_edge():
    if os == 'Windows':
        rpa.press('winleft')
        time.sleep(wait)
        rpa.write('edge')
        time.sleep(wait)
        rpa.press('enter')
    elif os == 'MacOS':
        rpa.hotkey('command', 'space')
        time.sleep(wait)
        rpa.write('edge')
        time.sleep(wait)
        rpa.press('enter')
        time.sleep(wait)
        rpa.hotkey('command', 't')
        time.sleep(wait)
        rpa.press('enter')
    elif os == 'Linux':
        rpa.hotkey('ctrl', 'alt', 't')
        rpa.write('edge')
        rpa.press('enter')
    else:
        print('Unknown OS')

# Detectar el sistema operativo

os = detect_os()

## Abrir excel abrir el documento y moverse a la primera celda de la hoja activa
open_excel()
time.sleep(wait)
rpa.press('tab')
time.sleep(wait)
rpa.press('tab')
time.sleep(wait)
rpa.write('formulario usuarios rpa')
time.sleep(wait)
rpa.press('enter')
time.sleep(wait*5)
# Moverse al inicio de la hoja
rpa.hotkey('ctrl', 'home')
time.sleep(wait)
rpa.press('down')
# Moverse a la primera celda de la hoja  

# Abrir edge e ir al formulario de google

open_edge()
time.sleep(wait)
rpa.write('https://forms.gle/FuJCsL1iZydZoF7w8')
time.sleep(wait)
rpa.press('enter')
time.sleep(wait*5)
rpa.press('tab')
time.sleep(wait)
rpa.press('tab')
time.sleep(wait)
rpa.press('tab')

## Excel abierto, y formulario en el primer campo
# Moverse entre el formulario y excel e ir copiando los datos de excel al formulario
rpa.hotkey('alt', 'tab')
# Nombre
rpa.hotkey('ctrl', 'c')
time.sleep(wait)
rpa.hotkey('tab')
time.sleep(wait)
rpa.hotkey('alt', 'tab')
time.sleep(wait)
rpa.hotkey('ctrl', 'v')
time.sleep(wait)
rpa.hotkey('tab')
time.sleep(wait)