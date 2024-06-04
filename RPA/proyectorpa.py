import pyautogui as rpa
import time
import platform

# Function to detect the OS
def detect_os():
    if platform.system() == 'Windows':
        os = 'Windows'
    elif platform.system() == 'Darwin':
        os = 'MacOS'
    elif platform.system() == 'Linux':
        os = 'Linux'
    else:   
        os = 'Unknown OS'

detect_os()
# verify if the os is windows, macos or linuxi
if platform.system() == 'Windows':
    print('Windows')
elif platform.system() == 'Darwin':
    print('MacOS')
elif platform.system() == 'Linux':
    print('Linux')
else:   
    print('Unknown OS')
wait = 2
# open a excel file and copy the data to put in the form\
rpa.hotkey('win')
rpa.write('excel')
rpa.press('enter')
time.sleep(wait)
rpa.press('tab')
rpa.press('tab')
rpa.write('Formulario usuarios rpa')
time.sleep(wait)
rpa.press('enter')
rpa.hotkey('ctrl', 'home')

# open this link https://forms.gle/3rHFV9Xa79JYX3Rf7 in edge browser and fill it

#rpa.hotkey('win', 'r')
#rpa.write('msedge https://forms.gle/3rHFV9Xa79JYX3Rf7')
#rpa.press('enter')

# verify if the os is windows, macos or linux
# if windows
rpa.hotkey('win')
rpa.write('edge')
rpa.press('enter')
time.sleep(wait)
rpa.write('https://forms.gle/3rHFV9Xa79JYX3Rf7')
rpa.press('enter')
