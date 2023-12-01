#!/usr/bin/env python

##################################################################################
##                                                                              ##
##	SYS-Miss Bib-Img.py                                                     ##
##	Adds images to Sierra repository and updates affiliated MARC.           ##
##                                                                              ##
##	Created By Zachary Lynn.                                                ##
##      Updated on 04.14.2023 by Zachary Lynn for BRPL-ILS.                     ##
##	Copyright © 2022 Boca Raton Public Library. All rights reserved.        ##
##                                                                              ##
##      Milti-thread design | Poly-thread executed.                             ##
##      The pyautogui & win32gui module are Required to Properly Run Script.    ##
##      HAS A NETWORK DEPENDANCY of Q>R                                         ##
##      HAS A BIBLIOGRAPHIC RECORD EDIT for PERMISSIONS                         ##
##      RELIANT OF ?.???.xlsx on the NETWORK                                    ##
##                                                                              ##
##      Forthcoming updates:                                                    ##
##      Read Current and Max Records searched on assigning M&M=Error, C&M=None  ##
##      Logs & data collection                                                  ##
##                                                                              ##
##  Rather move entire front end to backend SQL processing, and /cv do updates. ##
##                                                                              ##
##################################################################################

# Modules
from urllib.request import urlretrieve
from __main__ import *
from tool__ import *
try:
    from tool__Sierra import *
except:
    pass

TOOL.processing.Runtime_03()
TOOL.processing.Failsafe_on()
TOOL.processing.On()

local, user = PATH.Local()
cd, network = PATH.Network(None, None)

#Initialization
SELECT = 0

##############################################################################################################################

##############################################################################################################################

# Bibcore_ append #
def Append_name():
    log_service = 'CALL'
    cd, network = PATH.Network(log_service, None)
    for file in os.listdir(cd):
        os.chdir(cd)
        append = file.replace(' ', '_')
        os.rename(file, cd + "bibcore_" + append)
    
    log_service = 'TITLE'
    cd, network = PATH.Network(log_service, None)
    for file in os.listdir(cd):
        os.chdir(cd)
        append = file.replace(' ', '_')
        os.rename(file, cd + "bibcore_" + append)
        
    log_service = 'DOWN'
    cd, network = PATH.Network(log_service, None)
    for file in os.listdir(cd):
        os.chdir(cd)
        append = file.replace(' ', '_')
        os.rename(file, cd + "bibcore_" + append)

def Redact_name():
    log_service = 'CALL'
    cd, network = PATH.Network(log_service, None)
    for file in os.listdir(cd):
        os.chdir(cd)
        redact = file.replace('bibcore_', '').replace('_', ' ')
        os.rename(file, cd + redact)
    
    log_service = 'TITLE'
    cd, network = PATH.Network(log_service, None)
    for file in os.listdir(cd):
        os.chdir(cd)
        redact = file.replace('bibcore_', '').replace('_', ' ')
        os.rename(file, cd + redact)
    
    log_service = 'DOWN'
    cd, network = PATH.Network(log_service, None)
    for file in os.listdir(cd):
        os.chdir(cd)
        redact = file.replace('bibcore_', '').replace('_', ' ')
        os.rename(file, cd + redact)

def Destroy_name():
    log_service = 'CALL'
    cd, network = PATH.Network(log_service, None)
    for file in os.listdir(cd):
        os.rmdir(cd)
    
    log_service = 'TITLE'
    cd, network = PATH.Network(log_service, None)
    for file in os.listdir(cd):
        os.rmdir(cd)
    
    log_service = 'DOWN'
    cd, network = PATH.Network(log_service, None)
    for file in os.listdir(cd):
        os.rmdir(cd)

    try:
        shutil.rmtree(local + 'Image Repository')
    except:
        pass

    
def GALE_download(): # /cv do
    x=0
    cd = PATH.Network(None, None)
    cd = cd[1] + 'Image Repository\\' + 'download\\'
    
    # ISBN format conversion #
    def ISBN_format(x, cd):
        filedump = cd.replace('download\\', '') + 'ISBN.txt'

        with open(filedump) as file:
            data = file.read().splitlines()
                        
            for count, line in enumerate(data):
                data[count] = line[:3] + '-' + line[3:4] + '-' + line[4:8] + '-' + line[8:12] + '-' + line[12:13]

                if '----' in data:
                    print("data incorrectly formated, an error exists within the list that does not follow standard ISBN formating. Please double check that the list ONLY contains ISBN numbers, one per line.")
                    exit()

            ISBN = data
            
        return ISBN, count
    
    # Gale image Load #
    def GALE_img(x):
        ISBN, count = ISBN_format(x, cd)
        GALE = [None] * count
        
        while x < count:
            GALE[x] = "https://callisto.ggsrv.com/imgsrv/FastFetch/UBER1/" + ISBN[x] + "_00001-p" + "?legacy=no&pdf2img=true&format=jpeg&density=200&download=true&dl=" + ISBN[x] + "0_00001-p.jpg"
            x+=1

        return GALE, ISBN, cd

    GALE_URL, ISBN, cd = GALE_img(x)

    for count, line in enumerate(GALE_URL):
        pass
    print(ISBN)
    print(GALE_URL)
    print(cd)
    
    while x <= count:
        try:
            urlretrieve(GALE_URL[x], cd  + ISBN[x].replace('-', '') + '.jpg')
            file = open(cd + r'\ISBN.txt', 'a')
            file.write(ISBN[x].replace('-', '') + '\n')
            file.close()  
            print(GALE_URL[x])
            
        except:
            file = open(cd + r'\non-ISBN.txt', 'a')
            file.write(ISBN[x].replace('-', '') + '\n')
            file.close()
            print(ISBN[x].replace('-', ''))            
            
        x+=1
        TOOL.wait(5)

    return cd


# Image Repository List(s) #
def Repo_list():

    def Sort_ascending():
        subprocess.Popen([r'C:\Program Files\Notepad++\Notepad++.exe', sub_dir]) # Based on v8.4.6 (64-bit)
        TOOL.wait(5)
        
        for process in range(0, 2):  
            a.hotkey('ctrl', 'a')
            a.hotkey('ctrl', 'h')
            if process == 0:
                a.write('list.txt')
            if process == 1:
                a.write('Thumbs.db')
            a.press('tab')
            a.press('del')
            a.hotkey('alt', 'a')
            a.press('esc')
        
        a.press('left')
        a.hotkey('alt', 'e')
        
        a.press('L')
            
        for process in range(0, 15):
            a.press('down')

        a.press('return')
        a.hotkey('ctrl', 'home')
        
        for process in range(0, 2):
            a.press('del')

        a.hotkey('ctrl', 's')
        a.hotkey('ctrl', 'w')
    
    try:
        shutil.rmtree(local + 'Image Repository')
    except:
        pass
    
# Move : Network -> Local #
    try:            
        shutil.move(network + 'Image Repository', local)
    except:
        a.alert("Image Repository does not exist")
        pass
    
# Call #
    ARM = os.system("cd ~\\cache\Image Repository") 
    os.chdir(local + r'Image Repository\call') 
    
    if ARM == 1:
        try:
            os.remove("list.txt")
        except:
            pass
            
        os.system("dir /b > list.txt")
        ARM = 0

# Title #
    ARM = os.system("cd ~\\cache\Image Repository") 
    os.chdir(local + r'Image Repository\title')
    
    if ARM == 1:
        try:
            os.remove("list.txt")
        except:
            pass
            
        os.system("dir /b > list.txt")
        ARM = 0

# ISBN #
    ARM = os.system("cd ~\\cache\Image Repository") 
    os.chdir(local + r'Image Repository\download')
    
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
##            a.alert("end")
        
        TOOL.processing.Runtime_01()

        # work around #
        TOOL.wait(5)
        
        # Call #
        sub_dir, user = PATH.Local()
        sub_dir = sub_dir + r'Image Repository\call\list.txt'
        Sort_ascending()

        # Title #
        sub_dir, user = PATH.Local()
        sub_dir = sub_dir + r'Image Repository\title\list.txt'
        Sort_ascending()

        # ISBN #
        sub_dir, user = PATH.Local()
        sub_dir = sub_dir + r'Image Repository\download\list.txt'
        Sort_ascending()

        a.hotkey('alt', 'f4')

        TOOL.wait(7)
                
    TOOL.processing.Runtime_04()
    
# Move : Local -> Network #
    try:
        shutil.move(local + 'Image Repository', network)
    except:
        print(local)
        print(network)
        a.alert("Image Repository does not exist")
        pass

    
# Upload Image to Repository #    
def Repository():
    TOOL.processing.Runtime_03()
    
    def Upload():
        a.hotkey('alt', 't')
        a.press('g')
        a.press('1') # number 1 not L
           
        a.hotkey('alt', 'i')            
        a.press('r') # R:\
  
        for process in range(0, 6):                        
            a.press('tab')
            
        a.write('ILS ADMINISTRATOR')
        a.press('return')
        
        a.write('Image Repository')
        a.press('return')

        a.write(sub_dir)
        a.press('return')
        
        a.hotkey('ctrl', 'shift', 'tab')

        print("Uploading :", sub_dir, '\n')

        a.hotkey('ctrl', 'a')
        a.press('return')

        while MAIN.root != 'I':
            a.hotkey('alt', 'o')
            try:
                MAIN.Input()
            except:
                a.hotkey('alt', 'g')
                a.press('u')
                a.press('h')
                 
    SIERRA.Check_in()
    SIERRA.Web_master()
    
    # Call #
    sub_dir = 'call'
    Upload()
    
    SIERRA.Check_in()
    SIERRA.Web_master()

    # Title #
    sub_dir = 'title'
    Upload()
    
    SIERRA.Check_in()
    SIERRA.Web_master()

    # Title #
    sub_dir = 'down'
    Upload()


# Write to 856 42 #
def MARC_856():
    TOOL.processing.Runtime_03()
    x = 1 # 1 or 0 depending on if a blank exists or not

    ##########################################################################
    # ^ Recode this so that it detects blank or not since everytime it breaks.
    ##########################################################################

    while x < len(lines):
        TOOL.wait(1)
        a.write(lines[x].replace('.jpeg', '').replace('.jpg', '').split("(")[0])
##        CAKE
##        INSTURMENTS
##        KIT
##        TABLEGAME
##        YARDGAME >> BYG
##        BACKPACK
##        JIGSAW
##        DOLL
    
        a.hotkey('alt', 'e')
        a.hotkey('alt', 's')
        a.hotkey('alt', 's')
        for process in range(0, 14):
            TOOL.wait(1) # find in selection list, jic because the catalogging is not coming up with the exact record.
            if process == 13:
                print(x, ':', lines[x])
                        
        TOOL.wait(1)
        a.hotkey('ctrl', 'shift', 'e')
        a.hotkey('ctrl', 'shift', 'e')
        a.hotkey('ctrl', 'shift', 'e')
        a.hotkey('ctrl', 'shift', 'e')
        a.hotkey('ctrl', 'shift', 'e')
        TOOL.wait(2)
        a.hotkey('ctrl', 'i')
        a.press('y')
        a.hotkey('ctrl', 'left')
        
        for process in range(0, 3):
            a.press('del')
            
        a.write('85642')
        a.write('|zCover image|uhttps://catalog.bocalibrary.org/screens/bibcore_')
        a.write(lines[x].replace(' ', '_'))
        for process in range(0, 2):       
            a.press('del')
        a.hotkey('alt', 'o')
        a.hotkey('alt', 'q')
        a.press('y')
        a.press('tab')
        TOOL.wait(5) # make the right selection call no., keyword, etc.
        x+=1


###################################################################################################

###################################################################################################

# Script
if __name__ == "__398__": # 398
    print(f"\n* SYS- {MAIN.NAME} *\n")

    while SELECT == 0 or SELECT == '0':
        if SELECT == 0:    
            print("""   Welcome!

   Please be aware that the images must be formated to the correct format
   and placed in the correct folders to be able to load properly into the
   server.
    
   What material are you working with?

   Please make a selection from the list below:
       1) Physical
       2) Digital
       3) Both
       0) Exit
        
    """)

            SELECT = input()

        #choice:Physical
        if SELECT == '1':
            print("Loading Physical Images")
            TOOL.wait(1)
            SELECT = 'P'

        #choice:GALE
        elif SELECT == '2':
            print("Loading Digital Images")
            TOOL.wait(1)
            SELECT = 'D'
            
        elif SELECT == '3':
            print("Loading both Physical and Digital Images")
            TOOL.wait(1)
            SELECT = 'B'
            
        #choice:Exit
        elif SELECT == '0':
            TOOL.wait(1)
            TOOL.Exit()

            print("\nThank you, have a great day.")
            TOOL.wait(1)
            exit()
                
        #choice:Other
        else:
            print("\nInvalid program selection.")
            SELECT = 0
            TOOL.wait(1)
      
    if SELECT == 'D' or SELECT == 'B':

        GALE_download()
        
        Repo_list() 
        Append_name()
        
        SIERRA.Launch()
        SIERRA.Check_in()
        SIERRA.Catalog()

###while loop through list Z)
        
        a.press('i') # search term
        
        log_service = 'DOWN'
        cd, Finn  = PATH.Network(log_service, None)
        
        try:
            with open(cd + 'bibcore_list.txt') as download:
                lines = download.read().splitlines()
            os.remove(cd + 'bibcore_list.txt')

        except:
            print("\nNo database for: downloads exist.")

        MARC_856()
                   
        a.hotkey('shift', 'tab')
    
        SELECT == '0'

    if SELECT == 'P' or SELECT == 'B':
        
        Repo_list()         ## CMNT OUT IF RUN ##
        Append_name()       ## CMNT OUT IF RUN ##
        
        SIERRA.Launch()
        SIERRA.Check_in()
        SIERRA.Catalog()

###while loop through list A)

        a.press('c') # search term
        
        log_service = 'CALL'
        cd, Finn  = PATH.Network(log_service, None)
        
        try:
            with open(cd + 'bibcore_list.txt') as call:
                lines = call.read().splitlines()

        except:
            print("\nNo database for: call numbers exist.")

        MARC_856()
        os.remove(cd + 'bibcore_list.txt')
           
        a.hotkey('shift', 'tab')

###while loop through list B)
        
        a.press('w') # search term
        
        log_service = 'TITLE'
        cd, Finn = PATH.Network(log_service, None)
        
        try:            
            with open(cd + 'bibcore_list.txt') as title:
                lines = title.read().splitlines()
            
        except:
            print("\nNo database for: titles exist.")

        MARC_856()
        os.remove(cd + 'bibcore_list.txt')

        Repository()
       
#        Destory_name()    

        SELECT == '0'

###################################################################################################

###################################################################################################  

elif __name__ == "__main__":  
    print(f"\n* SYS-Miss Bib-Img(Redact) *\n")

##    Redact_name()
##    Append_name()

    try:
        shutil.rmtree(local + 'Image Repository')

    except:
        pass

    try:
        os.remove(cd + 'list.txt')
        os.remove(cd + 'list.txt')

    except:
        pass
    
    exit()
    
    
else:
    print(f'9999 : 398 {{MAIN.NAME}}')

print(__name__, '{Miss Bib-Img} COMPLETE!')
