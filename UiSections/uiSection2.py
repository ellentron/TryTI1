import tkinter as tk
# from tkinter import ttk, font
import customtkinter as ctk
from UiSections.uiLed import LED


class UiSect2(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)

        self.radio_var = tk.IntVar(value=0)     # Variable to hold the value of the selected radio button

        self.ip_list = ["10.0.30.1", "10.0.30.20", "10.0.30.80"]
        self.com_list = ["COM3", "COM8", "COM12"]

        if self.radio_var.get() == 0:
            self.connection_list = self.ip_list
        else:
            self.connection_list = self.com_list

        def radiobutton_event():
            print("radiobutton toggled, current value:", self.radio_var.get())
            # if radio_var is 0: connection_list = ip_list
            # if radio_var is larger than 0: connection_list = serial_list
            if self.radio_var.get() == 0:
                self.connection_list = self.ip_list
            else:
                self.connection_list = self.com_list

            # Update self.combobox_ip
            self.combobox_ip.configure(values=self.connection_list)
            self.combobox_ip.set(self.connection_list[0])
            self.combobox_ip.update_idletasks()

        # self._border_width = 2
        # self._border_color = "white"

        # Create bold font
        bold_font = ctk.CTkFont(size=12, weight="bold")
        group_label_font = ctk.CTkFont(size=14, weight="bold")

        # 2) Create a Grid Layout that contains 2 rows and 1 column (1st title, 2nd --> 3 group frames for UUT).
        self.grid_rowconfigure(0, weight=1)     # 2.0) Title (Unit Under Test)
        self.grid_rowconfigure(1, weight=111)   # 2.1) 3 frames (Laser Brand radio buttons, Connection, and Details)

        # 2.0) Create a label for top frame of section 2 header and place it in the 1st row of the grid layout
        self.lbl_uut = ctk.CTkLabel(self, text="Unit Under Test", font=ctk.CTkFont(size=16, weight="bold"))
        self.lbl_uut.grid(row=0, column=0, sticky="nsw", padx=(15, 0), pady=(1, 1))

        # 2.1) Create a frame for holding 3 frames -
        # 2.1.0) Laser Brand radio buttons,
        # 2.1.1) Laser Controller Connection, and Details),
        # 2.1.2) Details and set grid layout to 1 row and 3 columns
        self.frame_uut = ctk.CTkFrame(self)                     # 2.1)
        # Place the frame in the 2nd row of the grid layout
        self.frame_uut.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")

        self.frame_uut.grid_rowconfigure(0, weight=1)
        self.frame_uut.grid_columnconfigure(0, weight=1)
        self.frame_uut.grid_columnconfigure(1, weight=1)
        self.frame_uut.grid_columnconfigure(2, weight=1)

        # ===================== 2.1.0) Laser Brand radio buttons,======================================================
        # 2.1.0) Create frame for the radio buttons group
        self.frame_radio_group = ctk.CTkFrame(master=self.frame_uut)
        # 2.1.0) Place the frame in the 1st column of the grid layout
        self.frame_radio_group.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="new")

        # 2.1.0) Create grid layout for the radio button group frame with 4 rows and 1 column
        self.frame_radio_group.grid_rowconfigure((0, 1, 2, 3), weight=1)
        # self.frame_radio_group.grid_rowconfigure(1, weight=1)
        # self.frame_radio_group.grid_rowconfigure(2, weight=1)
        # self.frame_radio_group.grid_rowconfigure(3, weight=1)
        self.frame_radio_group.grid_columnconfigure(0, weight=1)

        # Create a label for the radio button group
        self.label_radio_group = ctk.CTkLabel(master=self.frame_radio_group, text="Laser Brand", font=group_label_font)
        self.label_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=0, sticky="n")

        # Create and place the radio buttons in the radio button group frame
        self.radio_button_1 = ctk.CTkRadioButton(master=self.frame_radio_group, variable=self.radio_var,
                                                 value=0, text="Toptica 405", command=radiobutton_event)
        self.radio_button_1.grid(row=1, column=0, pady=2, padx=20,  sticky="n")

        self.radio_button_2 = ctk.CTkRadioButton(master=self.frame_radio_group, variable=self.radio_var,
                                                 value=1, text="Cobolt 457", command=radiobutton_event)
        self.radio_button_2.grid(row=2, column=0, pady=2, padx=20, sticky="n")

        self.radio_button_3 = ctk.CTkRadioButton(master=self.frame_radio_group, variable=self.radio_var,
                                                 value=2, text="Cobolt 532", command=radiobutton_event)
        self.radio_button_3.grid(row=3, column=0, pady=2, padx=20, sticky="n")

        # ===================== 2.1.1) Laser Controller Connection) ===================================================
        # 2.1.1) Create Frame container for "Laser Controller Connection" widgets
        self.connection_group = ctk.CTkFrame(master=self.frame_uut)
        # 2.1.1) Place the frame in the 2nd column of the grid layout
        self.connection_group.grid(row=0, column=1, padx=(0, 0), pady=(5, 5), sticky="nsew")

        # 2.1.1) Create grid layout for the "Laser Controller Connection" frame with 2 rows and 4 columns
        self.connection_group.grid_rowconfigure(0, weight=1)
        self.connection_group.grid_rowconfigure(1, weight=1)
        self.connection_group.grid_columnconfigure((0, 1, 2, 3), weight=1)
        # self.connection_group.grid_columnconfigure(1, weight=1)
        # self.connection_group.grid_columnconfigure(2, weight=1)
        # self.connection_group.grid_columnconfigure(3, weight=1)

        # 2.1.1.0) Create a label for the "Laser Controller Connection" frame
        self.label_connection_group = ctk.CTkLabel(master=self.connection_group, text="Laser Controller Connection",
                                                   font=group_label_font)
        self.label_connection_group.grid(row=0, column=0, columnspan=4, padx=10, pady=0, sticky="n")

        # 2.1.1.1.0) Create and place the "IP Address" label and entry widget in the "Laser Controller Connection" frame
        self.label_ip = ctk.CTkLabel(master=self.connection_group, text="IP Address:", font=bold_font)
        self.label_ip.grid(row=1, column=0, padx=[10, 0], pady=0, sticky="n")

        # 2.1.1.1.1) Create and place the "IP Address" combobox widget in the "Laser Controller Connection" frame
        # if self.connection_list equals to self.ip_list then select_list_justify_dir = "right", else "left"
        if self.connection_list == self.ip_list:
            select_list_justify_dir = "right"
        else:
            select_list_justify_dir = "left"

        self.combobox_ip = ctk.CTkComboBox(master=self.connection_group, width=140, justify=select_list_justify_dir, values=self.connection_list)

        self.combobox_ip.grid(row=1, column=1, padx=[5, 5], pady=0, sticky="ne")

        # 2.1.1.1.2) Create and place the "Connect" button in the "Laser Controller Connection" frame
        self.button_connect = ctk.CTkButton(master=self.connection_group, text="Connect", width=90)
        self.button_connect.grid(row=1, column=2, padx=[0, 5], pady=[0, 10], sticky="n")

        # 2.1.1.1.3) Create and place the "is_connected" Led in the "Laser Controller Connection" frame
        led = LED(self.connection_group, size=16, color="green")
        led.grid(row=1, column=3, padx=[0, 10], pady=[2, 8], sticky="n")
        led.on()

        # ===================== 2.1.1) Details=========================================================================
        # 2.1.2) Create Frame container for "Details" widgets
        self.details_group = ctk.CTkFrame(master=self.frame_uut)
        # 2.1.2) Place the frame in the 3rd column of the grid layout
        self.details_group.grid(row=0, column=2, padx=(5, 5), pady=(5, 5), sticky="nsew")

        # 2.1.2) Create grid layout for the "Details" frame with 3 rows and 4 columns
        self.details_group.grid_rowconfigure((0, 1, 2), weight=1)
        # self.details_group.grid_rowconfigure(1, weight=1)
        # self.details_group.grid_rowconfigure(2, weight=1)
        self.details_group.grid_columnconfigure((0, 1, 2, 3), weight=1)
        # self.details_group.grid_columnconfigure(1, weight=1)
        # self.details_group.grid_columnconfigure(2, weight=1)
        # self.details_group.grid_columnconfigure(3, weight=1)

        # 2.1.2.0) Create a label for the "Details" frame
        self.label_details_group = ctk.CTkLabel(master=self.details_group, text="Details", font=group_label_font)
        self.label_details_group.grid(row=0, column=0, columnspan=4, padx=10, pady=0, sticky="n")

        # 2.1.2.1.0) Create and place the "Controller S/N" label widget in the "Details" frame
        self.label_controller_sn = ctk.CTkLabel(master=self.details_group, text="Controller S/N:", font=bold_font)
        self.label_controller_sn.grid(row=1, column=0, padx=10, pady=0, sticky="nw")

        # 2.1.2.1.1) Create and place the "Controller S/N" value (label widget) in the "Details" frame
        self.label_controller_sn_value = ctk.CTkLabel(master=self.details_group, text="12345")
        self.label_controller_sn_value.grid(row=1, column=1, padx=10, pady=0, sticky="ne")

        # 2.1.2.1.2) Create and place the "Controller FW Ver" label widget in the "Details" frame
        self.label_controller_fw = ctk.CTkLabel(master=self.details_group, text="Controller FW Ver:", font=bold_font)
        self.label_controller_fw.grid(row=1, column=2, padx=10, pady=0, sticky="nw")

        # 2.1.2.1.3) Create and place the "Controller FW Ver" value (label widget) in the "Details" frame
        self.label_controller_fw_value = ctk.CTkLabel(master=self.details_group, text="1.0.0")
        self.label_controller_fw_value.grid(row=1, column=3, padx=10, pady=0, sticky="ne")

        # 2.1.2.2.0) Create and place the "Laser S/N" label widget in the "Details" frame
        self.label_laser_sn = ctk.CTkLabel(master=self.details_group, text="Laser Emitter S/N:", font=bold_font)
        self.label_laser_sn.grid(row=2, column=0, padx=10, pady=0, sticky="nw")

        # 2.1.2.2.1) Create and place the "Laser S/N" value (label widget) in the "Details" frame
        self.label_laser_sn_value = ctk.CTkLabel(master=self.details_group, text="123456789")
        self.label_laser_sn_value.grid(row=2, column=1, padx=10, pady=0, sticky="ne")

        # 2.1.2.2.2) Create and place the "Laser Emitter FW Ver" label widget in the "Details" frame
        self.label_laser_fw = ctk.CTkLabel(master=self.details_group, text="Laser Emitter FW Ver:", font=bold_font)
        self.label_laser_fw.grid(row=2, column=2, padx=10, pady=0, sticky="nw")

        # 2.1.2.2.3) Create and place the "Laser Emitter FW Ver" value (label widget) in the "Details" frame
        self.label_laser_fw_value = ctk.CTkLabel(master=self.details_group, text="1.0.0")
        self.label_laser_fw_value.grid(row=2, column=3, padx=10, pady=0, sticky="ne")

