import tkinter as tk
import customtkinter as ctk
from PIL import Image


class StartButton(ctk.CTkButton):
    """A class representing a Start button with icon."""
    def __init__(self, master=None, state='normal', width=40, **kwargs):
        ctk.CTkButton.__init__(self, master, state='normal', **kwargs)
        """ Constructor for the StartButton class.
        Args:
            master (str): The master container.
        """
        self._my_state = state
        self._width = width
        self._icon = ctk.CTkImage(light_image=Image.open("images/play_circle_FILL_blue_sz42.png"),
                                  dark_image=Image.open("images/play_circle_FILL_blue_sz42.png"),
                                  size=(self._width, self._width))

        self._icon_enabled = ctk.CTkImage(light_image=Image.open("images/play_circle_FILL_blue_sz42.png"),
                                          dark_image=Image.open("images/play_circle_FILL_blue_sz42.png"),
                                          size=(self._width, self._width))

        self._icon_disabled = ctk.CTkImage(light_image=Image.open("images/play_circle_FILL_blue_disabled_sz42.png"),
                                           dark_image=Image.open("images/play_circle_FILL_blue_disabled_sz42.png"),
                                           size=(self._width, self._width))

        # self._icon = tk.PhotoImage(file="images/play_circle_FILL_blue_sz42.png")
        # self._icon_enabled = tk.PhotoImage (file="images/play_circle_FILL_blue_sz42.png")
        # self._icon_disabled = tk.PhotoImage(file="images/play_circle_FILL_blue_disabled_sz42.png")

        # self._icon_size = 0
        # self._icon_padding = 0

        self._value = True

        # if state is disabled configure frame to _icon_off
        if self._my_state == 'disabled':
            self.configure(image=self._icon_disabled, fg_color='transparent', hover_color='lightgray', state=self._my_state, width=self._width)
            # self.configure(image=self._icon_disabled, fg_color='transparent', hover_color='lightgray', state=self._my_state, width=self._icon_disabled.width())

        else:
            self.configure(image=self._icon_enabled, fg_color='transparent', hover_color='lightgray', state=self._my_state, width=self._width)
            # self.configure(image=self._icon_enabled, fg_color='transparent', hover_color='lightgray', state=self._my_state, width=self._icon_enabled.width())

    # def on(self):
    #     self._value = True
    #     self.configure(image=self._icon_on)
    #
    # def off(self):
    #     self._value = False
    #     self.configure(image=self._icon_off)
