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

    def __init__(self, master=None):
        # Boilerplate from pygubu-designer.
        self.__builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)

        if master is None:
            # Standalone mode: use tk.Toplevel as the GUI root
            self.__mainwindow = builder.get_object('mainwindow')
            self.__mainwindow.protocol("WM_DELETE_WINDOW", self.__mainwindow.quit)
            self.__top_frame = builder.get_object('top_frame')
        else:
            # Notebook tab mode: extract only top_frame into master
            self.__mainwindow = builder.get_object('top_frame', master)
            self.__top_frame = self.__mainwindow

        builder.connect_callbacks(self)

    def get_top_frame(self):
        # Return the top frame
        return self.__top_frame

    def run(self):
        self.__mainwindow.mainloop()


if __name__ == '__main__':
    import tkinter as tk

    root = tk.Tk()
    root.withdraw()
    app = AboutApp()
    app.run()