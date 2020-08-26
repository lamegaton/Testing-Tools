# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 17:46:41 2020

@author: sonph
"""

import tkinter as tk
import os, subprocess

def printout(x):
    if x != "":
        os.chdir("D:/tools/platform-tools")
        start = subprocess.Popen("adb start-server",shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        start.wait()
        if "adb logcat" in x:
            subprocess.Popen(x,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if "stop" in x:
            subprocess.Popen("adb kill-server",shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            #print(os.popen('cmd /c '+ x).read()) #/k for keep
            #os.system('cmd /c '+ x)
            output = subprocess.run(x,capture_output=True, check=True)
            print(output)
        
window = tk.Tk()
# create instance
window.title("Run CMD")

# adding a lable
a_label = tk.Label(window, text="CMD commands")
a_label.grid(column=0, row=0)


i = 1
for index, rows in enumerate(["a","b","c","d","e","f","g","h","i","j"]):
    # adding a textbox
    name = tk.StringVar()
    name_entered = tk.Entry(window, width=48, textvariable=name)
    #name_entered.pack(side = LEFT)
    name_entered.grid(column=0, row=index+1, padx=7, pady=7)
    b = tk.Button(window,  
                       text=rows, width=10,
                       command=lambda name=name:printout(name.get()))
    b.grid(row=index+1, column=1,  padx=7)
    i = i + 1

window.mainloop()