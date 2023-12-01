#!/usr/bin/env python

####################################################################################
##                                                                                ##
##	SYS-On Order Delete.py Rev.6                                              ##
##	Delete items on order for x < period of time.                             ##
##                                                                                ##
##	Created By Zachary Lynn.                                                  ##
##      Updated on 05.02.2022 by Zachary Lynn for BRPL-ILS.                       ##
##	Copyright © 2022 Boca Raton Public Library. All rights reserved.          ##
##                                                                                ##
##      Multi-thread design | Poly-thread executed.                               ##
##      The pyautogui & win32gui module are Required to Properly Run Script.      ##
##      Current Records and Max Records must match which index referencing.       ##
##      HAS A NETWORK DEPENDANCY of Q>R                                           ##
##      HAS A CREATE LIST DEPENDANCY for PERMISSIONS                              ##
##      HAS A CATALOGING DEPENDANCY for PERMISSIONS                               ##
##      RELIANT OF CREATE LIST | index:(384 | i Type) Review File                 ##
##      RELIANT OF On Order Delete.xlsx on the NETWORK                            ##
##                                                                                ##
##      Forthcoming updates:                                                      ##
##      Read Current and Max Records searched on assigning M&M=Error, C&M=None    ##
##      Logs & data collection                                                    ##
##                                                                                ##
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
if __name__ == "__384__": # 384
    print(f"\n* SYS-{MAIN.NAME} *\n")

    TOOL.Thread() # Assign I
    SIERRA.Launch()
    
    SIERRA.FTF()
    FTS = SIERRA.FTS()
    THREAD = TOOL.Thread() # Assign II     
    
    echo('#########################')
    echo('##                     ##')
    echo('## SYS-On Order Delete ##')
    echo('##                     ##')
    echo('#########################')

                    
    #####################
    ##                 ##
    ## ILS Work Manuel ##
    ##                 ##
#################################################
                                                #       
    SIERRA.Create_lists()                       #  
    # "Create Lists" window #                   #    
                                                #
    a.write('384')                              #
    a.hotkey('ctrl', 'c')                       #
    Line = TOOL.ClipboardCopy()                 #
    Line = Line.decode("utf-8")[11:-9]          #  
                                                #    
    a.hotkey('alt', 's')                        # 
                                                #     
    if Line == 'empty':                         #
        a.write('SYS-' + MAIN.NAME)             #
        a.press('tab')                          #
        a.press('i')                            #
        a.press('return')                       #
        SIERRA.Create_lists.JSON(MAIN.NAME)     #                                     
                                                #
        SIERRA.FTF()                            #                                   
        THREAD = TOOL.Thread() # Assign III     #
        print('first iii', THREAD)###########################################
                                                #
    elif THREAD <= 2:                           #  
        print('in thread 2')########################################### already posed not blank
        a.hotkey('alt', 'r')                    # # Caution to how long the search can take to run and might eat any inputs such as 'tab', and 'g', 'd', 'r'.
                                                #
        SIERRA.FTF()                            #                                                                        
        THREAD = TOOL.Thread() # Assign III     #  
        print('should be iii second',THREAD) ###########################################
                                                #                                                                                                    #     
    while Line == '0\t50\ti\tin progress' or Line == '0\t50\tb\tin progress':                           # 
        SIERRA.FTF()                                                                                    #
        a.write('384')                                                                                  #  
        a.hotkey('ctrl', 'c')                                                                           #  
        Line = TOOL.ClipboardCopy()                                                                     #
        Line = Line.decode("utf-8")[24:-27]                                                             #
        print('progress tin', Line)###########################################
        Records = 'In progress'                                                                         # In progress
                                                                                                        #        
    if Line == '50\t50\ti\tcomplete' or Line == '0\t50\tb\tcomplete' or Line == '50\t50\tb\tcomplete':  #
        THREAD = 1                                                                                      #
        print('error or')###########################################
        Records = 'Error' # Error                                                                       #
                                                                                                        #
    elif Line != '0\t50\ti\tcomplete': # iRecords Deleted                                               #
        print(Line)       ###########################################                                      
        Records = '1' # Load Records                                                                    #
        print('to delete')###########################################
                                                                                                        #
    else:                                                                                               #
        THREAD = 0                                                                                      #
        Records = 'No Records to delete' # No Records to delete                                         #
                                                                                                        #                                                                            #
    if THREAD >= 3: # To delete records         #########################################################
        print('should be iii inside delete records',THREAD)###########################################
        THREAD = TOOL.Thread() # Assign IV      #
        print('should be iv',THREAD)########################################
                                                #
        SIERRA.Delete_records()                 #
                                                #
        a.write('384')                          #
        a.keyDown('alt')                        #
        a.press('r')                            #
        a.press('o')                            #
##        a.press('d') # delete dialog          #
        a.keyUp('alt')                          #
                                                #
        print(timeout)         ######################################################                 
        # Fail Safe # ??????????????????????????????????????????????????????
        while counter >= 0:                                                                                                                                                                         #
            TOOL.wait(3)
            counter -= 1
                                                                                                                                                                                                    #
            if counter > 0:                                                                                                                                                                         #
                print('Process will auto-abort in:', counter)                                                                                                                                       #
                                                                                                                                                                                                    #
                accept = a.confirm(timeout=2000, text='Process requires explicit autherization\n            Click ''ACCEPT'' to continue', title='Permissions Check', buttons=['ACCEPT','abort'])   #
                print(accept)                                                                                                                                                                       #
                                                                                                                                                                                                    #
                if accept == 'ACCEPT':                                                                                                                                                              #
                    print('\nContinuing with delete.')                                                                                                                                              # 
                    counter = -1                                                                                                                                                                    #
                                                                                                                                                                                                    #
                elif accept == 'abort':                                                                                                                                                             #
                    thread = 0                                                                                                                                                                      #
                    counter = 0                                                                                                                                                                     #
                                                                                                                                                                                                    #                                                                                                                                                                 #                                                                                                                                                                                                    #
            if counter == 0:                                                                                                                                                                        #
                print('\nProcess aborting due to inactivity.')                                                                                                                                      #   
                thread = 0                                                                                                                                                                          #
                counter = 0
                
            print(counter)
            print(accept)
            print(timeout)
            print(THREAD)##
            
    if THREAD >= 1:                             #
        print('should be 1 did not delete because of error need to re-JSON', THREAD)###################################
        print('should be V went to delete', THREAD)################################################
        THREAD = TOOL.Thread() # Assign IV | V  #
        print('should be IV | V ', THREAD)######################################################
        SIERRA.Create_lists()                   #
        TOOL.processing.Runtime_04()            # 
                                                #
        a.write('384')                          #   
        a.hotkey('alt', 's')                    #   
        a.hotkey('alt', 'e')                    #
                                                #
        a.write('SYS-' + MAIN.NAME)             #
                                                #
        SIERRA.Create_lists.JSON(MAIN.NAME)     #
                                                #
#################################################
                                                          
        THREAD = TOOL.Thread() # Assign VI
                                                
        SIERRA.FTF()                            
        SIERRA.Log(FTS)                         
                                                
    print('pre excel', Records)##############################################
    SIERRA.FTF()                                
    SIERRA.Exit()                               
                                                
    THREAD = TOOL.Thread() # Assign VI          
##    JSON.Launch()                             
##    Records = JSON.Write()                    
    EXCEL.Launch()                              
                                                
    if Records == '1':                          
        Records, Return = EXCEL.Write(FTS)      
        print(Records)      ##########################################################
                                                
    try: # Always try | except.                 
        if Records == 'Error':                  
            a.write(FTS[2:])                    
            a.press('tab')                      
            a.write('Error')                    
            a.press('tab')                      
            a.write('1')                        
                                                
        elif Records == 'No Records to delete': 
            a.write(FTS[2:])                    
            a.press('tab')                      
            a.write('No Records to delete')     
            a.press('tab')                      
            a.write('0')                        
                                                
        else:                                   
            a.write(Records)                    
            a.press('tab')                      
            a.write('0')                        
                                                
    except: # Error                             
        a.write(FTS[2:])                        
        a.press('tab')                          
        a.write('Error')                        
        a.press('tab')                          
        a.write('1')                        
                                                
    EXCEL.Exit()                                                                                
    exit()                                      
                      
else:
    print('9999 : 384 {SYS-On Order Delete}')

print(__name__, '{SYS-On Order Delete} COMPLETE!')
