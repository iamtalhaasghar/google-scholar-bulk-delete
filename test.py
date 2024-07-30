import pyautogui as pg
import time

total = 180
for i in range(total):
    x,y = pg.locateCenterOnScreen('actions.png', confidence=0.6)
    pg.moveTo(x+20, y)
    pg.click()
    time.sleep(3)
    print(total-i)
