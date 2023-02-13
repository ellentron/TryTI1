import tkinter as tk
# from tkinter import ttk, font
import customtkinter as ctk
# from UiSections.uiLed import LED


class UiPowerMeter(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)

        self.com_list = ["COM3", "COM8", "COM12"]

        # Create bold font
        bold_font = ctk.CTkFont(size=12, weight="bold")
        group_label_font = ctk.CTkFont(size=14, weight="bold")

        # Create grid layout for the frame - 2 rows, 1 column
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Create Power Measurement heading label
        self.pm_heading = ctk.CTkLabel(self, text="Power Measurement", font=group_label_font)
        self.pm_heading.grid(row=0, column=0, sticky="nw", padx=(10, 0), pady=(10, 10))

        # # Create Power Measurement container group
        # self.pm_group = ctk.CTkFrame(self)
        # self.pm_group.grid(row=1, column=0, sticky="nsew", padx=(10, 10), pady=(10, 10))

        # # In the Power Measurement group, create a grid layout - 2 rows, 2 columns
        # self.pm_group.grid_columnconfigure(0, weight=1)
        # self.pm_group.grid_columnconfigure(1, weight=1)
        # self.pm_group.grid_rowconfigure(0, weight=1)
        # self.pm_group.grid_rowconfigure(1, weight=1)
        #
        # # self.kukulabel = ctk.CTkLabel(self.pm_group, text="KUKU !!!!!", font=group_label_font)
        # # self.kukulabel.grid(row=1, column=0, sticky="nw", padx=(10, 0), pady=(10, 10))
        #
        # # self.pm_connection = self.UiPowerMeterConnection(self.pm_group)
        # # self.pm_connection.grid(row=1, column=0, sticky="nw", padx=(10, 0), pady=(10, 10))
        #

    # Create class for Power Meter Connection
    class UiPowerMeterConnection(ctk.CTkFrame):
        def __init__(self, master=None, **kwargs):
            ctk.CTkFrame.__init__(self, master, **kwargs)

            # Create bold font
            bold_font = ctk.CTkFont(size=12, weight="bold")
            group_label_font = ctk.CTkFont(size=14, weight="bold")

            # Create grid layout for the frame - 2 rows, 1 column
            self.grid_columnconfigure(0, weight=1)
            self.grid_rowconfigure(0, weight=1)
            self.grid_rowconfigure(1, weight=1)

            # Create Power Measurement heading label
            self.pm_heading = ctk.CTkLabel(self, text="Power Meter Connection", font=group_label_font)
            self.pm_heading.grid(row=0, column=0, sticky="nw", padx=(10, 0), pady=(10, 10))

            # Create Power Measurement container group
            self.pm_group = ctk.CTkFrame(self)
            self.pm_group.grid(row=1, column=0, sticky="nsew", padx=(10, 10), pady=(10, 10))

            # In the Power Measurement group, create a grid layout - 2 rows, 2 columns
            self.pm_group.grid_columnconfigure(0, weight=1)
            self.pm_group.grid_columnconfigure(1, weight=1)
            self.pm_group.grid_rowconfigure(0, weight=1)
            self.pm_group.grid_rowconfigure(1, weight=1)

            # self.kukulabel = ctk.CTkLabel(self.pm_group, text="KUKU !!!!!", font=group_label_font)
            # self.kukulabel.grid(row=1, column=0, sticky="nw", padx=(10, 0), pady=(10, 10))
