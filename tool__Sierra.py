#!/usr/bin/env python
##################################################################################
##                                                                              ##
##	Sierra TOOLS                                                            ##
##	Functions using Sierra.                                                 ##
##                                                                              ##
##	Created By Zachary Lynn.                                                ##
##      Updated on 04.28.2022 by Zachary Lynn for BRPL-ILS.                     ##
##	Copyright © 2022 Boca Raton Public Library. All rights reserved.        ##
##                                                                              ##
##################################################################################

# Modules
import glob

from __main__ import *
from tool__ import *
##from tool__JSON import * # One or the other, not both
from tool__Excel import * # One or the other, not both

#### testing WORKSPACE ####
# from WORKSPACE import * #
###########################

# Definitions
class Sierra:
     
# Sierra Log & Log-in function #       
    def Launch(self):
        global window
        TOOL.processing.Runtime_02()
        
        window = 'Sierra - Boca Raton Public Library'
        
        subprocess.Popen("%s" % (r'C:\Sierra Desktop App\iiirunner.exe'))
        
        TOOL.Window(window)
        TOOL.Input()
        
        a.hotkey('ctrl', 'a')
        a.write('SYSTEM')
        a.press('tab')
        a.write('brpltechserv')
        a.press('return')
        
        window = 'Sierra · Boca Raton Public Library · Automation Service'     
        TOOL.Window(window)
        
        return window


# File | Select | Printer #
    def FTS(self):
        filestamp = CHRONOS()
        TOOL.processing.Runtime_02()
        FTS = MAIN.MENU + '.' + filestamp

        print('menu filestamp:', MAIN.MENU, filestamp) # run twice from option 3 to option 5 as I believe the filestamp is not being updated globally? or 
        a.keyDown('altright')
        a.press('f')
        a.press('t')
        a.press('s')
        a.keyUp('altright')
        a.press('down')
        a.press('return')
        TOOL.Input()
        a.write(FTS)
        a.hotkey('alt', 'o')

        return FTS


# File | Select | Form #
    def FTF(void):
        TOOL.processing.Runtime_02()
        timeout = O = 0
        
        while O != '1':
            a.keyDown('alt')
            a.press('f')
            a.press('t')
            a.press('f')
            a.keyUp('alt')            
            a.press('down')
            a.press('return')
            
            O, Input_timeout = TOOL.Input()
            timeout += Input_timeout
            
            if timeout >= 40: # 4x iterations | Return unique code to indicate input error occured.
                print('An error occured and processing timed out. Please see the reported error in the log.')
                exit() # Turn into logging error to datasheets. 
            a.press('esc')
            
 
# Put_PC > C:\ > R:\.p > Excel #
    def Log(self, FTS):
        TOOL.processing.Runtime_07()
        cache, user = PATH.Local()
        local = cache + FTS + '.p'
        network, Finn = PATH.Network('FTS', MAIN.NAME)
        timeout = X = Y = x = y = 0

        # Downloading #
        SIERRA.Data_exchange()
        
        a.press('tab')
        a.press('space')
        a.press('pagedown')
        a.press('return')   

        while cache != FTS: # Put_PC

            while x == y:
                try:
                    x, y = a.locateCenterOnScreen('Last_Modified.png') # CANNOT EDIT ORIGINAL PNG, works off snippit only
                    print(x, y)
                except:
                    TOOL.Window(window)
                    a.hotkey('alt', 'tab')
                    print('Cannot locate on screen')
                
            timeout += 1
            a.rightClick(x, y)                      
            a.press('tab')
            a.hotkey('ctrl', 'c')
            
            try: # correct || wrong copy.
                O = TOOL.ClipboardCopy()
                cache = O.decode("utf-8")[5:20] #### [7:] for datestamp only, [5:] for MENU option included, [:20] for datestamp only, [:22] for including .p
                print(cache, 'first copy')
                
                if cache != FTS:
                    Y = TOOL.ClipboardCopy()
                    cache = Y.decode("utf-8")[4:19] ### [6:] for datestamp only, [4:] for MENU option included, [:19] for datestamp only, [:21] for including .p
                    print(cache, "after click copy")
                    
            except: # timeout for function.
                if timeout == 5: # how many itterations until break
                    print("broke in the except of Put_PC")  # test del line
                    # skip all the below as wrong download and will load into excel.
                    exit() # transition to error logging.
                pass

        a.press('tab')
        a.keyDown('alt')
        a.press('t')
        TOOL.wait(10)
        print('t')
        
        a.press('u')
        TOOL.wait(10)
        print('u') 
        
        a.press('2')
        TOOL.wait(10)
        print('2') 

        a.hotkey('i')  #   does not consistantly work
        TOOL.wait(10)
        print('i') 
        
        a.keyUp('alt')
        a.press('backspace')  #   ~/ 
        TOOL.wait(10)
        print('/user/')
        
        for process in range(0, 4):
            a.hotkey('shift', 'tab')
        TOOL.wait(10)
        print('File Name:') 
        
        a.write('AppData')
        TOOL.wait(10)
        print('AppData') 
        
        a.press('return')
        TOOL.wait(10)
        print('return')
        
        a.hotkey('ctrl', 'backspace')
        a.write('Local')
        a.press('return')
        a.hotkey('ctrl', 'backspace')
        a.write('Temp')
        a.press('return')
        a.hotkey('ctrl', 'backspace')
        a.write(FTS + '.p')
        a.press('return')
        
        # Moving #
        shutil.move(local, network)

  
# Check-In(No Patron) Function #    
    def Check_in(self):
        echo('* Running Function: Check-in *')
        TOOL.processing.Runtime_02()
        
        a.hotkey('altright', 'g')
        a.press('u')
        a.press('c')

        TOOL.Input()

        
# Search/Holds Function #    
    def Search(self):
        echo('* Running Function: Search/Holds *')
        TOOL.processing.Runtime_01()

        a.hotkey('alt', 'g')
        a.press('u')
        a.press('c')

        TOOL.Input()


# Catalog Function #    
    def Catalog(self):
        echo('* Running Function: Catalog *')
        TOOL.processing.Runtime_06()

        a.hotkey('alt', 'g')
        a.press('c')
        a.press('g')

        TOOL.Input()


# Global Update Function #    
    def Global_update(self):
        echo('* Running Function: Global Update *')
        TOOL.processing.Runtime_03()

        a.hotkey('altright', 'g')
        a.press('c')
        a.press('u')

        SIERRA.FTF()
        

# Rapid Update Function #    
    def Rapid_update(self):
        echo('* Running Function: Rapid Update *')
        TOOL.processing.Runtime_02()

        a.hotkey('alt', 'g')
        a.press('d')
        a.press('r')

        SIERRA.FTF()


# Create List Function #    
    class Create_lists:
        create_lists = 0
        
        def JSON(self, NAME):
            print("IN JSON!")
            x, y = a.locateCenterOnScreen('JSON.png')
            
            for process in range(0, 2):  
                a.rightClick(x, y)

            a.hotkey('alt', 'j')
##            a.keyDown('alt')
##            a.press('j')
##            a.press('i')
##            a.keyUp('alt')
            
            for process in range(0, 4):
                a.press('tab')
            a.press('r') # R:\
            
##            a.hotkey('alt', 'n')
            a.keyDown('shift')
            for process in range(0, 4):
                a.press('tab')
            a.keyUp('shift')
        
            a.write('ILS ADMINISTRATOR')
            a.press('return')
            for process in range(0, 2):  
                a.hotkey('ctrl', 'backspace')
            
            a.write('Sierra_logs')
            a.press('return')
            a.hotkey('ctrl', 'backspace')
             
            a.write('Automation Services')
            a.press('return')
            for process in range(0, 2): 
                a.hotkey('ctrl', 'backspace')
            
            a.write('runtime.logs')
            a.press('return')
            a.hotkey('ctrl', 'backspace')
            
            a.write('JSON-' + NAME)
        
            for process in range(0, 2):
                a.press('tab')
        
            a.press('space')
            a.hotkey('alt', 's')
            pass
                
        def __call__(create_lists):
            if create_lists == 0:
                create_lists = 1
                pass

            else:
                echo('* Running Function: Create List *')
                TOOL.processing.Runtime_03()

                a.hotkey('alt', 'g')
                a.press('d')
                a.press('l')

                SIERRA.FTF()

                a.press('tab')
                a.write('400')
                         
    Create_lists = Create_lists()


# Data Exchange Function #    
    def Data_exchange(self):
        echo('* Running Function: Data Exchange *')
        TOOL.processing.Runtime_03()

        a.hotkey('alt', 'g')
        a.press('d')
        a.press('d')


# Delete Records Function #    
    def Delete_records(self):
        echo('* Running Function: Delete Records *')
        TOOL.processing.Runtime_01()

        a.hotkey('alt', 'g')
        a.press('d')
        a.press('1')


# Web Master Function #    
    def Web_master(self):
        echo('* Running Function: Web Master *')
        TOOL.processing.Runtime_01()

        a.hotkey('alt', 'g')
        a.press('d')
        a.press('b')


# Exit Sierra # 
    def Exit(self):
        echo('* Exiting Sierra *')
        TOOL.processing.Runtime_05()
        
        a.hotkey('alt', 'f')
        a.press('x')
        a.press('y')
        a.hotkey('alt', 'q')

        app = 'O'
        
        return app
        
SIERRA = Sierra()

##############################################################################################################################

##############################################################################################################################
if __name__ == '__main__':
    print('')
