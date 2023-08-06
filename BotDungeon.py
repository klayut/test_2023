import  pyautogui as gui
from time import sleep
from time import time

class BotDungeon:
    def __init__(self) -> None:
        pass

    def runBot(self):
        z = 100
        while True:
            try:
                x, y = gui.locateCenterOnScreen('main_dungeon_bt.png')
                gui.click(x, y)
                sleep(0.5)
                gui.click(x, y-100)
                sleep(0.5)
                gui.click(x, y-700)
                sleep(0.5)
                gui.click(x, y-680)
                sleep(0.5)
                gui.click(x, y-90)
                sleep(0.5)
                gui.click(x+z, y-500)
                sleep(0.5)
                gui.click(x, y-90)
                if z==0:
                    z=100
                else:
                    z=0
                sleep(5)
            except:
                sleep(5)
            try:
                x, y = gui.locateCenterOnScreen('main_dungeon_bt_3.png')
                gui.click(x+250, y-180)
                sleep(2)
                gui.click(x+100, y)
                sleep(2)
                gui.click(x, y)
                sleep(2)
                gui.click(x, y-100)
                sleep(2)
                gui.click(x+150, y)
            except:
                pass




bot = BotDungeon()
bot.runBot()





