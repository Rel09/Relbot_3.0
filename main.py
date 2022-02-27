from select import select
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
    def tutorial_island():
        path = 'Bot/tutorial_island/'
        #----------------First Page, Typing Username-----------------
        while True:
            __username = input('Type Username:> ')
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
        
        select_target('Gielinor Guide')

        #Target Gielinor Guide
        while True:
            left_click(f'{path}7gielinor_guide.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x5
        for x in range(4):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,4))

        #I am an experienced player lol
        left_click(f'{path}8iamexperienced.png')

        #Click here to Continue x3
        for x in range(2):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,4))

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
            time.sleep(random.randint(2,4))

        import_sprite('[{"RegionId":12336,"RegionX":26,"RegionY":35,"plane":0,"spriteId":1980,"scale":100},{"RegionId":12336,"RegionX":30,"RegionY":23,"plane":0,"spriteId":1982,"scale":100},{"RegionId":12336,"RegionX":27,"RegionY":23,"plane":0,"spriteId":1985,"scale":100},{"RegionId":12336,"RegionX":18,"RegionY":19,"plane":0,"spriteId":1989,"scale":100},{"RegionId":12336,"RegionX":7,"RegionY":12,"plane":0,"spriteId":1991,"scale":100},{"RegionId":12336,"RegionX":4,"RegionY":10,"plane":0,"spriteId":1970,"scale":100},{"RegionId":12336,"RegionX":1,"RegionY":18,"plane":0,"spriteId":1971,"scale":100},{"RegionId":12336,"RegionX":2,"RegionY":34,"plane":0,"spriteId":1956,"scale":100},{"RegionId":12336,"RegionX":4,"RegionY":48,"plane":0,"spriteId":1957,"scale":100},{"RegionId":12336,"RegionX":14,"RegionY":54,"plane":0,"spriteId":1964,"scale":100},{"RegionId":12336,"RegionX":17,"RegionY":47,"plane":0,"spriteId":1968,"scale":100}]')

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
            time.sleep(random.randint(2,4))

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
            time.sleep(random.randint(2,4))
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

        #SET NPC BACKGROUND TO BLACK
        #Target Master Chef
        while True:
            left_click(f'{path}22masterchief.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x3
        for x in range(3):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,4))

        #Mix the Flour
        use_item('PLAYER_INVENTARY/flour.png', 'use')

        #With the Water
        left_click('PLAYER_INVENTARY/water.png')

        #Get closer to the sprite
        left_click(f'{path}23map.png')
        time.sleep(5)

        #Make bread
        left_click_from(f'{path}24sprite.png', -10, 25)
        time.sleep(5)

        #Get Closer to the door
        left_click(f'{path}25map.png')

        #Leave the house
        left_click_from(f'{path}26sprite.png', -15, 0)
        time.sleep(3)

        #Change house 1/3
        left_click(f'{path}27sprite.png')
        time.sleep(6)

        #Change house 2/3
        left_click(f'{path}28sprite.png')
        time.sleep(6)

        #Change house 3/3
        left_click(f'{path}29sprite.png')
        time.sleep(7)

        #Enter the house
        left_click_from(f'{path}30sprite.png',0, 10)

        #Select Quest Guide
        select_target('Quest Guide')

        #Target Quest Guide
        while True:
            left_click(f'{path}31questguide.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue
        left_click(f'common/click_here_to_continue.png')

        #Click on the Quest page
        left_click(f'{path}32questpage.png')

        #Target Quest Guide
        while True:
            left_click(f'{path}31questguide.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x6
        for x in range(7):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(1,3))

        #Get closer to the ladder
        left_click_from(f'{path}33sprite.png', -20, 0)   

        #Get down the Ladder
        left_click_from(f'{path}33sprite.png', -30, -10) 

        #-------------------------------------------Mines

        import_sprite('[{"RegionId":12436,"RegionX":9,"RegionY":35,"plane":0,"spriteId":1960,"scale":100},{"RegionId":12436,"RegionX":7,"RegionY":23,"plane":0,"spriteId":1963,"scale":100},{"RegionId":12436,"RegionX":22,"RegionY":32,"plane":0,"spriteId":1964,"scale":100},{"RegionId":12436,"RegionX":29,"RegionY":38,"plane":0,"spriteId":1966,"scale":100},{"RegionId":12436,"RegionX":39,"RegionY":45,"plane":0,"spriteId":1967,"scale":100}]')

        select_target('Mining Instructor')

        #Get closer to the instructor
        left_click(f'{path}34sprite.png')
        time.sleep(8)

        #And a little bit closer
        left_click_from(f'{path}34sprite.png', 0, 5)
        time.sleep(3)

        #Target Mining instructor
        while True:
            left_click(f'{path}35mininginstructor.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x5
        for x in range(4):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(1,3))

        #Mining
        while True:
            left_click(f'{path}36mining.png')
            time.sleep(7)
            if itemcheck(f'common/click_here_to_continue.png'):
                    break

        #Get closer to the Tin ore
        left_click_from(f'{path}34sprite.png', 20, 20)
        time.sleep(8)

        #Get closer to LOven
        left_click_from(f'{path}34sprite.png', -8, 45)
        time.sleep(5)

        #Use the oven
        left_click(f'{path}38sprite.png')
        time.sleep(8)

        #And a little bit closer
        left_click_from(f'{path}34sprite.png', 0, 5)
        time.sleep(3)

        #Target Mining instructor
        while True:
            left_click(f'{path}35mininginstructor.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x3
        for x in range(2):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(1,3))

        #Get next to the anvil
        left_click_from(f'{path}34sprite.png', 5, 30)
        time.sleep(3)

        #Click on the anvil
        left_click(f'{path}39anvil.png')

        #Make a dagger
        left_click(f'{path}40dagger.png')

        #Get to the next zone
        left_click_from(f'{path}34sprite.png', 54, 13)
        
        #--------------------------------COMBAT 
        #Select the Next NPC
        select_target('Combat Instructor')

        #Open the gate
        left_click_from(f'{path}41sprite.png', 5, 20)

        #Get closer to the instructor
        left_click_from(f'{path}42sprite.png', 20, 0)

        #Target Mining instructor
        while True:
            left_click(f'{path}43combatinstructor.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x3
        for x in range(2):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,4))
        
        #Equip dagger 1/3
        left_click(f'{path}44icon.png')

        #Equip dagger 2/3
        left_click(f'{path}45icon.png')

        #Equip dagger 3/3
        left_click(f'{path}46dagger.png')

        #Close Equip window
        left_click_from(f'{path}47closewindow.png', 230, 0)

        #Target Combat instructor
        while True:
            left_click(f'{path}43combatinstructor.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x2
        for x in range(1):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,4))

        #Equip sword&shield
        left_click(f'{path}48sword.png')
        left_click(f'{path}49shield.png')

        #Click on skills tab
        left_click(f'{path}50skills.png')

        #Get ready for the fight
        select_target('Giant rat')

        #Get close to the gate
        left_click_from(f'{path}51sprite.png', 0, -5)
        time.sleep(6)

        #Open the gate
        left_click_from(f'{path}52sprite.png', -15, -20)

        #kill ehc leader
        engage_npc('Giant rat')

        #Get close to the gate
        left_click_from(f'{path}51sprite.png', 0, -5)
        time.sleep(4)

        #Open the gate
        left_click_from(f'{path}52sprite.png', -10, -30)

        #Get closer to the instructor
        left_click_from(f'{path}42sprite.png', 20, 0)

        #Select the Combat instructor
        select_target('Combat Instructor')

        #Target Combat instructor
        while True:
            left_click(f'{path}43combatinstructor.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x4
        for x in range(3):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,4))

        #Get ready for the fight
        select_target('Giant rat')

        #Grab Bow & Arrow
        open_inventary()
        left_click(f'{path}52bow.png')
        left_click(f'{path}53arrow.png')

        #Get close to the gate
        left_click_from(f'{path}51sprite.png', 0, -5)

        #Shoot Rat with a Bow
        while True:
            left_click(f'{path}54rat.png')
            time.sleep(6)
            if itemcheck(f'{path}55rat.png'):
                break
            #Get close to the gate
            left_click_from(f'{path}51sprite.png', 0, -5)
            time.sleep(5)

        #Wait until the fight is done
        while itemcheck(f'{path}55rat.png'):
            pass

        #Get closer of the exit
        left_click_from(f'{path}51sprite.png', 0, -40)
        time.sleep(8)

        #Climb the ladder
        left_click(f'{path}56ladder.png')

        #-------------------------Next Area

        import_sprite('[{"RegionId":12336,"RegionX":26,"RegionY":35,"plane":0,"spriteId":1980,"scale":100},{"RegionId":12336,"RegionX":30,"RegionY":23,"plane":0,"spriteId":1982,"scale":100},{"RegionId":12336,"RegionX":27,"RegionY":23,"plane":0,"spriteId":1985,"scale":100},{"RegionId":12336,"RegionX":18,"RegionY":19,"plane":0,"spriteId":1989,"scale":100},{"RegionId":12336,"RegionX":7,"RegionY":12,"plane":0,"spriteId":1991,"scale":100},{"RegionId":12336,"RegionX":4,"RegionY":10,"plane":0,"spriteId":1970,"scale":100},{"RegionId":12336,"RegionX":1,"RegionY":18,"plane":0,"spriteId":1971,"scale":100},{"RegionId":12336,"RegionX":2,"RegionY":34,"plane":0,"spriteId":1956,"scale":100},{"RegionId":12336,"RegionX":4,"RegionY":48,"plane":0,"spriteId":1957,"scale":100},{"RegionId":12336,"RegionX":14,"RegionY":54,"plane":0,"spriteId":1964,"scale":100},{"RegionId":12336,"RegionX":17,"RegionY":47,"plane":0,"spriteId":1968,"scale":100}],{"RegionId":12336,"RegionX":50,"RegionY":51,"plane":0,"spriteId":1967,"scale":100}],{"RegionId":12336,"RegionX":59,"RegionY":35,"plane":0,"spriteId":1968,"scale":100}],{"RegionId":12336,"RegionX":60,"RegionY":16,"plane":0,"spriteId":1969,"scale":100}]')

        #Get close to the bank
        left_click(f'{path}57bank.png')
        time.sleep(10)

        #Open the Bank
        left_click(f'{path}58bank.png')

        #Close the bank
        left_click_from(f'{path}59bank.png', 240, 0)

        #Get closer to the booth
        left_click_from(f'{path}57bank.png', -10, 10)
        
        time.sleep(3)
        #Click on Booth
        left_click(f'{path}60bank.png')

        #Click here to Continue x3
        for x in range(2):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(1,3))

        #Exit the booth
        left_click_from(f'{path}61poll.png', 230, 0)
        
        #Get close to the door
        left_click_from(f'{path}57bank.png', 10, -4)
        time.sleep(3)

        #Open the door
        left_click(f'{path}62closeddoor.png')

        #------------------------------------------Next room
        #Switch target to guide
        select_target('Account Guide')


        #Target account guide
        while True:
            left_click(f'{path}63guide.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break
            
         #Click here to Continue x5
        for x in range(4):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(1,3))

        #Click on the Account tab
        left_click(f'{path}64account.png')

        #Re-Target account guide
        while True:
            left_click(f'{path}63guide.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x16
        for x in range(15):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(1,3))

        #Get closer to the door
        left_click_from(f'{path}57bank.png', 30, -4)
        time.sleep(3)

        #Opening the door
        left_click(f'{path}65door.png')
        time.sleep(2)
        
        #-----------------------Next area

        #Walking outside
        left_click_from(f'{path}57bank.png', 50, 40)
        time.sleep(5)
        
        #Getting near the house
        left_click(f'{path}66sprite.png')
        time.sleep(4)

        #Entering the house
        left_click_from(f'{path}66sprite.png', -30, 0)

        #Target the NPC
        select_target('Brother Brace')

        #Target Brother brace
        while True:
            left_click(f'{path}67brotherbrace.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x2
        for x in range(1):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(1,3))

        #Click on prayer icon
        left_click(f'{path}68prayer.png')

        #Target Brother brace
        while True:
            left_click(f'{path}67brotherbrace.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x4
        for x in range(3):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(1,3))

        #Target the Smiley icon
        left_click(f'{path}69icon.png')

        #Target Brother brace
        while True:
            left_click(f'{path}67brotherbrace.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x4
        for x in range(3):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(1,3))

        #Getting close of the door
        left_click_from(f'{path}66sprite.png', -35, 15)
        time.sleep(4)

        #Leaving the house
        left_click(f'{path}70door.png')
        time.sleep(2)

        #----------------------Next area

        #Getting closer of the house
        left_click(f'{path}71sprite.png')

        #Enter the house
        left_click_from(f'{path}71sprite.png', 40, 0)
        
        #Target the magic instructor
        select_target('Magic Instructor')

        #Target the Magic Instructor
        while True:
            left_click(f'{path}72magicinstructor.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x2
        for x in range(1):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(1,3))

        #Click on the spell book
        left_click(f'{path}73spellbook.png')

        #Target the Magic Instructor
        while True:
            left_click(f'{path}72magicinstructor.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x2
        for x in range(1):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(1,3))

        #Select spell
        left_click(f'{path}74spell.png')

        #Selecting Chicken
        select_target('Chicken')    


      



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
    elif action == 'Tutorial Island':
         time.sleep(1.5)
         tutorial_island()

if __name__ == '__main__':

    dev = 0
    if dev == 1:
        #Ajouter Fill color = black ? pour les NPC
        path = 'Bot/tutorial_island/'
        
        

        while True:
            left_click(f'NPC_ENGAGE/chicken.png')
            time.sleep(6)
            if itemcheck(f'{path}55rat.png'):
                break
            #Get close to the gate
            left_click_from(f'{path}51sprite.png', 0, -5)
            time.sleep(5)
 



        #This Section is purely for Testing & implementing
        pass
    else:
        
        botlist = ["Runelite Settings","Tutorial Island", "Chicken Farming", "Crab Farming"]
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

            elif bot == 'Tutorial Island':
                relbot('Tutorial Island')

            # If X is clicked
            elif bot == None:
                print("Exit")
                quit()