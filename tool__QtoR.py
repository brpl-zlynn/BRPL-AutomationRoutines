#!/usr/bin/env python

##################################################################################
##                                                                              ##
##	QtoR.py                                                                 ##
##	Replaces target directory path from Q to R network path.	        ##           
##                                                                              ##
##	Created By Zachary Lynn.                                                ##
##      Updated on 09.01.2020 by Zachary Lynn for BRPL-ILS.                     ##
##	Copyright © 2020 Boca Raton Public Library. All rights reserved.        ##
##                                                                              ##
##      null-thread design.                                                     ##
##      The pyautogui & win32gui module are Required to Properly Run Script.    ##
##      HAS A NETWORK DEPENDANCY of Q>R.                                        ##
##                                                                              ##
##################################################################################

# Modules
import os 
import subprocess
import pyautogui
import win32process
import win32gui
import win32con
import tkinter

from time import sleep

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# Definitions
tk = tkinter
a = pyautogui
wgui = win32gui
wpro = win32process
wcon = win32con
echo = print

cd = r'Network:\\Dir\\Default'
location = 'GPS'
window = 'null'

# File Location (Centeral location for pointers to external networks) --change to title if you have to reference more than one of similar file type from the network.
Path_Dir = r'C:\\Sierra Desktop App\\iiirunner.lax'
FROM = 'Q:' # What path letter was in place.
TO = 'R:' # What path letter is changing to.
filestamp = r'R:\\ILS ADMINISTRATOR\\Sierra_logs\\Automation Services\\runtime.logs\\filestamp.txt'
fts = r'R:\ILS ADMINISTRATOR\Sierra_logs\Automation Services\FTS.p\SYS-Daily Accounts Expired' # Generic file directory for where to on the NETWORK drive.
local = r'C:\Users\zlynn\Desktop\LOCAL\cache' # Generic file directtory for user on C drive. Where C:\Users\{USER}\cache

# Initialization
hwnd = 0
filedump = '1.' # which program run, defined by index sheet.

# iiirunner.lax
STDERR = '#   LAX.STDERR.REDIRECT\n#   -------------------\n#   leave blank for no output, "console" to send to a console window,\n#   and any path to a file to save to the file\n\n'
STDIN = '#   LAX.STDIN.REDIRECT\n#   ------------------\n#   leave blank for no input, "console" to read from the console window,\n#   and any path to a file to read from that file\n\n'
STDOUT = '#   LAX.STDOUT.REDIRECT\n#   -------------------\n#   leave blank for no output, "console" to send to a console window,\n#   and any path to a file to save to the file\n\n'
FOOTER = '#   LAX.USER.DIR\n#   ------------\n#   left blank, this property will cause the native launcher to not\n#   alter the platform default behavior for setting the user dir.\n#   To override this you may set this property to a relative or absolute path.\n#   Relative paths are relative to the launcher.\n\nlax.user.dir=.\n\n\n#   LAX.VERSION\n#   -----------\n#   version of LaunchAnywhere that created this properties file\n\nlax.version=14.0\n\n\n'

# Clock-speed Function #
def Processing():
    pyautogui.PAUSE = 1

def Runtime():
    pyautogui.PAUSE =.2

def Window(pid):

    echo('######################')
    echo('##                  ##')
    echo('## Window Handle.py ##') 
    echo('##                  ##')
    echo('######################')
    
    def callback (hwnd, hwnds):
        if wgui.IsWindowVisible(hwnd) and wgui.IsWindowEnabled(hwnd):
            _, found_pid = wpro.GetWindowThreadProcessId(hwnd)

            if found_pid == pid:
                hwnds.append (hwnd)

        return True
    
    hwnds = []
    wgui.EnumWindows (callback, hwnds)
    
    return hwnds

def Focus(hwnd):

    echo('#####################')
    echo('##                 ##')
    echo('## Window Focus.py ##') 
    echo('##                 ##')
    echo('#####################')
    
    hwnd = wgui.FindWindow(None, window)
    wgui.SetForegroundWindow(hwnd)
    wgui.ShowWindow(hwnd, 9)
    
# Computer ID Collector #
def Computer_ID():
    
    echo('###########################')
    echo('##                       ##')
    echo('## Collection Service.py ##')
    echo('##    -initialization-   ##')
    echo('##                       ##')
    echo('###########################')

    global location
    global filedump
    global window
    
    global ERR
    global IN
    global OUT
    
    Runtime()
    hwnd = process = Tk = 0
    
    cd = filestamp
    
    local = r'C:\WINDOWS\system32\Notepad.exe'
    window = 'filestamp.txt - Notepad'
    
    Notepad = subprocess.Popen("%s %s" % (local, cd))

    sleep(2)
    Focus(hwnd)
    
    filedump = os.environ['COMPUTERNAME']

    a.hotkey('ctrl', 'a')
    a.write(filedump)
    a.press('backspace', presses=5)
    a.press('home')
    a.press('delete', presses=5)
    a.hotkey('ctrl', 'a')
    a.hotkey('ctrl', 'x')

    while Tk <= 2:
        Tk += 1
        root = tk.Tk()
        root.withdraw()
        location = root = root.clipboard_get()

    a.hotkey('alt', 'f4')
    a.press('n')

    ERR = 'lax.stderr.redirect='+TO+'//ILS ADMINISTRATOR//Sierra_logs//'+location+'//'+filedump+'//Std_Error.log'
    IN = 'lax.stdin.redirect='+TO+'//ILS ADMINISTRATOR//Sierra_logs//'+location+'//'+filedump+'//Std_IN.log'
    OUT = 'lax.stdout.redirect='+TO+'//ILS ADMINISTRATOR//Sierra_logs//'+location+'//'+filedump+'//Std_OUT.log'
        
    print(ERR)
    print(IN)
    print(OUT)
    
# Path Update Function #
def Path_Object():
    
    echo('####################')
    echo('##                ##')
    echo('## Update_Path.py ##')
    echo('##                ##')
    echo('####################')
    
    global Path_Dir
    global window

    Processing()
    hwnd = process = Tk = 0
    
    cd = Path_Dir
    
    clipboard = root = None
    
    local = r'C:\WINDOWS\system32\Notepad.exe'
    window = 'iiirunner.lax - Notepad'
    
    Notepad = subprocess.Popen("%s %s" % (local, cd))
    
    sleep(2)
    Focus(hwnd)
    
    local = 'lax.stderr.redirect=' # Log path exists !XOR.
    
    a.hotkey('ctrl', 'f')
    a.write(local)
    a.hotkey('return')
    a.press('esc')
    a.hotkey('ctrl', 'c')

    while Tk <= 2:
        Tk += 1
        root = tk.Tk()
        root.withdraw()
        window = root = root.clipboard_get()
    
    if local == window:
        a.hotkey('ctrl', 'h')
        a.write(FROM)
        a.press('tab')
        a.write(TO)
        a.hotkey('alt', 'a')
        a.press('esc')
        a.hotkey('ctrl', 's')
        a.hotkey('alt', 'f4')

    else:
        local = 'lax.root.install.dir=C:\\'+'\Sierra Desktop App'
        
        if location == 'SRL': # Not nessesary to seperate the locations.
            a.hotkey('ctrl', 'f')
            a.write(local)
            a.press('return')
            a.press('esc')
            a.write(local)
            a.press('return', presses=3)

            a.write('#                       #\n')
            a.write('#       ---log---       #\n')
            a.write('#                       #\n')
            a.press('return', presses=2)

            a.write(STDERR)
            a.write(ERR)
            a.press('return', presses=3)
            
            a.write(STDIN)
            a.write(IN)
            a.press('return', presses=3)
            
            a.write(STDOUT)
            a.write(OUT)
            a.press('return', presses=3)

            a.hotkey('shiftright', 'down', presses=99)
            a.press('delete')

            a.write(FOOTER)
            
            a.hotkey('ctrl', 's')
            a.hotkey('alt', 'f4')
            
        if location == 'DTL':# Not nessesary to seperate the locations.
            a.hotkey('ctrl', 'f')
            a.write(local)
            a.press('enter')
            a.press('esc')
            a.write(local)
            a.press('return', presses=3)

            a.write('#                       #\n')
            a.write('#       ---log---       #\n')
            a.write('#                       #\n')
            a.press('return', presses=3)

            a.write(STDERR)
            a.write(ERR)
            a.press('return', presses=3)
            
            a.write(STDIN)
            a.write(IN)
            a.press('return', presses=3)
            
            a.write(STDOUT)
            a.write(OUT)
            a.press('return', presses=3)

            a.hotkey('shiftright', 'down', presses=99)
            a.press('delete')

            a.write(FOOTER)
            
            a.hotkey('ctrl', 's')
            a.hotkey('alt', 'f4')


##############################################################################################################################

##############################################################################################################################

# Script
if __name__ == '__main__':
    print("\n", '* SYS-QtoR *', "\n")
    print('THANKS FOR HELPING OUT PEARCE!')

    Computer_ID()
    
    Path_Object()


exit()
