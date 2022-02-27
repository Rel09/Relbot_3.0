from tools import *

#Fix healing circle 

def relbot(action):
    #Actual Bot/Automation
    def settings(_mode_):

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
        #----Overlay color
        left_click('rl_settings/runelite_overlaysetttings.png')
        left_click_from('rl_settings/runelite_overlaycolor.png',100, 0)
        left_click_from('rl_settings/runelite_overlaycolor_opacity.png', 320, 0)
        pyautogui.hotkey('ctrl', 'a')
        write('255', 1)
        left_click_from('rl_settings/runelite_overlaycolor_opacity.png', 350, -350)
        left_click('rl_settings/runelite_overlaysetttings.png')
        #--Windows Settings
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

        #0 is for Tutorial island, Skip in-game settings
        if _mode_ == 1:
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
            crab_roll = read_config('config.ini', 'Crab Bot', 'crab_ending')
            crab_pause_x, crab_pause_y  = read_config('config.ini', 'Crab Bot', 'crab_ending_rand_pause').split(',')
        except:print(f'{now_time()} ERROR [Config.ini - crab_roll or crab_ending_rand_pause')

        bot = pyautogui.confirm(text='Import Sprite?', title='RelBot', buttons=['yes', 'no'])
        if bot == 'yes':
            import_sprite('[{"RegionId":6966,"RegionX":3,"RegionY":1,"plane":0,"spriteId":1980,"scale":100},{"RegionId":6966,"RegionX":11,"RegionY":8,"plane":0,"spriteId":1981,"scale":100},{"RegionId":6966,"RegionX":21,"RegionY":5,"plane":0,"spriteId":1982,"scale":100},{"RegionId":6966,"RegionX":33,"RegionY":6,"plane":0,"spriteId":1983,"scale":100},{"RegionId":6966,"RegionX":59,"RegionY":0,"plane":0,"spriteId":1985,"scale":100},{"RegionId":6966,"RegionX":57,"RegionY":14,"plane":0,"spriteId":1987,"scale":100},{"RegionId":6966,"RegionX":45,"RegionY":1,"plane":0,"spriteId":1993,"scale":100}]')
        
        first_loop = True
        while True:
            idle_switch = True
            toggle_run()

            #From the Bank to the Chest
            for x in range(1, 7):                    
                if x != 1 or first_loop:
                    print(f'{now_time()} {x} - From Bank to Chest')
                    while True:
                        if itemcheck(f'crabs/sprite{x}.png'):
                            left_click_from(f'crabs/sprite{x}.png', random.randint(-5, 5), random.randint(-15, -7))
                            break
                        else:print(f'{now_time()} Not detecting [sprite{x}]')

                        toggle_run()

                    time_Start = datetime.datetime.now()
                    while r_timer(time_Start, 12) or not player_InFight('player_state/crab.png'):
                        pass
                        #Check Hp

            #When at the chest, Roll Dice to IDLE
            roll_dice = random.randint(1, int(crab_roll))
            print(f'{now_time()} Roll Dice [ {roll_dice} ]')

            #If the Dice roll 1 or 2
            if roll_dice == 1 or roll_dice == 2:
                print(f"{now_time()} Going to IDLE Spot [ {roll_dice} ]")
                for x in range(1, 4):
                    while True:
                        if itemcheck(f'crabs/rand_ending\{roll_dice}\{x}.png'):
                            left_click_from(f'crabs/rand_ending\{roll_dice}\{x}.png', random.randint(-5, 5), random.randint(-5, 5))
                            print('9 second pause ..[DEV]')
                            time.sleep(9)
                            break
                        else:print(f'{now_time()} Not detecting [sprite{x}]')
                        
                        toggle_run()

                #Pause in IDLE spot
                _crabpause = random.randint(int(crab_pause_x), int(crab_pause_y))
                print(f'{now_time()} Pause [{_crabpause} seconds]')
                idle_switch = False
                time.sleep(_crabpause)

                #From IDLE spot to chest
                for x in range(2, 0, -1):
                    print(f'{now_time()} Path[{x}] - From IDLE to Chest')
                    while True:
                        if itemcheck(f'crabs/rand_ending\{roll_dice}\{x}.png'):
                            left_click_from(f'crabs/rand_ending\{roll_dice}\{x}.png', random.randint(-5, 5), random.randint(-5, 5))
                            time.sleep(7)
                            break
                        else:print(f'{now_time()} Not detecting [sprite{x}]')

                        toggle_run()

            #From chest to Bank
            first_loop = False

            for x in range(6, 0, -1):
                if x != 6 or not idle_switch:
                    print(f'{now_time()} Path[{x}] - From Chest to Bank')
                    
                    while True:
                        if itemcheck(f'crabs/sprite{x}.png'):
                            left_click_from(f'crabs/sprite{x}.png', random.randint(0, 5), random.randint(-15, -10))
                            break
                        else:print(f'{now_time()} Not detecting [sprite{x}]')

                        toggle_run()

                    time_Start = datetime.datetime.now()
                    while r_timer(time_Start, 12) or not player_InFight('player_state/crab.png'):
                        pass
    def chicken():
        bot = pyautogui.confirm(text='Import Sprite and Config?', title='RelBot', buttons=['yes', 'no'])
        if bot == 'yes':
            select_target('Chicken')
            import_sprite('[{"RegionId":12851,"RegionX":22,"RegionY":35,"plane":0,"spriteId":1983,"scale":100}]')

        while True:
            left_click_from('chicken/location.png', 30, 15)
            time.sleep(3)
            engage_npc('Chicken')                        
    def tutorial_island(__username):
        path = 'Bot/tutorial_island/'
        #----------------First Page, Typing Username-----------------
        while True:
            #Click on Display name, then write name
            left_click_from(f'{path}1nickname.png', 0, 55)
            time.sleep(0.7)

            pyautogui.press('backspace', presses=200)
            write(__username, 0)
            left_click(f'{path}2lookupname.png')
            time.sleep(2)
            
            if itemcheck(f'{path}2.1notavailable.png'):
                print(f'{now_time()} Cannot use this username, Please try another one')
                continue

            elif itemcheck(f'{path}2.2available.png'):
                print(f'{now_time()} {__username} is Valid')
                break

        left_click(f'{path}3setname.png')
        time.sleep(2)

        #----------------Second page, Character page---------------  
        
        #----Design list (head,jaw,torso,arms,hands,legs,feet)
        list_design = [30, 60, 97, 130, 170, 200, 235]
        #Left or Right
        list_design_side = [-50, 60]

        for x in list_design:
            roll = random.randint(1,2)
            if roll == 1:
                side = list_design_side[0]
            else:
                side = list_design_side[1]

            roll = random.randint(1,8)
            for each in range(roll):
                #Might change this for something faster, like click=x)
                left_click_from(f'{path}4design.png', side, x)

        #------Colour list (Hair,Torso,Legs,Feet,Skin)
        list_colour = [30, 65, 100, 135, 170]
        list_color_side = [-50, 50]

        for x in list_colour:
            roll = random.randint(1,2)
            if roll == 1:
                side = list_color_side[0]
            else:
                side = list_color_side[1]

            roll = random.randint(1,8)
            for each in range(roll):
                #Might change this for something faster, like click=x)
                left_click_from(f'{path}5colour.png', side, x)

        #Choose the sex of the character
        roll = random.randint(1,2)
        if roll == 1:
            side = list_color_side[0]
        else:
            side = list_color_side[1]

        left_click_from(f'{path}5colour.png', side, 237)
        left_click(f'{path}6confirm.png')
        #-------------------------------Tutorial Island Start
        #-----------------------Set the screen correctly
        settings(0)
        
        #Target Gielinor Guide
        while True:
            left_click(f'{path}7gielinor_guide.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x5
        for x in range(6):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,4))

        #I am an experienced player lol
        left_click(f'{path}8iamexperienced.png')

        #Click here to Continue x3
        for x in range(2):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(1,3))

        #Settings icon
        left_click(f'{path}9settings.png')


        #Target Gielinor Guide
        while True:
            left_click(f'{path}7gielinor_guide.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x2
        for x in range(1):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(1,3))

        sprite = ''
        #NEED TO LOAD SPRITE

        #Select the next NPC
        select_target('Survival Expert')

        #Open the door
        left_click(f'{path}10door.png')

        #Get close to the next npc
        left_click(f'{path}11map.png')

        #Target Survival Expert
        while True:
            left_click(f'{path}12survival_expert.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x3
        for x in range(2):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(1,3))

        #Click on the inventary
        left_click(f'{path}13inventary.png')

        #Click on Fish
        left_click(f'{path}14fish.png')

        #Next to continue
        left_click(f'common/click_here_to_continue.png')

        #Click on Stats
        left_click(f'{path}15stats.png')

        #Target Survival Expert
        while True:
            left_click(f'{path}12survival_expert.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x3
        for x in range(2):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(1,3))
        #--------------Make fire camp
        
        #Click on tree
        left_click(f'{path}16tree.png')
        time.sleep(6)

        #Cut some more
        left_click(f'{path}16tree.png')

        #Next to continue
        left_click(f'common/click_here_to_continue.png')

        #User the Tinder Box
        use_item('PLAYER_INVENTARY/tinderbox.png','use')

        #Use with the wood
        left_click('PLAYER_INVENTARY/wood.png')

        #-----------------------Cooking

        #Select shrimp
        use_item('PLAYER_INVENTARY/shrimp.png', 'use')

        #Click on fire
        left_click(f'{path}17fire.png')

        #Click to continue
        left_click(f'common/click_here_to_continue.png')
        

        #------------------- Moving to next spot

        #Get close to the gate
        left_click(f'{path}18map.png')

        #Open the Gate
        left_click_from(f'{path}19sprite.png', -20, 0)

        #Get close to the house
        left_click(f'{path}20map.png')

        #prepare for the next npc
        select_target('Master Chef')

        #Open the door
        left_click(f'{path}21opendoor.png')


    #User Options
    if action == 'Settings':
        pyautogui.alert('Make sure Runelite is opened\n& click OK')
        time.sleep(1.5)
        settings(0)

    elif action == 'Chicken':
        pyautogui.alert("Make sure you're near the chicken spot\nNorth-Right of Lumbridge\n& click OK")
        time.sleep(1.5)
        chicken()
    elif action == 'Crabs':
        pyautogui.alert("Make sure you're on the beach infront of the stash\n& click OK")
        time.sleep(1.5)
        crabs()

if __name__ == '__main__':

    dev = 1
    if dev == 1:
        #auto_relog()
        #relbot('Chicken')
        #tutorial_island()
        path = 'Bot/tutorial_island/'

       # use_item('PLAYER_INVENTARY/shrimp.png', 'use')

        select_target('Master Chef')

        
       
        

        
        
        



        


    




        #left_click_from('chicken/location.png', 30, 15)
        #This Section is purely for Testing & implementing
        pass
    else:
        
        botlist = ["Runelite Settings", "Chicken Farming", "Crab Farming"]
        while True:
            bot = pyautogui.confirm(text='Choose bot action', title='RelBot', buttons=botlist)

            # Runelite Settings
            if bot == "Runelite Settings":
                relbot('Settings')

            # Crab Farming
            elif bot == "Crab Farming":
                relbot('Crabs')

            elif bot == "Chicken Farming":
                relbot('Chicken')

            # If X is clicked
            elif bot == None:
                print("Exit")
                quit()