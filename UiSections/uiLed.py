import tkinter as tk
from tkinter import ttk, font
import customtkinter as ctk
from PIL import Image

# create LED class that uses ledON1.png and ledOFF1.png based on CTkFrame
class LED(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)

        self.ledON = ctk.CTkImage(light_image=Image.open("images/LedON1.png"),
                                  dark_image=Image.open("images/LedON1.png"), size=(14, 14))
        self.ledOFF = ctk.CTkImage(light_image=Image.open("images/LedOFF1.png"),
                                   dark_image=Image.open("images/LedOFF1.png"), size=(14, 14))
        self.led = self.ledOFF

        self.button = ctk.CTkButton(self, image=self.led, text='', state='disabled', width=14, height=14)
        self.button.configure(bg_color='transparent', fg_color='transparent')
        self.button.pack()

    def on(self):
        self.led = self.ledON
        # self.configure(image=self.led)

    def off(self):
        self.led = self.ledOFF
        # self.configure(image=self.led)

    # def toggle(self):
    #     if self.led == self.ledON:
    #         self.led = self.ledOFF
    #     else:
    #         self.led = self.ledON
    #     self.configure(image=self.led)
    #
    # def change_color(self, color):
    #     self.color = color
    #     self.led = self.ledOFF
    #     self.configure(image=self.led)
    #
    # def change_radius(self, radius):
    #     self.radius = radius
    #     self.led = self.ledOFF
    #     self.configure(image=self.led)
    #
    # def change_color_and_radius(self, color, radius):
    #     self.color = color
    #     self.radius = radius
    #     self.led = self.ledOFF
    #     self.configure(image=self.led)


#
# class LED(ctk.CTkFrame):
#
#
#
#         self.ledOFF = ctk.CTkImage(light_image=Image.open("images/LedOFF1.png"),
#                                    dark_image=Image.open("images/LedOFF1.png"), size=(30, 30))
#         self.ledON = ctk.CTkImage(light_image=Image.open("images/LedON1.png"),
#                                   dark_image=Image.open("images/LedON1.png"), size=(30, 30))
#         # self.ledON = tk.PhotoImage(file="ledON1.png")
#         # self.ledOFF = tk.PhotoImage(file="ledOFF1.png")
#         self.led = self.ledOFF

    # def on(self):
    #     self.led = self.ledON
    #     self.configure(image=self.led)
    #
    # def off(self):
    #     self.led = self.ledOFF
    #     self.configure(image=self.led)
    #
    # def toggle(self):
    #     if self.led == self.ledON:
    #         self.led = self.ledOFF
    #     else:
    #         self.led = self.ledON
    #     self.configure(image=self.led)
    #
    # def change_color(self, color):
    #     self.color = color
    #     self.led = self.ledOFF
    #     self.configure(image=self.led)
    #
    # def change_radius(self, radius):
    #     self.radius = radius
    #     self.led = self.ledOFF
    #     self.configure(image=self.led)
    #
    # def change_color_and_radius(self, color, radius):
    #     self.color = color
    #     self.radius = radius
    #     self.led = self.ledOFF
    #     self.configure(image=self.led)

