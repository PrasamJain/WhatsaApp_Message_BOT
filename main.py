import pyautogui as pg
import webbrowser as wb
import time

wb.register('Chrome',None,wb.BackgroundBrowser("C://Program Files//Google//Chrome\Application\Chrome.exe"))
wb.get('Chrome').open("web.whatsapp.com")
time.sleep(60)
for i in range(10000):
    pg.press("H")
    pg.press("E")
    pg.press("Y")  
    pg.press("enter")
