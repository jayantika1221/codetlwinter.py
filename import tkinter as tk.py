import tkinter as tk
from tkinter import messagebox

pleas = ["Please?", "Pretty please?", "Won't you reconsider?", "Can't you make an exception for me?", "I won't take no for an answer.", "It will make me really happy.","Pleaseeeee Naaaaaaa","Please please please please please", ]

def valentine():
    answer = messagebox.askyesno("Question", "Will you be my valentine and make my heart skip a beat?", icon="question")
    if answer == 1:
        messagebox.showinfo("Response", "Yay! I promise this will be your best valentine ever. Happy Valentine's Day, my love! Meet me at the spot we usually meet at 6", icon="info")
    else:
        i = 0
        while True:
            answer = messagebox.askyesno("Question", pleas[i], icon="question")
            if answer == 1:
                messagebox.showinfo("Response", "Yay! I promise this will be your best valentine ever. Happy Valentine's Day, my love! Meet me at the spot we usually meet at 6", icon="info")
                break
            else:
                i = (i+1) % len(pleas)

root = tk.Tk()
root.geometry("500x500")
root.configure(background="#FFE5E5")
btn = tk.Button(root, text="you have been hacked! Click this to undo it.", command=valentine)
btn.pack(pady=50)
root.mainloop()