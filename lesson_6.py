# This program demonstraters a Button widgets
# when the user clicks the Button, an info dialog box is displayed.


import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create a Button widget. The text "Click me!"
        # should appear on the face pf the Button. The
        # do_something method should be executed when
        # the user clicks the Buttom.
        self.my_button = tkinter.Button(self.main_window, text="Click me!", command=self.do_something)
        # Create a Button widget. The text "Quit" should appear on the face pf the Button. The quit method
        # should be executed when the user clicks the button "Quit"
        self.my_button1 = tkinter.Button(self.main_window, text="Quit", command=self.quit)


        # Pack the Button.
        self.my_button.pack()
        # Pack the Button1.
        self.my_button1.pack()
        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The do_something method is a callback function
    # for the Button widget.
    def do_something(self):
        # Display an info dialog box.
        tkinter.messagebox.showinfo('Response', 'Thanks for click the button')
    def quit(self):
        self.main_window.destroy()

# Create an instance of the MyGUI class.
my_gui = MyGUI()
