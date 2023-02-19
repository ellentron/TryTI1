import customtkinter as ctk
from PIL import Image, ImageDraw


class IconButton(ctk.CTkButton):
    """A class representing a circular button with icon."""
    def __init__(self,
                 master=None,
                 state='normal',
                 width=42,
                 icon_file=None,
                 bg_color=None,
                 **kwargs):
        ctk.CTkButton.__init__(self, master, state=state, **kwargs)
        """ Constructor for the IconButton class.
        Args:
            master (str): The master container.
        """
        self._my_state = state
        self._width = width

        # Open icon image
        self.icon_image = Image.open(icon_file)

        # scale the image to the desired size
        self.icon_image = self.icon_image.resize((width, width), Image.ANTIALIAS)

        # Create image with solid color as background
        self.background = Image.new("RGBA", (width, width), (255, 255, 255, 0))

        # scale the image to the desired size
        self.background = self.background.resize((width, width), Image.ANTIALIAS)

        # Create a new image with a circle drawn on it
        self.circle = Image.new("RGBA", (width, width), (0, 0, 0, 0))  # set alpha channel to 0

        # scale the image to the desired size
        # circle = circle.resize((width, width), Image.ANTIALIAS)

        self.draw = ImageDraw.Draw(self.circle)
        # draw.ellipse((0, 0, width-1, width-1), fill=(0, 255, 0, 255))

        if self._my_state == 'disabled':
            self.draw.ellipse((0, 0, width-1, width-1), fill=None)
        else:
            self.draw.ellipse((0, 0, width-1, width-1), fill=bg_color)

        # Overlay the circle on top of background using the alpha_composite() method
        result = Image.alpha_composite(self.background, self.circle)

        # Crop the icon image to the same size as the circle image
        self.icon_image = self.icon_image.crop((0, 0, width, width))

        # Overlay the result image with the resized icon image
        final_result = Image.alpha_composite(result, self.icon_image)

        self._my_state = state
        # self._width = width

        self._icon = ctk.CTkImage(light_image=final_result, dark_image=final_result, size=(width, width))

        self._value = True
        self.configure(image=self._icon, fg_color='transparent', hover_color='lightgray', state=self._my_state, width=width+20, height=width+20)

        # bind the button click event to the on_button_click method
        self.bind("<Button-1>", self.on_button_click)

    def on_button_click(self, event):
        if self._my_state == 'disabled':
            self.draw.ellipse((0, 0, self.width-1, self.width-1), fill=None)
        else:
            self.draw.ellipse((0, 0, self.width-1, self.width-1), fill=bg_color)