#!/usr/bin/env python

####################################################################################
##                                                                                ##
##	SYS-HTML / MARC ARM.py                                                    ##
##	Script for loading records from ftp >> database.                          ##
##      Script for downloading forms from Civic Plus database.                    ##
##                                                                                ##
##	Created By Zachary Lynn.                                                  ##
##      Updated on 03.21.2022 by Zachary Lynn for BRPL-ILS.                       ##
##	Copyright © 2021 Boca Raton Public Library. All rights reserved.          ##
##                                                                                ##
##      Poly-thread design.                                                       ##
##      The pyautogui & win32gui module are Required to Properly Run Script.      ##
##      HAS A NETWORK DEPENDANCY of Q                                             ##
##      HAS A CREATE LIST DEPENDANCY for PERMISSIONS                              ##
##      HAS A DATA EXCHANGE DEPENDANCY for PERMISSIONS                            ##
##      RELIANT OF CREATE LIST | index:(400 | b Type)Review File                  ##
##      RELIANT OF CLS ARM.xlsx on the NETWORK                                    ##
##                                                                                ##
##      Forthcoming updates:                                                      ##
##      Window PID and definition.                                                ##
##      Process tree.                                                             ##
##                                                                                ##
##      —>Scheduler handler callable.                                             ##
##      —>Modular                                                                 ##
##                                                                                ##
####################################################################################

# Modules #
from tool__ import *
from tool__FTP import *
from tool__HTML import *
from tool__Sierra import *

global start
global datestamp
global cache

TOOL.processing.Runtime_03()
TOOL.processing.Failsafe_on()
TOOL.processing.On()

# Definitions
THREAD = 0

# Script
if __name__ == "__main__": # 400
##    print('\n', '* SYS-' + MAIN.NAME + ' Renewed' + ' *', '\n')

    PATH.Local()
    CIVIC.form()
   # FTP.ftp()
  #  TOOLS.marc()
        
    print(f'\n* CLS ARM *\n')
        
        #actual 400 do
        
        #load

    print("Returning to Menu")
    
    #TOOLS.move()
    
else:
    print(f'9999 : 400 {CLS ARM}')

print(__name__, '{CLS ARM} COMPLETE!')

