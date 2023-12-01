#!/usr/bin/env python

##################################################################################
##                                                                              ##
##	SYS-Master Collection Booklet.py                                        ##
##	Auto updates The Master Collection Booklets                             ##           
##                                                                              ##
##	Created By Zachary Lynn.                                                ##
##      Updated on 07.27.2022 by Zachary Lynn for BRPL-ILS.                     ##
##	Copyright © 2021 Boca Raton Public Library. All rights reserved.        ##
##                                                                              ##
##      Mono-thread design.                                                     ##
##	The puautogui module are Required to Properly run                       ##
##      HAS A NETWORK DEPENDANCY of R && Finn                                   ##
##                                                                              ##
##      Forthcoming updates:                                                    ##
##      Not sure what create list was used but 390 and 392 are not available    ##
##      since everything was moved. Remake the needed create list for record    ##
##      number.                                                                 ##
##      Move entire archetecture to Excel                                       ##
##          Move entire archetecture to HTML layout auto-gen layout should be   ##
##      instentanious                                                           ##
##      Change to poly-thread design for glancing over already done portions    ##
##      Ask what booklet to update                                              ##
##                                                                              ##
##################################################################################

# Modules #
import os               #should be able to del and rely on tool__excel or tool__word
import shutil               #should be able to del and rely on tool__excel or tool__word
import subprocess               #should be able to del and rely on tool__excel or tool__word

import pyautogui as a

from __main__ import *
try:
    from tool__ import *
    from tool__Sierra import *
except:
    pass

TOOL.processing.Runtime_03()
TOOL.processing.Failsafe_on()
TOOL.processing.On()

# Definitions
THREAD = SELECT = 0              ###NOT IMPLIMENTED YET
COLLECTION = ''         ###NOT IMPLIMENTED YET
local, user = PATH.Local()
cd, network = PATH.Network(None, None)

datestamp = CHRONOS()

class tools:

    def Database(self):
        TOOL.processing.Runtime_07()
        
        a.write('390')
        a.keyDown('altleft')
        a.keyDown('altright')
        a.press('s')
        a.press('e')
        a.press('p')
        a.keyUp('altright')
        a.keyUp('altleft')
        a.press('b')
        a.press('return')
        a.press('tab', presses=6, interval=1)
        a.write(material)
        a.press('return')
        a.hotkey('alt', 's')
        
        a.keyDown('altleft')
        a.keyDown('altright')
        a.press('x')
        a.press('b')
        a.press('i')
        a.keyUp('altright')
        a.keyUp('altleft')
        a.press('R')
        a.press('return', interval=1)
        a.keyDown('altleft')
        a.keyDown('altright')
        a.keyDown('n')
        a.keyUp('altright')
        a.keyUp('altleft')
        a.write('ILS ADMINISTRATOR')
        a.press('return')
        a.hotkey('ctrl', 'a')
        a.write(sub_dir)
        a.press('return', presses=4, interval=1)


# Updates URL # 
    def URL(self, material):

        print('\n\tFinding a URL for:", x, lines[x]')
 
        with open(network + sub_dir + material[1] + ".txt") as file:
            material = [l.strip() for l in file]
            
        m = 0
        for m in range(len(material)):
            material[m] = material[m].replace(',', '')

            #   Dont need induvidual lines since this is coming from booklet
            #
            #   with open(network + sub_dir + subdir.replace('/', '') + ".txt") as file:
            #       item = [l.strip() for l in file]

            #   n = 0
            #   for n in range(len(item)):
            #       item[n] = item[n].replace(' ', '').split("(")[0]
            #       item[n] = item[n][:0] + '"' + item[n][0:] + '"'

        item = lines[x].split("(")[0]
        item = item[:0] + '"' + item[0:] + '"'
            

        legnth = len(material)
            #   width = len(item)
        m = 0
            #   n = 0

        try:
            while m <= legnth:
                m += 1
                                 
                if item in material[m]:
                    print("\t\tFound a match of:", item, "in", material[m].replace(';', "&"))
                    material[m] = material[m].split("b")[-1]
                    material[m] = material[m][:7]
                    self.http = 'https://bocalibrary.bibliocommons.com/v2/record/' + 'S179' + 'C' + material[m]
                    m = legnth
                    m += 1
                        
                else:
                    pass
                    
        except:
            print("\t\tNo match exists on:", item, "in", material[m])
 
COLLECTION = tools()

##############################################################################################################################

##############################################################################################################################

if __name__ == "__392__": # 392
    print('\n', '* SYS-' + MAIN.NAME + ' *', '\n')
    
    while SELECT == 0:
        print("""   Welcome!
        
        What material booklet are you creating?
        
        Please make a selection from the list below:
            1) Jigsaw Puzzle Booklet
            2) Cake Pan Booklet [UNAVAILABLE]
            3) Literacy Backpack Booklet [UNAVAILABLE]
            4) Citizen Science Kit Booklet [UNAVAILABLE]
            5) STEM Kit Booklet [UNAVAILABLE]
            0) Exit
            
        """)

        MENU = input()

    #choice:JPMC_booklet
        if MENU == '1':
            print("Program starting")
            TOOL.wait(1)
            SELECT = 'x'
            material = 'v', 'JIGSAW'
            sub_dir = 'Jigsaw Puzzles\\'
            sup_dir = 'JPMC_booklet'

    #choice:CPMC_booklet
        elif MENU == '2':
            print("Program starting")
            TOOL.wait(1)
            SELECT = 'x'
            material = 'q', 'CAKE'
            sub_dir = 'Cake Pans\\'
            sup_dir = 'CPMC_booklet'

    #choice:BPlMC_booklet
        elif MENU == '3':
            print("Program starting")
            TOOL.wait(1)
            SELECT = 'x'
            material = 'o', 'Literacy'
            sub_dir = 'Back Packs\Literacy\\'
            sup_dir = 'BPlMC_booklet'

    #choice:BPcMC_booklet
        elif MENU == '4':
            print("Program starting")
            TOOL.wait(1)
            SELECT = 'x'
            material = 'oc', 'Citizen'
            sub_dir = 'Back Packs\Citizen\\'
            sup_dir = 'BPcMC_booklet'

    #choice:BPsMC_booklet
        elif MENU == '5':
            print("Program starting")
            TOOL.wait(1) 
            SELECT = 'x'
            material = 'o', 'STEM'
            sub_dir = 'Back Packs\STEM\\'
            sup_dir = 'BPsMC_booklet'

    #choice:Exit
        elif MENU == '0':
            TOOL.wait(1)
            TOOL.Exit()

            print("\nThank you, have a great day.")
            TOOL.wait(1)
            exit()
            
    #choice:Other
        else:
            print("Invalid program selection.")
            TOOL.wait(1)

################################################################################################################

################################################################################################################

    while SELECT == 'x':
        print("""
        Which list needs to be created:

        Please select your answer:
        Press 'C' if the DATABASE list from Sierra needs to be created.
        Press 'N' if the NETWORK list on the shared drive needs to be created.
        Press 'B' if BOTH lists need to be created.
        Press 'O' if neither of the lists need to be created.
        """)

        SELECT = input()

        if SELECT == 'C' or SELECT == 'c' or SELECT == 'B' or SELECT == 'b':
            print("Creating DATABASE list")
            TOOL.wait(1)
            SIERRA.Launch()
            SIERRA.Create_lists()
            COLLECTION.Database()
            SIERRA.Check_in()
            SIERRA.Exit()

            TOOL.List()
            TOOL.Sort_ascending()

        if SELECT == 'N' or SELECT == 'n' or SELECT == 'B' or SELECT == 'b':
            print("Creating NETWORK list")
            TOOL.wait(1)
            #JIGSAW.Puzzle_list() # this includes sort asend
            exit()

        elif SELECT == 'O' or SELECT == 'o':
            TOOL.wait(1)

        else:
            print("Selection Invalid.")
            SELECT = 'x'
            TOOL.wait(1)

################################################################################################################

################################################################################################################

    ## to do automatic compare and delete of missing items
    
    with open(network + sub_dir + 'list.txt') as file:
            lines = [l.strip() for l in file]

    # initalize no. of lines /3 == no. of table rows #
##    while 1==1:
    count = 0
    for line in open(network + sub_dir + 'list.txt'):
            print(count,lines[count])
            count += 1
##            l-=1
      
    rows = count/3
    rows = int(rows)
    rows = str(rows)
    
    ##    x = 1
    ##    while x!=count:
    ##        JIGSAW.Check_list()
    ##        x+=1

################################################################################################################

################################################################################################################

    TOOL.wait(5) # Dont use sleep but, moving windows #

    # Word #
    # Opens word document and sets up margins and format #

    local = r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'
    subprocess.Popen(local)

    TOOL.wait(7) # Dont use sleep but, waits until word starts #

    a.hotkey('ctrl', 'n')
    a.press('return', presses = 2)

    a.keyDown('altleft')
    a.keyDown('altright')
    a.press('p')
    a.press('m')
    a.press('a')
    a.keyUp('altleft')
    a.keyUp('altright')

    x = 0
    while x!=4:
            a.write('0')
            a.press('tab')
            x+=1

    a.press('return')
    a.press('i')

    a.keyDown('altleft')
    a.keyDown('altright')
    a.press('p')
    a.press('s')
    a.press('z')
    a.press('a')
    a.keyUp('altleft')
    a.keyUp('altright')
    a.press('tab')
    a.write('8.5')
    a.press('tab')
    a.write('9.63')

    a.press('return')
    a.press('i')

    TOOL.processing.Runtime_01()

    a.keyDown('altleft')
    a.keyDown('altright')
    a.press('f')
    a.press('a')
    a.press('o')
    a.press('t')
    a.press('n')
    a.keyUp('altleft')
    a.keyUp('altright')
    a.write(sup_dir[:-10] + "." + datestamp)
    a.press('f4')
    a.hotkey('ctrl','a')
    a.press('backspace', presses=28)
    a.write(network + 'Master Collection Booklets')
    a.press('return')

    a.keyDown('altleft')
    a.keyDown('altright')
    a.press('s')
    a.press('n')
    a.press('t')
    a.press('i')
    a.keyUp('altleft')
    a.keyUp('altright')

    a.press('3')
    a.press('tab')
    a.write(rows)
    a.press('return')

    a.hotkey('ctrl', 'a')
    a.keyDown('altleft')
    a.keyDown('altright')
    a.press('h')
    a.press('a')
    a.press('c')
    a.keyUp('altleft')
    a.keyUp('altright')
    a.press('left')

################################################################################################################

################################################################################################################

    # rework area #

    x=1 # Cell being worked on
    y=0
    n=0 # start pieces and piece++
    page=10
    item=1
    total=count
    psx=999 # infinite case for pieces till sort finds correct number of pices in line
    cell='null'
    pieces='null'
    material='Call no.' # Made executive decision to get rid of p or partial puzzle piece numbers. Just rounding to the whole.
    match='match'
    found='found'

    print('\n--\n--')


    #choice:JPMC_booklet
    if MENU == '1':

        # Filling in the table #
        while x!=count: # Cannot strictly just follow cell as cell increases by one and does NOT account for missing MATERIAL.
                match='match'
                total=x*100/count
                print('\nProcessing Cell:', x, 'of', page, ' - ', lines[x].replace('.jpeg', ''), 'Remaining:', '%', total , 'Done')

                if x==page: # Create new page at cell(10) #
                        page+=9
                        a.hotkey('ctrl', 'return')
                        a.press('right')
                        
                # MATERIAL #
                # Assigning current line material call no. #
                while material != lines[x]:
                        print("Searching for", sub_dir.replace('/', ''), "number")
                        print('\t', material.replace('.jpeg', ''), ' -> ', lines[x].replace('.jpeg', ''), 'of', count, sub_dir.replace('/' ,''), '\n')
                        y+=1
                        n=0
                        item=str(y)
                        
                        material = 'JIGSAW ' + item + '(' + pieces + ').jpeg' # ???????????
                        print('Searching for number of pieces\n') # ?????????????
                              
                        while n<100: # first to 100
                            n+=5
                            pieces=str(n)
                            
                            jigsaw = 'JIGSAW ' + item + '(' + pieces + ').jpeg'
                            print('\t\t ', material.replace('.jpeg', ''))
                            
                            if material == lines[x]:
                                    print('Found a match on:', lines[x].replace('.jpeg', ''))
                                    n=999
                            
                        while n!=psx: # count by 50 from here
                            n+=50
                            pieces=str(n)
                            
                            material = 'JIGSAW ' + item + '(' + pieces + ').jpeg'
                            print('\t\t ', jigsaw.replace('.jpeg', ''))
                            
                            if material == lines[x]:
                                    print('Found a match on:', lines[x].replace('.jpeg', ''))
                                    n=999
                                    
                            if n==2500:
                                    print('\nNo match found')
                                    match='found'
                                    n=999
                                
                while match!=found: 
                    a.write(lines[x].replace('.jpeg', ''))

            # URL #
            # Total Fuckery of curcumventing WORD's autocomplete hypertext "feature" BS #
        
                    TOOL.processing.Runtime_01()
                    COLLECTION.URL(material)
                    TOOL.processing.Runtime_03()

            # name linking #
                    a.keyDown('shiftleft')
                    a.keyDown('shiftright')
                    a.keyDown('ctrlleft')
                    a.keyDown('ctrlright')
                    a.press('up')        
                    a.keyUp('ctrlleft')
                    a.keyUp('ctrlright')
                    a.keyUp('shiftleft')
                    a.keyUp('shiftright')
                    a.press('apps')
                    a.press('i', presses=2)
                    a.press('return')
                    
            # actual link insert. * MAKE SURE YOUR WORD IS NOT AUTOCOMPLETING Links, Turn this "feature" off #
            # Unfortunately you CANT turn off this feature and you'll never know the autofill it will use you you have to clear your internet auto fill cache before using, Rediculious ##

                    # Steps to clearing AutoComplete setting in WORD #
                    # 1.Press and hold the Windows key + R.
                    # 2.Type inetcpl.cpl.
                    # 3.Click on Content tab.
                    # 4.Under AutoComplete, click on the Settings button.
                    # 5.Uncheck all items, and then click on the Delete AutoComplete History... button.
                    # 6.Click on OK button.

            # Should not have to hotfix / code around microsoft. These "features" are intrusive, unhelpful, and aweful #
                    a.write(COLLECTION.http)
                    #a.hotkey('ctrl', 'v') # shit workaround
                    a.press('return')

                    a.press('return')

            # Insert Picture #
                    a.keyDown('altleft')
                    a.keyDown('altright')
                    a.press('n')
                    a.press('p')
                    a.press('d')
                    a.keyUp('altleft')
                    a.keyUp('altright')
                    a.press('f4')
                    a.hotkey('ctrl', 'a')
                    a.press('backspace')
                    a.write(network + sub_dir)
                    a.press('return')
                    a.keyDown('altleft')
                    a.keyDown('altright')
                    a.press('n')
                    a.keyUp('altleft')
                    a.keyUp('altright')
                    a.write(lines[x])
                    a.press('return')
                    
                    a.press('apps')
                    a.press('w')
                    a.press('return')
                    
            # size #
                    a.press('apps')
                    a.press('z')
                    a.keyDown('altleft')
                    a.keyDown('altright')
                    a.press('a')
                    a.press('e')
                    a.keyUp('altleft')
                    a.keyUp('altright')
                    a.press('tab')
                    a.write('2.94')
                    a.keyDown('altleft')
                    a.keyDown('altright')
                    a.press('b')
                    a.keyUp('altleft')
                    a.keyUp('altright')
                    a.press('tab')
                    a.write('2.70')
                    a.press('return')

            # URL afix #        
                    a.press('apps')
                    a.press('i', presses=2)
                    a.press('return')
                    a.write(COLLECTION.http)
                    
                    #a.hotkey('ctrl', 'v') # shit workaround
                    a.press('return')

            # end of cell #
                    a.press('right')
                    a.press('tab')
                    x+=1
                    n=50
                    match='found'
                    
                n=50
                
        #not working past for some reason.
        TOOL.processing.Runtime_01()

        a.hotkey('ctrl', 'a')
        a.hotkey('ctrl', 'b')
        a.hotkey('ctrl', 's')

        # PDF #
        # Converts WORD doc to finalized PDF booklet #

        TOOL.wait(5)

        a.keyDown('altleft')
        a.keyDown('altright')
        a.press('f')
        a.press('a')
        a.press('o')
        a.press('t')
        a.keyUp('altleft')
        a.keyUp('altright')
        a.press('p')
        a.keyDown('altleft')
        a.keyDown('altright')
        a.press('n')
        a.keyUp('altleft')
        a.keyUp('altright')
        a.write(sup_dir) 
        a.press('f4')
        a.hotkey('ctrl', 'a')
        a.press('backspace')
        a.write(network + '\Master Collection Booklets')
        a.press('return')
        a.keyDown('altleft')
        a.keyDown('altright')
        a.press('s')
        a.keyUp('altleft')
        a.keyUp('altright')

        a.hotkey('ctrl', 'f4', presses=2)
  
###choice:CPMC_booklet
##    elif MENU == '2':
##
##        # Filling in the table #
##        while x!=count: # Cannot strictly just follow cell as cell increases by one and does NOT account for missing CAKES.
##            match='match'
##            material=lines[x]
##
##            if x==cell: # Row #
##                    cell+=3
##                    row+=1
##                    
##            print('\n-\n-')
##            print('\nProcessing Cell:', x, 'of', page)
##            print('   Working in Row:', row)
##            total=x*100/count
##            print('      Remaining:', '%',total , 'Done')
##            
##            if x==page: # Create new page at cell(10) #
##                    page+=9
##                    a.hotkey('ctrl', 'return')
##                    a.press('right')
##
##            while cake == lines[x]:
##                print('\nSearching for pan name')
##                print('\t', ' Found:', lines[x].replace('.jpg', ''), '\n')
##
##                material = lines[x].replace(' ', '+')
##                item = material.replace('.jpg', '')
##                            
##            while match!=found:
##                    a.write(lines[x].replace('.jpg', ''))


###choice:BPlMC_booklet/BPcMC_booklet/BPsMC_booklet
##    elif MENU == '3' or menu == '4' or menu == '5':
##        
##        # Filling in the table #
##        while x!=count: # Cannot strictly just follow cell as cell increases by one and does NOT account for missing CAKES.
##            match='match'

################################################################################################################

################################################################################################################
        
if __name__ == '__main__':
    while SELECT == 0:
        print("""   Welcome!
        
        What material are you comparing?
        
        Please make a selection from the list below:
            1) Jigsaw Puzzle
            2) Cake Pan
            3) Literacy Backpack
            4) Citizen Science Kit
            5) STEM Kit
            0) Exit
            
        """)

        MENU = input()

    #choice:JPMC_booklet
        if MENU == '1':
            TOOL.wait(1)
            SELECT = 'Jigsaw Puzzles', '\JIGSAW'

    #choice:CPMC_booklet
        elif MENU == '2':
            TOOL.wait(1)
            SELECT = 'Cake Pans', '\CAKE'

    #choice:BPlMC_booklet
        elif MENU == '3':
            TOOL.wait(1)
            SELECT = r'Back Packs\Literacy', '\Literacy'

    #choice:BPcMC_booklet
        elif MENU == '4':
            TOOL.wait(1)
            SELECT = r'Back Packs\Citizen', '\Citizen'

    #choice:BPsMC_booklet
        elif MENU == '5':
            TOOL.wait(1) 
            SELECT = r'Back Packs\STEM', '\STEM'

    #choice:Exit
        elif MENU == '0':
            TOOL.wait(1)
            TOOL.Exit()

            print("\nThank you, have a great day.")
            TOOL.wait(1)
            exit()
            
    #choice:Other
        else:
            print("Invalid program selection.")
            TOOL.wait(1)
    
    location_A = network + SELECT[0] + r'\list.txt'
    location_B = network + SELECT[0] + SELECT[1] + '.txt'
    TOOL.Compare_list(location_A, location_B)
    print("completed.")          

