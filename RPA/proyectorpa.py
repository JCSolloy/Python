
import platform
import pyautogui as rpa
import time

# Variable para modificar el tiempo de espera entre acciones
wait = sleep = 0.75
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

os = detect_os()
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

def copy_paste():
    rpa.hotkey('alt', 'tab')
    time.sleep(wait)
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

def copy_paste_fields(n):
    for i in range(n):
        copy_paste()

# Funcion para llenar el formulario
def fill_form():
    copy_paste_fields(6)
    time.sleep(wait)
    rpa.press('enter')
    time.sleep(wait)
    rpa.press('tab')
    time.sleep(wait)
    rpa.press('enter')
    time.sleep(wait*2)
    rpa.press('tab')
    time.sleep(wait)
    rpa.press('tab')
    time.sleep(wait)
    rpa.press('tab')

# function replicate fill_form() n times
def replicate_fill_form(n):
    for i in range(n):
        fill_form()

## Abrir excel abrir el documento y moverse a la primera celda de la hoja activa
open_excel()
time.sleep(wait)
rpa.press('tab')
time.sleep(wait)
rpa.press('tab')
time.sleep(wait)
rpa.write('Formulario usuarios rpa')
time.sleep(wait)
rpa.press('enter')
time.sleep(wait*3)
rpa.hotkey('ctrl', 'home')
time.sleep(wait)
rpa.press('down')

# Abrir edge e ir al formulario de google
open_edge()
time.sleep(wait*3)
rpa.write('https://forms.gle/FuJCsL1iZydZoF7w8')
time.sleep(wait)
rpa.press('enter')
time.sleep(wait*3)
rpa.press('tab')
time.sleep(wait)
rpa.press('tab')
time.sleep(wait)
rpa.press('tab')

# Funcion para llenar el formulario n veces
replicate_fill_form(20)