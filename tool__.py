#!/usr/bin/python

##################################################################################
##                                                                              ##
##	Library Tools                                                           ##
##	Containers and Functions for general use.                               ##
##                                                                              ##
##	Created By Zachary Lynn.                                                ##
##      Updated on 05.14.2021 by Zachary Lynn for BRPL-ILS.                     ##
##	Copyright © 2021 Boca Raton Public Library. All rights reserved.        ##
##                                                                              ##
##################################################################################

# Modules #
import ctypes
import glob
import threading

import win32clipboard as xcp

from index import *

#### testing WORKSPACE ####
# from WORKSPACE import * #
###########################

# Definitions #

# File Location #

# Initialization #

# TIME #
def TIMESTAMP():
    import time
    global timestamp
    
    timestamp = time.strftime('%H:%M:%S')
    return timestamp
#_TIME_#
# DATE #
def DATESTAMP():
    import datetime
    global datestamp   

    datestamp = datetime.datetime.now()
    datestamp = datestamp.strftime('%m-%d-%Y')
    return datestamp
#_DATE_#
# CHRONOS #
def CHRONOS():
    global filestamp
    timestamp=TIMESTAMP() # possibly timestamp = with return if not updating
    datestamp=DATESTAMP() # possibly datestamp = with return if not updating
#_CHRONOS_#
# FILE #
    datetime = datestamp + ' ' + timestamp
    timedate = timestamp + ' ' + datestamp

    filestamp = datetime 
    filestamp = filestamp[:-2].replace("-", "").replace(":", "").replace(" ", ".")
    return filestamp
#_FILE_#
# THREAD #
THREAD = 0
#_THREAD_#

class paths:
    # Address Chain Function Resolves : source | destination | local | network #
    def Network(self, log_service, MENU): # which service to network, MENU name of script run
        Finn = r'\\FINN\shared\ILS ADMINISTRATOR' + '\\'
        print(log_service)
        print(MENU)
        
        try:
            if log_service == 'FTS': # File path
                cd = Finn + r'Sierra_logs\Automation Services\FTS.p\SYS-' + MENU
                
            elif log_service == 'MARC': # Load path
                cd = Finn + r'Sierra_logs\Automation Services\MARC' + '\\' + MENU + FILE # will have to add to what is being brought in and 'None' the rest.
                
            elif log_service == 'LOGS': # Excel path
                cd = Finn + r'Sierra_logs\Automation Services\runtime.logs\SYS-' + MENU
                
            elif log_service == 'CALL': # Image repo path
                cd = Finn + r'Image Repository\call' + '\\'
                
            elif log_service == 'TITLE': # Image repo path
                cd = Finn + r'Image Repository\title' + '\\'
                
            elif log_service == 'DOWN': # Image repo path
                cd = Finn + r'Image Repository\download' + '\\'
                
            else:
                cd = log_service = None
                
        except:
            cd = log_service = None

        return cd, Finn


    # Temp. directory. Where C:\Users\{USER}\cache #
    def Local(self):
        local = os.path.expanduser("~")

        if not os.path.exists(local + r'\AppData\Local\Temp'):
            os.makedirs(local + r'\AppData\Local\Temp')
        os.system("attrib +h " + local + r'\AppData\Local\Temp')
        
        cache = local + r'\AppData\Local\Temp' + '\\'
        user = cache[9:-20] # Probably based on user name legnth. So more or less username would break this.

        return cache, user
    
##    def Software(self):
            
PATH = paths()


class tools:
# Clock-speed Function #
    class processing:
        def On():    
            pyautogui.DARWIN_CATCH_UP_TIME = 1
            
        def Failsafe_off():
            pyautogui.FAILSAFE = False
            
        def Failsafe_on():
            pyautogui.FAILSAFE = True
            
        def Runtime_00():
            pyautogui.PAUSE = .01
        
        def Runtime_01():
            pyautogui.PAUSE = .2
            
        def Runtime_02():
            pyautogui.PAUSE = .5
                        
        def Runtime_03():
            pyautogui.PAUSE = 1
                        
        def Runtime_04():
            pyautogui.PAUSE = 1.5
            
        def Runtime_05():
            pyautogui.PAUSE = 2
            
        def Runtime_06():
            pyautogui.PAUSE = 3
            
        def Runtime_07():
            pyautogui.PAUSE = 5


# wait/sleep #
    def wait(void, delay):
        for process in range(0, delay):
            event = threading.Event()   
            event.wait(.1)


# Num Lock #
    def numlock(void):
        hllDll = ctypes.WinDLL ("User32.dll")
        VK_NUMLOCK = 0x90
        
        if hllDll.GetKeyState(VK_NUMLOCK)== 1:
            pass
        else:
            a.press('numlock')


# PID #
    def GetPID(PID):
        return [item.split()[1] for item in os.popen('tasklist').read().splitlines()[4:] if PID in item.split()]
    

# Window focus #
    def Window(self, window): #done. full screens correctly.        
        PID = timeout = MAIN.timeout = 0
        
        while PID == 0:
            PID = w.FindWindow(None, window)
            timeout += 1
            MAIN.timeout += 1
            MAIN.Loading() # will reset window PID to '0'
            
            if timeout == 600000: # Timeout for opening window, increase x00000 for longer period.
                print('Application timed out for: ', window)
                PID = -1 # Return PID to log error code as window failure.
                exit()
                
        try:    
            w.ShowWindow(PID, 9)       
            a.getWindowsWithTitle(window)[0].minimize()
            a.getWindowsWithTitle(window)[0].maximize()
            a.hotkey('win', 'up', presses=5)
            print(PID, window)
            
        except:
            print(PID, window)
            pass
        
        return a.getWindowsWithTitle(window)[0].maximize()
     
        
# Input function #
    def Input(window):
        TOOL.processing.Runtime_01()
        I = timeout = '1'
        O = Y = None
    
        timeout = int(timeout)
        
        while I != O:
            timeout += 1 # Timeout can be doubled as loading y += 1
##            Loading()
            
            a.write('1')
            a.hotkey('ctrl', 'a')
            a.hotkey('ctrl', 'c')
            a.hotkey('ctrl', 'x')
            
            try:
                xcp.OpenClipboard()
                O = xcp.GetClipboardData()
                O = str(O)
                xcp.CloseClipboard()
##                Y = O[:-15]
                
                if Y == "None": # FTS/FTF conditional delay
                    a.press('down')
                    a.press('return')
                    I = O

                elif Y == "FTS file save": # FTS/FTF conditional delay
                    a.press('down')
                    a.press('return')
                    I = O

            except:
                xcp.OpenClipboard()
                O = xcp.EmptyClipboard()
                xcp.CloseClipboard()
                TOOL.ClipboardVoid()
                            
            if timeout == 8: # Timeout for searching for writeable area, increase x0 for longer period.
                print('Process timed out for:', window)
                I = O

        TOOL.ClipboardVoid()
        TOOL.processing.Runtime_04()
        return O, timeout
    
 
# Clear Clipboard Contents #
    def ClipboardVoid(void): # Clears clipboard by window handle,(per software clipboard)
        
        if xcp.OpenClipboard(None):
            xcp.EmptyClipboard()
            xcp.CloseClipboard()
            print("Clearing contents...")
##        Main.y += 1
##        MAIN.Loading()
##        print(Main.y)

        else:
            print("Cached contents...")
            pass


# Copy Clipboard Contents #
    def ClipboardCopy(self): # Copies clipboard by window handle, (per software clipboard)

        try:
            xcp == process
            print("Copied contents...")
            pass
        
        except:
            xcp.OpenClipboard(None)
            process = xcp.GetClipboardData(1)
            process = ctypes.c_char_p(process).value
            xcp.CloseClipboard()
            print("Copying contents...")

        return process
    

# Move from R:\ dir \b > output
    def List(void):
        try:
            shutil.rmtree(local + sub_dir)
            
        except:
            pass
        
    # Move : Network -> Local #
        try:            
            shutil.move(network + sub_dir, local)
            
        except:
            pyautogui.alert("R:/>cache")
            pass

    # Create list.txt #
        ARM = os.system("cd ~\\cache" + sub_dir)
        os.chdir(local + sub_dir)
        
        if ARM == 1:
            try:
                os.remove("list.txt")
                
            except:
                pass
                
            os.system("dir /b > list.txt")
            ARM = 0

##          # application blocked #
##            with open(local + '\\Jigsaw Puzzles') as f:
##                lines = f.read().splitlines()
##            print(lines)
##            pyautogui.alert("end")
            
            TOOL.processing.Runtime_01()
            
            # work around #
            subprocess.Popen(r'C:\Users\zlynn\Desktop\LOCAL\UPDATE\iii\Sierra\OTHER\Tool_kit\Notepad++\Notepad++.exe')
            sleep(5)

            txt = 'list.txt'
            Sort_ascending()
            
            #txt = 'JIGSAW.txt'
            #Sort_ascending()

            pyautogui.hotkey('alt', 'f4')

        TOOL.processing.Runtime_02()
        
    # Move : Local -> Network #
        try:
            shutil.move(local + sub_dir, network)
            
        except:
            pass

        
# Perform line operation sort by: 'Integers Ascending' #
    def Sort_ascending(void):                    
        pyautogui.hotkey('alt', 'f')
        pyautogui.press('o')
        pyautogui.press('f4')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')

        pyautogui.write(local + sub_dir)
        pyautogui.press('return')
        pyautogui.hotkey('alt', 'n')
        pyautogui.write('list.txt')
        pyautogui.press('return')

        pyautogui.hotkey('ctrl', 'h')
        pyautogui.write(txt)
        pyautogui.press('tab')
        pyautogui.press('del')
        pyautogui.hotkey('alt', 'a')
        pyautogui.press('esc')

        pyautogui.hotkey('ctrl', 'h')
        pyautogui.write(special, + '.txt')
        pyautogui.press('tab')
        pyautogui.press('del')
        pyautogui.hotkey('alt', 'a')
        pyautogui.press('esc')

        pyautogui.hotkey('ctrl', 'h')
        pyautogui.write('Thumbs.db')
        pyautogui.press('tab')
        pyautogui.press('del')
        pyautogui.hotkey('alt', 'a')
        pyautogui.press('esc')

        pyautogui.press('left')
        pyautogui.hotkey('alt', 'e')
        pyautogui.press('down', presses=11)
        pyautogui.press('right')
        pyautogui.press('down', presses=11)
        pyautogui.press('return')

        pyautogui.hotkey('ctrl', 'home')
        pyautogui.press('del', presses=3)

        pyautogui.hotkey('ctrl', 's')
        pyautogui.hotkey('ctrl', 'w')


# Compare two lists from LOCAL #
    def Compare_list(self, location_A, location_B):
        global list_C
        global list_D
        
        with open(location_A) as file: # MUST state location of list_A to compare onto list_B
            list_A = [l.strip() for l in file]

        with open(location_B) as file: # MUST state location of list_B to compare from list_A
            list_B = [l.strip() for l in file]    

        x = 0
#        print('List A')
        for x in range(len(list_A)): # dir /b > list.txt
            list_A[x] = list_A[x].split("(")[0] # puzzle specific / will ignore
            list_A[x] = list_A[x].split(".")[0] # puzzle specific / will ignore
            list_A[x] = list_A[x][:0] + '"' + list_A[x][0:] + '"'
#            print('\t', list_A[x])

#        print('\n')
        
        y = 0
#        print('List B')
        for y in range(len(list_B)): # list export from Sierra AS-IS
            list_B[y] = list_B[y].replace(',', '')
#            print('\t', list_B[y])
                    
        legnth = len(list_A)
        width = len(list_B)
        height = legnth + width

        list_C = []
        list_D = []
    
#        print('\n')
        
        z = 0
#        print('List C')
        for z in range(height):
            list_C.append(None)

#        print('\n')
            
        n = 0
#        print('List D')
        for n in range(height):
            list_D.append(None)

#        print('\n--\n--\n')
        
        x = y = z = n = 0
        while x <= legnth:
#            print('\t', list_A[x], '\t', list_B[y])
            y += 1
            
            try:
                if list_A[x] in list_B[y]:
#                    print('\t\tMATCH FOUND on:', x, list_A[x], 'with', list_B[y])
                    list_C[z] = 'MATCH FOUND on:' + list_B[y]
                    y = 0
                    x += 1
                    z += 1
                    
            except:
                try:
#                    print('\t\tNO MATCH FOUND on:', x, list_A[x])
                    list_D[n] = 'NO MATCH on:' + list_A[x] 
                    y = 0
                    x += 1
                    n += 1
                    
                except:
#                    print('Compare lists, Exhausted')
                    x = legnth
                    x += 1
                    
                    while None in list_C:
                        list_C.remove(None)
                        
                    while None in list_D:
                        list_D.remove(None)

                    pass

        with open("list_MATCH.txt", "w") as output:
            output.write(str(list_C))
    
        with open("list_NOMATCH.txt", "w") as output:
            output.write(str(list_D))
    
        return list_C, list_D

# Thread count #
    def Thread(self):
        global THREAD

        THREAD += 1

        return THREAD
        

# Exit function #
    def Exit(void):
        n = 4
        while n > 1:
            n -= 1
            print("Exiting in ", n)
            
            for i in range(20):
                sleep(0.05)

            
TOOL = tools()
    
##############################################################################################################################

##############################################################################################################################
if __name__ == '__main__':
    location_A = 'R:\ILS ADMINISTRATOR\Jigsaw Puzzles\list.txt'
    location_B = 'R:\ILS ADMINISTRATOR\Jigsaw Puzzles\JIGSAW.txt'
    TOOL.Compare_list(location_A, location_B)
