import os

#############################
# WARNING                   #
# This will clear all logs! #
#############################

print('reset')
os.system('rm /mnt/ram_disk/test.txt')
os.system('rm /mnt/ram_disk/com.txt')
print ("removed test.txt")
print ("removed com.txt")
