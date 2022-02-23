from win32gui import FindWindow, GetWindowRect
from pywinauto import Desktop
import pyperclip, time, sys, random, configparser
import pyautogui

def relbot(action):
    #Actual Bot/Automation
    def settings():
        def settings_handler():
            while True:
                #If settings is not Opened
                if itemcheck('rl_settings/unselected_settings.png'):
                    left_click('rl_settings/unselected_settings.png')
                #If we are in a tab, close it
                if itemcheck('rl_settings/back_arrow_textbox.png'):
                    left_click('rl_settings/back_arrow_textbox.png')
                #if there is text already, remove it
                if itemcheck('rl_settings/red_x_textbox.png'):
                    left_click('rl_settings/red_x_textbox.png')
                #if we finally detect the empty text box
                if itemcheck('rl_settings/empty_textbox.png'):
                    left_click('rl_settings/empty_textbox.png')
                    break
        
        #Take care of opening the Settings
        settings_handler()

        #Write Runelite
        write('runelite', 1)    

        #Click on Runelite Settings icon
        left_click_from('rl_settings/runelite_config.png', 105, 0)

        #We close all the Runelite tab
        while True:
            if itemcheck('rl_settings/arrow_opened.png'):
                left_click('rl_settings/arrow_opened.png')
                time.sleep(0.5)
            else: break

        #Reset
        left_click('rl_settings/reset_button.png')

        #Reset? Yes
        left_click('rl_settings/reset_yes.png')

        #Re-open Runelite/Windows Settings
        left_click('rl_settings/runelite_windowsetttings.png')

        #Set Windows Size
        left_click_from('rl_settings/runelite_gamesize.png', 50, 0)
        pyautogui.hotkey('ctrl', 'a')
        write('800', 1)
        time.sleep(0.5)
        left_click_from('rl_settings/runelite_gamesize.png', 150, 0)
        pyautogui.hotkey('ctrl', 'a')
        write('650', 1)
        time.sleep(0.5)
        
        #Lock Set Windows Size
        left_click_from('rl_settings/runelite_lockwindowssize.png', 160, 0)

        #Get back on Settings
        settings_handler()

        #Low Detail
        #Hide entity
        #Camera (Should do after plugin)
        #Ground marker (Switch to Layout)
        #Download plugin

        


    #Bot_Toolkit
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
    def itemcheck(x):
        game_region = get_winpos()
        item = pyautogui.locateCenterOnScreen(img_folder + x, confidence=0.9, region=game_region)
        if item != None:
            return True
        else:return False
    def write(text, click_switch):
        pyautogui.write(text)
        if click_switch == 1:
            time.sleep(0.3)
            pyautogui.press('enter')
    def left_click(x):
        while True:
            game_region = get_winpos()
            try:
                x, y = pyautogui.locateCenterOnScreen(img_folder + x, confidence=0.9, region=game_region)
                pyautogui.moveTo(x, y)
                time.sleep(0.3)
                pyautogui.click()
                pyautogui.moveTo(1, 1)
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
                pyautogui.moveTo(1, 1)
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
                pyautogui.moveTo(1, 1)
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
                pyautogui.moveTo(1, 1)
                break

            except:
                time.sleep(0.7)
                pass
    
    if action == 'Settings':
        pyautogui.alert('Make sure Runelite is opened\n& click OK')
        time.sleep(1.5)
        settings()

    elif action == 'Crabs':
        print('crabs')













if __name__ == '__main__':

    dev = 0
    if dev == 1:
        #TESTING ---------- Bot_Toolkit
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
        def itemcheck(x):
            game_region = get_winpos()
            item = pyautogui.locateCenterOnScreen(img_folder + x, confidence=0.9, region=game_region)
            if item != None:
                return True
            else:return False
        def write(text, click_switch):
            pyautogui.write(text)
            if click_switch == 1:
                time.sleep(0.3)
                pyautogui.press('enter')
        def left_click(x):
            while True:
                game_region = get_winpos()
                try:
                    x, y = pyautogui.locateCenterOnScreen(img_folder + x, confidence=0.9, region=game_region)
                    pyautogui.moveTo(x, y)
                    time.sleep(0.3)
                    pyautogui.click()
                    pyautogui.moveTo(1, 1)
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
                    pyautogui.moveTo(1, 1)
                    break
                except:
                    time.sleep(0.7)
                    pass
        def left_click_from(x, coord_x, coord_y):

            img_folder = "img/"   
            while True:
                game_region = get_winpos()
                try:
                    x, y = pyautogui.locateCenterOnScreen(img_folder + x, confidence=0.9, region=game_region)
                    print(x,y)
                    x = x + coord_x
                    y = y + coord_y
                    pyautogui.moveTo(x, y)
                    time.sleep(0.3)
                    pyautogui.click()
                    #pyautogui.moveTo(1, 1)
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
                    pyautogui.moveTo(1, 1)
                    break

                except:
                    time.sleep(0.7)
                    pass
        

        left_click_from('rl_settings/runelite_lockwindowssize.png', 160, 0)
        
    
    else:
        #Read the Config file
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
                relbot('Settings')

            # Crab Farming
            elif bot == "Crab Farming":
                relbot('Crabs')

            # If X is clicked
            elif bot == None:
                print("Exit")
                quit()

