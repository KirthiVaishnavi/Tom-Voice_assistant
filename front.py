# -*- coding: utf-8 -*-
"""
Created on Sat May 15 09:33:38 2021


"""
from tkinter import *
root=Tk()
root.geometry("1000x1000")
root.configure(bg="#EEE8AA")
root.title("VOICE ASSISTANT")

label1=Label(root,text="VaMoHa",font=("Arial Bold",60),bg="purple",fg="white").pack(padx=10,pady=30)

canvas=Canvas(root,width=500,height=500)
img=PhotoImage(file="C:/Users/lavan/Downloads/va-icon.jpg")
canvas.create_image(250,250,anchor=CENTER,image=img)
canvas.pack(padx=10,pady=30)

b1=Button(root,text="Tap to Speak",bg="Black",fg="white",font='bold',width=30).pack()

root.mainloop()
    
