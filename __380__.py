#!/usr/bin/env python

##################################################################################
##                                                                              ##
##	SYS-Summary Availability.py Rev.1                                       ##
##	item available; bib not available. Bib Unsuppressed>Suppress>Unsuppress ##
##                                                                              ##
##	Created By Zachary Lynn.                                                ##
##      Updated on 08.28.2020 by Zachary Lynn for BRPL-ILS.                     ##
##	Copyright © 2020 Boca Raton Public Library. All rights reserved.        ##
##                                                                              ##
##      Mono-thread design.                                                     ##
##      The pyautogui & win32gui module are Required to Properly Run Script.    ##
##      HAS A NETWORK DEPENDANCY of Q>R                                         ##
##      HAS A CREATE LIST DEPENDANCY for PERMISSIONS                            ##
##      HAS A GLOBAL UPDATE DEPENDANCY for PERMISSIONS                          ##
##      HAS A DATA EXCHANGE DEPENDANCY for PERMISSIONS                          ##
##      RELIANT OF CREATE LIST | index:(380 | b Type)Review File                ##
##      RELIANT OF Summary Availability.xlsx on the NETWORK                     ##
##                                                                              ##
##      Forthcoming updates:                                                    ##
##      Printer processing catch.                                               ##
##      Window PID and definition.                                              ##
##      Process tree.                                                           ##
##                                                                              ##
##      —>Scheduler handler callable.                                           ##
##      —>Modular                                                               ##
##                                                                              ##
##################################################################################

# Modules
import os
import sys
import subprocess
import pyautogui
import win32gui
import tkinter
import calendar

from datetime import date

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False

# Definitions
tk = tkinter
a = pyautogui
w = win32gui
echo = print

date = date.today()
dd = date.strftime('%d')
yyyy = date.strftime('%y')
mm = date.strftime('%m')

dd = int(dd)
yyyy = int(yyyy)
mm = int(mm)

ld = calendar.monthrange(yyyy, mm)[1]

cd = r'Network:\\Dir\\Default'
window = 'null'
services = 'SYS-Summary Availability.xlsx'
sierra = 'I/O' # Only happens with executable programs of if Sierra is running or not.

# File Location (Centeral location for pointers to external networks) --change to title if you have to reference more than one of similar file type from the network.
datestamp = r'R:\\ILS ADMINISTRATOR\\Sierra_logs\\Automation Services\\runtime.logs\\datestamp.txt'
filestamp = r'R:\\ILS ADMINISTRATOR\\Sierra_logs\\Automation Services\\runtime.logs\\filestamp.txt'
run = r'R:\ILS ADMINISTRATOR\Sierra_logs\Automation Services\runtime.logs'
fts = r'R:\ILS ADMINISTRATOR\Sierra_logs\Automation Services\FTS.p\SYS-Summary Availability' # Generic file directory for where to on the Q drive.
local = r'C:\Users\zlynn\Desktop\LOCAL\cache' # Generic file directtory for user on C drive. Where C:\Users\{USER}\cache

# Initialization
n = 1
GCU = ' '
hwnd = 0
thread = 0
process = 0
progress = '.'

var = 'received'
packet = 'null'
load = 'Complete'
update = 'processing'
filedump = '7.' # which program run, defined by index sheet.

initalization = pyautogui.PAUSE = 1

# Clock-speed Function #
def Processing():
    pyautogui.PAUSE = 1

def Runtime():
    pyautogui.PAUSE = .2

# Window Focus Function #
def Window():

    echo('#####################')
    echo('##                 ##')
    echo('## Window Focus.py ##') # Eventually read in open processes, read and copy open window name. This enables this to be a module rather than a portion of a script.
    echo('##                 ##')
    echo('#####################')
    
    global progress
    global update
    global hwnd
    global n
    
    while load != update:
        print('')
        
        while hwnd == 0:
            n += 1
            TOOL.wait(1)
            a.hotkey('win', 'up')
            print('Loading', progress)
            progress = ('.')*n
            
            if hwnd == 0:
                try:
                    hwnd = win32gui.FindWindow(None, window)
                    w.SetForegroundWindow(hwnd)
                    w.ShowWindow(hwnd, 9)
                    a.hotkey('win', 'up')
                    update = 'Complete' # Must match load for Thread(thread, process).
       
                except:
                    pass
                    
            else:
                pass
            
        n = n -1
        progress = ('.')*n
        print(update, progress, '[done]')
        
# Datestamp Function #
def Datestamp():
    
    echo('######################')
    echo('##                  ##')
    echo('##    Logging.py    ##')
    echo('## -initialization- ##')
    echo('##                  ##')
    echo('######################')
    
    global sierra
    
    global datestamp
    global filedump
    global window
    
    sierra = 'O'
    
    Runtime()
    hwnd = process = 0
    
    cd = datestamp
    
    local = r'C:\WINDOWS\system32\notepad.exe'
    window = 'datestamp.txt - Notepad'
    
    subprocess.Popen("%s %s" % (local, cd))
    Window()

    # Numlock State Function #
    while process != '2':
        TOOL.wait(1)
        a.press('numlock')
        a.press('num2')
        a.hotkey('ctrl', 'a')
        a.hotkey('ctrl', 'c')
        root = tk.Tk()
        root.withdraw()
        process = root = root.clipboard_get()
        
    TOOL.wait(1)
    a.press('numlock')
    echo('######## end #########')
         
    a.hotkey('ctrl', 'a')
    a.press('f5')
    a.hotkey('ctrl', 's')
    
    a.press('left', presses=4)
    
    while hwnd <= 3: # Dependant on 24h time format.
        a.press('backspace')
        hwnd += 1
        
        a.press('left', presses=2)
            
    else:
        a.press('backspace')

    a.keyDown('shiftleft')
    a.keyDown('shiftright')

    a.press('right', presses=4) 
    
    a.keyUp('shiftleft')
    a.keyUp('shiftright')    

    a.hotkey('ctrl', 'x')
    a.press('end')
    a.press('.')
    a.hotkey('ctrl', 'v')
    a.hotkey('ctrl', 'a')
    a.hotkey('ctrl', 'x')
    
    root = tk.Tk()
    root.withdraw()
    datestamp = root = root.clipboard_get()

    a.write(filedump)
    
    a.hotkey('ctrl', 'v')
    a.hotkey('ctrl', 'a')
    a.hotkey('ctrl', 'x')
    
    root = tk.Tk()
    root.withdraw()
    datestamp = root = root.clipboard_get()

    a.hotkey('alt', 'f4')
    a.press('n')
    
# Thread Check Function #
def Thread(thread, process):
    global var 
    global packet
    global update

    Runtime()
    TOOL.wait(1)
    
    while var == packet: # Possible error cause.
        process += 1
        print("\n", thread,':',process, "\n")
        
        a.hotkey('ctrl', 'a')
        a.hotkey('ctrl', 'c')
        a.hotkey('ctrl', 'x')
        print('sent >>')
        
        a.write('received')
        
        try:
            root = tk.Tk()
            root.withdraw()
            packet = root = root.clipboard_get()

        except:
            clipboard = None
            
        print('<<', packet)
        
        if load != update:
            a.press('tab')
            a.hotkey('ctrl', 'e', interval=0.1)

            if sierra == 'I':
                a.press('backspace') # Conditional thread for Sierra function only. 

            else:
                update = ' >> processing'
            
        else:
            packet = 'null'
            
    while var != packet:
        process += 1
        print("\n", thread,':',process, "\n")
        
        a.hotkey('ctrl', 'a')
        a.hotkey('ctrl', 'c')
        a.hotkey('ctrl', 'x')
        print('sent >>')
        
        a.write('received')
        
        try:
            root = tk.Tk()
            root.withdraw()
            packet = root = root.clipboard_get()

        except:
            clipboard = None
        
        print('<<', packet)
        
        if load != update:
            a.press('tab')
            a.hotkey('ctrl', 'e', interval=0.1)

            if sierra == 'I':
                a.press('backspace') # Conditional thread for Sierra function only. 
            
# Re-initialize Function #
def Process(initalization):
    global var 
    global packet
    global update
    global process
    global progress
    global root
    global hwnd
    global n
    
    n = 0
    Processing()
    pyautogui.FAILSAFE = False
    
    print('\n >> running')
    
    while var == packet:
        n += 1
        hwnd = 0
        progress = ('.')*n
        
        try: 
            print(update)
            update = ' >> processing'
            packet = 'null'
            root = 'null'
            process = 1
            
            a.hotkey('ctrl', 'a')
            a.hotkey('ctrl', 'c')
            a.hotkey('ctrl', 'x')
            
            while process <= thread + 5:
                print('Loading', progress)
                TOOL.wait(.1)
                n += 1
                progress = ('.')*n
                process += 1
               
            print('Loading', progress)     
            a.write('\mem.clr')
            process = 0
            root = tk.Tk()
            root.withdraw()
            packet = root = root.clipboard_get()
        
        except:    
            n += 1
            progress = ('.')*n
            a.moveTo(x=0, y=0)
            update = ' >> memory cleared <<\n >> initalizing memory <<\n'
            print('Complete', progress, '[done]')
            pass
        
    else:
        n = 1
        hwnd = 0
        a.moveTo(x=0, y=0)
        print('\n >> running')
        progress = ('.')*n
        update = ' >> memory cleared <<\n >> initalizing memory <<\n'
        print(' >> processing\n')
        pass

    Processing()
    initalization = pyautogui.PAUSE = 1
    
# Sierra Log & Log-in function #
def Sierra():

    echo('###############')
    echo('##           ##')
    echo('## Sierra.py ##')
    echo('##           ##')
    echo('###############')

    global sierra
    
    global var 
    global packet
    global update
    
    global process
    global progress
    global root
    global hwnd
    global n
    
    global datestamp
    global window
    global thread
    
    sierra = 'I'
    
    local = r'C:\Sierra Desktop App\iiirunner.exe'
                  
    subprocess.Popen(local)     

    window = 'Sierra - Boca Raton Public Library'

    Window() # Capitalization is critical.
    
    # Thread Check Function #
    thread += 1
    Thread(thread, process)
    # Re-initialize Function #
    Process(initalization)
    
    TOOL.wait(1)
    
    a.hotkey('ctrl', 'a')
    a.write('SYSTEM')
    a.press('tab', interval=0.1)
    a.write('brpltechserv')
    a.press('return')
    
    # Thread Check Function #
    thread += 1 
    Thread(thread, process)
    # Re-initialize Function #
    Process(initalization)
    
    window = 'Sierra · Boca Raton Public Library · Automation Service'
    
    Window()

def Close():
    a.hotkey('alt', 'f4')
    a.hotkey('alt', 'y')
    a.hotkey('alt', 'q') # Must run a seperate FTS dump program inputing this ouput fts.p into date log durring post.
    sierra = 'O'

# Screen Function Check #
def Check():
    TOOL.wait(2)
    Runtime()

    root = packet = update = 'clear'
    load = var = 'updating'

    while var != packet:

        a.hotkey('alt', 'g')
        a.hotkey('alt', 'u')
        a.hotkey('alt', 'c')
        a.hotkey('alt', 'w', interval=0.5)
        
        a.write('updating')
        
        a.hotkey('ctrl', 'a')
        a.hotkey('ctrl', 'c')
        a.hotkey('ctrl', 'x')
        print('scanning >>')
        
        try:
            root = tk.Tk()
            root.withdraw()
            packet = root = root.clipboard_get()
            a.rightClick(x=0, y=0)

        except:
            clipboard = None
        
    print('<<', packet)    
    Processing()
    
# Global Update Function check #
def check(GCU): # Particular attention to the capitalization.
    global process
    global progress
    
    Runtime()
    TOOL.wait(2)

    n = 0
    
    root = packet = 'clear'
    packet = var = 'updating'

    while var == packet:
        progress = ('.')*n
        print('updating', progress)
        TOOL.wait(.1)
        n += 1
        process += 1
        a.hotkey('alt', 'f')
        a.hotkey('alt', 't')
        a.hotkey('alt', 'l')
        a.hotkey('ctrl', 'c')
        a.press('esc')
        
        try:
            root = tk.Tk()
            root.withdraw()
            packet = root = root.clipboard_get()

        except:
            clipboard = None
    
    progress += ('.')*1
    print('updating', progress, '[done]')
    
# Global Update Screen Initalization Function #
def Global(update):
    a.hotkey('alt', 'g')                            
    a.hotkey('alt', 'c')                            
    a.hotkey('alt', 'u')                            
                                                    
    a.keyDown('ctrlright')                            
    a.hotkey('shift', 't', presses=2)                   
    a.keyUp('ctrlright')                            
                                                    
    a.hotkey('alt', 'g')                            
    a.hotkey('alt', 'u')                            
    a.hotkey('alt', 'c')                            

    Check()
                                                    
    a.hotkey('alt', 'g')                            
    a.hotkey('alt', 'c')                            
    a.hotkey('alt', 'u')                            

def Records():
        
    echo('################')
    echo('##            ##')
    echo('## Records.py ##')
    echo('##            ##')
    echo('################')

    global filestamp

    line = 0
    cd = fts
    
    echo('\t##################')
    echo('\t#                #')
    echo('\t# Max Records.py #')
    echo('\t#                #')
    echo('\t##################')

    filedump = open("%s" "\\" "%s" "%s" % (cd, datestamp, ".p"), "r")

    for data in filedump:
        data = str(data) # Convert data from file into readable string.
        
        for n in data:
            data = filedump.read(1)
            
            if data == 'X':
                line += 1
                filestamp = line
                print("Processing:", line)

    filestamp = str(filestamp)
        
    echo('\n####### end ######\n')
    
def Filedump():

    global thread
    global window

    # Thread Check Function #
    thread += 1
    # Re-initialize Function #
    Process(initalization)
    
    window = 'Excel'
    
    cd = run
    
    excel = r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.exe'
    
    subprocess.Popen("%s" % (excel))
    TOOL.wait(1)
    
    Window()
    
    a.hotkey('alt', 'o')
    a.press('o')
    
    Thread(thread, process)
    # Re-initialize Function #
    Process(initalization)
    
    a.press('f4')
    a.hotkey('ctrl', 'a')
    
    a.write(cd)
    
    a.press('return')
    a.hotkey('alt', 'n')
    a.write(services)
    a.press('return', interval=1)
    
    a.write(datestamp) # Automation Logs Run.
    a.press('f2')
    a.press('up')
    a.press('del', presses=2)

    a.press('tab') # Records Expired.
    if filestamp == '1':
        a.write('No records')
        
    else:
        a.write(filestamp)

    a.press('tab') # Errors.
    
    if filestamp == '1':
        a.write('1')

    else:
        a.write('0')

    a.hotkey('ctrl', 's')

    a.keyDown('ctrlright')
    a.keyDown('shiftright')
    
    a.press('+') # Not recognizing for some reason? Num-lock state?
    
    a.keyUp('shiftright')
    a.press('left')
    a.keyUp('ctrlright')
    
    a.hotkey('ctrl', 's')
    a.hotkey('alt', 'f4')
    
def FTS(filedump):
    
    echo('#################')
    echo('##             ##')
    echo('## FTS dump.py ##') # Reliant on Sierra() being ran before calling.
    echo('##             ##')
    echo('#################')
    
    global thread
    global window
    
    pyautogui.FAILSAFE = False
    filedump = 'null'
    
    a.hotkey('alt', 'g')
    a.hotkey('alt', 'd')
    a.hotkey('alt', 'd')
    a.press('tab')
    
    a.press('down', presses=3, interval=0.1)
    
    a.rightClick(x=0, y=0) # Mouse initalization.
        
    for process in range (3, 5):
        TOOL.wait(.1)
        a.rightClick(x=1408, y=206) # Last Modified.
        a.press('tab')
        
    a.hotkey('alt', 't')
    a.hotkey('alt', 'u')
    a.hotkey('alt', '2')

    Runtime()
    
    a.press('tab', presses=10, interval=0.1) # Dump to local cache.
    a.press('c')
    
    a.press('return', presses=2)
        
    # Re-initialize Function #
    Process(initalization)

    Processing()
    
    a.hotkey('alt', 'o')
    
    Close()

    echo('\t###############')
    echo('\t#             #')
    echo('\t# Save dir.py #')
    echo('\t#             #')
    echo('\t###############')
    
    a.hotkey('win', 'e')
    a.press('f4')
    a.hotkey('ctrl', 'a')
    
    a.write(local)
    
    a.press('return')
    a.hotkey('ctrl', 'a')
    a.hotkey('ctrl', 'x')
    a.press('f4')
    a.hotkey('ctrl', 'a')
    
    a.write(fts)

    echo('\n##### end #####\n')
    
    a.press('return')
    a.hotkey('ctrl', 'v')
    a.press('space', presses=2, interval=2) # redundantcy, in case of an overwrite.

    echo('\t##################')
    echo('\t#                #')
    echo('\t# Max Records.py #')
    echo('\t#                #')
    echo('\t##################')

    Records()
    if filestamp == "1":
        print("Error")

    else:
        print("Records total:", filestamp)
    
    echo('\n####### end ######\n')

    Filedump()                 
    
##############################################################################################################################

##############################################################################################################################

# Script
if __name__ == "__380__":
    print('\n', '* SYS-' + MAIN.NAME + ' *', '\n')
    
    a.hotkey('ctrl', 'a')
    a.hotkey('ctrl', 'c')
    a.hotkey('ctrl', 'x')
    
    thread += 1 # Assign I
    Datestamp()
    Window()
    # Re-initialize Function #
    Process(initalization)

    a.keyDown('ctrl')
    Sierra() # Assign II 
    a.keyUp('ctrl')
    
    for n in range (2):
        a.hotkey('alt', 'f')
        a.hotkey('alt', 't')
        a.hotkey('alt', 's')
        a.press('down')
        a.hotkey('alt', 'o', interval=1)
        
        a.write(datestamp)
        a.hotkey('alt', 'o', interval=1)

        Check()      
    
    echo('#################################')
    echo('##                             ##')
    echo('## SYS-Summary Availability.py ##')
    echo('##                             ##')
    echo('#################################')
    
    #####################
    ##                 ##
    ## ILS Work Manuel ##
    ##                 ##
#####################################################
                                                    #
    # Sequence to "Create Lists"                    #
                                                    #
    # Re-initialize Function #                      #
    Process(initalization)                          #
                                                    #
    a.hotkey('alt', 'g')                            #
    a.hotkey('alt', 'd')                            #
    a.hotkey('alt', 'l')                            #
                                                    #
    # "Create Lists" window                         #
                                                    #
    a.write('380')                                  #
                                                    #
    a.hotkey('alt', 's', interval=1)                #
    a.hotkey('alt', 'e')                            #
                                                    #
    Check()                                         # # Check function to make sure all records get updated.
    a.write(services)                               #
                                                    #
    a.press('backspace', presses=5, interval=0.1)   # # Deleting .xlsx from naming convention
    a.hotkey('alt', 'p', interval=1)                #
    a.press('b', interval=1)                        #
                                                    #
    a.hotkey('alt', 's')                            # # Caution to how long the search can take to run and might eat any inputs such as 'tab', and 'g', 'd', 'r'.
                                                    #
    # Re-initialize Function #                      #
    Process(initalization)                          #
                                                    #
    a.press('tab', interval=0.1)                    #
                                                    #
    # Sequence to "Global Update"                   # # Find:Unsuppressed Bibs (Unsuppressed Bibs>Suppress Bibs)
                                                    #
    # Re-initialize Function #                      #
    Process(initalization)                          #
                                                    #
    Global(update)                                  #
                                                    #
    # "Global Update" window                        #  
                                                    #    
    a.press('space')                                #  
    a.press('r')                                    #   
    a.press('tab')                                  #   
    a.write('382')                                  #   
    a.write('380')                                  #   
    a.hotkey('alt', 'r', interval=1)                #   
                                                    #  
    a.hotkey('ctrl', 'tab')                         # # initalize selection.
    a.press('space', presses=4, interval=1)         #
                                                    #
    check(GCU)                                      # 
                                                    # 
    a.keyDown('ctrlright')                          #
    a.press('t', presses=2)                         # # Advance to "2. Command input" tab. 
    a.keyUp('ctrlright')                            #
                                                    #   
    a.hotkey('alt', 'd')                            #  
    a.hotkey('alt', 'f')                            #   
    a.hotkey('alt', 'o')                            #   
    a.hotkey('alt', 'x', presses=5, interval=0.2)   #               
                                                    #    
    a.write('3')                                    #   
    a.write('1')                                    # # Must be seperated as populate menu was eating the 4.
    a.press('return')                               #
                                                    #
    a.hotkey('alt', 'f', presses=5, interval=0.2)   #
    a.press('-')                                    #
    a.press('return')                               #
    a.hotkey('alt', 'r', presses=5, interval=0.2)   #   
    a.press('n')                                    #  
    a.press('return')                               #    
                                                    #   
    a.hotkey('alt', 'o')                            #   
                                                    # 
    a.keyDown('ctrlright')                          #  
    a.press('t')                                    # # Advance to "3. Preview" tab.    
    a.keyUp('ctrlright')                            #
                                                    #
    check(GCU)                                      #
                                                    #
    a.hotkey('alt', 'r')                            #  
    a.hotkey('alt', 'y')                            #  
                                                    #
#####################################################

    echo('##################')
    echo('##              ##')
    echo('## Check Rec.py ##')
    echo('##              ##')
    echo('##################')
    
    Check() # Check function to make sure all records get updated.
    # Re-initialize Function #
    Process(initalization)
    Check() # Check function to make sure all records get updated.

#####################################################
                                                    #
    # Sequence to "Global Update"                   # # Find:Unsuppressed Bibs (Suppressed Bibs>Unsuppress Bibs)
                                                    #
    # Re-initialize Function #                      #
    Process(initalization)                          #
                                                    #
    Global(update)                                  #
                                                    #
    # "Global Update" window                        #  
                                                    #    
    a.press('space')                                #  
    a.press('r')                                    #   
    a.press('tab')                                  #   
    a.write('382')                                  #   
    a.write('380')                                  #   
    a.hotkey('alt', 'r', interval=1)                #   
                                                    #  
    a.hotkey('ctrl', 'tab')                         # # initalize selection.
    a.press('space', presses=4, interval=1)         #
                                                    #
    check(GCU)                                      # 
                                                    #  
    a.keyDown('ctrlright')                          #
    a.press('t', presses=2)                         # # Advance to "2. Command input" tab. 
    a.keyUp('ctrlright')                            #
                                                    #  
    a.hotkey('alt', 'd')                            #  
    a.hotkey('alt', 'f')                            #   
    a.hotkey('alt', 'o')                            #   
    a.hotkey('alt', 'x', presses=5, interval=0.2)   #               
                                                    #    
    a.write('3')                                    #   
    a.write('1')                                    # # Must be seperated as populate menu was eating the 4.
    a.press('return')                               #
                                                    #
    a.hotkey('alt', 'f', presses=5, interval=0.2)   #
    a.press('n')                                    #
    a.press('return')                               #
    a.hotkey('alt', 'r', presses=5, interval=0.2)   #   
    a.press('-')                                    #  
    a.press('return')                               #    
                                                    #   
    a.hotkey('alt', 'o')                            #   
                                                    # 
    a.keyDown('ctrlright')                          #  
    a.press('t')                                    # # Advance to "3. Preview" tab.    
    a.keyUp('ctrlright')                            #
                                                    #
    a.hotkey('alt', 'f', presses=2, interval=10)    # # Update Summary fts.p dump.
    a.hotkey('alt', 'p')                            # 
                                                    #
    check(GCU)                                      #
                                                    #
    a.hotkey('alt', 'r')                            #
    a.hotkey('alt', 'y')                            #
                                                    #
#####################################################

    Check() # Check function to make sure all records get updated.
    # Re-initialize Function #
    Process(initalization)
    Check() # Check function to make sure all records get updated.
    Close()
    # End of exit thread.

    Sierra() # Assign IV

    FTS(filedump) # Assign V & VI

    a.hotkey('alt', 'f4')
    
else:
    print('9999 : 380 {Summary Availability}')

print(__name__, 'COMPLETE!')
