import tkinter
import tkinter.ttk as ttk

from UiSections.uiSection1 import UiSect1
from UiSections.uiSection2 import UiSect2


# Create the main window
root = tkinter.Tk()
# Set the title of the main window
root.title("Laser Testing Utility - LTU")

# Set the size of the main window
root.geometry("960x800")
root.maxsize(960, 800)
root.minsize(700, 500)

# Create main app gui frame, set size to 960x800
frm = ttk.Frame(root, height=800, width=960, padding="3 3 3 3")
frm.pack(fill="both", expand=True)

# Create a Grid Layout that contains 4 rows and 1 column.
frm.grid_rowconfigure(0, weight=1)
frm.grid_rowconfigure(1, weight=100)
frm.grid_rowconfigure(2, weight=100)
frm.grid_rowconfigure(3, weight=100)
frm.grid_columnconfigure(0, weight=1)

# frm.rowconfigure(0, minsize=20)

# Create a ttk style object for the frame
frame_style = ttk.Style()
frame_style.theme_use("clam")
frame_style.configure("TFrame", background="lightgray")

# Create GUI section 1
sect1 = UiSect1(frm, sw_name="Laser Test Utility - LTU", sw_ver="Ver: 0.0.0", spec_ver="Spec: 0.0.0")
sect1.grid(row=0, column=0, sticky="nsew")

# Create GUI section 2
sect2 = UiSect2(frm)
#sect2 = tkinter.LabelFrame(frm, text="", padx=20, pady=20)
sect2.grid(row=1, column=0, sticky="nsew")

sect3 = tkinter.LabelFrame(frm , text="", padx=20, pady=20)
sect4 = tkinter.LabelFrame(frm, text="", padx=20, pady=20)

# Add the frames to the grid layout


sect3.grid(row=2, column=0, sticky="nsew")
sect4.grid(row=3, column=0, sticky="nsew")



lbl3 = tkinter.Label(sect3, text="Section 3")
lbl3.pack()
btn3 = tkinter.Button(sect3, text="Button 3")
btn3.pack()

lbl4 = tkinter.Label(sect4, text="Section 4")
lbl4.pack()
btn4 = tkinter.Button(sect4, text="Button 4")
btn4.pack()

# Display the window
root.mainloop()