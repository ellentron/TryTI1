import customtkinter as ctk
from PIL import Image


# A class representing a Stop button with icon
# class StopButton(ctk.CTkButton):
#     """A class representing a Stop button with icon."""
#     def __init__(self, master=None, state='normal', width=42, **kwargs):
#         ctk.CTkButton.__init__(self, master, state='normal', **kwargs)
#         """ Constructor for the StopButton class.
#         Args:
#             master (str): The master container.
#         """
#         self._width = width
#
#         # Open icon image
#         self.stop_icon_image = Image.open("images/PlayCircle.png")
#         # scale the image to the desired size
#         self.stop_icon_image = self.stop_icon_image.resize((self._width, self._width), Image.ANTIALIAS)
#
#         # Create image with solid color as background
#         background = Image.new("RGBA", (self._width, self._width), (255, 255, 255, 0))
#         # scale the image to the desired size
#         background = background.resize((self._width, self._width), Image.ANTIALIAS)
#
#         # Create a new image with a circle drawn on it
#         #circle = Image.new("RGBA", (self._width, self._width), (0, 0, 0, 0))  # set alpha channel to 0
#         circle = Image.new("RGBA", (self._width, self._width), (0, 0, 0, 0))  # set alpha channel to 0
#
#         # scale the image to the desired size
#         circle = circle.resize((self._width, self._width), Image.ANTIALIAS)
#
#         draw = ImageDraw.Draw(circle)
#         draw.ellipse((0, 0, self._width, self._width), fill=(255, 0, 0, 255))
#
#         # Overlay the circle on top of background using the alpha_composite() method
#         result = Image.alpha_composite(background, circle)
#
#
#         # Save the overlaid image to a file or display it on the screen
#         # result.save("overlay.png", format="PNG")
#         # result.show()
#
#         #self.kuku_image = Image.open("overlay.png")
#         self.kuku_image = result
#
#         # Print the width and height of kuku_image with description
#         print(f"kuku_image: {self.kuku_image.width}, {self.kuku_image.height}")
#         print(f"stop_icon_image: {self.stop_icon_image.width}, {self.stop_icon_image.height}")
#
#         # Overlay the result image with the resized stop icon image
#         final_result = Image.alpha_composite(self.kuku_image, self.stop_icon_image)
#
#
#         self._my_state = state
#         # self._width = width
#
#         self._icon = ctk.CTkImage(light_image=final_result, dark_image=final_result, size=(self._width, self._width))
#
#         self._value = True
#         self.configure(image=self._icon, fg_color='transparent', hover_color='lightgray', state=self._my_state, width=self._width)
#
#
#
#         # if state is disabled configure frame to _icon_off
#         # if self._my_state == 'disabled':
#         #     self.configure(image=self._icon_disabled, fg_color='transparent', hover_color='lightgray', state=self._my_state, width=self._width)
#         #     # self.configure(image=self._icon_disabled, fg_color='transparent', hover_color='lightgray', state=self._my_state, width=self._icon_disabled.width())
#         #
#         # else:
#         #     self.configure(image=self._icon_enabled, fg_color='transparent', hover_color='lightgray', state=self._my_state, width=self._width)
#         #
#


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

        self._value = True

        # if state is disabled configure frame to _icon_off
        if self._my_state == 'disabled':
            self.configure(image=self._icon_disabled, fg_color='transparent', hover_color='lightgray', state=self._my_state, width=self._width)
            # self.configure(image=self._icon_disabled, fg_color='transparent', hover_color='lightgray', state=self._my_state, width=self._icon_disabled.width())

        else:
            self.configure(image=self._icon_enabled, fg_color='transparent', hover_color='lightgray', state=self._my_state, width=self._width)




