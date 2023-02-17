import tkinter as tk
# from tkinter import ttk, font
import customtkinter as ctk
from UiSections.uiLed import LED
from UiSections.uiButtons import StartButton


class UiConnection(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)

        def connect_clicked():
            self.led.toggle()

        # Create fonts
        bold_font = ctk.CTkFont(size=12, weight="bold")
        group_label_font = ctk.CTkFont(size=14, weight="bold")

        # Create frame for the Power Meter Connection section
        self.power_meter_frame = ctk.CTkFrame(self)
        self.power_meter_frame.pack(expand=True, fill="both", padx=(5, 5), pady=(5, 5))

        # Create grid layout for the frame - 2 rows, 4 column
        self.power_meter_frame.grid_columnconfigure(0, weight=1)
        self.power_meter_frame.grid_columnconfigure(1, weight=1)
        self.power_meter_frame.grid_columnconfigure(2, weight=1)
        self.power_meter_frame.grid_columnconfigure(3, weight=1)
        self.power_meter_frame.grid_rowconfigure(0, weight=1)
        self.power_meter_frame.grid_rowconfigure(1, weight=1000)

        # Create Power Meter Connection heading label
        self.pm_connect_heading = ctk.CTkLabel(self.power_meter_frame, text="Power Meter Connection", font=group_label_font)
        self.pm_connect_heading.grid(row=0, column=0, columnspan=4, sticky="nw", padx=(10, 0), pady=(10, 10))

        # Create COM port label
        self.com_port_label = ctk.CTkLabel(self.power_meter_frame, text="COM Port:", font=bold_font)
        self.com_port_label.grid(row=1, column=0, sticky="ew", padx=(10, 0), pady=(10, 10))

        # Create COM port combobox
        self.connection_list = ["COM5", "COM7", "COM15"]
        self.combobox_connection_list = ctk.CTkComboBox(master=self.power_meter_frame, width=140, justify="left",
                                                        values=self.connection_list)
        self.combobox_connection_list.grid(row=1, column=1, sticky="ew", padx=(10, 0), pady=(10, 10))

        # Create and place the "is_connected" Led
        self.led = LED(self.power_meter_frame)
        # display the led while keeping it aligned and centered relative to the widget in the cell to its left
        self.led.grid(row=1, column=3, sticky="nsew", padx=(0, 0), pady=(10, 10))

        # Create Connect button when clicked will connect to the power meter
        self.connect_button = ctk.CTkButton(self.power_meter_frame, text="Connect", command=connect_clicked, width=10)
        self.connect_button.grid(row=1, column=2, sticky="ew", padx=(5, 0), pady=(10, 10))

        self.led.on()


""" ==================================================================================================== """


# Class for RunControl frame
class UiRunControl(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)

        # Create fonts
        bold_font = ctk.CTkFont(size=12, weight="bold")
        group_label_font = ctk.CTkFont(size=14, weight="bold")

        # Create frame for the Run Control section
        self.run_control_frame = ctk.CTkFrame(self)
        self.run_control_frame.pack(expand=True, fill="both", padx=(5, 5), pady=(5, 5))

        # Create grid layout for the frame - 3 rows, 5 column
        self.run_control_frame.grid_columnconfigure(0, weight=1)
        self.run_control_frame.grid_columnconfigure(1, weight=1)
        self.run_control_frame.grid_columnconfigure(2, weight=1)
        self.run_control_frame.grid_columnconfigure(3, weight=1)
        self.run_control_frame.grid_columnconfigure(4, weight=1)
        self.run_control_frame.grid_rowconfigure(0, weight=1)
        self.run_control_frame.grid_rowconfigure(1, weight=1)
        self.run_control_frame.grid_rowconfigure(2, weight=1)

        # Create label "Measurement Time [hours]:"
        self.measurement_time_label = ctk.CTkLabel(self.run_control_frame, text="Measurement Time:", font=bold_font)
        self.measurement_time_label.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=(10, 10))

        # Create entry for measurement time. Default text = "24"
        self.measurement_time_entry = ctk.CTkEntry(self.run_control_frame, width=55, justify="center")
        self.measurement_time_entry.insert(0, '24')
        self.measurement_time_entry.grid(row=0, column=1, sticky="w", padx=(10, 0), pady=(10, 10))

        # Create frame for the Start and Stop buttons, width=10
        self.start_stop_frame = ctk.CTkFrame(self.run_control_frame)
        self.start_stop_frame.grid(row=0, column=2, columnspan=2, sticky="nsew", padx=(1, 1), pady=(5, 5))

        # create grid layout for the start_stop_frame - 1 rows, 2 columns
        self.start_stop_frame.grid_rowconfigure(0, weight=1)
        self.start_stop_frame.grid_columnconfigure(0, weight=1)
        self.start_stop_frame.grid_columnconfigure(1, weight=1)

        # Create Start button
        self.start_button = StartButton(master=self.start_stop_frame, text="", state='normal')
        self.start_button.grid(row=0, column=0, sticky="nsw", padx=(0, 0), pady=(0, 0))

        self.stop_button = StartButton(master=self.start_stop_frame, text="", state='disabled')
        self.stop_button.grid(row=0, column=1, sticky="nsw", padx=(0, 0), pady=(0, 0))

        self.time_info = "Time left: 10:00:00. Time elapsed: 14:00:00 of 24:00:00 hours"
        # Create label for time information
        self.time_info_label = ctk.CTkLabel(self.run_control_frame, text=self.time_info)
        self.time_info_label.grid(row=1, column=0, columnspan=5, sticky="sew", padx=(0, 0), pady=(0, 0))

        # Create label "Progress:"
        self.progress_label = ctk.CTkLabel(self.run_control_frame, text="Progress:", font=bold_font)
        self.progress_label.grid(row=2, column=0, sticky="nse", padx=(0, 10), pady=(10, 10))

        # Create progress bar
        self.progress_bar = ctk.CTkProgressBar(self.run_control_frame)
        self.progress_bar.grid(row=2, column=1, columnspan=3, sticky="nsew", padx=(0, 0), pady=(16, 16))

        # Create label "50%"
        self.progress_label = ctk.CTkLabel(self.run_control_frame, text="50%")
        self.progress_label.grid(row=2, column=4, sticky="nse", padx=(5, 10), pady=(0, 0))


""" ==================================================================================================== """

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
        self.grid_rowconfigure(1, weight=123)

        # Create Power Measurement heading label
        self.pm_heading = ctk.CTkLabel(self, text="Power Measurement", font=group_label_font)
        self.pm_heading.grid(row=0, column=0, sticky="nw", padx=(10, 0), pady=(0, 0))

        # Create UiConnection frame
        self.ui_pm_connect_frame = UiConnection(self)
        self.ui_pm_connect_frame.grid(row=1, column=0, sticky="nsew", padx=(10, 10), pady=(10, 10))

        # Create UiRunControl instance and place it in the master frame
        self.ui_run_control_frame = UiRunControl(self)
        self.ui_run_control_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 10), pady=(10, 10))

