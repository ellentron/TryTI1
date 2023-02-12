import tkinter
import customtkinter as ctk
import uiLogger

# import UiLog

from UiSections.uiSection1 import UiSect1
from UiSections.uiSection2 import UiSect2
from UiSections.uiSection3 import UiSect3

print("Starting...")

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Create the main window
root = ctk.CTk()

# Set the title of the main window
root.title("Laser Testing Utility - LTU")

# Set the size of the main window
# root.geometry("960x800")

# Create grid layout for the main window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create main app gui frame, set size to 960x800 with y padding
frm = ctk.CTkFrame(master=root, height=800, width=960)

# set the size of the frame
frm.configure("960x800")
# frm.grid(row=0, column=0, sticky="ew")
frm.pack(padx=10, pady=10)

# Create a Grid Layout that contains 4 rows and 1 column.
frm.grid_rowconfigure(0, weight=1)
frm.grid_rowconfigure(1, weight=1)
frm.grid_rowconfigure(2, weight=1)
frm.grid_rowconfigure(3, weight=1)
frm.grid_columnconfigure(0, weight=1)

# frm.rowconfigure(0, minsize=20)

# Create a ttk style object for the frame
# frame_style = ttk.Style()
# frame_style.theme_use("clam")
# frame_style.configure("TFrame", background="lightgray")

# Create GUI section 1
sect1 = UiSect1(master=frm, sw_name="Laser Test Utility - LTU", sw_ver="Ver: 0.0.0", spec_ver="Spec: 0.0.0")
sect1.grid(row=0, column=0, sticky="new", padx=10, pady=[10,0])

# Create GUI section 2
sect2 = UiSect2(master=frm)
sect2.grid(row=1, column=0, sticky="nsew", padx=10, pady=[0, 0])
# sect2.grid(row=1, column=0, sticky="n")

sect3 = UiSect3(master=frm)
# sect3.grid(row=2, column=0, sticky="nsew", padx=10, pady=[0, 0])
sect3.grid(row=2, column=0, sticky="nsew", padx=10, pady=[0, 0])

# lbl3 = tkinter.Label(sect3, text="Section 3")
# lbl3.pack()
# btn3 = tkinter.Button(sect3, text="Button 3")
# btn3.pack()

ui_log = uiLogger.UiLog(frm)
ui_logger = uiLogger.UiLogger(ui_log.text)
logger = ui_logger.logger

sect4 = uiLogger.UiLog(master=frm)
sect4.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)


logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")

#
# lbl4 = tkinter.Label(sect4, text="Section 4")
# lbl4.pack()
# btn4 = tkinter.Button(sect4, text="Button 4")
# btn4.pack()

# Display the window
root.mainloop()