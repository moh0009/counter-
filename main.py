import tkinter as tk
import time 
import os

def printt(string, delay = 0.07):
  for i in str(string):
    print(i, end="", flush = True)
    time.sleep(delay)
  print("")
printt("What do you want the window name to be?")
input1 = input()
os.system("clear")

root = tk.Tk()
root.title(input1)
root.geometry("300x400")
#root.iconbitmap("png.ico")
#defs

  
def clicker():
	lbl["text"] += 1

def Reset():
  lbl1 = str(lbl["text"])
  lb.config(text = f"you had been clicked {str(lbl1)} times")
  lbl["text"] = 0
def quit():
  printt("the app closed well")
  time.sleep(3)
  root.destroy()
  os.system("clear")

#button and label

button = tk.Button(text="Reset ", command=Reset, fg="blue")
button1 = tk.Button(text="count!", command=clicker, fg="green",bd = "4")
lbl = tk.Label(text=0, font=("", 60))
lb = tk.Label(text = "")
button_quit = tk.Button(text="exit program", command=quit, fg="red")

button1.pack(pady=30)
lbl.pack()
button.pack(pady = 10)
button_quit.pack(pady = 10)
lb.pack()
root.mainloop()
