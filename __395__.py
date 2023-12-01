#!/usr/bin/env python

##################################################################################
##                                                                              ##
##	SYS-Daily Accounts Renewed.py : 1 year & 3 year rev.13                   ##
##	Script for applying Renewed account create lists.                       ##
##                                                                              ##
##	Created By Zachary Lynn.                                                ##
##      Updated on 02.23.2023 by Zachary Lynn for BRPL-ILS.                     ##
##	Copyright © 202 Boca Raton Public Library. All rights reserved.         ##
##                                                                              ##
##      Multi-thread design | Poly-thread executed.                             ##
##      The pyautogui & win32gui module are Required to Properly Run Script.    ##
##      HAS A NETWORK DEPENDANCY of Q>R                                         ##
##      HAS A CREATE LIST DEPENDANCY for PERMISSIONS                            ##
##      HAS A GLOBAL UPDATE DEPENDANCY for PERMISSIONS                          ##
##      HAS A DATA EXCHANGE DEPENDANCY for PERMISSIONS                          ##
##      RELIANT OF CREATE LIST | index:(394 | p Type) Review File               ##
##      RELIANT OF JSON-Daily Accounts Renewed 1 year on the NETWORK            ##
##      RELIANT OF JSON-Daily Accounts Renewed 3 year on the NETWORK            ##
##                                                                              ##
##      Forthcoming updates:                                                    ##
##      None [;                                                                 ##
##  Rather move entire front end to backend SQL processing, and /cv do updates. ##
##                                                                              ##
##################################################################################

# Modules6
from __main__ import *
from tool__ import *
from tool__Sierra import *
from tool__JSON import *

TOOL.processing.Runtime_03()
TOOL.processing.Failsafe_on()
TOOL.processing.On()

# Definitions
THREAD = 0
year = 1
if MAIN.MENU != '3':
    MAIN.MENU = '3'
    MAIN.NAME = MAIN.NAME[:-8]
    THREAD = 3
SUB.NAME = MAIN.NAME + " Renewed"


##############################################################################################################################

##############################################################################################################################

# Script
if __name__ == "__395__": # 395
    print(f"\n* SYS-{SUB.NAME} : 1 & 3 year *\n")

    print(THREAD)
    THREAD = TOOL.Thread() # Assign I
    TOOL.numlock()
    print(THREAD)
    SIERRA.Launch()
    
    SIERRA.FTF()
    FTS = SIERRA.FTS()
    THREAD = TOOL.Thread() # Assign II
    
    echo('####################################')
    echo('##                                ##')
    echo('## SYS-Daily Renewed : 1 & 3 year ##')
    echo('##                                ##')
    echo('####################################')

    #####################
    ##                 ##
    ## ILS Work Manuel ##
    ##                 ##
#########################################################
                                                        #
    TOOL.processing.Runtime_05()                        # 
    while year <= 3:                                    #
        year = str(year)                                #
                                                        #
        SIERRA.Check_in()                               #
        SIERRA.Create_lists()                           #
        # "Create Lists" window #                       #
                                                        #
        SIERRA.FTF()                                    #
                                                        #
        TOOL.wait(2)                                    #
        a.write('394')                                  # # NOT 395, resuing line ! Num Lock in 'O' gumming things up.
        a.hotkey('alt', 's')                            #  
        a.hotkey('alt', 'e')                            #
        TOOL.wait(2)                                    #
                                                        #
        a.write('SYS-' + SUB.NAME  + ' : ' + year + ' year')   # Renewed : 1 year ⊃ 3 year #
                                                        #
        year = int(year)                                #
        JSON.Conversion(year, 'year', SUB.NAME)         #
        year = str(year)                                #
                                                        #
        SIERRA.Create_lists.JSON(SUB.NAME + ' ' + year + ' year')  
                                                        # [ Term 1 #
        a.hotkey('alt', 's')                            # # Caution to how long the search can take to run and might eat any inputs such as 'tab', and 'g', 'd', 'r'.
                                                        #
        SIERRA.FTF()                                    #                       
        THREAD = TOOL.Thread() # Assign III             #
                                                        #
        SIERRA.Global_update()                          #
        # "Global Update" window #                      #  
                                                        # 
        if THREAD == 3 or THREAD == 8:                  # # (mono-thread)3 | (poly-thread)8
            for process in range (0, 9):                #   
                a.hotkey('ctrl', 'tab')                 # # initalize selection. 
                                                        #
            a.press('space')                            # # De-select ☑ BILIOGRAPHIC.    
            a.press('tab')                              #
            a.press('space')                            # # Select ☐ PATRON.  
                                                        #
            for process in range (0, 3):                #   
                a.press('tab')                          #
                                                        # 
        for process in range (0, 2):                    #
            a.press('space')                            #
            a.press('r')                                # # 1. Select records  
            a.press('tab')                              #
            a.write('394')                              # # 396.Renewed
            a.press('tab')                              #
            a.press('return')                           # 
            a.keyDown('alt')      # reduntant method    #
            a.press('r')          # reduntant method    #
            a.press('e')          # reduntant method    #
            a.keyUp('alt')        # reduntant method    #
            a.hotkey('ctrl', 'a') # reduntant method    #
                                                        # 
            SIERRA.FTF()                                #
                                                        #   
            for subprocess in range (0, 2):             #   
                a.hotkey('ctrl', 't')                   #
                                                        #
            a.keyDown('alt')                            # # 2. Command input
            a.press('d')                                #
            a.press('f')                                #
            a.press('o')                                #
            a.press('x')                                #
            a.keyUp('alt')                              #
            a.press('5')                                #
            a.press('4')                                # # Item Code 2
            a.press('return')                           #
            a.hotkey('alt', 'r')                        #
            a.press('-')                                #
                                                        #  
            for subprocess in range (0, 2):             # 
                a.press('r')                            #
            a.press('return')                           #
            a.hotkey('alt', 'o')                        #
                                                        #
            if process == 0:                            #
                SIERRA.Check_in()                       #
                SIERRA.Global_update()                  #
                                                        #
        a.hotkey('ctrl', 't')                           #
        SIERRA.FTF()                                    #
                                                        #
        a.hotkey('alt', 'f')                            # # FTP
        a.press('p')                                    #
                                                        #
        SIERRA.FTF()                                    #
                                                        #
        a.hotkey('alt', 'r')                            # # 3. Preview
        a.press('y')                                    #
                                                        #
        SIERRA.FTF()                                    #
                                                        #
        year = int(year)                                #
        year += 2                                       #
                                                        #     
#########################################################
    
    TOOL.Thread() # Assign IV

    SIERRA.Exit()
    
    TOOL.Thread() # Assign V

else:
    print('9999 : 395 {,' + {SUB.NAME}, + ': 1 & 3 year}')
