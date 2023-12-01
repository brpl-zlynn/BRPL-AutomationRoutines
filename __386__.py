#!/usr/bin/env python

####################################################################################
##                                                                                ##
##	SYS-Suppress Orders.py rev.8                                              ##
##	Suppresses order records for titles cataloged.                            ##
##                                                                                ##
##	Created By Zachary Lynn.                                                  ##
##      Updated on 05.12.2022 by Zachary Lynn for BRPL-ILS.                       ##
##	Copyright © 2022 Boca Raton Public Library. All rights reserved.          ##
##                                                                                ##
##      Multi-thread design | Mono-thread executed.                               ##
##      The pyautogui & win32gui module are Required to Properly Run Script.      ##
##      HAS A NETWORK DEPENDANCY of Q>R                                           ##
##      HAS A CREATE LIST DEPENDANCY for PERMISSIONS                              ##
##      HAS A GLOBAL UPDATE DEPENDANCY for PERMISSIONS                            ##
##      HAS A DATA EXCHANGE DEPENDANCY for PERMISSIONS                            ##
##      RELIANT OF CREATE LIST | index:(386 | o Type) Review File                 ##
##      RELIANT OF Suppress Orders.xlsx on the NETWORK                            ##
##                                                                                ##
##      Forthcoming updates:                                                      ##
##      None [;                                                                   ##
##  Rather move entire front end to backend SQL processing, and /cv do updates.   ##
##                                                                                ##
####################################################################################

# Modules
import win32gui as w
import pyautogui as a

from __main__ import *
from tool__ import *
from tool__Sierra import *
from tool__Excel import *

TOOL.processing.Runtime_03()
TOOL.processing.Failsafe_on()
TOOL.processing.On()

# Definitions
THREAD = 0

##############################################################################################################################

##############################################################################################################################

# Script
if __name__ == "__386__": # 386
    print(f"\n* SYS-{MAIN.NAME} *\n")
    
    TOOL.Thread() # Assign I
    SIERRA.Launch()
    
    SIERRA.FTF()
    FTS = SIERRA.FTS()
    TOOL.Thread() # Assign II     
    
    echo('#########################')
    echo('##                     ##')
    echo('## SYS-Suppress Orders ##')
    echo('##                     ##')
    echo('#########################')

                    
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
    a.write('386')                                  #   
    a.hotkey('alt', 's')                            #   
    a.hotkey('alt', 'r')                            # # Caution to how long the search can take to run and might eat any inputs such as 'tab', and 'g', 'd', 'r'.
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
    for process in range (0, 3):                    #      
        a.press('tab')                              #
    a.press('space')                                # # Select ☐ ORDER.  
                                                    # 
    a.press('tab')                                  # 
                                                    # 
    for process in range (0, 2):                    #
        a.press('space')                            #
        a.press('r')                                # # 1. Select records  
        a.press('tab')                              #
        a.write('386')                              #
        a.press('pagedown')                         #  
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
        a.write('0')                                #   
        a.write('9')                                # # Order Code 4
        a.press('return')                           #
        a.hotkey('alt', 'r')                        #
        a.press('n')                                #
        a.press('return')                           #
        a.hotkey('alt', 'o')                        #
                                                    #
        if process == 0:                            #
            SIERRA.Check_in()                       #
            SIERRA.Global_update()                  #              
                                                    #
    a.hotkey('ctrl', 't')                           # # Global_update() print sequence 
    SIERRA.FTF()                                    #
                                                    #
    a.hotkey('alt', 'f')                            # # FTP
    for process in range (0, 2):                    #
        a.press('p')                                #
                                                    #
    SIERRA.FTF()                                    #
    SIERRA.FTF()                                    #
                                                    #
    for subprocess in range (0, 2):                 #   
        a.hotkey('alt', 'r')                        # # 3. Preview
        a.press('y')                                #
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
        if Records == '1': # Program specific conditional : Orders Suppressed
            a.write('No Records')
            a.press('tab')
            a.write('0')

        elif Records != '': 
            a.write(Records)
            a.press('tab')
            a.write('0')
            
        else:
            a.write('Error')
            a.press('tab')
            a.write('1')
            
    except: # Error
        a.write('Error')
        a.press('tab')
        a.write('1')

    EXCEL.Exit()

else:
    print(f"9999 : 386 {{MAIN.NAME}}")
    
print(__name__, '{Suppress Orders} COMPLETE')
