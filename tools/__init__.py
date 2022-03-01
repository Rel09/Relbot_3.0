# Need to add documentations
import time, datetime, pyautogui, random, configparser, pyperclip
from turtle import right
from win32gui import FindWindow, GetWindowRect
from pywinauto import Desktop

#Handler
def write(text, click_switch):
    pyautogui.write(text)
    if click_switch == 1:
        time.sleep(0.3)
        pyautogui.press('enter')
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
    print('No Runelite as been found, Please call Bill Gates')
    quit()
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
                print(f'{now_time()} You need to set an Image folder in Config.ini')
                quit()
            return info

#Bot/Automations functions
def itemcheck(x):
    game_region = get_winpos()
    item = pyautogui.locateCenterOnScreen(img_folder + x, confidence=0.9, region=game_region)
    if item != None:
        return True
    else:return False
def import_sprite(sprite):
    settings_handler()
    write('sprite markers', 1)
    left_click_from('rl_settings/spritemarket_settings.png', 120, 0)
    left_click_from('rl_settings/sprite_clearsprites.png', 0, 20)
    pyautogui.hotkey('ctrl', 'a')
    write('clear', 0)
    right_click('rl_settings/sprite_clearsprites.png')
    left_click('rl_settings/options_reset.png')
    settings_handler()
    left_click('rl_settings/selected_settings.png')
    pyperclip.copy(sprite)
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen(img_folder + 'g_settings/north.png', confidence=0.9,region=get_winpos())
            break
        except:
            print(f'{now_time()} Cannot locate the North icon')
    pyautogui.moveTo(x + 10, y + 100)
    pyautogui.click(button='right')
    left_click('g_settings/import_spritemarker.png')        
def r_timer(time_Start, wait_time_in_second):
    #time_Start = datetime.datetime.now()
    #pass time_Start as Arg
    time_End = datetime.datetime.now()
    z = datetime.timedelta(hours=(time_End.hour - time_Start.hour),minutes=(time_End.minute - time_Start.minute), seconds=(time_End.second- time_Start.second))
    z = int(str(z.total_seconds()).replace(".0", ""))
    if z > wait_time_in_second:
        return False
    return True

#Player attack/Select(NPC INDICATOR)
def engage_npc(npc_topleft):
    #Need picture in player_state/NPC_NAME.png
    #Need picture in NPC_ENGAGE/NPC_NAME.png
    while True:
        try:
            #Target only a certain location
            if npc_topleft.lower() == 'chicken':
                x = get_winpos()
                region = x[0] + 255, x[1] + 211, 300, 230
            else:
                region = get_winpos()
            x = pyautogui.locateCenterOnScreen(img_folder + f'NPC_ENGAGE/{npc_topleft.lower()}.png', confidence=0.9, region=region)
            break
        except:
            print(f'{now_time} Could not find [{npc_topleft.lower()}]')
    pyautogui.moveTo(x)
    pyautogui.click()
    

    time_Start = datetime.datetime.now()
    while r_timer(time_Start, 7) or not player_InFight(f'player_state/{npc_topleft}.png'):
        pass
def select_target(target_name):
    settings_handler()
    write('npc indicators', 1)
    left_click_from('rl_settings/npc_indicator_settings.png', 120, 0)
    left_click_from('rl_settings/npcindic_render.png', -10, 0)
    reset_handler()
    left_click_from('rl_settings/npcindic_render.png', -10, 0)
    switch_handler(1)
    left_click_from('rl_settings/npcindic_highlighthull.png', 170, 0)
    left_click_from('rl_settings/npcindic_npc2highlight.png', 0 , 15)
    pyautogui.hotkey('ctrl', 'a')
    write(target_name, 1)
    left_click_from('rl_settings/npcindic_drawname.png', 170, 0)
    settings_handler()
    #Closing settings
    left_click('rl_settings/selected_settings.png')
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

#Clicks
def left_clicks_from(x, coord_x, coord_y, count):
    while True:
        game_region = get_winpos()
        try:
            x, y = pyautogui.locateCenterOnScreen(img_folder + x, confidence=0.9, region=game_region)
            x = x + coord_x
            y = y + coord_y
            pyautogui.moveTo(x, y)
            time.sleep(0.3)
            pyautogui.click(clicks=int(count), interval=0.15)
            pyautogui.moveTo(game_region[0], game_region[1])
            break
        except:
            time.sleep(0.7)
            pass    
def left_click(x):
    while True:
        game_region = get_winpos()
        try:
            x, y = pyautogui.locateCenterOnScreen(img_folder + x, confidence=0.9, region=game_region)
            pyautogui.moveTo(x, y)
            time.sleep(0.3)
            pyautogui.click()
            pyautogui.moveTo(game_region[0], game_region[1])
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
            pyautogui.moveTo(game_region[0], game_region[1])
            break
        except:
            time.sleep(0.7)
            pass
def right_click_from(x, coord_x, coord_y):
    while True:
        game_region = get_winpos()
        try:
            x, y = pyautogui.locateCenterOnScreen(img_folder + x, confidence=0.9, region=game_region)
            pyautogui.moveTo(x + coord_x, y + coord_y)
            time.sleep(0.3)
            pyautogui.click(button='right')
            pyautogui.moveTo(game_region[0], game_region[1])
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
            pyautogui.moveTo(game_region[0], game_region[1])
            break
        except:
            time.sleep(0.7)
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
def toggle_run():
    if itemcheck('player_state/ready_run.png'):
        left_click('player_state/ready_run.png')
def close_bank():
    if itemcheck('common/bank_opened.png'):
        left_click_from('common/bank_opened.png', 15, 50)
def auto_relog():
    #Retrieve the account info
    accinfo = read_config('config.ini', 'User Infos','location')
    if accinfo != '':
        #Loading user info
        acc_name = read_config(f'{accinfo}','User Infos','account')
        acc_pass = read_config(f'{accinfo}','User Infos','password')
        print(f'[{acc_name}] - Account Loaded')

        log = True
        while log:
            for x in range(2):
                #If we detect the first button
                if itemcheck(f'login/disconnected{x}.png'):
                    if x == 0:
                        left_click_from(f'login/disconnected{x}.png', 0, 45)
                    elif x == 1:
                        left_click_from(f'login/disconnected{x}.png', 70, 15)
                        log = False
        
        #Deleting Login email & password
        left_click_from('login/login.png', 50, 0)
        while not itemcheck('login/empty_user.png') and itemcheck('runelite.png'):
            pyautogui.press('backspace', presses=100)
        left_click_from('login/password.png', 50, 0)
        while not itemcheck('login/empty_password.png') and itemcheck('runelite.png'):
            pyautogui.press('backspace', presses=100)

        #Entering User info
        left_click_from('login/login.png', 50, 0)
        write(f'{acc_name}', 1)
        left_click_from('login/password.png', 50, 0)
        write(f'{acc_pass}', 0)
        left_click('login/login_main.png')

        log = True
        while log:
            for x in range(3):
                #If we detect the first button
                if itemcheck(f'login/click2play{x}.png'):
                    if x == 0:
                        left_click('login/click2play{x}.png')
                    #If it detect the Character Creation windows or Tutorial island Start(no char creation)
                    elif x == 1 or x == 3:
                        #Just let log turn False
                        pass
                    log = False
                    
        print(f"{now_time()} Login Completed")
        #Set back the windows config, just in case
        left_click('g_settings/north.png')
        pyautogui.keyDown('up')
        time.sleep(3)
        pyautogui.keyUp('up')
        pyautogui.press('ctrl')
def open_skilltab():
    left_click('g_settings/skilltab.png')
def open_inventary():
    left_click('g_settings/inventary.png')
def open_combattab():
    left_click('g_settings/combattab.png')
def open_logoutmenu():
    left_click('g_settings/logoutbutton.png')
def use_item(item_picture, action):
    def do_actions(item_picture, options):
            x = pyautogui.locateCenterOnScreen(img_folder + item_picture, confidence=0.9, region=(x_[0] + 571, x_[1] + 346, 226, 324))
            pyautogui.moveTo(x)
            pyautogui.rightClick()
            left_click(f'PLAYER_INVENTARY/options/{options}.png')
    #Open inventary(if not in a bank), Locate & Count items on screen
    if not itemcheck('common/bank_opened.png') and not itemcheck(item_picture.lower()):
        open_inventary()
    amount = 0
    location_list = []
    path = img_folder + item_picture
    x_ = get_winpos()
    game_region = (x_[0] + 571, x_[1] + 346, 226, 324)
    for x in pyautogui.locateAllOnScreen(path, confidence=0.9, region=game_region):
        amount += 1
        location_list.append(list(x))

    action = action.lower()
    if action == 'amount':
        return amount

    elif action == 'use':
        do_actions(item_picture, action)
    
    elif action == 'drop':
        do_actions(item_picture, action)

    elif action == 'dropall':
        for x in range(len(location_list)):
            action = 'drop'
            time.sleep(0.6)
            do_actions(item_picture, action)

    elif action == 'depositall':
        do_actions(item_picture, action)

#Image folder
img_folder = read_config('config.ini', 'IMAGE FOLDER', 'folder')
#Player State
p_state = 'idle'