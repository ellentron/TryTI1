# import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


class UiSect1(ctk.CTkFrame):
    def __init__(self, master=None, sw_name="Software Name", sw_ver="Ver: 0.0.0", spec_ver="0.0.0", **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)

        # Create horizontal grid for the frame labels 1 raw, 4 columns
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Set sw_name Label font to 14pt bold, and padding to 3px
        self.sw_name = ctk.CTkLabel(self, text=sw_name, font=("Calibri", 14, "bold"), anchor="center")
        self.sw_name.grid(row=0, column=0, sticky="nsew")

        self.sw_ver = ctk.CTkLabel(self, text=sw_ver)
        self.sw_ver.grid(row=0, column=1, sticky="nsew")

        self.spec_ver = ctk.CTkLabel(self, text=spec_ver)
        self.spec_ver.grid(row=0, column=2, sticky="nsew")
