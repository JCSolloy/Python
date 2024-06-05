import pyautogui as rpa
import platform

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

wait = 1
os = detect_os()
open_excel()