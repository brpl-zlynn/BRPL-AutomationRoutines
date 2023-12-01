#!/usr/bin/env python

##################################################################################
##                                                                              ##
##	HTML                                                                    ##
##	Connecting to HTTP and downloading forms.                               ##
##                                                                              ##
##	Created By Zachary Lynn.                                                ##
##      Updated on 01.12.2023 by Zachary Lynn for BRPL-ILS.                     ##
##	Copyright © 2022 Boca Raton Public Library. All rights reserved.        ##
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
from datetime import datetime

memory = False
a = pyautogui
# Definitions #

# Initialization #
files = []
lines = []
index = 'null'

# HTTP #
local = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
HTTP = 'https://www.myboca.us/Admin/FormCenter/Submissions/Index/' + index + '?categoryID=10'
FORM = '\\HYDE\Shared\ADMIN\ADMIN HR\request forms'
                    
class Civic_Plus:

    print(f'\n* Loading Civic Plus *\n')

# forms Request download #
    def Form(self):

        global start
        global datestamp
        global memory
        global cache

        n = int(0)
        pyautogui.alert('stop')
        a.alert()
        
    def Request(self):

        global index

        if RECIEVED == ''
            index = '66'  # Book a Librarian

        elif 
            index = '75'  # Concierge Reading List Request Form

        elif 
            index = '73'  # Feedback Form

        elif 
            index = '103' # Giving Tree Plaque Request Form

        elif 
            index = '67'  # Interlibrary Loan Request for a Book

        elif 
            index = '68'  # Interlibrary Loan Request for a Periodical or Magazine Article

        elif 
            index = '101' # Next Level Instruction Request

        elif 
            index = '63'  # Patron Request for Reconsideration of a Work

        elif 
            index = '72'  # Request a Title for Purchase

        elif 
            index = '65'  # Sign Up for Our Newsletter

        elif 
            index = '71'  # Special Event Request Form
       

CIVIC = Civic_Plus()

class HTML:

    # web browser automation stuff
    
HTTP = HTML()
    
##############################################################################################################################

##############################################################################################################################

