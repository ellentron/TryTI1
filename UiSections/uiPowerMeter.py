# from tkinter import ttk, font
import customtkinter as ctk

from UiSections.uiConnection import UiConnection
from UiSections.uiRunControl import UiRunControl

""" ==================================================================================================== """

class UiPowerMeter(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)

        self.com_list = ["COM3", "COM8", "COM12"]

        # Create bold font
        bold_font = ctk.CTkFont(size=12, weight="bold")
        group_label_font = ctk.CTkFont(size=14, weight="bold")

        # Create grid layout for this frame - 2 rows, 2 columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=123)

        # Create Power Measurement heading label
        self.pm_heading = ctk.CTkLabel(self, text="Power Measurement", font=group_label_font)
        self.pm_heading.grid(row=0, column=0, sticky="nw", padx=(10, 0), pady=(0, 0))

        # Create connection list
        self.connection_list = ["COM1", "COM3", "COM23"]
        # Create UiConnection frame
        self.ui_pm_connect_frame = UiConnection(self, connection_title="Power Meter Connection",
                                                connect_to_label="COM Port:", connection_list=self.connection_list)
        self.ui_pm_connect_frame.grid(row=1, column=0, sticky="nsew", padx=(10, 10), pady=(10, 10))

        # Create UiRunControl instance and place it in the master frame
        self.ui_run_control_frame = UiRunControl(self)
        self.ui_run_control_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 10), pady=(10, 10))

