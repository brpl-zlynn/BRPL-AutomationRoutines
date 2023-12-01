#!/usr/bin/env python

##################################################################################
##                                                                              ##
##	FTP                                                                     ##
##	Connecting to FTP and downloading MARC.                                 ##
##                                                                              ##
##	Created By Zachary Lynn.                                                ##
##      Updated on 03.31.2021 by Zachary Lynn for BRPL-ILS.                     ##
##	Copyright © 2021 Boca Raton Public Library. All rights reserved.        ##
##                                                                              ##
##      Mono-thread design.                                                     ##
##      The pyautogui & win32gui module are Required to Properly Run Script.    ##
##                                                                              ##
##      Forthcoming updates:                                                    ##
##      Window PID and definition.                                              ##
##      Process tree.                                                           ##
##                                                                              ##
##      —>Scheduler handler callable.                                           ##
##      —>Modular                                                               ##
##                                                                              ##
##################################################################################

# Modules #
import glob

from index import *
from tool__ import *
from ftplib import FTP
from datetime import datetime

global MARC
    
memory = False
a = pyautogui
# Definitions #

# FTP (baker-taylor MARC index) #
CON = 'BOCARATON'
AVCON = 'BOCARATONAV'

# File Location #
MARC = 'R:\ILS ADMINISTRATOR\Sierra_logs\Automation Services\MARC'
FORM = 'R:\ADMIN'

# FTP #
                    
# Initialization #
files = []
lines = []

class File_Transfer_Protocol:
        
    print("\n", '* Loading FTP Server *')

# batch MARC download #   
    def Ftp(self):

        global start
        global datestamp
        global memory
        global cache
        
        n = int(0)
        
        ftp = FTP('ftp1.baker-taylor.com')
        ftp.login('btcust','btcust')
        ftp.cwd("CLS_OPS/")

        #MAIN.Loading()

        # CON & ADD pull
        ftp.cwd(CON)

        # Get a list of files in /dir/
        files = ftp.nlst() # files = rename.item
        
        ##  Legacy pull design
        ##  All files STORE into list
        ##  Search through list and download
        ##  on match.

        ##    i = 0                       
        ##    while i < len(item):        
        ##        files.append(item[i])   
        ##        i += 1                  

        TOOLS.datestamp = "04-06-21" # test retrieve

        #############################
        #                           #
        #    Date =/= Batch pull    # # CON, COM & ADD
        #                           #
        #############################
        
        # compare date batch /dir/ FILES and pull match files
        # create /dir/ list

        i = 0
        ftp.retrlines('LIST', lines.append)
                                       
        while i < len(files):
            check = lines[i].startswith(TOOLS.datestamp)
            print(lines[i])
            
            if check == True: 
                
                n += 1
                path = os.path.join(cache, files[i])
                with open(path, "wb") as file:
                    ftp.retrbinary(f"RETR {files[i]}", file.write) # Download of the files
                    
            end = datetime.now()
            diff = end - TOOLS.start

            ##  CON = lines[i].split()[0] # Stores last file uploaded # Legacy last retrieval
            print(f'Searching files for ', {str(diff.seconds)}, 's')
            i += 1
            
        # UP dir
        ftp.cwd("..")

        # AV pull
        ftp.cwd(AVCON)
        
        # Overwrite list of files in /dir/
        files = ftp.nlst() # files = rename.item
        lines.clear()

        ##  Legacy pull design
        ##  All files STORE into list
        ##  Search through list and download
        ##  on match.

        ##    i = 0                       
        ##    while i < len(item):        
        ##        files.append(item[i])   
        ##        i += 1                  

        #############################
        #                           #
        #    Date =/= Batch pull    # # AVCON & AVADD
        #                           #
        #############################
        
        # compare date batch /dir/ FILES and pull match files
        # create /dir/ list
        
        i = 0
        ftp.retrlines('LIST', lines.append)
                    
        while i < len(files):
            check = lines[i].startswith(TOOLS.datestamp)
            print(lines[i])
            
            if check == True:
                
                n += 1
                path = os.path.join(cache, files[i])
                with open(path, "wb") as file:
                    ftp.retrbinary(f"RETR {files[i]}", file.write) # Download of the files

            end = datetime.now()
            diff = end - start

            ##  AVCON = lists[i].split()[0] # Stores last file uploaded # Legacy last retrieval
            print('Searching files for ' + str(diff.seconds) + 's')
            i += 1

        i -= 1

        # match
        if n >= 1:
            memory = True
            print("""
  ____________________________________________________________________________
 /                                                                            \\
|                 There were""", n, """file(s) found and downloaded                    |
|                           Loading file(s) to memory.                         |
 \____________________________________________________________________________/
                      
            """)
            return memory
                           
        # no match
        if path == None:
            files = 0

            print("""
  ____________________________________________________________________________
 /                                                                            \\
|   There are no new records to load, or retrieval is not properly formatted   |
|                              No Records loaded!                              |
"""
#|                                                                              |
#|                 Last Records were loaded on:""", TOOLS.datestamp, """                       |
""" \____________________________________________________________________________/
                      
            """)
            
# Read type and sort #
    def Marc(self):
                
        global blocks
        global cache
        
        os.chdir(cache)
        blocks = glob.glob('*.mrc')

##        while i < len(blocks)
##            block = blocks[i][:3]

            #CON
            #COM
            #ADD
            #AVA
            #AVC

# Move MARC to R:\MARC folders #                  
    def Move(self):
                
        import shutil
        import time
        i = int(0)

        global cache
        
        global CON
        global COM
        global ADD
        global AVA
        global AVC
        
        while i < len(blocks):
                if 'CON' == blocks[i][:3]:
                    print('Moving file', i+1, blocks[i])
                    source = cache + '/' + blocks[i]
                    shutil.move(source, MARC)

                    CON = os.listdir(MARC)
                    
                    time.sleep(2)
                    source = MARC + '/' + blocks[i]
                    shutil.move(source, MARC + '/cls.CON')
                    
                if 'COM' == blocks[i][:3]:
                    print('Moving file', i+1, blocks[i])
                    source = cache + '/' + blocks[i]
                    shutil.move(source, MARC)
                    
                    COM = os.listdir(MARC)
                    
                    time.sleep(2)
                    source = MARC + '/' + blocks[i]
                    shutil.move(source, MARC + '/cls.COM')
                    
                if 'ADD' == blocks[i][:3]:
                    print('Moving file', i+1, blocks[i])
                    source = cache + '/' + blocks[i]
                    shutil.move(source, MARC)
                    
                    ADD = os.listdir(MARC)
                    
                    time.sleep(2)
                    source = MARC + '/' + blocks[i]
                    shutil.move(source, MARC + '/cls.ADD')
                    
                if 'AVA' == blocks[i][:3]:
                    print('Moving file', i+1, blocks[i])
                    source = cache + '/' + blocks[i]
                    shutil.move(source, MARC)
                    
                    AVA = os.listdir(MARC)
                    
                    time.sleep(2)
                    source = MARC + '/' + blocks[i]
                    shutil.move(source, MARC + '/cls.AVA')
                    
                if 'AVC' == blocks[i][:3]:
                    print('Moving file', i+1, blocks[i])
                    source = cache + '/' + blocks[i]
                    shutil.move(source, MARC)
                    
                    AVC = os.listdir(MARC)
                    
                    time.sleep(2)
                    source = MARC + '/' + blocks[i]
                    shutil.move(source, MARC + '/cls.AVC')
                    print(AVC)
                    
                i += 1
                
    #def log(self): # can edit later to look at log file
                
print('MARC Batch Download COMPLETE!')
    
FTP = File_Transfer_Protocol()
    
##############################################################################################################################

##############################################################################################################################

