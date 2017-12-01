import os
import sys
import time
from re import*

###############################################
# watchdog receives information from watchpup #
# 1: data is being written                    #
# 0: data acquisition is interrupted          #
# watchDog gives reassurance or sounds alarm  #
# > Allows quick recognition of fatal errors  #
###############################################

try:
    if len(sys.argv) > 1:
        title = sys.argv[1]
    else:
        title = ""
    lastSum = 0
    while(True):
        #fetch communication from watch pup
        os.system('scp -c arcfour analysis@192.168.2.5:/mnt/ram_disk/com.txt .')
        comFile = open('com.txt', 'r') #open file
        com = int(comFile.read()) #read bin
        comFile.close() #close file
    
        if com: #if uninterrupted
            os.system('date >> ' + title + '_uninterrupts.txt') #append uninterrupt to log
            os.system('echo . >> ' + title + '_uninterrupts.txt') #append . for future readability

            print("Uninterrupted data acquisition")

        else: #if interrupted
            os.system('date >> ' + title + '_interrupts.txt') #append interrupt to log
            os.system('echo . >> ' + title + '_interrupts.txt') #append . for future readability
        
            print("ALARM! Data taking interrupted.")
            print("Restart data acquisition!")
        
            os.system('cygstart siren.wav') #play alarm
        
        time.sleep(3) #pause for duration of alarm
except IOError:
    print ("Failed communication: run watch_pup.py on destination and check connection")
