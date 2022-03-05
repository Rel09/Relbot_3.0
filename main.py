from select import select
from tools import *

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
        #left_click_from('rl_settings/sprite_showtiles.png', 160, 0)
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

        bot = input('Skip initial config? ( Y / N )').lower()
        if bot != 'y':
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
        bot = input('Skip initial config? ( Y / N )').lower()
        if bot != 'y':
            select_target('Chicken')
            import_sprite('[{"RegionId":12851,"RegionX":22,"RegionY":35,"plane":0,"spriteId":1983,"scale":100}]')

        while True:
            left_click_from('chicken/location.png', 30, 15)
            time.sleep(3)
            engage_npc('Chicken')                        
    def tutorial_island(__username,__skipsettings):
        path = 'Bot/tutorial_island/'
        #----------------First Page, Character Creation-----------------
        if username != None:
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
                    __username = input('Enter Character username :> ')
                    continue

                elif itemcheck(f'{path}2.2available.png'):
                    #print(f'{now_time()} {__username} is valid')
                    break

            left_click(f'{path}3setname.png')
            time.sleep(2)

            #----------------Second page, Character page---------------  
            
            #----Design list (head,jaw,torso,arms,hands,legs,feet)
            list_design = [30, 60, 97, 130, 170, 200, 235]
            list_design_side = [-50, 60]
            list_colour = [30, 65, 100, 135, 170]
            list_color_side = [-50, 50]

            #Choose the sex of the character
            roll = random.randint(1,2)
            if roll == 1:
                #already a male
                pass
            else:
                side = list_color_side[1]
                left_click_from(f'{path}5colour.png', side, 237)

            

            for x in list_design:
                roll = random.randint(1,2)
                if roll == 1:
                    side = list_design_side[0]
                else:
                    side = list_design_side[1]

                roll = random.randint(1,8)
                left_clicks_from(f'{path}4design.png', side, x, roll)

            #------Colour list (Hair,Torso,Legs,Feet,Skin)

            for x in list_colour:
                roll = random.randint(1,2)
                if roll == 1:
                    side = list_color_side[0]
                else:
                    side = list_color_side[1]

                roll = random.randint(1,8)
                left_clicks_from(f'{path}5colour.png', side, x, roll)

            left_click(f'{path}6confirm.png')
        #-------------------------------Tutorial Island Start
        #-----------------------Set the screen correctly
        if __skipsettings != 'y':
            settings(0)
        
        select_target('Gielinor Guide,Survival Expert,Master Chef,Quest Guide,Mining Instructor,Combat Instructor,Giant rat,Account Guide,Brother Brace,Magic Instructor,Chicken')

        #Target Gielinor Guide
        while True:
            left_click(f'{path}7gielinor_guide.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x6
        for x in range(5):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,3))

        #I am an experienced player lol
        left_click(f'{path}8iamexperienced.png')

        #Click here to Continue x3
        for x in range(3):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,3))

        #Settings icon
        left_click(f'{path}9settings.png')

        #Target Gielinor Guide
        while True:
            left_click(f'{path}7gielinor_guide.png')
            time.sleep(random.randint(2,3))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x2
        for x in range(2):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,3))

        import_sprite('[{"RegionId":12336,"RegionX":30,"RegionY":23,"plane":0,"spriteId":1982,"scale":100},{"RegionId":12336,"RegionX":18,"RegionY":19,"plane":0,"spriteId":1989,"scale":100},{"RegionId":12336,"RegionX":7,"RegionY":12,"plane":0,"spriteId":1991,"scale":100},{"RegionId":12336,"RegionX":4,"RegionY":10,"plane":0,"spriteId":1970,"scale":100},{"RegionId":12336,"RegionX":1,"RegionY":18,"plane":0,"spriteId":1971,"scale":100},{"RegionId":12336,"RegionX":2,"RegionY":34,"plane":0,"spriteId":1956,"scale":100},{"RegionId":12336,"RegionX":4,"RegionY":48,"plane":0,"spriteId":1957,"scale":100},{"RegionId":12336,"RegionX":14,"RegionY":54,"plane":0,"spriteId":1964,"scale":100},{"RegionId":12336,"RegionX":17,"RegionY":47,"plane":0,"spriteId":1968,"scale":100},{"RegionId":12336,"RegionX":26,"RegionY":36,"plane":0,"spriteId":1961,"scale":100}]')

        #Select the next NPC
        #select_target('Survival Expert')

        #Get closer of the door
        left_click_from(f'{path}10door.png', -5, 0)
        time.sleep(3)

        #Exit the house
        left_click_from(f'{path}10door1.png', -7, 32)
        time.sleep(2)



        #------------------------------ next area

        #Get close to the next npc
        _x = random.randint(-10, 10)
        _y = random.randint(-10, 10)
        left_click_from(f'{path}11map.png', _x, _y)
        time.sleep(random.randint(5, 6))

        #Target Survival Expert
        while True:
            left_click(f'{path}12survival_expert.png')
            time.sleep(random.randint(1, 2))
            if itemcheck(f'{path}12survival_expert_confirm.png'):
                break

        #Click here to Continue x3
        for x in range(2):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2, 3))

        #Get close to the Fishs
        while True:
            if itemcheck(f'{path}11map.png'):
                left_click_from(f'{path}11map.png', -8, 5)
                break
            elif itemcheck(f'{path}11.5map.png'):
                y = random.randint(-30,30)
                x = random.randint(-5,30)
                left_click_from(f'{path}11.5map.png', x, y)
                time.sleep(3)
                
        time.sleep(random.randint(3, 4))

        #Click on the inventary
        left_click(f'{path}13inventary.png')
        time.sleep(1)

        #Target Fish
        while True:
            left_click(f'{path}14fish.png')
            time.sleep(random.randint(6, 7))
            if itemcheck(f'{path}14fish_confirm.png'):
                left_click_from(f'{path}11map.png', 5, 10)
                time.sleep(random.randint(3, 4))
                break

        #Click on Stats
        left_click(f'{path}15stats.png')
        time.sleep(1)

        #Target Survival Expert
        while True:
            left_click(f'{path}12survival_expert.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x2
        for x in range(2):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,4))

        #--------------Make fire camp
        
        #Get closer to the tree
        left_click_from(f'{path}11map.png', 6, -5)
        time.sleep(random.randint(4, 5))

        #Click on tree
        left_click(f'{path}16tree.png')
        time.sleep(random.randint(6, 7))

        #Click on the inventary
        left_click(f'{path}13inventary.png')

        #User the Tinder Box
        use_item('PLAYER_INVENTARY/tinderbox.png','use')
        time.sleep(random.randint(1, 2))

        #Use with the wood
        left_click('PLAYER_INVENTARY/wood.png')
        time.sleep(random.randint(1, 2))

        #Select shrimp
        use_item('PLAYER_INVENTARY/shrimp.png', 'use')
        time.sleep(random.randint(1, 2))

        #Click on fire
        left_click(f'{path}17fire.png')
        time.sleep(3)

        #Click to continue
        left_click(f'common/click_here_to_continue.png')
        
        #------------------- Moving to next spot

        #Get close to the gate
        left_click(f'{path}18map.png')
        time.sleep(random.randint(6, 7))

        #Open the Gate
        left_click_from(f'{path}19sprite.png', -20, 0)
        time.sleep(random.randint(2, 3))

        #Get close to the house
        left_click(f'{path}20map.png')
        time.sleep(random.randint(6, 7))

        #Open the door
        left_click(f'{path}21opendoor.png')
        time.sleep(random.randint(2, 4))

        input('take chef screenshots')

        #Target Master Chef
        while True:
            left_click(f'{path}22masterchief.png')
            time.sleep(random.randint(2,3))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x3
        for x in range(3):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,3))

        #Mix the Flour
        use_item('PLAYER_INVENTARY/flour.png', 'use')

        #With the Water
        left_click('PLAYER_INVENTARY/water.png')

        #Get closer to the sprite
        left_click(f'{path}23map.png')
        time.sleep(random.randint(4, 6))

        #Make bread
        left_click_from(f'{path}24sprite.png', -10, 25)
        time.sleep(random.randint(5, 7))

        #Get Closer to the door
        left_click(f'{path}25map.png')
        time.sleep(random.randint(5, 7))

        #Leave the house
        left_click_from(f'{path}26sprite.png', -15, 0)
        time.sleep(random.randint(5, 7))

        #Change house 1/3
        left_click(f'{path}27sprite.png')
        time.sleep(random.randint(5, 7))

        #Change house 2/3
        left_click(f'{path}28sprite.png')
        time.sleep(random.randint(6, 7))

        #Change house 3/3
        left_click(f'{path}29sprite.png')
        time.sleep(random.randint(8, 9))

        #Enter the house
        left_click_from(f'{path}30sprite.png',0, 10)
        time.sleep(random.randint(2, 3))

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

        #Click here to Continue x8
        for x in range(8):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,3))

        #Get closer to the ladder
        left_click_from(f'{path}32map.png', -10, -5)
        time.sleep(2)

        #Get down the Ladder
        left_click_from(f'{path}33sprite.png', -24, 10) 
        time.sleep(2)

        #-------------------------------------------Mines

        import_sprite('[{"RegionId":12436,"RegionX":9,"RegionY":35,"plane":0,"spriteId":1960,"scale":100},{"RegionId":12436,"RegionX":7,"RegionY":23,"plane":0,"spriteId":1963,"scale":100},{"RegionId":12436,"RegionX":22,"RegionY":32,"plane":0,"spriteId":1964,"scale":100},{"RegionId":12436,"RegionX":29,"RegionY":38,"plane":0,"spriteId":1966,"scale":100},{"RegionId":12436,"RegionX":39,"RegionY":45,"plane":0,"spriteId":1967,"scale":100}]')

        #Get closer to the instructor
        left_click(f'{path}34sprite.png')
        time.sleep(random.randint(7, 8))

        #And a little bit closer
        left_click_from(f'{path}34sprite.png', 0, 5)
        time.sleep(random.randint(3, 4))

        #Target Mining instructor
        while True:
            left_click(f'{path}35mininginstructor.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x5
        for x in range(5):
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
        time.sleep(random.randint(8, 9))

        #Mining
        while True:
            left_click(f'{path}37mining.png')
            time.sleep(7)
            if itemcheck(f'common/click_here_to_continue.png'):
                    break

        #Get closer to Oven
        left_click_from(f'{path}34sprite.png', -8, 45)
        time.sleep(random.randint(5, 6))

        #Use the oven
        left_click(f'{path}38sprite.png')
        time.sleep(random.randint(7, 8))

        #And a little bit closer
        left_click_from(f'{path}34sprite.png', 0, 5)
        time.sleep(random.randint(3, 4))

        #Target Mining instructor
        while True:
            left_click(f'{path}35mininginstructor.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x3
        for x in range(3):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(1,3))

        #Get next to the anvil
        left_click_from(f'{path}34sprite.png', 5, 30)
        time.sleep(3)

        #Click on the anvil
        left_click(f'{path}39anvil.png')

        #Make a dagger
        left_click(f'{path}40dagger.png')
        time.sleep(8)

        #Get to the next zone
        left_click_from(f'{path}34sprite.png', 54, 13)
        
        #--------------------------------COMBAT 

        time.sleep(8)

        #Open the gate
        left_click_from(f'{path}41sprite.png', 5, 20)
        time.sleep(2)

        #Get closer to the instructor
        left_click_from(f'{path}42sprite.png', 20, 0)
        time.sleep(7)

        #Target Mining instructor
        while True:
            left_click(f'{path}43combatinstructor.png')
            time.sleep(random.randint(2,4))
            if itemcheck(f'common/click_here_to_continue.png'):
                break

        #Click here to Continue x3

        for x in range(3):
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
        for x in range(2):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,4))

        #Equip sword&shield
        left_click(f'{path}48sword.png')
        left_click(f'{path}49shield.png')

        #Click on skills tab
        left_click(f'{path}50skills.png')

        #Get ready for the fight
        #select_target('Giant rat')

        #Get close to the gate 667
        left_click_from(f'{path}51sprite.png', -7, -3)
        time.sleep(6)

        #Open the gate
        left_click_from(f'{path}52sprite.png', -12, -26)
        time.sleep(2)

        #kill ehc leader
        engage_npc('Giant rat')

        #Get close to the gate
        left_click_from(f'{path}51sprite.png', 0, -5)
        time.sleep(4)

        #Open the gate
        left_click_from(f'{path}52sprite.png', -10, -30)
        time.sleep(2)

        #Get closer to the instructor
        left_click_from(f'{path}42sprite.png', 20, 0)
        time.sleep(4)

        #Target Combat instructor
        target_until(f'{path}43combatinstructor.png', f'common/click_here_to_continue.png')

        #Click here to Continue x4
        for x in range(4):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,4))

        #Get ready for the fight
        #select_target('Giant rat')

        #Grab Bow & Arrow
        open_inventary()
        left_click(f'{path}52bow.png')
        left_click(f'{path}53arrow.png')

        #Get close to the gate
        left_click_from(f'{path}51sprite.png', 0, -5)
        time.sleep(2)

        #Shoot Rat with a Bow
        while True:
            left_click(f'{path}54rat.png')
            time.sleep(6)
            if itemcheck(f'{path}55rat.png'):
                break

        #Get close to the gate
        left_click_from(f'{path}51sprite.png', 0, -5)
        time.sleep(7)

        #Shoot Rat with a Bow
        while True:
            left_click(f'{path}54rat.png')
            time.sleep(6)
            if itemcheck(f'{path}55rat.png'):
                while itemcheck(f'{path}55rat.png'):
                    time.sleep(1)
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
        time.sleep(4)

        #-------------------------Next Area

        #Get closer of the bank
        left_click_from(f'{path}57sprite.png', 10, 20)
        time.sleep(7)
        
        #We open the bank
        left_click_from(f'{path}58sprite.png', 75, 100)
        time.sleep(2)
       
        #Close the bank
        left_click_from(f'{path}59bank.png', 230, 0)
        
        #Open the Poll Booth
        left_click_from(f'{path}58sprite.png', 0, 182)
        time.sleep(2)
        
        #Click here to Continue x3
        for x in range(2):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,4))
        
        #Close the Poll Booth
        left_click_from(f'{path}60poolhistory.png', 230, 0)
        
        #Get close to the door
        left_click_from(f'{path}58sprite.png', 130, 100)
        time.sleep(2)
        
        #Open the door
        left_click_from(f'{path}58sprite.png', 150, 100)
        time.sleep(2)
        
        #Target the account guide
        target_until(f'{path}61accountguide.png', 'common/click_here_to_continue.png')
        
        #Click 5x
        for x in range(4):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,4))
        left_click(f'{path}62accsettings.png')
        time.sleep(1)
        target_until(f'{path}61accountguide.png', 'common/click_here_to_continue.png')
        
        #Click 17x
        for x in range(16):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,4))
       
        #Click on the door
        left_click_from(f'{path}58sprite.png', 275, 100)
        
        #Get closer of the next area
        left_click_from(f'{path}63mapsprite.png', 5, 15)
        time.sleep(7)
        
        #Even closer
        left_click_from(f'{path}63mapsprite.png', -10, 24)
        time.sleep(2)
        target_until(f'{path}64brotherbrace.png', 'common/click_here_to_continue.png')
        
        #Click 2x
        for x in range(1):
            left_click(f'common/click_here_to_continue.png')
            time.sleep(random.randint(2,4))
        
        #Open the prayer menu
        left_click(f'{path}65prayermenu.png')
        time.sleep(1)
        
        #Target brother brace
        target_until(f'{path}64brotherbrace.png', 'common/click_here_to_continue.png')
        
        #Click 4x
        ctc_x(3)

        #Target brother brace
        target_until(f'{path}64brotherbrace.png', 'common/click_here_to_continue.png')
        
        ctc_x(3)
        
        #Leave the bouse
        left_click_from(f'{path}67sprite.png', -150, 250)
        
        #Get closer of the next house
        left_click_from(f'{path}68mapsprite.png', 0, 15)
        time.sleep(6)
        
        #Get in the house
        left_click_from(f'{path}68mapsprite.png', 35, 15)
        time.sleep(3)

        target_until(f'{path}69magicinstructor.png', 'common/click_here_to_continue.png')
        
        ctc_x(1)
        
        time.sleep(1)
        #Target instructor
        target_until(f'{path}69magicinstructor.png', 'common/click_here_to_continue.png')
        ctc_x(1)
        
        #Click on the Fireball
        left_click(f'{path}71fireball.png')
        time.sleep(1)
        #Attack chicken
        engage_npc('Chicken')

        #Click here to continue
        target_until(f'{path}69magicinstructor.png', 'common/click_here_to_continue.png')
        left_click(f'common/click_here_to_continue.png')
        left_click(f'{path}72mainland.png')
        left_click(f'common/click_here_to_continue.png')
        #-----IRON MAN------- check IRONMAN.png for more info
        left_click(f'{path}73noty.png')
        ctc_x(4)

        

        

    #User Options
    if action == 'Settings':
        input('Make sure Runelite is opened\n& Click Any key to Continue')
        time.sleep(1.5)
        settings(0)
    elif action == 'Chicken':
        input("Make sure you're near the chicken spot\n& Click Any key to Continue")
        time.sleep(1.5)
        chicken()
    elif action == 'Crabs':
        input("Make sure you're near the Beach's Bank\n& Click Any key to Continue")
        time.sleep(1.5)
        crabs()
    elif action == 'Tutorial Island':
        
        #Skip Character Creation?
        skip_username = input('Skip Character Creation? ( Y / N ) :> ').lower()
        if skip_username != 'y':
            while True:
                username = input('Enter Character username :> ')
                if not len(username) > 12:break
                else: print('_____12 Character max_____')


        else: username = None
        #Skip Auto-Setting?  
        skip_settings = input('Skip Auto-Settings? ( Y / N ) :> ').lower()
        print(f'\n\n{now_time()}Bot Starting...')
        
        time.sleep(1.5)
        auto_relog()
        tutorial_island(username,skip_settings)

if __name__ == '__main__':
    pyautogui.FAILSAFE = False

    dev = 0
    if dev == 1:
        #Ajouter Fill color = black ? pour les NPC
        path = 'Bot/tutorial_island/'



    
        #This Section is purely for Testing & implementing
        pass
    else:
        botlist = [ "Runelite Settings",
                    "Tutorial Island",
                    "Chicken Farming",
                    "Crab Farming" ]
        while True:

            print('\n__________       .__ ___.           __   ')
            print('\______   \ ____ |  |\_ |__   _____/  |_ ')
            print(' |       _// __ \|  | | __ \ /  _ \   __/')
            print(' |    |   \  ___/|  |_| \_\ (  <_> )  | ')
            print(' |____|_  /\___  >____/___  /\____/|__|\n')
            print('______________ Bot options _____________\n')
            for i, x in enumerate(botlist):
                print(f'       [{i}] - [{x}]')
            print('________________________________________')
            bot = int(input('\nChoose bot Action:> '))
            bot = botlist[bot]

            if bot == "Runelite Settings":
                relbot('Settings')

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