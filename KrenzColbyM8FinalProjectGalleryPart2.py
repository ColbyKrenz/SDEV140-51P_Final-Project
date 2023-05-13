"""
Author: Colby Krenz
Date written: 04/28/23 - 05/11/23
Assignment: Module 8 Final Project - Gallery Window
Short Desc: GUI program that displays a manicure gallery part 2
"""

#import modules
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
import tkinter as tk

#instantiate the window
root = tk.Tk()
root.geometry("330x510")

#define a new class
class ManiGallery(EasyFrame):
    """displays an image and caption of a manicure from the gallery"""
    def __init__(self):
        """sets up window and widgets"""
        EasyFrame.__init__(self, title = "Nailed It! Mani Gallery")
        #can't resize the window and displays the image/label
        self.setResizable(False)
        imageLabel = self.addLabel(text = "", row = 0, column = 0, sticky = "NSEW")
        textLabel = self.addLabel(text = "Mani with Glitter \nby Maria D.", row = 1, column = 0, sticky = "NSEW")
        
        #loads the image and the label
        self.image = PhotoImage(file = "linedMani.gif")
        imageLabel["image"] = self.image
        
        #set font and size of the caption
        font = Font(family = "Segoe Script", size = 13, weight = "bold")
        textLabel["font"] = font      
                        
#makes the program run
def main():
    """makes the window pop up"""
    ManiGallery().mainloop()

if __name__ == "__main__":
        main()