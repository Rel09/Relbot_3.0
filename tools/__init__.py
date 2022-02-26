import time, datetime, pyautogui, random, configparser
from win32gui import FindWindow, GetWindowRect
from pywinauto import Desktop

#Handler
def reset_handler():
    #Reset
    left_click('rl_settings/reset_button.png')
    #Reset? Yes
    left_click('rl_settings/reset_yes.png')
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
def read_config(file, title, subtitle):
            config = configparser.ConfigParser()
            config.read(file)
            config.sections()
            info = config[title][subtitle]
            if info == '':
                pyautogui.alert('You need to set an Image folder in Config.ini\n\nPlease call Bill gates')
                quit()
            return info

#Bot/Automations functions
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
def write(text, click_switch):
    pyautogui.write(text)
    if click_switch == 1:
        time.sleep(0.3)
        pyautogui.press('enter')
def select_target(target_name):                                           
    settings_handler()
    write('npc indicators', 1)
    left_click_from('rl_settings/npc_indicator_settings.png', 120, 0)
    reset_handler()
    switch_handler(1)
    left_click_from('rl_settings/npcindic_highlighthull.png', 170, 0)
    left_click('rl_settings/npcindic_npc2highlight.png')
    write(target_name, 1)
    left_click_from('rl_settings/npcindic_drawname.png', 170, 0)
    settings_handler()
    #Closing settings
    left_click('rl_settings/selected_settings.png')
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
    if z > wait_time_in_second:
        return False

    return True
    
    
    
    
    pass

#Take care of Addons & Plugins in Runelite
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
def addons_switch(addons_name, switch):
    settings_handler()
    write(addons_name.lower())
    #need to have the same name in addons_switch folder
    left_click_from(f"rl_settings/addons_switch/{addons_name}.png", 80, 0)
    #0 for closed, 1 for open
    switch_handler(int(switch))
    settings_handler()
    left_click('rl_settings/selected_settings.png')

#Basic in-game Functions
def auto_relog():
    #Retrieve the account info
    accinfo = config['User Infos']['location']
    if accinfo != '':
        #Loading user info
        config = configparser.ConfigParser()	
        config.read(accinfo)
        config.sections()
        acc_name = config['User Infos']['account']
        acc_pass = config['User Infos']['password']
        #Set it back, for later use
        config.read('config.ini')
        config = configparser.ConfigParser()
        config.sections()
        print(f'[{acc_name}] - Account Loaded')

        #If we detect the first button
        if itemcheck('login/disconnected1.png'):
            left_click('login/disconnected1.png')
            time.sleep(1.5)

        #If we detect the second one, Relog
        if itemcheck('login/disconnected2.png'):
            left_click('login/disconnected2.png')
            time.sleep(1.5)

        left_click_from('login/login.png', 50, 0)
def open_skilltab():
    left_click('g_settings/skilltab.png')
def open_inventary():
    left_click('g_settings/inventary.png')
def open_combattab():
    left_click('g_settings/combattab.png')
def open_logoutmenu():
    left_click('g_settings/logoutbutton.png')
def use_item(item_picture, action):
    pass

#Image folder
img_folder = read_config('config.ini', 'IMAGE FOLDER', 'folder')
#Player State
p_state = 'idle'