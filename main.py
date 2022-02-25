from win32gui import FindWindow, GetWindowRect
from pywinauto import Desktop
import pyperclip, time, sys, random, configparser, pyautogui, datetime

#Good Sprite:
#1980 a 1985-1987 a 1994
#[{"RegionId":6966,"RegionX":3,"RegionY":1,"plane":0,"spriteId":1980,"scale":100},{"RegionId":6966,"RegionX":11,"RegionY":8,"plane":0,"spriteId":1981,"scale":100},{"RegionId":6966,"RegionX":21,"RegionY":5,"plane":0,"spriteId":1982,"scale":100},{"RegionId":6966,"RegionX":33,"RegionY":6,"plane":0,"spriteId":1983,"scale":100},{"RegionId":6966,"RegionX":59,"RegionY":0,"plane":0,"spriteId":1985,"scale":100},{"RegionId":6966,"RegionX":57,"RegionY":14,"plane":0,"spriteId":1987,"scale":100},{"RegionId":6966,"RegionX":45,"RegionY":1,"plane":0,"spriteId":1993,"scale":100}]
#Fix RUNELITE opacity (overlay color)
#Fix healing circle 

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
    def crabs():

        #Read the Config file
        try:
            crab_roll = config['Crab Bot']['crab_ending']
            crab_pause_x, crab_pause_y = config['Crab Bot']['crab_ending_rand_pause'].split(',')
            print(f'{crab_pause_x}{crab_pause_y}')
        except:print(f'{now_time()} ERROR [Config.ini - crab_roll or cran_ending_rand_pause\nPlease contact Bill gates]')

        first_loop = True
        while True:
            idle_switch = True

            #From the Bank to the Chest
            for x in range(1, 7):                    
                if x != 1 or first_loop:
                    print(f'{now_time()} {x} - From Bank to Chest')
                    while True:
                        if itemcheck(f'crabs/sprite{x}.png'):
                            left_click_from(f'crabs/sprite{x}.png', random.randint(-5, 5), random.randint(-15, -7))
                            break
                        else:print(f'{now_time()} Not detecting [sprite{x}]')

                        #Check Running
                        if itemcheck('player_state/ready_run.png'):
                            left_click('player_state/ready_run.png')
                            pass

                    time_Start = datetime.datetime.now()
                    while r_timer(time_Start, 12) or not player_InFight('crabs/player_state/fight_crab.png'):
                        pass
                        #Check Hp

            #When at the chest, Roll Dice to IDLE
            roll_dice = random.randint(1, int(crab_roll))
            print(f'{now_time()} Roll Dice[{roll_dice}]')

            #If the Dice roll 1 or 2
            if roll_dice == 1 or roll_dice == 2:
                print(f"{now_time()} Going to IDLE Spot {roll_dice}")
                for x in range(1, 4):
                    while True:
                        if itemcheck(f'crabs/rand_ending\{roll_dice}\{x}.png'):
                            left_click_from(f'crabs/rand_ending\{roll_dice}\{x}.png', random.randint(-5, 5), random.randint(-5, 5))
                            print('9 second pause ..[DEV]')
                            time.sleep(9)
                            break
                        else:print(f'{now_time()} Not detecting [sprite{x}]')
                        
                        #Check Running
                        if itemcheck('player_state/ready_run.png'):
                            left_click('player_state/ready_run.png')

                #Pause in IDLE spot
                _crabpause = random.randint(int(crab_pause_x), int(crab_pause_y))
                print(f'{now_time()} Pause [{_crabpause} seconds]')
                idle_switch = False
                time.sleep(_crabpause)

                #From IDLE spot to chest
                for x in range(2, 0, -1):
                    print(f'{x} - From IDLE to Chest')
                    while True:
                        if itemcheck(f'crabs/rand_ending\{roll_dice}\{x}.png'):
                            left_click_from(f'crabs/rand_ending\{roll_dice}\{x}.png', random.randint(-5, 5), random.randint(-5, 5))
                            time.sleep(7)
                            break
                        else:print(f'{now_time()} Not detecting [sprite{x}]')

                        #Check Running
                        if itemcheck('player_state/ready_run.png'):
                            left_click('player_state/ready_run.png')

            #From chest to Bank
            first_loop = False

            for x in range(6, 0, -1):
                if x != 6 or not idle_switch:
                    print(f'{now_time()} {x} - From Chest to Bank')
                    
                    while True:
                        if itemcheck(f'crabs/sprite{x}.png'):
                            left_click_from(f'crabs/sprite{x}.png', random.randint(0, 5), random.randint(-15, -10))
                            break
                        else:print(f'{now_time()} Not detecting [sprite{x}]')

                        #Check Running
                        if itemcheck('player_state/ready_run.png'):
                            left_click('player_state/ready_run.png')
                            pass

                    time_Start = datetime.datetime.now()
                    while r_timer(time_Start, 12) or not player_InFight('crabs/player_state/fight_crab.png'):
                        pass
    def oak_tree():
        pass
                            #Check Hp
    #Bot_Toolkit
    def player_InFight(top_left_enemy_name):
        global p_state
        
        #If the player status is Idle, check if we detect a fight
        if p_state == 'idle':
                if itemcheck(top_left_enemy_name):
                    p_state = 'fight'
                    print(f"{now_time()} Player_State[{p_state.upper()}]")
                    return False
                #No fight detected, return True
                return True
        
        #If the player status is FIGHT, check if fight is over
        elif p_state == 'fight':
            if not itemcheck(top_left_enemy_name):
                    p_state = "idle"
                    print(f"{now_time()} Player_State[{p_state.upper()}]")
                    return True
            return False
    def r_timer(time_Start, wait_time_in_second):

        #time_Start = datetime.datetime.now()
        #pass time_Start as Arg
        time_End = datetime.datetime.now()
        z = datetime.timedelta(hours=(time_End.hour - time_Start.hour),minutes=(time_End.minute - time_Start.minute), seconds=(time_End.second- time_Start.second))
        z = int(str(z.total_seconds()).replace(".0", ""))
        if z > wait_time_in_second:
            return False

        return True
    def now_time():
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        return f'[{current_time}]'
    def get_winpos():
        windows = Desktop(backend="uia").windows()
        for w in windows:
            if "RuneLite" in w.window_text():
                bor = str(w.window_text())
                window_handle = FindWindow(None, bor)
                win_position = GetWindowRect(window_handle)
                return win_position
        pyautogui.alert('No Runelite as been found\n\nPlease call Bill Gates')
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
        pyautogui.alert("Make sure you're on the beach infront of the stash\n& click OK")
        time.sleep(1.5)
        crabs()

if __name__ == '__main__':

    dev = 0
    if dev == 1:
        #This Section is purely for Testing & implementing
        #Bot_Toolkit
        img_folder = 'img/'
        def get_winpos():
            windows = Desktop(backend="uia").windows()
            for w in windows:
                if "RuneLite" in w.window_text():
                    bor = str(w.window_text())
                    window_handle = FindWindow(None, bor)
                    win_position = GetWindowRect(window_handle)
                    return win_position
            pyautogui.alert('No Runelite as been found\n\nPlease call Bill gates')
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
        def r_timer(time_Start, wait_time_in_second):
            #time_Start = datetime.datetime.now()
            #pass time_Start as Arg
            time_End = datetime.datetime.now()
            z = datetime.timedelta(hours=(time_End.hour - time_Start.hour),minutes=(time_End.minute - time_Start.minute), seconds=(time_End.second- time_Start.second))
            z = int(str(z.total_seconds()).replace(".0", ""))

            if z >= wait_time_in_second:
                return False
            return True
        def now_time():
            now = datetime.datetime.now()
            curr_time = now.strftime("%H:%M:%S")
            return [f'{curr_time}']
        #-------------------
        print(now_time())
    else:
        #Player state, Shared Variable
        p_state = 'idle'
        #Reading the Config file
        config = configparser.ConfigParser()
        config.read('config.ini')
        config.sections()
        img_folder = config['IMAGE FOLDER']['folder']
        if img_folder == '':
            pyautogui.alert('You need to set an Image folder in Config.ini\n\nPlease call Bill gates')
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

