import customtkinter as ctk
from PIL import Image, ImageTk

class UiSect1(ctk.CTkFrame):
    def __init__(self, master=None, sw_name="Software Name", sw_ver="Ver: 0.0.0    |    ", spec_ver="0.0.0", **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)

        # Set frame to expand with master
        self.pack(expand=True)

        # Create bold font
        bold_font = ctk.CTkFont(size=22, weight="bold")

        # Create horizontal grid for the frame labels 1 raw, 4 columns
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure(1, weight=100)

        # Create Logo Picture container
        self.logo_image = ctk.CTkImage(light_image=Image.open("images/Nova_Logo.png"),
                                       dark_image=Image.open("images/Nova_Logo.png"), size=(170, 29))
        self.logo = ctk.CTkLabel(self, text='', image=self.logo_image, justify="left")
        self.logo.grid(row=0, column=1, sticky="nsw", padx=(10, 0), pady=(0, 0))

        # Software Name sw_name Label
        self.sw_name = ctk.CTkLabel(self, text=sw_name, font=bold_font, text_color="gray")
        self.sw_name.grid(row=0, column=1, sticky="nsew", padx=(200, 0), pady=(10, 10))

        self.sw_ver = ctk.CTkLabel(self, text=sw_ver)
        self.sw_ver.grid(row=0, column=2, sticky="nse", padx=(0, 0), pady=(10, 10))

        self.spec_ver = ctk.CTkLabel(self, text=spec_ver)
        self.spec_ver.grid(row=0, column=3, sticky="nse", padx=(0, 50), pady=(10, 10))
