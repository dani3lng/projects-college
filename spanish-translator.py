#Spanish Translator

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        #create the main window widget
        self.main_window = tkinter.Tk()

        #create label widget for top frame
        self.label = tkinter.Label(self.main_window,
                                   text='Spanish Translator')

        #create 3 button widget for middle frame
        self.my_button1 = tkinter.Button(self.main_window,
                                        text='Uno',
                                        command=self.do_something1)
        self.my_button2 = tkinter.Button(self.main_window,
                                         text='Dos',
                                         command=self.do_something2)
        self.my_button3 = tkinter.Button(self.main_window,
                                         text='Tres',
                                         command=self.do_something3)
        self.quit_button = tkinter.Button(self.main_window,
                                          text='Quit',
                                          command=self.main_window.destroy)

        #pack the widgets
        self.label.pack()
        self.my_button1.pack()
        self.my_button2.pack()
        self.my_button3.pack()
        self.quit_button.pack()

        #enter the tkinter main loop
        tkinter.mainloop()

    #do_something method callback function
    def do_something1(self):
        #display info dialog box
        tkinter.messagebox.showinfo('English Translation',
                                    'One')
    def do_something2(self):
        tkinter.messagebox.showinfo('English Translation',
                                    'Two')
    def do_something3(self):
        tkinter.messagebox.showinfo('English Translation',
                                    'Three')

#create instance of the MyGUI class
my_gui = MyGUI()
