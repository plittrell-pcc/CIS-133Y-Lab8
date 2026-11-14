# ***************************************************************************
#
# Author: Paul Littrell & Adolfo Garcia
# Lab:    CIS-133Y Lab8
# Date:   November 11, 2026
# Desc:   Main driver program for the GUI project. Loads a tabbed notebook
#         interface containing the About tab and the Distance Calculator tab.
#
# Input:  User tab selection and button clicks.
# Output: UI window containing respective application modules.
# Source: Module 8 Lab 8
# GitHub: https://github.com/plittrell-pcc/CIS-133Y-Lab8
#
# ***************************************************************************

import tkinter as tk
import tkinter.ttk as ttk

from AboutApp import AboutApp
from MilesToKilometersApp import MilesToKilometersApp
from KilometersToMilesApp import KilometersToMilesApp

#Modified class to use tk.Toplevel instead of tk.Frame
class MainApp:
    def __init__(self, master=None):
        # Create a Toplevel widget as the root of the GUI
        self.__mainwindow = tk.Toplevel(master)
        self.__mainwindow.title("Distance Converter")
        self.__mainwindow.protocol("WM_DELETE_WINDOW", self.__mainwindow.quit)

        # Allow the notebook to stretch when the Toplevel window resizes
        self.__mainwindow.columnconfigure(0, weight=1)
        self.__mainwindow.rowconfigure(0, weight=1)

        # Build ui
        self.__main_notebook = ttk.Notebook(self.__mainwindow)
        self.__main_notebook.grid(column=0, row=0, sticky='nsew')
        self.__main_notebook.rowconfigure(0, weight=1)
        self.__main_notebook.columnconfigure(0, weight=1)

        # Add About... tab
        about_app = AboutApp(self.__main_notebook)
        self.__main_notebook.add(about_app.get_top_frame(), text="About...")

        # Add miles to kilometer calculator tab
        miles_to_km_app = MilesToKilometersApp(self.__main_notebook)
        self.__main_notebook.add(miles_to_km_app.get_top_frame(), text="Miles to Kilometers")

        # Kilometers to miles calculator tab
        km_to_miles_app = KilometersToMilesApp(self.__main_notebook)
        self.__main_notebook.add(km_to_miles_app.get_top_frame(), text="Kilometers to Miles")

    def run(self):
        self.__mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  # Hide the default Tk root so only the Toplevel window is shown
    app = MainApp(root)
    app.run()