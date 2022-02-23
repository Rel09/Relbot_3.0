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
        def switch_handler(state):
            if state == 1:
                if itemcheck('rl_settings/off_switch.png'):
                    left_click('rl_settings/off_switch.png')
            elif state == 0:
                if itemcheck('rl_settings/on_switch.png'):
                    left_click('rl_settings/on_switch.png')
        def reset_handler():
            #Reset
            left_click('rl_settings/reset_button.png')
            #Reset? Yes
            left_click('rl_settings/reset_yes.png')
        def install_plugin(plugin_name):
            left_click('rl_settings/plugin_hub.png')
            left_click('rl_settings/plugin_emptytextbox.png')
            write(plugin_name, 1)
            time.sleep(3)
            while True:
                if itemcheck('rl_settings/plugin_install.png'):
                    left_click('rl_settings/plugin_install.png')
                    time.sleep(2)
                elif itemcheck('rl_settings/plugin_remove.png'):
                    break
                time.sleep(1)
            left_click('rl_settings/back_arrow_textbox2.png')
        #Take care of opening the Settings
        settings_handler()

        #-------------------------- RUNELITE SETTINGS ----------------
        write('runelite', 1)    
        left_click_from('rl_settings/runelite_config.png', 105, 0)
        while True:
            if itemcheck('rl_settings/arrow_opened.png'):
                left_click('rl_settings/arrow_opened.png')
                time.sleep(0.5)
            else: break
        reset_handler()
        left_click('rl_settings/runelite_windowsetttings.png')
        left_click_from('rl_settings/runelite_gamesize.png', 50, 0)
        pyautogui.hotkey('ctrl', 'a')
        write('800', 1)
        time.sleep(0.5)
        left_click_from('rl_settings/runelite_gamesize.png', 150, 0)
        pyautogui.hotkey('ctrl', 'a')
        write('650', 1)
        time.sleep(0.5)
        left_click_from('rl_settings/runelite_lockwindowssize.png', 160, 0)
        settings_handler()
        
        #-----------------------CAMERA SETTINGS---------------------
        write('camera', 1)
        left_click_from('rl_settings/camera_settings.png', 135, 0)
        reset_handler()
        switch_handler(1)
        left_click_from('rl_settings/camera_vertical.png', 158, 0)
        left_click_from('rl_settings/camera_controlfunction.png', 130, 0)
        time.sleep(0.5)
        left_click_from('rl_settings/camera_controlfunction.png', 130, 80)
        left_click_from('rl_settings/camera_resetzoomposition.png', 90, 0)
        pyautogui.hotkey('ctrl', 'a')
        write('296', 1)
        left_click_from('rl_settings/camera_preservepitch.png', 120, 0)
        left_click_from('rl_settings/camera_preserveyaw.png', 130, 0)
        settings_handler()
        #--------------------------- LOW DETAIL SETTINGS -------------------
        write('low detail', 1)
        left_click_from('rl_settings/settings_lowdetail.png', 130, 0)
        reset_handler()
        switch_handler(1)
        left_click_from('rl_settings/lowdetail_lowerplane.png', 160, 0)
        settings_handler()

        #Hide entity - Not needed for now

        #Install Sprite marker
        install_plugin('sprite marker')

        #Back to settings
        settings_handler()
        #----------------------------SPRITE MARKER--------------------------
        write('sprite markers', 1)
        left_click_from('rl_settings/spritemarket_settings.png', 120, 0)
        reset_handler()
        switch_handler(1)
        left_click_from('rl_settings/sprite_display.png', 160, 0)
        left_click_from('rl_settings/sprite_showonmap.png', 165, 0)
        left_click_from('rl_settings/sprite_showtiles.png', 160, 0)
        left_click_from('rl_settings/sprite_importexport.png', 160, 0)
        settings_handler()

        #Closing settings
        left_click('rl_settings/selected_settings.png')


        #--------------------- IN GAME SETTINGS ----------------------------
        while True:
            if itemcheck('g_settings/unselected_settings.png'):
                left_click('g_settings/unselected_settings.png')
            elif itemcheck('g_settings/selected_settings.png'):
                break        
        left_click('g_settings/unselected_screen.png')   
        left_click('g_settings/game_format_arrow.png')
        left_click('g_settings/resizable_classic.png')
        left_click('g_settings/north.png')
        pyautogui.keyDown('up')
        time.sleep(2.7)
        pyautogui.keyUp('up')
        pyautogui.press('ctrl')





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
        img_folder = 'img/'
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
                    print('test')
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
        

        #left_click_from('rl_settings/sprite_display.png', 160, 0)
        #left_click_from('rl_settings/sprite_showonmap.png', 165, 0)
        #left_click_from('rl_settings/sprite_showtiles.png', 160, 0)
        left_click_from('rl_settings/sprite_importexport.png', 160, 0)

        
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

