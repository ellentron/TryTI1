import tkinter as tk
from tkinter import ttk, font
import customtkinter as ctk


class LED(ctk.CTkFrame):
    def __init__(self, parent, color="red", size=20, padding=4, **kwargs):
        ctk.CTkFrame.__init__(self, parent, width=size+2*padding, height=size+2*padding, **kwargs)

        self._color = color
        self._size = size
        self._padding = padding
        self._value = False

        self._circle = ctk.CTkCanvas(self, width=size+2*padding, height=size+2*padding)
        self._circle.grid(row=0, column=0, sticky="nsew")

        self._oval = self._circle.create_oval(padding, padding, size+padding, size+padding, fill="")
        self._circle.pack(anchor="center", expand=True)

        self.pack_propagate(False)


# import tkinter as tk
# from tkinter import ttk, font
# import customtkinter as ctk
#
#
# class LED(ctk.CTkFrame):
#     def __init__(self, parent, color="red", size=20, **kwargs):
#         ctk.CTkFrame.__init__(self, parent, width=size, height=size, **kwargs)
#
#         self._color = color
#         self._size = size
#         self._value = False
#
#         # # Create grid layout for the frame 1 row, 1 column
#         # self.grid_rowconfigure(0, weight=1)
#         # self.grid_columnconfigure(0, weight=1)
#
#         self._circle = ctk.CTkCanvas(self, width=size, height=size)
#         self._circle.grid(row=0, column=0, sticky="nsew")
#
#         # Create ovel for the LED centered in the frame
#         self._oval = self._circle.create_oval(0, 0, size, size, fill="")
#         self._circle.pack(anchor="center", expand=True)
#
#
#         # self._circle.pack(anchor="center", expand=True)
#         # self._circle.pack()
#         # self._oval = self._circle.create_oval(0, 0, size, size, fill=self._color)
#         self.pack_propagate(False)

    def on(self):
        self._value = True
        self._circle.itemconfig(self._oval, fill=self._color)

    def off(self):
        self._value = False
        self._circle.itemconfig(self._oval, fill="")

