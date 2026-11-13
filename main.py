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

class MainApp:
    def __init__(self, master):
        # This is needed to allow the notebook tabs to stretch.
        tk.Grid.columnconfigure(master, 0, weight=1)
        tk.Grid.rowconfigure(master, 0, weight=1)

        # Build ui
        self.__main_notebook = ttk.Notebook(master)
        self.__main_notebook.grid(column='0', row='0', sticky='nsew')
        self.__main_notebook.rowconfigure('0', weight='1')
        self.__main_notebook.columnconfigure('0', weight='1')

        # Main widget
        self.__mainwindow = self.__main_notebook

        # Add About... tab
        about_app = AboutApp(self.__mainwindow)
        self.__main_notebook.add(about_app.get_top_frame(), text="About...")

        # Add miles to kilometer calculator tab
        miles_to_km_app = MilesToKilometersApp(self.__mainwindow)
        self.__main_notebook.add(miles_to_km_app.get_top_frame(), text="Miles to Kilometers")


        # Kilometers to miles calculator tab
        km_to_miles_app = KilometersToMilesApp(self.__mainwindow)
        self.__main_notebook.add(km_to_miles_app.get_top_frame(), text="Kilometers to Miles")


    def run(self):
        self.__mainwindow.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    app.run()