import pyautogui
from time import sleep
sleep(5)
try:
    n = int(input())
except error:
    exit()

x, y = 500, 500  
spacing = 20 

for i in range(1, n + 1):
    for j in range(1, i + 1):
        pyautogui.moveTo(x + (j - 1) * spacing, y - (i - 1) * spacing)
        pyautogui.click()


