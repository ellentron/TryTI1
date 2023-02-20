import customtkinter as ctk
# from UiSections.uiButtons import StartButton
from UiSections.uiIconButton import IconButton


class UiRunControl(ctk.CTkFrame):
    # Class for RunControl frame
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
        self.measurement_time_label = ctk.CTkLabel(self.run_control_frame, text="Measurement Time [Hours]:",
                                                   font=bold_font)
        self.measurement_time_label.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=(10, 10))

        # Create entry for measurement time. Default text = "24"
        self.measurement_time_entry = ctk.CTkEntry(self.run_control_frame, width=55, justify="center")
        self.measurement_time_entry.insert(0, '24')
        self.measurement_time_entry.grid(row=0, column=1, sticky="w", padx=(10, 0), pady=(10, 10))

        # Create frame for the Start and Stop buttons, width=10
        self.start_stop_frame = ctk.CTkFrame(self.run_control_frame)
        self.start_stop_frame.grid(row=0, column=2, columnspan=1, sticky="nsew", padx=(0, 0), pady=(5, 5))

        # create grid layout for the start_stop_frame - 1 rows, 2 columns
        self.start_stop_frame.grid_rowconfigure(index=0, weight=1)
        self.start_stop_frame.grid_columnconfigure(index=0, weight=1)
        self.start_stop_frame.grid_columnconfigure(index=1, weight=1)

        def on_start_button_click(event):
            if self.start_button.state == 'normal':
                print("Start button was clicked!")
                self.start_button.configure(state='disabled')
                self.stop_button.configure(state='normal')
                self.stop_button.update_button()
                self.start_button.update_button()

        def on_stop_button_click(event):
            if self.stop_button.state == 'normal':
                print("Stop button was clicked!")
                self.stop_button.configure(state='disabled')
                self.start_button.configure(state='normal')
                self.start_button.update_button()
                self.stop_button.update_button()

        # self.start_button = StartButton(master=self.start_stop_frame, text="", state='normal')
        self.start_button = IconButton(master=self.start_stop_frame,
                                       state='normal', width=40, height=40,
                                       icon_file="images/PlayCircle.png",
                                       text="", bg_color='#3A7EBF'
                                       )
        self.start_button.bind("<Button-1>", on_start_button_click)
        self.start_button.grid(row=0, column=0, sticky="nsew", padx=(0, 0), pady=(0, 0))

        # Create Stop button
        self.stop_button = IconButton(master=self.start_stop_frame,
                                      state='disabled', width=40, height=40,
                                      icon_file="images/StopCircle.png",
                                      # text="", bg_color=(255,0,255,255)
                                      text="", bg_color='#3A7EBF'
                                      )
        self.stop_button.bind("<Button-1>", on_stop_button_click)
        self.stop_button.grid(row=0, column=1, sticky="nsew", padx=(0, 0), pady=(0, 0))

        self.time_info = "Time left: 10:00:00. Time elapsed: 14:00:00 of 24:00:00 hours"
        # Create label for time information
        self.time_info_label = ctk.CTkLabel(self.run_control_frame, text=self.time_info)
        self.time_info_label.grid(row=1, column=0, columnspan=5, sticky="sew", padx=(0, 0), pady=(0, 0))

        # Create label "Progress:"
        self.progress_label = ctk.CTkLabel(self.run_control_frame, text="Progress:", font=bold_font)
        self.progress_label.grid(row=2, column=0, sticky="nse", padx=(0, 10), pady=(10, 10))

        # Create progress bar
        self.progress_bar = ctk.CTkProgressBar(self.run_control_frame)
        self.progress_bar.grid(row=2, column=1, columnspan=3, sticky="nsew", padx=(0, 0), pady=(22, 22))

        # Create label "50%"
        self.progress_label = ctk.CTkLabel(self.run_control_frame, text="50%")
        self.progress_label.grid(row=2, column=4, sticky="nse", padx=(5, 10), pady=(0, 0))
