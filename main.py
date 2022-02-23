from win32gui import FindWindow, GetWindowRect
from pywinauto import Desktop
import pyperclip, time, sys, random, configparser
import pyautogui

def relbot(action):
    #To get the Coord of Runelite
    def get_winpos():
        windows = Desktop(backend="uia").windows()
        for w in windows:
            if "RuneLite" in w.window_text():
                bor = str(w.window_text())
                window_handle = FindWindow(None, bor)
                win_position = GetWindowRect(window_handle)
                return win_position
        pyautogui.alert('No Runelite as been found')
        quit()
    #Runelite Settings
    def settings():
        pass
    #Bot Stuff
    def itemcheck(x):
        game_region = get_winpos()
        item = pyautogui.locateCenterOnScreen(img_folder + x, confidence=0.9, region=game_region)
        if item != None:
            return True
        else:return False
    def left_click(x):
        while True:
            game_region = get_winpos()
            try:
                x, y = pyautogui.locateCenterOnScreen(img_folder + x, confidence=0.9, region=game_region)
                pyautogui.moveTo(x, y)
                time.sleep(0.3)
                pyautogui.click()
                break
            except:
                time.sleep(0.7)
                pass          
    def right_click(x):
        while True:
            game_region = get_winpos()
            try:
                x, y = pyautogui.locateCenterOnScreen(img_folder + x, confidence=0.9, region=game_region)
                pyautogui.moveTo(x, y)
                time.sleep(0.3)
                pyautogui.click(button='right')
                break
            except:
                time.sleep(0.7)
                pass
    def left_click_from(x, coord_x, coord_y):
        while True:
            game_region = get_winpos()
            try:
                x, y = pyautogui.locateCenterOnScreen(img_folder + x, confidence=0.9, region=game_region)
                x = x + coord_x
                y = y + coord_y
                pyautogui.moveTo(x, y)
                time.sleep(0.3)
                pyautogui.click()
                break
            except:
                time.sleep(0.7)
                pass    
    def right_click_from(x, coord_x, coord_y):
        while True:
            game_region = get_winpos()
            try:
                x, y = pyautogui.locateCenterOnScreen(img_folder + x, confidence=0.9, region=game_region)
                x = x + coord_x
                y = y + coord_y
                pyautogui.moveTo(x, y)
                time.sleep(0.3)
                pyautogui.click(button='right')
                break

            except:
                time.sleep(0.7)
                pass
    
    if action == 'Settings':
        pass

    elif action == 'Crabs':
        print('crabs')



if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.read('config.ini')
    config.sections()
    img_folder = config['IMAGE FOLDER']['folder']
    if img_folder == '':
        pyautogui.alert('You need to set a folder in Config.ini\n\nProcess has been terminated')
        quit()

    botlist = ["Runelite Settings", "Crab Farming"]

    while True:
        bot = pyautogui.confirm(text='Choose bot action', title='RelBot', buttons=botlist)

        # Runelite Settings
        if bot == "Runelite Settings":
            bot = pyautogui.alert(text="Do not pause during this process", title='Runelite Settings', button='OK')
            if bot == 'OK': 
                relbot('Settings')

        # Crab Farming
        elif bot == "Crab Farming":
            bot = pyautogui.alert(text="Make sure you're: \nInfront of South Horidius Beach Bank", title='Crab Farming', button='OK')
            if bot == 'OK': 
                relbot('Crabs')

        # If X is clicked
        elif bot == None:
            print("Exit")
            quit()

