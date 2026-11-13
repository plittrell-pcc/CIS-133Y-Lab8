# ***************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-133Y Lab8
# Date:   November 11, 2026
# Desc:   Calculator app to convert distances from miles to kilometers.
#         Can be run standalone or within a tabbed notebook.
#
# Input:  Distance in Miles (decimal) entered by the user.
# Output: Distance in Kilometers displayed in the UI.
# Source: Module 8 Lab 8
# GitHub: https://github.com/plittrell-pcc/CIS-133Y-Lab8
#
# ***************************************************************************

import os
import pygubu
import tkinter as tk
import tkinter.messagebox as mb

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "miles_to_kilometers.ui")


class MilesToKilometersApp:
    KILOMETERS_PER_MILE = 1.60934

    def __init__(self, master):
        # Build the tkinter interface based on miles_to_kilometers.ui
        self.__builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('top_frame', master)
        builder.connect_callbacks(self)

        # Save these UI elements as properties
        self.__miles_entry = builder.get_object('miles_entry', master)
        self.__miles_entry.bind('<Return>', lambda event: self.calculate())
        self.__kilometers_entry_variable = builder.get_variable('kilometers_entry_variable')

    def calculate(self):
        # Convert miles to kilometers. If there's an error, display an error message.
        try:
            miles = float(self.__miles_entry.get())
            kilometers = miles * self.KILOMETERS_PER_MILE
            self.__kilometers_entry_variable.set("{:.2f} km".format(kilometers))
        except ValueError:
            mb.showerror(title="Error Calculating Kilometers!",
                         message="Miles must be a valid number. Please try again.")

    def get_top_frame(self):
        # Return the top frame
        return self.__mainwindow

    def run(self):
        self.__mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = MilesToKilometersApp(root)
    app.run()