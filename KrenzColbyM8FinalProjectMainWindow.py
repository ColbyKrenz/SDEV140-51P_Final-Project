"""
Author: Colby Krenz
Date written: 04/28/23 - 05/12/23
Assignment: Module 8 Final Project - Main Window
Short Desc: GUI program that displays the opening screen for a nail salon
"""

#import modules
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter.messagebox import showinfo

#create window and initialize properties
root = tk.Tk()
root.title("Nailed It! Salon")
root.resizable(0, 0)

#center the window on the screen when it is initiated
window_width = 500
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#create label and changes the font and size
main_page_message1 = tk.Label(root, text = "Thank you for choosing the Nailed It! Salon!", bg = "black", fg = "white")
main_page_message1.pack(ipadx = 10, ipady = 20, fill = tk.BOTH, anchor = CENTER)
font = Font(family = "Verdana", size = 14)
main_page_message1["font"] = font
#create label and change the font and size
main_page_message2 = tk.Label(root, text = "Select Schedule if you'd like to make an appointment.")
main_page_message2.pack(ipadx = 5, ipady = 5, anchor = CENTER)
font = Font(family = "Verdana", size = 12)
main_page_message2["font"] = font
#create label and change the font and size
main_page_message3 = tk.Label(root, text = "Or select the Mani Gallery if you need some inspiration.")
main_page_message3.pack(ipadx = 5, ipady = 5, anchor = CENTER)
font = Font(family = "Verdana", size = 12)
main_page_message3["font"] = font
 
#creates function for the schedule button to call and opens in a new window
def open_appointment():
    """opens the schedule appointment window"""
    sched_appt = Toplevel(root)
    sched_appt.geometry("550x420")
    sched_appt.title("Appointment")
    frame = Frame(sched_appt)
    frame.place(x=5, y=10, width=635, height=700)
    #closes the top window
    def exit_top():
        sched_appt.destroy()
    #creates an exit button    
    exit_btn = tk.Button(sched_appt, text = "Exit", command = exit_top)
    exit_btn.pack(ipadx = 10, ipady = 10, expand = True, side = tk.LEFT)    

#creates function for the gallery button to call and opens in a new window    
def open_gallery():
    """opens the mani gallery window"""
    gallery = Toplevel(root)
    gallery.geometry("550x420")
    gallery.title("Mani Gallery")
    frame = Frame(gallery)
    frame.place(x=5, y=10, width=635, height=700)
    #closes the top window
    def exit_top():
        gallery.destroy()
    #creates an exit button
    exit_btn = tk.Button(gallery, text = "Exit", command = exit_top)
    exit_btn.pack(ipadx = 10, ipady = 10, expand = True, side = tk.LEFT)
   
#command button to close the program
def exit_program():
    root.destroy()
  
#displays a schedule, gallery and exit button
schedule_btn = tk.Button(root, text = "Schedule", command = open_appointment)
schedule_btn.pack(ipadx = 10, ipady = 10, expand = True, side = tk.LEFT)
gallery_btn = tk.Button(root, text = "Mani Gallery", command = open_gallery)
gallery_btn.pack(ipadx = 10, ipady = 10, expand = True, side = tk.LEFT)
exit_btn = tk.Button(root, text = "Exit", command = exit_program)
exit_btn.pack(ipadx = 10, ipady = 10, expand = True, side = tk.LEFT)

#make the program run
mainloop()
