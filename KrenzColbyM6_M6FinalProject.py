"""
Author: Colby Krenz
Date written: 04/28/23
Assignment: Module 6 Example 1
Short Desc: GUI program that converts Celsius to Fahrenheit and vice versa
"""

#import modules
from breezypythongui import EasyFrame
from tkinter import *
import tkinter as tk
from tkinter.font import Font

root = tk.Tk()

#center the window on the screen when it is initiated
window_width = 300
window_height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#define a new class
class NailShapes(EasyFrame):
    """displays an image and caption of a nail shape option"""
    def __init__(self):
        """sets up window and widgets"""
        EasyFrame.__init__(self, title = "Nailed It Salon Shapes")
        self.setResizable(False)
        imageLabel = self.addLabel(text = "", row = 0, column = 0, sticky = "NSEW")
        textLabel = self.addLabel(text = "Ballerina", row = 1, column = 0, sticky = "NSEW")
        
        #loads the image and the label
        self.image = PhotoImage(file = "ballerina.png")
        imageLabel["image"] = self.image
        
        #set font and size of the caption
        labelFont = tk.font.Font(family = "Segoe Script", size = 30, weight = "bold")
        textLabel.configure(font = labelFont)
                        
#make the program run
def main():
    """makes the window pop up"""
    NailShapes().mainloop()

if __name__ == "__main__":
        main()