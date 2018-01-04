# This program converts distances in kilometers to miles. the result is displayed in a info dialog box.

from tkinter import *
import tkinter.messagebox
class KiloConverter:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create two frames to group widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create the widgets for the top frame.
        self.prompt_label = tkinter.Label(self.top_frame, text="Enter a distance in kilometers")
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        # Pack the top frame's widgets.
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        # Create the button widgets for bottom frame.
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the Frame.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # The convert method is callback function for calculate button.
    def convert(self):
        # Get the value entered by the user into the kilo_entry widget.
        kilo = float(self.kilo_entry.get())
        # Convert kilometers to miles
        miles = kilo * 0.6214

        # Display the results in an info dialog box.
        tkinter.messagebox.showinfo('Results', str(kilo) + ' kilometers is equal to ' + str(miles) + 'miles')
# Create an instance pf the KiloConverter class.
kilo_conver = KiloConverter()
