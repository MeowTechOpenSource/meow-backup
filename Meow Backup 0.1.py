import os
import sys
from tkinter import filedialog
from tkinter import *
import shutil
from datetime import datetime
from datetime import date

#Part B define

filepath = ""
data_buffer = "MOUNTVOL L: "
data_str_wrapper = open(r"demofile.txt","r")
try:
    str += data_str_wrapper
except Exception as e:
    print("Proccess Running")
data_buffer += data_str_wrapper.read()
os.popen(data_buffer)
def browse_button():
    filename = filedialog.askdirectory()
    print(filename)
    filepath = filename
    return filename

def browse_button2():
    filename = filedialog.askdirectory()
    print(filename)
    filepath = filename
    copyDirectory(filepath, to)
    return filename
 
def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)




to = "L:\Meow Backup\backup_"


root = Tk()
v = StringVar()
button2 = Button(text="Browse", command=browse_button).grid(row=0, column=3)
