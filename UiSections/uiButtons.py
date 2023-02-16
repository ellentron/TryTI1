import tkinter as tk
import customtkinter as ctk


class StartButton(ctk.CTkButton):
    """A class representing a Start button with icon."""
    def __init__(self, master=None, state='normal', **kwargs):
        ctk.CTkButton.__init__(self, master, state='normal', **kwargs)
        """ Constructor for the StartButton class.
        Args:
            master (str): The master container.
        """
        self._my_state = state

        self._icon = tk.PhotoImage(file="images/play_circle_FILL_blue_sz42.png")
        self._icon_on = tk.PhotoImage(file="images/play_circle_FILL_blue_sz42.png")
        self._icon_off = tk.PhotoImage(file="images/play_circle_FILL_blue_disabled_sz42.png")

        self._icon_size = 0
        self._icon_padding = 0

        self._value = True

        # if state is disabled configure frame to _icon_off
        if self._my_state == 'disabled':
            self.configure(image=self._icon_off, fg_color='transparent', hover_color='lightgray', state=self._my_state, width=self._icon_off.width())

        else:
            self.configure(image=self._icon, fg_color='transparent', hover_color='lightgray', state=self._my_state, width=self._icon_off.width())

    # def on(self):
    #     self._value = True
    #     self.configure(image=self._icon_on)
    #
    # def off(self):
    #     self._value = False
    #     self.configure(image=self._icon_off)
