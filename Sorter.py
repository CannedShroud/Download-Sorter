# import os,shutil,os.path,time
import os as os
from os import *
import shutil as sh
from shutil import *
import time as time 
from time import sleep
import colorama
from colorama import Fore


print( Fore.BLUE, 'Initialising Programme...')
sleep(0.7)


# Create needed variables
acc_list_path = '/Users'
accounts = os.listdir(acc_list_path)
for account in accounts:
    print(account)
UserID = str(input('Enter userID related to Windows account -->  '))
wr_dir = '/Users/' + UserID + '/Downloads'
au_dir = '/Users/' + UserID + '/Music'
pic_dir = '/Users/' + UserID + '/Pictures'
vid_dir = '/Users/' + UserID + '/Videos'
txt_dir = '/Users/' + UserID + '/Documents'
zip_dir = '/Users/' + UserID + '/Downloads/zip'
rar_dir = '/Users/' + UserID + '/Downloads/rar'
exe_dir = '/Users/' + UserID + '/Downloads/Software'
iso_dir = '/Users/' + UserID + '/Downloads/iso'
tor_dir = '/Users/' + UserID + '/Downloads/torrents'
full_dir = os.path.join

    
print('Creating required directories...')
sleep(1.6)


if os.path.isdir(zip_dir):
    pass    
else:
    os.mkdir(zip_dir)
if os.path.isdir(tor_dir):
    pass
else:
    os.mkdir(tor_dir)
if os.path.isdir(rar_dir):
    pass
else:
    os.mkdir(rar_dir)
if os.path.isdir(exe_dir):
    pass
else:
    os.mkdir(exe_dir)
if os.path.isdir(iso_dir):
    pass
else:
    os.mkdir(iso_dir)
    

# Create Read function
print('Main function started.')
sleep(.5)
def sorter():
    try:
        # Read Filenames
        print('Reading Files from Downloads directory.')
        sleep(3)
        print('Magic begins...')
        sleep(0.6)
        print('.')
        sleep(0.6)
        print('.')
        sleep(0.6)
        print('.')
        sleep(0.6)
        print('.')
        sleep(0.6)
        print('.')
        sleep(0.6)
        print('.')
        sleep(0.6)
        print('.')
        sleep(0.6)
        print('.')
        sleep(0.6)
        for dirname, dirnames, filenames in os.walk(wr_dir):
            for filename in filenames:
                source = full_dir(dirname, filename)
                # Create Sort and move function
                # Move file to respective directories
                # MP3 to audio
                if filename.endswith('mp3'):
                    sh.move(source, full_dir(au_dir, filename))
                # jpeg to pics
                elif filename.endswith('jpeg'):
                    sh.move(source, full_dir(pic_dir, filename))
                # MP4 to Video
                elif filename.endswith('mp4'):
                    sh.move(source, full_dir(vid_dir, filename))
                # txt documents
                elif filename.endswith('txt'):
                    sh.move(source, full_dir(txt_dir, filename))
                # Sorting Software
                elif filename.endswith('zip'):   
                    sh.move(source, full_dir(zip_dir, filename))           
                elif filename.endswith('rar'):
                    sh.move(source, full_dir(rar_dir, filename))
                elif filename.endswith('exe'):
                    sh.move(source, full_dir(exe_dir, filename))
                elif filename.endswith('iso'):
                    sh.move(source, full_dir(iso_dir, filename))
                elif filename.endswith('torrent'):
                    sh.move(source, full_dir(tor_dir, filename))    
                else:
                    pass
        sleep(2)
    except PermissionError as p:
        pass
# Call function
if __name__ == '__main__':
    sorter()
print(end='')
sleep(2)
print('Done...')
exit = input('Entre any key to exit.')