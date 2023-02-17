import customtkinter as ctk

from UiSections.uiLed import LED


class UiConnection(ctk.CTkFrame):
    # Class for Connection frame
    def __init__(self,
                 master=None,
                 connection_title='',
                 connect_to_label='COM Port:',
                 connection_list=None,
                 **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)

        self.connect_to_label = connect_to_label

        # Tempory function for testing the LED
        def connect_clicked():
            self.led.toggle()

        # Create fonts
        bold_font = ctk.CTkFont(size=12, weight="bold")
        group_label_font = ctk.CTkFont(size=14, weight="bold")

        # Create frame for the Power Meter Connection section
        self.power_meter_frame = ctk.CTkFrame(self)
        self.power_meter_frame.pack(expand=True, fill="both", padx=(5, 5), pady=(5, 5))

        # Create grid layout for the frame - 2 rows, 4 column
        self.power_meter_frame.grid_columnconfigure(index='all', weight=1)
        # self.power_meter_frame.grid_columnconfigure(1, weight=1)
        # self.power_meter_frame.grid_columnconfigure(2, weight=1)
        # self.power_meter_frame.grid_columnconfigure(3, weight=1)
        self.power_meter_frame.grid_rowconfigure(index='all', weight=1)
        # self.power_meter_frame.grid_rowconfigure(1, weight=1)

        # Create Connection title label
        self.pm_connect_heading = ctk.CTkLabel(self.power_meter_frame, text=connection_title, font=group_label_font)
        self.pm_connect_heading.grid(row=0, column=0, columnspan=4, sticky="new", padx=(10, 0), pady=(5, 0))

        # Create Connection port label
        self.com_port_label = ctk.CTkLabel(self.power_meter_frame, text=self.connect_to_label, font=bold_font)
        self.com_port_label.grid(row=1, column=0, sticky="ew", padx=(10, 0), pady=(0, 35))

        # Create COM port combobox
        self.connection_list = connection_list
        self.combobox_connection_list = ctk.CTkComboBox(master=self.power_meter_frame, width=140, justify="left",
                                                        values=self.connection_list)
        self.combobox_connection_list.grid(row=1, column=1, sticky="ew", padx=(0, 0), pady=(0, 35))

        # Create Connect button when clicked will connect to the power meter
        self.connect_button = ctk.CTkButton(self.power_meter_frame, text="Connect", command=connect_clicked, width=10)
        self.connect_button.grid(row=1, column=2, sticky="ew", padx=(10, 0), pady=(0, 35))

        # Create and place the "is_connected" Led
        self.led = LED(self.power_meter_frame)
        # display the led while keeping it aligned and centered relative to the widget in the cell to its left
        self.led.grid(row=1, column=3, sticky="w", padx=(0, 0), pady=(0, 35))
