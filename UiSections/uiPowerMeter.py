import tkinter as tk
# from tkinter import ttk, font
import customtkinter as ctk
from UiSections.uiLed import LED


class UiConnection(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)

        # Create fonts
        bold_font = ctk.CTkFont(size=12, weight="bold")
        group_label_font = ctk.CTkFont(size=14, weight="bold")

        # Create grid layout for the frame - 2 rows, 4 column
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Create Power Meter Connection heading label
        self.pm_connect_heading = ctk.CTkLabel(self, text="Power Meter Connection", font=group_label_font)
        self.pm_connect_heading.grid(row=0, column=0, columnspan=4, sticky="nw", padx=(10, 0), pady=(10, 10))

        # Create COM port label
        self.com_port_label = ctk.CTkLabel(self, text="COM Port:", font=bold_font)
        self.com_port_label.grid(row=1, column=0, sticky="nw", padx=(10, 0), pady=(10, 10))

        # Create COM port combobox
        self.connection_list = ["COM5", "COM7", "COM15"]
        self.combobox_connection_list = ctk.CTkComboBox(master=self, width=140, justify="left",
                                                        values=self.connection_list)
        self.combobox_connection_list.grid(row=1, column=1, sticky="nw", padx=(10, 0), pady=(10, 10))

        # Create Connect button
        self.connect_button = ctk.CTkButton(self, text="Connect", width=10)
        self.connect_button.grid(row=1, column=2, sticky="nw", padx=(10, 0), pady=(10, 10))

        # Create and place the "is_connected" Led
        self.led = LED(self, size=16, color="green")
        self.led.grid(row=1, column=3, padx=[0, 10], pady=[2, 8], sticky="n")
        self.led.on()






class UiPowerMeter(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)

        self.com_list = ["COM3", "COM8", "COM12"]

        # Create bold font
        bold_font = ctk.CTkFont(size=12, weight="bold")
        group_label_font = ctk.CTkFont(size=14, weight="bold")

        # Create grid layout for this frame - 2 rows, 2 columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=111)

        # Create Power Measurement heading label
        self.pm_heading = ctk.CTkLabel(self, text="Power Measurement", font=group_label_font)
        self.pm_heading.grid(row=0, column=0, sticky="nsw", padx=(10, 0), pady=(10, 10))

        # Create UiConnection frame
        self.ui_pm_connect_frame = UiConnection(self)
        self.ui_pm_connect_frame.grid(row=1, column=0, sticky="nsw", padx=(10, 10), pady=(10, 10))

        # # Create Power Measurement container group
        # self.pm_group = ctk.CTkFrame(self)
        # self.pm_group.grid(row=1, column=0, sticky="nsew", padx=(10, 10), pady=(10, 10))
        #
        # # In the Power Measurement group, create a grid layout - 2 rows, 4 columns
        # self.pm_group.grid_columnconfigure((0, 1, 2, 3), weight=1)
        # self.pm_group.grid_rowconfigure((0, 1), weight=1)
        #
        # # Create label "Power Meter Connection"
        # self.pm_connection_label = ctk.CTkLabel(self.pm_group, text="Power Meter Connection", font=bold_font)
        # self.pm_connection_label.grid(row=0, column=0, sticky="nw", padx=(10, 0), pady=(10, 10))
        #
        # # Create label "COM Port:"
        # self.com_port_label = ctk.CTkLabel(self.pm_group, text="COM Port:", font=bold_font)
        # self.com_port_label.grid(row=1, column=0, sticky="nw", padx=(10, 0), pady=(10, 10))
        #
        # # Create COM Port combobox
        # self.com_port_combobox = ctk.CTkCombobox(self.pm_group, values=self.com_list, width=10)
        # self.com_port_combobox.grid(row=1, column=1, sticky="nw", padx=(10, 0), pady=(10, 10))




        # self.kukulabel = ctk.CTkLabel(self, text="KUKU !!!!!", font=group_label_font)
        # self.kukulabel.grid(row=1, column=0, sticky="nw", padx=(10, 0), pady=(10, 10))

        # self.pm_connection = self.UiConnection(self)
        # self.pm_connection.grid(row=1, column=0, sticky="nsew", padx=(10, 0), pady=(10, 10))


    # Create class for Power Meter Connection

