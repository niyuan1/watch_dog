import os
import time

#############################
# WARNING                   #
# This will clear all logs! #
#############################

print("WARNING!")
print("This will clear logs!")
time.sleep(3)

os.system('rm _interrupts.txt')
os.system('rm _uninterrupts.txt')
os.system('rm com.txt')
print ("removed _interrupts.txt")
print ("removed _uninterrupts.txt")
print ("removed com.txt")
