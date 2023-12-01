#!/usr/bin/env python

##################################################################################
##                                                                              ##
##	SYS-Suppress Items.py rev.1                                             ##
##	Suppress unavailable items from public catalog.                         ##
##	Un-suppress items that come back from the ether.                        ##
##                                                                              ##
##	Created By Zachary Lynn.                                                ##
##      Updated on 05.12.2022 by Zachary Lynn for BRPL-ILS.                     ##
##	Copyright © 2022 Boca Raton Public Library. All rights reserved.        ##
##                                                                              ##
##      Multi-thread design | Mono-thread executed.                             ##
##      The pyautogui & win32gui module are Required to Properly Run Script.    ##
##      HAS A NETWORK DEPENDANCY of Q>R                                         ##
##      HAS A CREATE LIST DEPENDANCY for PERMISSIONS                            ##
##      HAS A GLOBAL UPDATE DEPENDANCY for PERMISSIONS                          ##
##      HAS A DATA EXCHANGE DEPENDANCY for PERMISSIONS                          ##
##      RELIANT OF CREATE LIST | index:(390 | i Type) Review File               ##
##      RELIANT OF Suppress Items.xlsx on the NETWORK                           ##
##                                                                              ##
##      Forthcoming updates:                                                    ##
##      None [;                                                                 ##
##  Rather move entire front end to backend SQL processing, and /cv do updates. ##
##                                                                              ##
##################################################################################

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

print("temp test")
exit()
                         
##############################################################################################################################

##############################################################################################################################

# Script
if __name__ == "__390__": # 390
    print(f"\n* SYS-{MAIN.NAME} *\n")
    
    TOOL.Thread() # Assign I
    
    SIERRA.Launch()
    prt = SIERRA.FTS()
    
    TOOL.Thread() # Assign II     
    
    echo('########################')
    echo('##                    ##')
    echo('## SYS-Suppress Items ##')
    echo('##                    ##')
    echo('########################')
                      
    #####################
    ##                 ##
    ## ILS Work Manuel ##
    ##                 ##
#####################################################
                                                    # 
    SIERRA.Create_lists()                           #
    # "Create Lists" window #                       #
                                                    #   
    a.write('390')                                  #   
    a.hotkey('alt', 's')                            #   
    a.hotkey('alt', 'e')                            #
    TOOL.wait(5)                                    #
                                                    #
    TOOL.processing.Runtime_04()                    # 
    a.write('SYS-' + 'UN' + MAIN.NAME)              # # UNSuppress Items - (from suppressed to unsuppressed)
                                                    #
    a.press('tab')                                  #
    a.press('space')                                #
    a.press('i')                                    # # Update record record storage type - dependant on record type.                                                    #
    a.press('return')                               #
    a.hotkey('alt', 'p')                            #   
    a.press('i')                                    # # Update record stopping block - dependant on record type.
    a.press('return')                               #
                                                    # 
    for process in range (0, 99):                   #                                                                   
        a.press('tab')                              #
    a.hotkey('alt', 'i')                            # # AND Operator, Insert Line,
                                                    # [ Term 1 - Item Code 2   
    a.press('i')                                    #   # Type 
    a.press('return')                               #
    a.write('60')                                   #   # Field # Item Code 2  
    a.press('return')                               #
    a.write('=')                                    #   # Condition # equal to  
    a.press('return')                               #
    a.press('n')                                    #   # Value A # SUPPRESSED  
    a.press('return')                               # ]
                                                    # [ Term 2 - Status
    a.press('a')                                    #   # Operator # AND
    a.press('return')                               #  
    a.press('i')                                    #   # Type
    a.press('return')                               #  
    a.write('88')                                   #   # Field # Status   
    a.press('return')                               #
    a.write('!=')                                   #   # Condition # equal to 
    a.press('return')                               #
    a.write('-')                                    #   # Value A # AVAILABLE 
    a.press('return')                               # ]
                                                    # [ Term 3 - Item Type
    a.press('a')                                    #   # Operator # AND
    a.press('return')                               #               
    a.press('i')                                    #   # Type   
    a.press('return')                               #  
    a.write('61')                                   #   # Field # Item Type  
    a.press('return')                               #
    a.write('!=')                                   #   # Condition # not equal to 
    a.press('return')                               #
    a.write('27')                                   #   # Value A # Magazines 
    a.press('return')                               # 
                                                    # # Term 4
    a.press('a')                                    #   # Operator # AND
    a.press('return')                               #               
    a.press('i')                                    #   # Type   
    a.press('return')                               #  
    a.write('61')                                   #   # Field # Item Type  
    a.press('return')                               #
    a.write('!=')                                   #   # Condition # not equal to 
    a.press('return')                               #
    a.write('27')                                   #   # Value A # Magazines 
    a.press('return')                               # 
                                                    # # Term 5
    a.press('a')                                    #   # Operator # AND
    a.press('return')                               #               
    a.press('i')                                    #   # Type   
    a.press('return')                               #  
    a.write('61')                                   #   # Field # Item Type  
    a.press('return')                               #
    a.write('!=')                                   #   # Condition # not equal to 
    a.press('return')                               #
    a.write('27')                                   #   # Value A # Magazines 
    a.press('return')                               #
                                                    # # Term 6
    a.press('a')                                    #   # Operator # AND
    a.press('return')                               #               
    a.press('i')                                    #   # Type   
    a.press('return')                               #  
    a.write('61')                                   #   # Field # Item Type  
    a.press('return')                               #
    a.write('!=')                                   #   # Condition # not equal to 
    a.press('return')                               #
    a.write('27')                                   #   # Value A # Magazines 
    a.press('return')                               #
                                                    # # Term 7
    a.press('a')                                    #   # Operator # AND
    a.press('return')                               #               
    a.press('i')                                    #   # Type   
    a.press('return')                               #  
    a.write('61')                                   #   # Field # Item Type  
    a.press('return')                               #
    a.write('!=')                                   #   # Condition # not equal to 
    a.press('return')                               #
    a.write('27')                                   #   # Value A # Magazines 
    a.press('return')                               #
                                                    # ]  
    a.hotkey('alt', 's')                            # # Caution to how long the search can take to run and might eat any inputs such as 'tab', and 'g', 'd', 'r'.
                                                    #
    TOOL.processing.Runtime_01()                    #
    SIERRA.FTF()                                    #                                                
    TOOL.Thread() # Assign III                      #   
                                                    #
    SIERRA.Global_update()                          # ######################
    # "Global Update" window #                      # # UNSuppress Records #
    TOOL.processing.Runtime_04()                    # ######################   
                                                    #    
    a.press('r')                                    # # 1. Select records
    for process in range (0, 9):                    #   
        a.hotkey('ctrl', 'tab')                     # # initalize selection.
    a.press('space')                                # # De-select ☑ BILIOGRAPHIC.    
    for process in range (0, 2):                    #   
        a.press('tab')                              #
    a.press('space')                                # # Select ☐ ITEM.  
    for process in range (0, 3):                    #    
        a.press('tab')                              # 
    a.write('390')                                  # 
    a.hotkey('alt', 'r')                            # 
                                                    #
    SIERRA.FTF()                                    #
    a.hotkey('ctrl' 't')                            #
                                                    #
    a.keyDown('alt')                                # # 2. Command input
    a.press('d')                                    #
    a.press('f')                                    #
    a.press('o')                                    #
    a.press('x')                                    #
    a.keyUp('alt')                                  #
    a.write('60')                                   # # Item Code 2
    a.press('return')                               #
    a.hotkey('alt', 'r')                            #
    a.write('-')                                    #
    a.press('return')                               #
    a.hotkey('alt', 'o')                            #
                                                    #    
    a.hotkey('ctrl' 't')                            #
    SIERRA.FTF()                                    #
                                                    #
    a.hotkey('alt', 'f')                            # # FTP
    a.press('p')                                    #
    a.hotkey('alt', 'r')                            # # 3. Preview
    a.press('y')                                    #
                                                    #
    SIERRA.FTF()                                    #
                                                    #  
    a.hotkey('alt', 'f')                            # # FTP
    a.press('p')                                    # # 4. Statistics
                                                    #
    TOOL.Thread() # Assign IV                       #
                                                    #
    SIERRA.Create_lists()                           #
    # "Create Lists" window #                       #
                                                    #   
    a.write('396')                                  #   
    a.hotkey('alt', 's')                            #   
    a.hotkey('alt', 'e')                            #
    TOOL.wait(5)                                    #
                                                    #
    TOOL.processing.Runtime_04()                    # 
    a.write('SYS-' + MAIN.NAME)                     # # Suppress Items - (from unsuppressed to suppressed)
                                                    #
    a.press('tab')                                  #
    a.press('space')                                #
    a.press('i')                                    # # Update record record storage type - dependant on record type.
    a.press('return')                               #
    a.hotkey('alt', 'p')                            #   
    a.press('i')                                    # # Update record stopping block - dependant on record type.
    a.press('return')                               #
                                                    # 
    for process in range (0, 99):                   #                                                                   
        a.press('tab')                              #
    a.hotkey('alt', 'i')                            # # AND Operator, Insert Line,
                                                    # [ Term 1
    a.press('i')                                    #   # Type 
    a.press('return')                               #  
    a.write('88')                                   #   # Field # Status   
    a.press('return')                               #
    a.write('=')                                    #   # Condition # equal to 
    a.press('return')                               #
    a.write('n')                                    #   # Value A # BILLED   
    a.press('return')                               # ]
                                                    # [ Term 2  
    a.press('a')                                    #   # Operator # AND
    a.press('return')                               #  
    a.press('i')                                    #   # Type - dependant on record type.   
    a.press('return')                               #
    a.write('60')                                   #   # Field # Item Code 2  
    a.press('return')                               #
    a.write('=')                                    #   # Condition # equal to  
    a.press('return')                               #
    a.press('-')                                    #   # Value A # Available  
    a.press('return')                               # ]
                                                    #    
    a.hotkey('alt', 's')                            # # Caution to how long the search can take to run and might eat any inputs such as 'tab', and 'g', 'd', 'r'.
                                                    #
    TOOL.processing.Runtime_01()                    #
    SIERRA.FTF()                                    #
                                                    #                                                
    TOOL.Thread() # Assign V                        #   
                                                    #
    SIERRA.Global_update()                          # ####################
    # "Global Update" window #                      # # Suppress Records #
    TOOL.processing.Runtime_04()                    # ####################   
                                                    #    
    a.press('r')                                    # # 1. Select records
    a.press('tab')                                  # 
    a.write('396')                                  # 
    a.hotkey('alt', 'r')                            # 
                                                    #
    SIERRA.FTF()                                    #
    a.hotkey('ctrl' 't')                            #
                                                    #
    a.keyDown('alt')                                # # 2. Command input
    a.press('d')                                    #
    a.press('f')                                    #
    a.press('o')                                    #
    a.press('x')                                    #
    a.keyUp('alt')                                  #
    a.write('60')                                   # # Item Code 2
    a.press('return')                               #
    a.hotkey('alt', 'r')                            #
    a.write('n')                                    # # Suppress
    a.press('return')                               #
    a.hotkey('alt', 'o')                            #
                                                    #    
    a.hotkey('ctrl' 't')                            #
    SIERRA.FTF()                                    #
                                                    #
    a.hotkey('alt', 'f')                            # # FTP
    a.press('p')                                    #
    a.hotkey('alt', 'r')                            # # 3. Preview
    a.press('y')                                    #
                                                    #
    SIERRA.FTF()                                    #
                                                    #  
    a.hotkey('alt', 'f')                            # # FTP
    a.press('p')                                    # # 4. Statistics
                                                    #
    TOOL.Thread() # Assign VI                       #
                                                    #
    print("""
        Process those of loaded logs manually until you get the logging software scripted, you scrub""")          
    exit()


    
    TOOL.Thread() # Assign IV
    
    SIERRA.Log(FTS)
    SIERRA.FTF()
    SIERRA.Exit()
    
    TOOL.Thread() # Assign V
##    JSON.Launch()
##    Records = JSON.Write()
    EXCEL.Launch()
    Records[A, B] = EXCEL.Write(FTS) #figure how to pass list for 2

    try: # Always try | except. For error catching.
##            if Records_A == '1':
##                a.write('No Records')
##            elif Records_A != '': # Items Un-Suppressed
##                a.write(Records)
##            if Records_B == '1':
##                a.write('No Records')
##            elif Records_B != '': # Items Suppressed
##                a.write(Records)

    except: # Error
        a.write('No Records')
        a.press('Tab')
        a.write('1')

    EXCEL.Exit()

    
else:
    print(f"9999 : 390 {Suppress Items}")
    
print(__name__, '{Suppress Items} COMPLETE')
