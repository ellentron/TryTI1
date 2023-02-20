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
        self.state = state
        self._width = width
        self.bg_color = bg_color

        # Open icon image
        self.icon_image = Image.open(icon_file)

        # scale the image to the desired size
        self.icon_image = self.icon_image.resize((width, width), Image.ANTIALIAS)

        self.update_button()

    def update_button(self):
        """ Update the button's appearance. """
        # Create image with solid color as background
        self.background = Image.new("RGBA", (self._width, self._width), (255, 255, 255, 0))
        # scale the image to the desired size
        self.background = self.background.resize((self._width, self._width), Image.ANTIALIAS)
        # Create a new image with a circle drawn on it
        self.circle = Image.new("RGBA", (self._width, self._width), (0, 0, 0, 0))  # set alpha channel to 0
        self.draw = ImageDraw.Draw(self.circle)
        # Draw the circle
        if self.cget("state") == 'disabled':
            self.state = 'disabled'
            # self.configure(state='disabled')
            self.draw.ellipse((0, 0, self._width - 1, self._width - 1), fill=None)
        else:
            self.state = 'normal'
            # self.configure(state='normal')
            self.draw.ellipse((0, 0, self._width - 1, self._width - 1), fill=self.bg_color)
        # Overlay the circle on top of background using the alpha_composite() method
        result = Image.alpha_composite(self.background, self.circle)
        # Overlay the result image with the resized icon image
        self._final_result = Image.alpha_composite(result, self.icon_image)
        # Compose the final image
        self._icon = ctk.CTkImage(light_image=self._final_result, dark_image=self._final_result,
                                  size=(self._width, self._width))
        # configure the button with the final image
        self.configure(image=self._icon, fg_color='transparent', hover_color='lightgray', state=self.state,
                       width=self._width + 20, height=self._width + 20)
