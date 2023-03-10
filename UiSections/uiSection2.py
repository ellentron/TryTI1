import tkinter as tk
# from tkinter import ttk, font
import customtkinter as ctk

from UiSections.uiConnection import UiConnection
from UiSections.uiLed import LED


class UiSect2(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)

        self.radio_var = tk.IntVar(value=0)  # Variable to hold the value of the selected radio button

        self.laser_ip_list = ["10.0.30.1", "10.0.30.20", "10.0.30.80"]
        self.laser_com_list = ["COM3", "COM8", "COM12"]

        if self.radio_var.get() == 0:
            self.connection_list = self.laser_ip_list
            self.connect_to_label = "IP Address:"
            # self.select_list_justify_dir = "right"
        else:
            self.connection_list = self.laser_com_list
            self.connect_to_label = "COM Port:"
            # self.select_list_justify_dir = "left"

        def radiobutton_event():
            # if radio_var is 0: connection_list = ip_list
            # if radio_var is larger than 0: connection_list = serial_list
            if self.radio_var.get() == 0:
                self.connection_list = self.laser_ip_list
                self.connect_to_label = "IP Address:"
            else:
                self.connection_list = self.laser_com_list
                self.connect_to_label = "COM Port:"

            print(f"radiobutton toggled, current value:{self.radio_var.get()}")
            # Update the values and justify option of the combobox
            # self.combobox_ip.configure(values=self.connection_list, justify=self.select_list_justify_dir)
            self.laser_connection.com_port_label.configure(text=self.connect_to_label)

            # self.laser_connection.com_port_label.update_idletasks()
            self.laser_connection.connection_list = self.connection_list
            self.laser_connection.combobox_connection_list.configure(values=self.connection_list)
            self.laser_connection.combobox_connection_list.set(self.connection_list[0])
            self.laser_connection.combobox_connection_list.update_idletasks()


        # self._border_width = 2
        # self._border_color = "white"

        # Create bold font
        bold_font = ctk.CTkFont(size=12, weight="bold")
        group_label_font = ctk.CTkFont(size=14, weight="bold")

        # 2) Create a Grid Layout that contains 2 rows and 1 column (1st title, 2nd --> 3 group frames for UUT).
        self.grid_rowconfigure(0, weight=1)  # 2.0) Title (Unit Under Test)
        self.grid_rowconfigure(1, weight=111)  # 2.1) 3 frames (Laser Brand radio buttons, Connection, and Details)

        # 2.0) Create a label for top frame of section 2 header and place it in the 1st row of the grid layout
        self.lbl_uut = ctk.CTkLabel(self, text="Unit Under Test", font=ctk.CTkFont(size=16, weight="bold"))
        self.lbl_uut.grid(row=0, column=0, sticky="nsw", padx=(15, 0), pady=(1, 1))

        # 2.1) Create a frame for holding 3 frames -
        # 2.1.0) Laser Brand radio buttons,
        # 2.1.1) Laser Controller Connection, and Details),
        # 2.1.2) Details and set grid layout to 1 row and 3 columns
        self.frame_uut = ctk.CTkFrame(self)  # 2.1)
        # Place the frame in the 2nd row of the grid layout
        self.frame_uut.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")

        # 2.1.1) Create grid layout for the frame with 1 row and 3 columns
        self.frame_uut.grid_rowconfigure(0, weight=1)
        self.frame_uut.grid_columnconfigure('all', weight=1)
        # self.frame_uut.grid_columnconfigure(1, weight=1)
        # self.frame_uut.grid_columnconfigure(2, weight=1)

        # ===================== 2.1.0) Laser Brand radio buttons,======================================================
        # 2.1.0) Create frame for the radio buttons group
        self.frame_radio_group = ctk.CTkFrame(master=self.frame_uut)
        # 2.1.0) Place the frame in the 1st column of the grid layout
        self.frame_radio_group.grid(row=0, column=0, padx=(5, 0), pady=(5, 5), sticky="new")

        # 2.1.0) Create grid layout for the radio button group frame with 4 rows and 1 column
        self.frame_radio_group.grid_rowconfigure(index="all", weight=1)
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
        self.radio_button_1.grid(row=1, column=0, pady=2, padx=10, sticky="nw")

        self.radio_button_2 = ctk.CTkRadioButton(master=self.frame_radio_group, variable=self.radio_var,
                                                 value=1, text="Cobolt 457", command=radiobutton_event)
        self.radio_button_2.grid(row=2, column=0, pady=2, padx=10, sticky="nw")

        self.radio_button_3 = ctk.CTkRadioButton(master=self.frame_radio_group, variable=self.radio_var,
                                                 value=2, text="Cobolt 532", command=radiobutton_event)
        self.radio_button_3.grid(row=3, column=0, pady=[2, 10], padx=10, sticky="nw")

        # ===================== 2.1.1) Laser Controller Connection) ===================================================
        # 2.1.1) Create Frame container for "Laser Controller Connection" widgets
        self.connection_group = ctk.CTkFrame(master=self.frame_uut)
        # 2.1.1) Place the frame in the 2nd column of the grid layout
        self.connection_group.grid(row=0, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")

        # 2.1.1) Create UiConnection frame for "Laser Controller Connection"
        self.laser_connection = UiConnection(self.connection_group, connection_title="Laser Controller Connection",
                                             connect_to_label="IP Address:", connection_list=self.connection_list)
        # self.laser_connection.grid(row=220, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.laser_connection.pack(side="top", fill="both", expand=True)


        # ===================== 2.1.1) Details=========================================================================
        # 2.1.2) Create Frame container for "Details" widgets
        self.details_group = ctk.CTkFrame(master=self.frame_uut)
        # 2.1.2) Place the frame in the 3rd column of the grid layout
        self.details_group.grid(row=0, column=2, padx=(0, 5), pady=(5, 5), sticky="nsew")

        # 2.1.2) Create grid layout for the "Details" frame with 3 rows and 4 columns
        self.details_group.grid_rowconfigure(index="all", weight=1)
        # self.details_group.grid_rowconfigure(1, weight=1)
        # self.details_group.grid_rowconfigure(2, weight=1)
        self.details_group.grid_columnconfigure(index="all", weight=1)
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
