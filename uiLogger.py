import logging
import tkinter as tk
import customtkinter as ctk

class UiLogger:
    def __init__(self, log_widget):
        logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')
        self.log_widget = log_widget
        self.logger = logging.getLogger("UiLogger")
        self.logger.setLevel(logging.DEBUG)
        self.handler = LogHandler(self.log_widget)
        self.handler.setLevel(logging.DEBUG)
        self.logger.addHandler(self.handler)


class LogHandler(logging.Handler):
    def __init__(self, log_widget):
        super().__init__()
        self.log_widget = log_widget
    def emit(self, record):
        message = self.format(record)
        self.log_widget.insert("end", message + "\n")

class UiLog(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)

        # Create for this frame a grid layout with 2 row2 and 1 column
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create a CTkLabel widget to display "log" heading and place it in the first row
        self.lbl_log_heading = ctk.CTkLabel(self, text="Log", font=ctk.CTkFont(size=16, weight="bold"))
        self.lbl_log_heading.grid(row=0, column=0, sticky="new", padx=(10, 10), pady=(10, 10))

        # Create a CTkTextBox widget to display log messages and place it in the second row
        self.text = ctk.CTkTextbox(self, height=200, width=50)
        self.text.grid(row=1, column=0, sticky="nsew", padx=(10, 10), pady=(10, 10))
        self.ui_logger = UiLogger(self.text)
