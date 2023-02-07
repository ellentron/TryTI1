# import tkinter as tk
from tkinter import ttk, font


class UiSect2(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        ttk.Frame.__init__(self, master, **kwargs)

        # Create a Grid Layout that contains 2 rows and 1 column.
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=6)

        # Create a label with padding for top frame of section 2
        lbl_uut = ttk.Label(self, text="Unit Under Test", font=font.Font(size=10, weight="bold"), foreground="#333333")
        lbl_uut.grid(row=0, column=0, sticky="nsew", padx=(10, 0))

        # Create a frame for the 2nd row of section 2
        frm_uut = ttk.Frame(self, padding="3 3 3 3")
        frm_uut.grid(row=1, column=0, sticky="nsew")

        # in the 2nd row frame, create a grid layout that contains 1 row and 3 columns
        frm_uut.grid_rowconfigure(0, weight=1)
        frm_uut.grid_columnconfigure(0, weight=1)
        frm_uut.grid_columnconfigure(1, weight=1)
        frm_uut.grid_columnconfigure(2, weight=1)

        # Create LabelFrame for the 1st column of the 2nd row frame
        # frm_uut1 = ttk.LabelFrame(frm_uut, text="UUT 1", padding="3 3 0 3")
        # frm_uut1 = ttk.LabelFrame(frm_uut, text="UUT 1", padding="3 3 0 3", labelanchor='n')
        font_small = font.Font(size=10)
        frm_uut1 = ttk.LabelFrame(frm_uut, text="UUT 1", padding="0 0 0 0")
        frm_uut1.grid(row=0, column=0, sticky="nsew")

        frm_uut1.grid(row=0, column=0, sticky="nsew")






