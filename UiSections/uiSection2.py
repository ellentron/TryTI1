import tkinter as tk
from tkinter import ttk, font
import customtkinter as ctk


class UiSect2(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)

        # 2) Create a Grid Layout that contains 2 rows and 1 column (1st title, 2nd --> 3 frames ).
        self.grid_rowconfigure(0, weight=1)     # 2.0) Title
        self.grid_rowconfigure(1, weight=111)   # 2.1) 3 frames (Laser Brand radio buttons, Connection, and Details)

        # 2.0) Create a label for top frame of section 2 header and place it in the 1st row of the grid layout
        self.lbl_uut = ctk.CTkLabel(self, text="Unit Under Test")
        self.lbl_uut.grid(row=0, column=0, sticky="nsew", padx=(10, 0))

        # 2.1) Create a frame for holding 3 frames -
        # 2.1.0) Laser Brand radio buttons,
        # 2.1.1) Laser Controller Connection, and Details),
        # 2.1.2) Details and set grid layout to 1 row and 3 columns
        self.frame_uut = ctk.CTkFrame(self)                     # 2.1)
        # Place the frame in the 2nd row of the grid layout
        self.frame_uut.grid(row=1, column=0, sticky="nsew")

        self.frame_uut.grid_rowconfigure(0, weight=1)
        self.frame_uut.grid_columnconfigure(0, weight=1)
        self.frame_uut.grid_columnconfigure(1, weight=1)
        self.frame_uut.grid_columnconfigure(2, weight=1)

        # 2.1.0) Create frame for the radio button group
        self.frame_radio_group = ctk.CTkFrame(master=self.frame_uut)
        # 2.1.0) Place the frame in the 1st column of the grid layout
        self.frame_radio_group.grid(row=0, column=0, padx=(1, 1), pady=(1, 1), sticky="new")
        self.frame_radio_group.configure(height=10, width=20)

        # 2.1.0) Create grid layout for the radio button group frame with 4 rows and 1 column
        self.frame_radio_group.grid_rowconfigure(0, weight=1)
        self.frame_radio_group.grid_rowconfigure(1, weight=1)
        self.frame_radio_group.grid_rowconfigure(2, weight=1)
        self.frame_radio_group.grid_rowconfigure(3, weight=1)
        self.frame_radio_group.grid_columnconfigure(0, weight=1)

        self.radio_var = tk.IntVar(value=0)     # Variable to hold the value of the selected radio button

        # Create a label for the radio button group
        self.label_radio_group = ctk.CTkLabel(master=self.frame_radio_group, text="Laser Brand:")
        self.label_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=2, sticky="n")

        # Create and place the radio buttons in the radio button group frame
        self.radio_button_1 = ctk.CTkRadioButton(master=self.frame_radio_group, variable=self.radio_var, value=0, text="Toptica 405")
        self.radio_button_1.grid(row=1, column=0, pady=2, padx=20,  sticky="n")

        self.radio_button_2 = ctk.CTkRadioButton(master=self.frame_radio_group, variable=self.radio_var, value=1, text="Cobolt 457")
        self.radio_button_2.grid(row=2, column=0, pady=2, padx=20, sticky="n")

        self.radio_button_3 = ctk.CTkRadioButton(master=self.frame_radio_group, variable=self.radio_var, value=2, text="Cobolt 532")
        self.radio_button_3.grid(row=3, column=0, pady=2, padx=20, sticky="n")









        # # Create radiobutton frame with grid layout that contains 4 rows and 1 column and place it in the 1st column
        # self.radiobutton_frame = ctk.CTkFrame(self.frame_uut)
        # self.radiobutton_frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        #
        # # Variable to hold the value of the selected radio button

        # Create frame for the radio button group
        # self.frame_radio_group = ctk.CTkFrame(master=self.frame_uut)
        # self.frame_radio_group.grid(row=0, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")



        # Create a label for the radio button group
        # self.label_radio_group = ctk.CTkLabel(master=self.frame_uut, text="Laser Brand:")
        # self.label_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="n")




        #
        # # create radiobutton frame
        # self.radiobutton_frame = ctk.CTkFrame(self)
        # self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        # self.radio_var = tk.IntVar(value=0)
        # self.label_radio_group = ctk.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
        # self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        # self.radio_button_1 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        # self.radio_button_2 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        # self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        # self.radio_button_3 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        # self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        #
        # # in the 2nd row frame, create a grid layout that contains 1 row and 3 columns
        # self.frame_uut.grid_rowconfigure(0, weight=1)
        # self.frame_uut.grid_columnconfigure(0, weight=1)
        # self.frame_uut.grid_columnconfigure(1, weight=1)
        # self.frame_uut.grid_columnconfigure(2, weight=1)

        # Create LabelFrame as the container for Laser Selection radio buttons, in the 1st column of the 2nd row frame.
        # frm_laser = tk.LabelFrame(frame_uut, text="Laser Brand")
        # self.frm_laser = ctk.CTkFrame(self.frame_uut)
        # self.frm_laser.grid(row=0, column=0, sticky="new")

        # # Create 3 radio buttons in the Laser Selection LabelFrame, only ony can be selected at a time
        # self.laser_var = tk.IntVar()
        # self.laser_var.set(1)
        # radiobtn_laser1 = ctk.CTkRadioButton(self.frm_laser, text="Toptica 405", variable=self.laser_var, value=1)
        # radiobtn_laser1.pack(fill="both", expand=True)
        # radiobtn_laser2 = ctk.CTkRadioButton(self.frm_laser, text="Cobolt 457", variable=self.laser_var, value=2)
        # radiobtn_laser2.pack(fill="both", expand=True)
        # radiobtn_laser3 = ctk.CTkRadioButton(self.frm_laser, text="Cobolt 532", variable=self.laser_var, value=3)
        # radiobtn_laser3.pack(fill="both", expand=True)

        # # Create LabelFrame as container for "Laser Controller Connection" widgets, in the 2nd column of the 2nd row.
        # frm_laser_conn = tk.LabelFrame(self.frame_uut, text="Laser Controller Connection")
        # frm_laser_conn.grid(row=0, column=1, sticky="new")
        #
        #
        # # Add label "IP Address" to the "Laser Controller Connection" LabelFrame
        # lbl_ip = ttk.Label(frm_laser_conn, text="IP Address:")
        # lbl_ip.grid(row=0, column=0, sticky="w", padx=(10, 0))
        #
        # # Add entry widget for IP Address
        # self.ent_ip = ttk.Entry(frm_laser_conn, width=15)
        # self.ent_ip.grid(row=0, column=1, sticky="w", padx=(10, 0))
        #
        # # Add Button to connect to laser controller with same height as the entry widget
        # btn_connect = ttk.Button(frm_laser_conn, text="Connect")
        # btn_connect.grid(row=0, column=2, sticky="w", padx=(10, 0))
        #
        #
        # # Add circular led to indicate laser controller connection status
        # self.led = ttk.Label(frm_laser_conn, text="●", foreground="red")
        # self.led.grid(row=0, column=3, sticky="w", padx=(10, 0))



