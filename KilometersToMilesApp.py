# ***************************************************************************
#
# Author: Adolfo Garcia
# Lab:    CIS-133Y Lab8
# Date:   November 11, 2026
# Desc:   Calculator app to convert distances from kilometers to miles.
#         Can be run standalone or within a tabbed notebook.
#
# Input:  Distance in kilometers entered by the user.
# Output: Distance in miles displayed in the UI.
# Source: Module 8 Lab 8
#
# ***************************************************************************

import os
import pygubu
import tkinter as tk
import tkinter.messagebox as mb

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "kilometers_to_miles.ui")


class KilometersToMilesApp:
    KILOMETERS_PER_MILE = 1.60934

    def __init__(self, master):
        # Build the tkinter interface based on kilometers_to_miles.ui
        self.__builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('top_frame', master)
        builder.connect_callbacks(self)

        # Save these UI elements as properties
        self.__kilometers_entry = builder.get_object('kilometers_entry', master)
        self.__miles_entry_variable = builder.get_variable('miles_entry_variable')

    def calculate(self):
        # Convert kilometers to miles and display the result.
        try:
            kilometers = float(self.__kilometers_entry.get())
            miles = kilometers / self.KILOMETERS_PER_MILE
            self.__miles_entry_variable.set("{:.2f} mi".format(miles))
        except ValueError:
            mb.showerror(
                title="Error Calculating Miles!",
                message="Kilometers must be a valid number. Please try again."
            )

    def get_top_frame(self):
        # Return the top frame
        return self.__mainwindow

    def run(self):
        self.__mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = KilometersToMilesApp(root)
    app.run()
