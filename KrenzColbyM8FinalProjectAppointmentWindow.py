"""
Author: Colby Krenz
Date written: 04/28/23 - 05/12/23
Assignment: Module 8 Final Project - Appointment Window
Short Desc: GUI program that displays a form to schedule a manicure
"""

#import modules
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

#create root window and initialize properties
root = tk.Tk()
root.title("Nailed It! Salon")
root.resizable(0, 0)

#center the window on the screen when it is initiated and create padding within the window
window_width = 310
window_height = 420
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
padding = {"padx": 5, "pady": 5}

#creates the variables, labels and entry boxes for First and Last Name + Phone Number sections
first_name_var = tk.StringVar()
first_name = ttk.Label(root, text = "First Name: ")
first_name.grid(column = 0, row = 0, **padding, sticky = E)
first_name_entry = ttk.Entry(textvariable = first_name_var)
first_name_entry.grid(column = 1, row = 0, columnspan = 2, **padding, sticky = W)

last_name_var = tk.StringVar()
last_name = ttk.Label(root, text = "Last Name: ")
last_name.grid(column = 0, row = 1, **padding, sticky = E)
last_name_entry = ttk.Entry(root, textvariable = last_name_var)
last_name_entry.grid(column = 1, row = 1, columnspan = 2, **padding, sticky = W)

phone_number_var = tk.StringVar()
phone_number = ttk.Label(root, text = "Phone Number: ")
phone_number.grid(column = 0, row = 2, **padding, sticky = E)
phone_number_entry = ttk.Entry(root, textvariable = phone_number_var)
phone_number_entry.grid(column = 1, row = 2, columnspan = 2, **padding, sticky = W)

#creates the variable, label and radio buttons for the Nail Technician section
nail_tech = ttk.Label(root, text = "Select A Nail Technician:")
nail_tech.grid(column = 0, row = 3, columnspan = 3, **padding)
nail_tech_var = StringVar()
nail_tech1 = ttk.Radiobutton(root, text = "Any", variable = nail_tech_var, value = "Any")
nail_tech1.grid(column = 0, row = 4, **padding, sticky = W)
nail_tech2 = ttk.Radiobutton(root, text = "Diane S", variable = nail_tech_var, value = "Diane S")
nail_tech2.grid(column = 1, row = 4, **padding, sticky = W)
nail_tech3 = ttk.Radiobutton(root, text = "Elizabeth D", variable = nail_tech_var, value = "Elizabeth D")
nail_tech3.grid(column = 2, row = 4, **padding, sticky = W)
nail_tech4 = ttk.Radiobutton(root, text = "Kevin L", variable = nail_tech_var, value = "Kevin L")
nail_tech4.grid(column = 0, row = 5, **padding, sticky = W)
nail_tech5 = ttk.Radiobutton(root, text = "Maria D", variable = nail_tech_var, value = "Maria D")
nail_tech5.grid(column = 1, row = 5, **padding, sticky = W)
nail_tech6 = ttk.Radiobutton(root, text = "Rebecca R", variable = nail_tech_var, value = "Rebecca R")
nail_tech6.grid(column = 2, row = 5, **padding, sticky = W)
 
#creates the variable, label and drop down menu for the Appointment Time section
appt_time_var = tk.StringVar()
appt_times = ("9:00am", "10:30am", "11:45am", "1:30pm", "3:00pm")
appt_time = ttk.Label(root, text = "Appointment Time:")
appt_time.grid(column = 0, row = 6, columnspan = 2, **padding)
appt_time_option_menu = ttk.OptionMenu(root, appt_time_var, appt_times[0], *appt_times)
appt_time_option_menu.grid(column = 2, row = 6, **padding, sticky = W)
 
#creates the variable, label and radio buttons for the Application Method section
appl_method_var = StringVar()
appl_method = ttk.Label(root, text = "Select An Application Method:")
appl_method.grid(column = 0, row = 8, columnspan = 3, **padding)
appl_method1 = ttk.Radiobutton(root, text = "Gel Polish", variable = appl_method_var, value = "Gel Polish")
appl_method1.grid(column = 0, row = 9, **padding, sticky = W)
appl_method2 = ttk.Radiobutton(root, text = "Dip Powder", variable = appl_method_var, value = "Dip Powder")
appl_method2.grid(column = 1, row = 9, **padding, sticky = W)
appl_method3 = ttk.Radiobutton(root, text = "Acrylic", variable = appl_method_var, value = "Acrylic")
appl_method3.grid(column = 2, row = 9, **padding, sticky = W)

#creates the variables, label and check boxes for the Embellishments section
embellishment_var1 = tk.StringVar()
embellishment_var2 = tk.StringVar()
embellishment_var3 = tk.StringVar()
embellishment_var4 = tk.StringVar()
embellishment_var5 = tk.StringVar()
embellishment_var6 = tk.StringVar()
embellishment = ttk.Label(root, text = "Select Your Embellishments:")
embellishment.grid(column = 0, row = 10, columnspan = 3, **padding)
embellishment1 = ttk.Checkbutton(root, text = "Glitter", variable = embellishment_var1, onvalue = "yes", offvalue = "no")
embellishment1.grid(column = 0, row = 11, **padding, sticky = W)
embellishment2 = ttk.Checkbutton(root, text = "Glow", variable = embellishment_var2, onvalue = "yes", offvalue = "no")
embellishment2.grid(column = 1, row = 11, **padding, sticky = W)
embellishment3 = ttk.Checkbutton(root, text = "Mood Change", variable = embellishment_var3, onvalue = "yes", offvalue = "no")
embellishment3.grid(column = 2, row = 11, **padding, sticky = W)
embellishment4 = ttk.Checkbutton(root, text = "Ombre Effect", variable = embellishment_var4, onvalue = "yes", offvalue = "no")
embellishment4.grid(column = 0, row = 12, **padding, sticky = W)
embellishment5 = ttk.Checkbutton(root, text = "Rhinestones", variable = embellishment_var5, onvalue = "yes", offvalue = "no")
embellishment5.grid(column = 1, row = 12, **padding, sticky = W)
embellishment6 = ttk.Checkbutton(root, text = "UV Change", variable = embellishment_var6, onvalue = "yes", offvalue = "no")
embellishment6.grid(column = 2, row = 12, **padding, sticky = W)
   
#creates functions for the buttons to call
def appt_msg():
    """displays a greeting/appointment information to the user based on their input and checking for invalid input"""
    first_name = first_name_var.get()
    last_name = last_name_var.get()
    if first_name.isnumeric() or last_name.isnumeric():
        showerror(title = "Error", message = "There shouldn't be any numbers in the name.")
    else:
        phone_number = phone_number_var.get()
        if phone_number.isnumeric() == False:
            showerror(title = "Error", message = "There shouldn't be any letters in the phone number.")
        else:
            nail_technician = str(nail_tech_var.get())
            appointment_time = str(appt_time_var.get())
            application_method = str(appl_method_var.get())
            full_name = (first_name + " " + last_name)
            if first_name == "" or last_name == "" or phone_number == "" or nail_technician == "" or appointment_time == "" or application_method == "":
                showerror(title = "Error", message = "Please ensure that you have filled out the form completely and you have left no blanks or unselected options.")
            else:
                showinfo(title = "Appointment Information", message = f"Hello {full_name}. \nYour appointment is scheduled for {appointment_time}.\
                \nYou will be getting a {application_method} manicure with {nail_technician}. \nWe hope to see you soon!")

#resets all the variables to empty
def clear_form():
    """clears the appointment form"""
    first_name_var.set("")
    last_name_var.set("")
    phone_number_var.set("")
    nail_tech_var.set("")
    appt_time_var.set("")
    appl_method_var.set("")
    embellishment_var1.set("")
    embellishment_var2.set("")
    embellishment_var3.set("")
    embellishment_var4.set("")
    embellishment_var5.set("")
    embellishment_var6.set("")

#closes the current screen
def return_main():
    """returns user to the main screen"""
    root.destroy()
  
#creates submit, clear and retun button for the appointment window and invokes a callback function when the button is clicked
submit_btn = ttk.Button(root, text = "Submit", command = appt_msg)
submit_btn.grid(column = 0, row = 13, **padding, sticky = W)
clear_btn = ttk.Button(root, text = "Clear Form", command = clear_form)
clear_btn.grid(column = 1, row = 13, **padding, sticky = W)
return_btn = ttk.Button(root, text = "Return", command = return_main)
return_btn.grid(column = 2, row = 13, **padding, sticky = W)
  
#make the program run
mainloop()

