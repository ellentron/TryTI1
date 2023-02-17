import tkinter as tk
from tkinter import ttk, font
import customtkinter as ctk
from PIL import Image

# create LED class that uses ledON1.png and ledOFF1.png based on CTkFrame
class LED(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)

        self.ledON = ctk.CTkImage(light_image=Image.open("images/LedON1.png"),
                                  dark_image=Image.open("images/LedON1.png"), size=(19, 19))
        self.ledOFF = ctk.CTkImage(light_image=Image.open("images/LedOFF1.png"),
                                   dark_image=Image.open("images/LedOFF1.png"), size=(19, 19))
        self.led = self.ledOFF
        self.state = False
        # set the color to transparent so that the image will show through
        self.configure(fg_color='transparent')
        self.button = ctk.CTkButton(self, image=self.led, text='', state='disabled', width=19, height=19)
        self.button.configure(bg_color='transparent', fg_color='transparent')
        # pack the button so that it will fill the frame while keeping the image centered
        self.button.pack(expand=True, fill="both", padx=(0, 0), pady=(0, 0))

    def on(self):
        self.led = self.ledON
        self.state = True
        # Refresh display for button
        self.button.configure(image=self.led)

    def off(self):
        self.led = self.ledOFF
        self.state = False
        # Refresh display for button
        self.button.configure(image=self.led)

    def toggle(self):
        if self.state:
            self.led = self.ledOFF
            self.state = False
        else:
            self.led = self.ledON
            self.state = True
        # Refresh display for button
        self.button.configure(image=self.led)
