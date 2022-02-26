from tools import *

#Fix RUNELITE opacity (overlay color)
#Fix healing circle 

def relbot(action):
    #Actual Bot/Automation
    def settings():

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
            crab_pause_x, crab_pause_y = read_config('config.ini', 'Crab Bot', 'crab_ending')
            crab_roll = read_config = read_config('config.ini', 'Crab Bot', 'crab_ending_rand_pause')
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
                            #Check Hp
    #User Options
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
        pass
        #This Section is purely for Testing & implementing
    else:
        
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