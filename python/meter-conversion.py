#Meters to feet converter

import tkinter

#create class
class MetersConverterGUI:
    def __init__(self):

        #create main window
        self.main_window = tkinter.Tk()

        #create 3 frames
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        #create and pack top frame
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text='Enter distance in meters:')
        self.meter_entry = tkinter.Entry(self.top_frame,
                                         width=10)
        self.prompt_label.pack(side='left')
        self.meter_entry.pack(side='left')

        #create widgets for middle frame
        self.descr_label = tkinter.Label(self.mid_frame,
                                         text='Converted to Feet:')

        #create stringvar object
        self.value = tkinter.StringVar()

        #create label and asspciate it with stringvar object
        self.meter_label = tkinter.Label(self.mid_frame,
                                         textvariable=self.value)

        #pack mid frame
        self.descr_label.pack(side='left')
        self.meter_label.pack(side='left')

        #create and pack button widgets for bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Convert',
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        #pack frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        #enter tkinter main loop
        tkinter.mainloop()

    #convert method defintion
    def convert(self):
        #get the values entered by user
        meter = float(self.meter_entry.get())

        #convert meters to feet
        feet = format(meter / 0.304, '.2f')

        #convert feet to a string and store in stringvar object
        self.value.set(feet)

#create instance of the MetersConverterGUI class
meter_conv = MetersConverterGUI()