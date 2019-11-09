#Import Something#
import os
import sys
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox 
import shutil
from datetime import datetime
from datetime import date
import tkinter as tk
today = date.today()
date = today.strftime("%Y_%m_%d")
print(date)
to = "L:\\Meow Backup\\backup\\" + date
filepath = ""
data_buffer = "MOUNTVOL L: "
data_str_wrapper = open(r"volname.txt","r")
tmp = ""
try:
    str += data_str_wrapper
except Exception as e:
    print("Proccess Running")
data_buffer += data_str_wrapper.read()
os.popen(data_buffer)

def browse_button():
    os.popen(data_buffer)
    filename = filedialog.askdirectory()
    print(filename)
    filepath = filename
    foldername = os.path.basename(filepath)
    global to
    to = to + "\\" + foldername
    copyDirectory(filepath, to)
    os.popen("mountvol L:\ /D")
    return filename

def browse_button2():
    filename2 = filedialog.askdirectory()
    messagebox.showinfo("File Name", filename)
    filepath2 = filename
    
    return filename
 
def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('%s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('%s' % e)


#GUI Window
root = Tk()
root.title("Meow Backup 0.2.1")
label = tk.Label(root, fg="dark green")
label.pack()
button = tk.Button(root, text='選擇路徑', width=25, command=browse_button)
button.pack()
#button2 = tk.Button(root, text='選擇路徑', width=25, command=browse_button)
#button2.pack()
root.mainloop()
