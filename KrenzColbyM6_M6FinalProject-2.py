"""
Author: Colby Krenz
Date written: 04/28/23
Assignment: Module 6 Final Project
Short Desc: GUI program that sets up an appointment for a manicure
"""

#import modules
from breezypythongui import EasyFrame
from tkinter import *
import tkinter as tk

root = tk.Tk()

#center the window on the screen when it is initiated
window_width = 300
window_height = 260
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#define a new class
class AppointmentBooking(EasyFrame):
    """allows clients to select their manicure options during their next appointment"""
    def __init__(self):
        """sets up window and widgets"""
        EasyFrame.__init__(self, title = "Nailed It Salon")
        self.setBackground("black")
        self.setResizable(False)

        #label and field for the user input
        self.addLabel(text = "First Name", row = 0, column = 0, sticky = "NSE", background = "black", foreground = "white")
        self.userFName = self.addTextField(text = "", row = 0, column = 1, sticky = "NSW")

        #label and field for the user input
        self.addLabel(text = "Last Name", row = 1, column = 0, sticky = "NSE", background = "black", foreground = "white")
        self.userLName = self.addTextField(text = "", row = 1, column = 1, sticky = "NSW")

        #label and field for the user input
        self.addLabel(text = "Phone Number", row = 2, column = 0, sticky = "NSE", background = "black", foreground = "white")
        self.userPhoneNum = self.addIntegerField(value = "", row = 2, column = 1, sticky = "NSW")
        
        #label and field for the user input
        self.addLabel(text = "Nail Technician", row = 3, column = 0, sticky = "NSE", background = "black", foreground = "white")
        self.userNailTech = self.addTextField(text = "", row = 3, column = 1, sticky = "NSW")
        
        #label and field for the user input
        self.addLabel(text = "Appointment Time", row = 4, column = 0, sticky = "NSE", background = "black", foreground = "white")
        self.userApptTime = self.addTextField(text = "", row = 4, column = 1, sticky = "NSW")
        
        #label and field for the user input
        self.addLabel(text = "Application Method", row = 5, column = 0, sticky = "NSE", background = "black", foreground = "white")
        self.userApplMethod = self.addTextField(text = "", row = 5, column = 1, sticky = "NSW")
        
        self.userGreeting = self.addTextField(text = "", row = 7, column = 0, columnspan = 2, state = "readonly", sticky = "NSEW", )
        
        #displays a submit button for the user to submit appointment info
        self.addButton(text = "Submit", row = 6, column = 0, columnspan = 2, command = self.welcomeMsg)
    
    #shows a greeting to the user based on their input
    def welcomeMsg(self):
        """displays a greeting"""
        fName = self.userFName.getText()
        fName = ("Hello " + fName + ", welcome to our salon!")
        self.userGreeting.setText(fName)
        
#make the program run
def main():
    """makes the window pop up"""
    AppointmentBooking().mainloop()

if __name__ == "__main__":
        main()