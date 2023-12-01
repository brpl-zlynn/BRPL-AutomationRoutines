#!/usr/bin/env python
##################################################################################
##                                                                              ##
##	Excel TOOLS                                                             ##
##	Functions using Excel.                                                  ##
##                                                                              ##
##	Created By Zachary Lynn.                                                ##
##      Updated on 04.28.2022 by Zachary Lynn for BRPL-ILS.                     ##
##	Copyright © 2022 Boca Raton Public Library. All rights reserved.        ##
##                                                                              ##
##################################################################################

# Modules
import glob

from __main__ import *
##from tool__ import *
##from tool__Sierra import FTS

#### testing WORKSPACE ####
# from WORKSPACE import * #
###########################
    
# Definitions

class Excel:
     
# Excel Executable function #       
    def Launch(self):
        global window
        TOOL.processing.Runtime_04()
        
        network, Finn = PATH.Network('LOGS', MAIN.NAME)
        window = 'SYS-' + MAIN.NAME + '.xlsx - Excel'
        subprocess.Popen([r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.exe', network])
    
        TOOL.Window(window)
        TOOL.Input()

        return window


    def Write(self, FTS): # Must be saved in correct cell.
        network, path = (PATH.Network('FTS', MAIN.NAME + '\\' + FTS + ".p"))
        filedump = open('%s' % (network), 'r')

        print(FTS)
        a.write(FTS[2:])
        a.press('tab')
        FTS = Records = 0
        
        try:
            for data in filedump:
                data = str(data) # Convert data from file into readable string.
                
                for process in data:
                    data = filedump.read(1) # read line depending on record type, all record types start in 1. p1, b1, i1, o1, v1. Only one record type should be read in
                    
                    if data == 'X': # Records affected /might not need since record types below/
                        FTS += 1
                        print("Processing :", FTS)

                    elif data == 'p1': # Patron Records
                        Records += 1
                        print("Processing :", Records)
                        
                    elif data == 'b1': # Bibliographic Records
                        Records += 1
                        print("Processing :", Records)
                        
                    elif data == 'i1': # Item Records
                        Records += 1
                        print("Processing :", Records)
                        
                    elif data == 'o1': # Order Records
                        Records += 1
                        print("Processing :", Records)

                    elif data == 'v1': # Vendor Records
                        Records += 1
                        print("Processing :", Records)

        except:
            pass
        
        FTS = str(FTS)
        Records = str(Records)

        return FTS, Records # Export list(s) handles on the induvidual level since sheets are unique.
    

# Exit Excel # 
    def Exit(self): # Save and exit.
        echo('* Exiting Excel *')
        TOOL.processing.Runtime_05()

        a.press('home')
        a.hotkey('ctrl', 'shift', '+')
        a.hotkey('ctrl', 's')
        a.hotkey('alt', 'F4')

        app = 'O'

        return app


EXCEL = Excel()
