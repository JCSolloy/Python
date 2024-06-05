import pyautogui as rpa
import platform

# Detect OS
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

# Open Excel
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

# Moverse al inicio de la hoja
open_excel()
time.sleep(wait)
rpa.write('formulario usuarios rpa')
time.sleep(wait)
rpa.press('tab')
time.sleep(wait)
rpa.press('enter')
time.sleep(wait*5)

# Moverse al inicio de la hoja
rpa.hotkey('command', 'left')
time.sleep(wait)
rpa.hotkey('command', 'up')
time.sleep(wait)
rpa.press('down')

# Open Edge y el link al formulari y moverse al primer campo
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

###