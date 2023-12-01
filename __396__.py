﻿#!/usr/bin/env python

##################################################################################
##                                                                              ##
##	SYS-Daily Accounts Expired.py rev.18                                    ##
##	Script for running Daily Accounts create lists.                         ##
##                                                                              ##
##	Created By Zachary Lynn.                                                ##
##      Updated on 02.23.2022 by Zachary Lynn for BRPL-ILS.                     ##
##	Copyright © 2023 Boca Raton Public Library. All rights reserved.        ##
##                                                                              ##
##      Multi-thread design | Mono-thread executed.                             ##
##      The pyautogui & win32gui module are Required to Properly Run Script.    ##
##      HAS A NETWORK DEPENDANCY of Q>R                                         ##
##      HAS A CREATE LIST DEPENDANCY for PERMISSIONS                            ##
##      HAS A GLOBAL UPDATE DEPENDANCY for PERMISSIONS                          ##
##      HAS A DATA EXCHANGE DEPENDANCY for PERMISSIONS                          ##
##      RELIANT OF CREATE LIST | index:(396 | p Type) Review File               ##
##      RELIANT OF SYS-Daily Accounts.xlsx on the NETWORK                       ##
##                                                                              ##
##      Forthcoming updates:                                                    ##
##      None [;                                                                 ##
##  Rather move entire front end to backend SQL processing, and /cv do updates. ##
##                                                                              ##
##################################################################################

# Modules
from __main__ import *
from tool__ import *
from tool__Sierra import *
from tool__Excel import *

TOOL.processing.Runtime_03()
TOOL.processing.Failsafe_on()
TOOL.processing.On()

# Definitions
THREAD = 0
if MAIN.MENU != '3':
    MAIN.MENU = '3'
    MAIN.NAME = MAIN.NAME[:-8]
SUB.NAME = MAIN.NAME + " Expired"

##############################################################################################################################

##############################################################################################################################

# Script
if __name__ == "__396__": # 396
    print(f"\n* SYS-{SUB.NAME} *\n")

    TOOL.Thread() # Assign I
    SIERRA.Launch()
    
    print(MAIN.NAME)
    SIERRA.FTF()
    FTS = SIERRA.FTS()
    TOOL.Thread() # Assign II     
    
    echo('################################')
    echo('##                            ##')
    echo('## SYS-Daily Accounts Expired ##')
    echo('##                            ##')
    echo('################################')

                    
    #####################
    ##                 ##
    ## ILS Work Manuel ##
    ##                 ##
#####################################################
                                                    # 
    SIERRA.Create_lists()                           #
    TOOL.processing.Runtime_04()                    # 
    # "Create Lists" window #                       #
                                                    #
    a.write('396')                                  #   
    a.hotkey('alt', 's')                            #   
    a.hotkey('alt', 'e')                            #
    TOOL.wait(2)                                    #
                                                    #
    a.write('SYS-' + SUB.NAME)                      #   # Expired #
                                                    # [ Term 1
    for process in range (0, 11):                   #                                                                   
        a.press('tab')                              #
    a.press('t')                                    #   # Value A # calendar 
    a.press('return')                               # ]  
                                                    #
    a.hotkey('alt', 's')                            # # Caution to how long the search can take to run and might eat any inputs such as 'tab', and 'g', 'd', 'r'.
                                                    #
    SIERRA.FTF()                                    #                                   
    TOOL.Thread() # Assign III                      # 
                                                    #
    SIERRA.Global_update()                          #
    # "Global Update" window #                      #   
                                                    #
    for process in range (0, 9):                    #   
        a.hotkey('ctrl', 'tab')                     # # initalize selection. 
                                                    #
    a.press('space')                                # # De-select ☑ BILIOGRAPHIC.    
    a.press('tab')                                  #
    a.press('space')                                # # Select ☐ PATRON.  
                                                    #
    for process in range (0, 3):                    #   
        a.press('tab')                              #
                                                    # 
    for process in range (0, 2):                    #
        a.press('space')                            #
        a.press('r')                                # # 1. Select records  
        a.press('tab')                              #
        a.write('396')                              # # 396.Expired
        a.press('tab')                              #
        a.press('return')                           # 
        a.keyDown('alt')      # reduntant method    #
        a.press('r')          # reduntant method    #
        a.press('e')          # reduntant method    #
        a.keyUp('alt')        # reduntant method    #
        a.hotkey('ctrl', 'a') # reduntant method    #
                                                    # 
        SIERRA.FTF()                                #   
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
        a.press('x')                                #
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
    a.hotkey('alt', 'f')                            # # FTP
    a.press('p')                                    # # 4. Statistics 
                                                    #     
#####################################################
    
    TOOL.Thread() # Assign IV
    
    SIERRA.Log(FTS)
    SIERRA.FTF()
    SIERRA.Exit()
    
    TOOL.Thread() # Assign V
##    JSON.Launch()
##    Records = JSON.Write()    
    EXCEL.Launch()
    Records, Return = EXCEL.Write(FTS)
    print(Records)
    
    try: # Always try | except. For error catching.
        if Records != '': # Program specific conditional : Patron(s) Expired
            a.write(Records)
            a.press('tab')
            a.write('Expired')
            a.press('tab')
            a.write('0')
            
        else:
            a.write('Error')
            a.press('tab')
            a.write('Expired')
            a.press('tab')
            a.write('1')
            
    except: # Error
        a.write('Error')
        a.press('tab')
        a.write('Expired')
        a.press('tab')
        a.write('1')

    EXCEL.Exit()

else:
    print(f'9999 : 396 {{SUB.NAME}}')

print(__name__, '{Daily Accounts Expired} COMPLETE!')
