#!/usr/bin/env python

####################################################################################
##                                                                                ##
##	Index.py Rev.4                                                            ##
##	Autorun scripts and menu options.                                         ##
##                                                                                ##
##	Created By Zachary Lynn.                                                  ##
##      Updated on 04.07.2022 by Zachary Lynn for BRPL-ILS.                       ##
##	Copyright © 2022 Boca Raton Public Library. All rights reserved.          ##
##                                                                                ##
##      Mono design.                                                              ##
##      The pyautogui & win32gui module are Required to Properly Run Script.      ##
##      HAS A NETWORK DEPENDANCY of Q>R                                           ##
##      RELIANT of SYS:1-9. on LOCAL                                              ##
##                                                                                ##
##      Forthcoming updates:                                                      ##
##      Automating run scripts.                                                   ##
##      Time looping.                                                             ##                               
##      Debug mode.                                                               ##
##      Error Log and status monitor.                                             ##
##      Window PID and definition.                                                ##
##      Process tree.                                                             ##
##                                                                                ##
##      —>Scheduler handler callable.                                             ##
##      —>Modular                                                                 ##
##                                                                                ##                  
####################################################################################

# Modules
import os
import sys
import shutil
import win32gui
import pyautogui
import subprocess
import progressbar

from time import sleep

from tool__ import *

#### testing WORKSPACE ####
# from WORKSPACE import * #
###########################

global __name__
global MENU

#Definitions
w = win32gui
a = pyautogui
echo = print

#Initialization
TIME = 1
MENU = '0'
EXIT = 'null'
PROGRAM = '__000__'

class tools:
    
# Timer/Cron #
    def Cron(self):
        global timer 
        global PROGRAM

        TOOL.processing.Failsafe_off()

        MENU = int(MENU)
        
        a.moveTo(0, 0)
        a.move(840, 525)
        
        while True:
            TOOL.processing.Runtime_00()
            timer = TIMESTAMP().replace(':','')
            timer = int(timer)
            
            print(TIMESTAMP())

            # Moving Menu #
            
            if (MENU % 2) == 0: # out
                a.moveRel(0, -MENU)
                a.moveRel(MENU, -MENU)
                a.moveRel(MENU, 0)
                a.moveRel(MENU, MENU)
                a.moveRel(0, MENU)
                a.moveRel(-MENU, MENU)
                a.moveRel(-MENU, 0)
                a.moveRel(-MENU, -MENU)
                MENU -= 2
                
                if MENU == 0:
                    MENU += 1

            else: # in
                a.moveRel(0, MENU)
                a.moveRel(-MENU, MENU)
                a.moveRel(-MENU, 0)
                a.moveRel(-MENU, -MENU)
                a.moveRel(0, -MENU)
                a.moveRel(MENU, -MENU)
                a.moveRel(MENU, 0)
                a.moveRel(MENU, MENU)
                MENU += 2
                
                if MENU == 255: 
                   MENU -= 1
                      
##            if timer == 110000: # Time which "CLS ARM "program runs at
##                processing()
##                echo('Running: SYS-CLS ARM')
##                TOOL.TIMESTAMP()
##                import __400__
##                PROGRAM = '400'
##                log()
##                TOOL.wait(5)
                   
            if timer == 100000: # time which "Daily Accounts" program runs at
                TOOL.processing.Runtime_02()
                echo('Running: SYS-Daily Accounts Expired')
                timestamp
                import __396__
                PROGRAM = '396'
                log()
                TOOL.wait(5)
                
            if timer == 100000: # time which "Daily Accounts" program runs at
                TOOL.processing.Runtime_02()
                echo('Running: SYS-Daily Accounts Renewed')
                timestamp
                import __394__
                PROGRAM = '394'
                log()
                TOOL.wait(5)
                    
            if timer == 100000: # time which "Daily Accounts" program runs at
                TOOL.processing.Runtime_02()
                echo('Running: SYS-Daily Accounts Created')
                timestamp
                import __392__
                PROGRAM = '392'
                log()
                TOOL.wait(5)
      
            if timer == 112600: # Time which "Suppress Orders" program runs at
                TOOL.processing.Runtime_02()
                echo('Running: SYS-Suppress Items')
                timestamp
                import __390__
                PROGRAM = '390'
                log()
                TOOL.wait(5)
                      
            if timer == 112600: # Time which "Suppress Orders" program runs at
                TOOL.processing.Runtime_02()
                echo('Running: SYS-UNSuppress Items')
                timestamp
                import __388__
                PROGRAM = '388'
                log()
                TOOL.wait(5)
                
            if timer == 112600: # Time which "Suppress Orders" program runs at
                TOOL.processing.Runtime_02()
                echo('Running: SYS-Suppress Orders')
                timestamp
                import __386__
                PROGRAM = '386'
                log()
                TOOL.wait(5)
                
##            if timer == 120000: # Time which "On Order Delete" program runs at, should get stuck until auto fix record selection process
##                TOOL.processing.Runtime_02()
##                echo('Running: On Order Delete')
##                timestamp
##                import __384__
##                PROGRAM = '384'
##                log()
##                TOOL.wait(5)

##            if timer == 130000: # Template
##                TOOL.processing.Runtime_02()
##                echo('Running: Daily Statistics')
##                TOOL.TIMESTAMP()
##                import __500__
##                PROGRAM = '500'
##                log()
##                TOOL.wait(5)
                
##            if timer == HHMMSS: # Template
##                TOOL.processing.Runtime_02()
##                echo('Running: $Y$-%%%%%%%%%%%')
##                TOOL.TIMESTAMP()
##                import __###__
##                PROGRAM = '###'
##                log()
##                TOOL.wait(5)


# Progress/Load Bar #
    def Loading(self): # Loading is apart of window
        from tqdm import tqdm

        from tool__ import TIMESTAMP

        global MENU
        global window
        global timeout
        
        self.sync = TIMESTAMP().replace(':', '')
        self.sync = int(self.sync)
        self.sync = self.sync/2500
        self.sync = int(self.sync)
        print(self.sync)
        
        if MENU != 'z': # pre-set parameters
            print("Syncing with database")
            for n in tqdm(range (self.sync), desc="Syncing..."):
                sleep(0.1)
            
            print("Loading Software")
            widgets = ['Loading...: ', progressbar.AnimatedMarker()] 
            self.bar = progressbar.ProgressBar(widgets=widgets).start()
            
            for i in range(self.timeout): 
                sleep(0.05) 
                self.bar.update(i)

            MENU = 'z'
            
        elif self.timeout == 0: # OTF parameters, const.update
            print('')
            widgets = ['Loading...: ', progressbar.AnimatedMarker()] 
            self.bar = progressbar.ProgressBar(widgets=widgets).start()
            self.timeout = 1

        if self.timeout == 0: # OTF parameters, const.update
            print('')
            widgets = ['Loading...: ', progressbar.AnimatedMarker()] 
            self.bar = progressbar.ProgressBar(widgets=widgets).start()
            self.timeout = 1

        try:
            if MAIN.window == 0:
                self.timeout += 1
                for i in range(self.timeout): 
                    sleep(0.1) 
                    self.bar.update(i)
    
        except:
            MAIN.window = 0

        else:
            self.timeout = 0

        return self.timeout
#        return self.x, self.y, self.z, self.bar

    
# Exit function #
    def Exit(void):
        
        if MENU == '0':
            n = 4
            while n > 1:
                n -= 1
                print("Exiting in ", n)
                
                for i in range(20):
                    TOOL.wait(1)

        else:
            print("Error")

MAIN = tools()
SUB = tools()
           
##############################################################################################################################

##############################################################################################################################

# Script
if __name__ == '__main__':
        
    print("\n", '* SYSTEM *')

    while MENU != '1':
        print("""
        Administering username--
        Authentication with local password--
        Loggin successful

        WARNING: This computer system is for offical use by authorized users
        and is subject to being monitored, recorded, audited, and/or restricted
        at any time. If monitoring reveals possible evidence of criminal
        activity, such evidence may be provided to Law Enforcement Prosonnel.
        Unauthorized or imporoper use of this system ma result in disciplinary
        action and/or criminal and civil penalties. This system contains private
        customer data and unauthorized access or use may also subject users to
        criminal and civil penalties under Title 26, Sections 7213, 7213A and
        7431 (Pub. 1075, Sec. 9.2 Exhibit 13). Users should have no expectation
        of privacy and any data processed using this system is the property of
        the Boca Raton Public Library. 
        
        ANYONE USING THIS SYSTEM EXPRESSLY CONSENTS TO SUCH MONITORING. LOG OFF
        IMMEDIATELY IF YOU DO NOT AGREE TO CONDITIONS STATED IN THIS WARNING.

        Created by Zachary Lynn
        Updated on 04.26.2022 by Zachary Lynn for BRPL-ILS
        Copyright � 2022 Boca Raton Public Library. All rights reserved.  

        Press 'Y' to accept these terms.
        Press 'N' to exit.
        """)

        TOOL.numlock()
        EXIT = input()
        
        if EXIT == 'Y' or EXIT == 'y':
            MENU = '2'
            
            while MENU == '2':
                
                TOOL.wait(1)
                print("""
              -------------------------------------------------------
             |                                                       |
             |     By continuing, you indicate you are aware of      |
             |      and consent to these terms and conditions.       |
             |                                                       |
             |                       Continue?                       |
             |                                                       |
             |      Press 'Y' to continue.                           |
             |      Press 'N' to return to Terms and Conditions.     |
             |                                                       |   
              -------------------------------------------------------
                """)
                
                EXIT = input()
                    
                if EXIT == 'Y' or EXIT == 'y':
                    TOOL.wait(2)
                    MENU = '1'                  
            
                elif EXIT == 'N' or EXIT == 'n':
                    print("Returning to the Terms and Conditions.")
                    TOOL.wait(2)
                    MENU = '0'
                    EXIT = 'N'
                    
                else:
                    print("Selection not valid.")
                    TOOL.wait(1)
                    MENU = '2'
            
        elif EXIT == 'N' or EXIT == 'n':
            MENU = '0'
            exit()

        else:
            print("Selection not valid.")
            TOOL.wait(1)
            MENU = 'z'
            
    while MENU != 'z':
            
        print("""

        Welcome! 

        Please make a selection from the list below:
             1) CLS ARM
             2) Miss Bib-img
             3) Daily Accounts
                 3a) Daily Expired
                 3b) Daily Renewed
                 3c) Daily Created
             4) Suppress Items
             5) Suppress Orders
             6) On Order Delete
             7) Summary Availability
             8) Daily Statistics [UNAVAILABLE]
             9) Special Collections Booklet
            10) Automated Daily Routine
             0) Exit
            
        """)

        MENU = input()
        
#choice:SYS-CLS ARM
        if MENU == '1':
            print("Program starting")
            TOOL.wait(1)
            MAIN.MENU = MENU
            MAIN.NAME = 'CLS ARM'
          
            print("Running program:", MAIN.NAME)
            TOOL.wait(1)
            import __400__
            
#choice:SYS-Miss Bib-img
        elif MENU == '2':
            print("Program starting")
            TOOL.wait(1)
            MAIN.MENU = MENU
            MAIN.NAME = 'Miss Bib-img.'
           
            print("Running program:", MAIN.NAME)
            TOOL.wait(5)
            import __398__
            
#choice:SYS-Daily Accounts
        elif MENU == '3':
            print("Program starting")
            TOOL.wait(1)
            MAIN.MENU = MENU
            MAIN.NAME = 'Daily Accounts'
          
            print("Running program:", MAIN.NAME)
            TOOL.wait(1)
            import __396__
            import __395__  # requires THREAD 8
            import __394__
            import __392__

#choice:SYS-Daily Accounts : Expired
        elif MENU == '3a' or MENU == '3A':
            print("Program starting")
            TOOL.wait(1)
            MAIN.MENU = MENU
            MAIN.NAME = 'Daily Accounts Expired'
          
            print("Running program:", MAIN.NAME)
            TOOL.wait(1)
            import __396__

#choice:SYS-Daily Accounts : Renewed
        elif MENU == '3b' or MENU == '3B':
            print("Program starting")
            TOOL.wait(1)
            MAIN.MENU = MENU
            MAIN.NAME = 'Daily Accounts Renewed'
          
            print("Running program:", MAIN.NAME)
            TOOL.wait(1)
            import __395__
            import __394__

#choice:SYS-Daily Accounts : Created
        elif MENU == '3c' or MENU == '3C':
            print("Program starting")
            TOOL.wait(1)
            MAIN.MENU = MENU
            MAIN.NAME = 'Daily Accounts Created'
          
            print("Running program:", MAIN.NAME)
            TOOL.wait(1) 
            import __392__

#choice:SYS-Suppress Items
        elif MENU == '4':
            print("Program starting")
            TOOL.wait(1)
            MAIN.MENU = MENU
            MAIN.NAME = 'Suppress Items'
            
            print("Running program:", MAIN.NAME)
            TOOL.wait(1)
            import __390__
            import __388__

#choice:SYS-Suppress Orders
        elif MENU == '5':
            print("Program starting")
            TOOL.wait(1)
            MAIN.MENU = MENU
            MAIN.NAME = 'Suppress Orders'
            
            print("Running program:", MAIN.NAME)
            TOOL.wait(1)
            import __386__
            
#choice:SYS-On Order Delete
        elif MENU == '6':
            print("Program starting")
            TOOL.wait(1)
            MAIN.MENU = MENU
            MAIN.NAME = 'On Order Delete'
            
            print("Running program:", MAIN.NAME)
            TOOL.wait(1)
            import __384__

#choice:SYS-Summary Availability
        elif MENU == '7':
            print("Program starting")
            TOOL.wait(1)
            MAIN.MENU = MENU
            MAIN.NAME = 'Summary Availability'
           
            print("Running program:", MAIN.NAME)
            TOOL.wait(1)
            import __380__
            
#choice:SYS-Daily Statistics
        elif MENU == '8':
            print("Program starting")
            TOOL.wait(1)
            MAIN.MENU = MENU
            MAIN.NAME = 'Daily Statistics'
           
            print("Running program:",  MAIN.NAME + "[UNAVAILABLE]")
            TOOL.wait(1)
            #import __500__

            #choice:SYS-Collection Master Booklet
        elif MENU == '9':
            print("Program starting")
            TOOL.wait(1)
            MAIN.Loading()
            MAIN.MENU = MENU
            MAIN.NAME = 'Collection Master Booklet'
           
            print("Running program:",  MAIN.NAME)
            TOOL.wait(1)
##            import __???__

#choice:SYS-Automated Daily Routine
        elif MENU == '10':
            print("Program starting")
            TOOL.wait(1)
            MAIN.MENU = MENU
            MAIN.NAME = 'Automated Daily Routine'

            echo(' ')
            while TIME <= 10:
                TOOL.wait(1)
                PROGRAM = ('.')*TIME
                print('Loading...:', PROGRAM)
                TIME += 1
                
            print(" Running program:", MAIN.NAME)
            TOOL.wait(1)
        
            MAIN.Cron() # Runs through all of time executing daily routines at a set time of day. 

#choice:Exit
        elif MENU == '0':
            TOOL.wait(1)
            MAIN.Exit()
            
            print("\nThank you, have a great day.")
            TOOL.wait(1)
            exit()

#choice:Other
        else:
            print("Invalid program selection.")
            TOOL.wait(1)
            
        print('999 : MENU')
        
    MENU = 'z'
            
    print('99 : MENU')
    
print('9 : MENU')
