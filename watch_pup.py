import os
import time
from re import*

###############################################
# watchpup checks if data is writing to file. #
# watchpup communicates this to watchdog.     #
# 1: data is being written                    #
# 0: data acquisition is interrupted          #
# > Allows quick recognition of fatal errors  #
###############################################
try:
    lastSum = 0
    while(True):   
        os.system('df > /mnt/ram_disk/test.txt') #get disk memory
        testFile = open('/mnt/ram_disk/test.txt', 'r') #read from file
        line = testFile.read() #get strings
        testFile.close() #close file
        lines = line.split('\n')[5:-2] #extract relevant hard disk lines
    
        nowSum = 0
        for line in lines:
            num = [int(s) for s in line.split() if s.isdigit()][1] #extract used memory
            nowSum += num #add to total used memory
    
        comFile = open('/mnt/ram_disk/com.txt', 'w') #open communications file
        if nowSum <= lastSum: #check if memory has stalled
            comFile.write('0') #communicate a 0
        else: #otherwise memory is writing
            comFile.write('1') #communicate a 1
        comFile.close() #close communications file
        lastSum = nowSum #make this the previous sum, make a new one to compare
        time.sleep(1) #sample at 1Hz
except KeyboardInterrupt:
    os.system('python watch_pup_reset.py')
