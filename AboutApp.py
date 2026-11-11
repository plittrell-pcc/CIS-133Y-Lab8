# ***************************************************************************
#
# Author: Paul Littrell & Adolfo Garcia
# Lab:    CIS-133Y Lab8
# Date:   November 11, 2026
# Desc:   Displays an About tab within a tabbed notebook interface or as a
#         stand-alone app, providing creator credits.
#
# Input:  None
# Output: Renders the about.ui layout in the GUI.
# Source: Module 8 Lab 8
# GitHub: https://github.com/plittrell-pcc/CIS-133Y-Lab8
#
# ***************************************************************************

import os
import pygubu

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "about.ui")


class AboutApp:

    def __init__(self, master):
        # Boilerplate from pygubu-designer.
        self.__builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('top_frame', master)
        builder.connect_callbacks(self)

    def get_top_frame(self):
        # Return the top frame
        return self.__mainwindow

    def run(self):
        self.__mainwindow.mainloop()


if __name__ == '__main__':
    import tkinter as tk

    root = tk.Tk()
    app = AboutApp(root)
    app.run()