# import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


class UiSect1(ctk.CTkFrame):
    def __init__(self, master=None, sw_name="Software Name", sw_ver="Ver: 0.0.0", spec_ver="0.0.0", **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)

        # Create bold font
        bold_font = ctk.CTkFont(size=22, weight="bold")

        # Create horizontal grid for the frame labels 1 raw, 3 columns
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Set sw_name Label font to 14pt bold, and padding to 3px
        self.sw_name = ctk.CTkLabel(self, text=sw_name, font=bold_font)
        self.sw_name.grid(row=0, column=0, sticky="nsw", padx=(10, 500), pady=(0, 0))

        self.sw_ver = ctk.CTkLabel(self, text=sw_ver)
        self.sw_ver.grid(row=0, column=1, sticky="ns")

        self.spec_ver = ctk.CTkLabel(self, text=spec_ver)
        self.spec_ver.grid(row=0, column=2, sticky="ns")
