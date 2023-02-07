# import tkinter as tk
from tkinter import ttk


class UiSect1(ttk.Frame):
    def __init__(self, master=None, sw_name="Software Name", sw_ver="Ver: 0.0.0", spec_ver="0.0.0", **kwargs):
        ttk.Frame.__init__(self, master, **kwargs)

        # Create horizontal grid for the frame labels 1 raw, 4 columns
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Set sw_name Label font to 14pt bold, and padding to 3px
        self.sw_name = ttk.Label(self, text=sw_name, font=("Calibri", 14, "bold"), anchor="center")
        self.sw_name.grid(row=0, column=0, sticky="nsew")

        self.sw_ver = ttk.Label(self, text=sw_ver)
        self.sw_ver.grid(row=0, column=1, sticky="nsew")

        self.spec_ver = ttk.Label(self, text=spec_ver)
        self.spec_ver.grid(row=0, column=2, sticky="nsew")
