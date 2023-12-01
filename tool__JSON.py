#!/usr/bin/env python
##################################################################################
##                                                                              ##
##	JSON TOOLS                                                              ##
##	Functions when scripting with JSON and CSV.                             ##
##                                                                              ##
##	Created By Zachary Lynn.                                                ##
##      Updated on 04.28.2022 by Zachary Lynn for BRPL-ILS.                     ##
##	Copyright © 2022 Boca Raton Public Library. All rights reserved.        ##
##                                                                              ##
##################################################################################

# Modules
import glob
from datetime import datetime, timedelta

from tool__ import *
from __main__ import *
##from tool__Sierra import FTS

#### testing WORKSPACE ####
# from WORKSPACE import * #
###########################
    
# Definitions
class json:
     
# JSON Editable function #       
    def Launch(self):
        global window
        FTS = 'test.p' #will already be available due to import from above
        
        log_service = 'LOGS'
        
        window = MAIN.NAME
        network = PATH.Network(log_service, MAIN.MENU)
        network = network + '.csv'
        window = network + ' - Notepad'

        TOOL.processing.Runtime_04()
        subprocess.Popen([r'C:\Windows\notepad.exe', network])
        TOOL.Window()
        
        a.hotkey('alt', 'o')
        a.press('o')
        a.press('f4')
        a.hotkey('ctrl', 'a')

        a.write(network)

        a.press('return')
        a.hotkey('alt', 'n')
        a.write(MAIN.MENU)
        a.press('return')

        a.write(FTS)
        a.press('F2')
        a.press('up')
        
        for process in range (0, 2):
            a.press('del')
        a.press('tab')
        
        TOOL.Window()
        app = [window, 'I']
        
        return window


# Date Conversion #
    def Conversion(void, year, MDY, MENU):
        if MDY == 'month':
            conversion = 1000000
        if MDY == 'day':
            conversion = 10000
        if MDY == 'year':
            conversion = 1

##  Get  ## From Internal Clock
        year = str(year)
        Finn = PATH.Network(None, None)
        path = Finn[1] + r'Sierra_logs\Automation Services\runtime.logs' + '\\' + 'JSON-' + SUB.NAME + ' ' + year + ' year'
        year = int(year)
        print(path)
        
        date = list()
        date = [DATESTAMP(), DATESTAMP()]

        for process in range (0, 2):
            datestamp = datetime.now() - timedelta(days=1)
            datestamp = datestamp.strftime('%m-%d-%Y')
            date[process] = datestamp.replace('-', '')
            date[process] = int(date[process])
                
            if process == 0:
                date[0] += year * conversion

            if date[process] < 10000000:
                date[process] = str(date[process])
                date[process] = '0' + date[process]
                
            date[process] = str(date[process])
            date[process] = date[process][:2] + '-' + date[process][2:]
            date[process] = date[process][:5] + '-' + date[process][5:]

            
##  Convert  ##
        for process in range(0, 2):
            date[process] = '          ' + '"' + date[process]
            date[process] = date[process] + '",' + '\n'

      
##  Write  ##
        data = []
        n = 0
        with open(path) as file:
            for line in file:
                data.append(line)
                if n == 12:
                    data[12] = date[0]
                if n == 28:
                    data[28] = date[1]
                if n == 44:
                    data[44] = date[1]
                n += 1
                
        with open(path, 'w') as file:
                file.writelines(data)    

        
JSON = json()
