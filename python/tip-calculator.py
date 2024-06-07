#Tips per hour calculator

import tkinter
import tkinter.font

class TipsGUI:
    def __init__(self):

        #create main window
        self.main_window = tkinter.Tk()

        #create font object
        myfont = tkinter.font.Font(family='Courier New', size=12, weight='normal')

        #create 3 frames for widgets
        self.top_frame = tkinter.Frame()
        self.hr_frame = tkinter.Frame()
        self.tip_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        #create and pack top frame widgets
        self.label = tkinter.Label(self.top_frame,
                                   text='Tips Per Hour Calculator',
                                   font = myfont)
        self.label.pack()
        
        #create and pack hour widgets
        self.hour_label = tkinter.Label(self.hr_frame,
                                        text='Enter total hours worked:',
                                        font = myfont)
        self.hour_entry = tkinter.Entry(self.hr_frame,
                                        width = 10)
        self.hour_label.pack(side='left')
        self.hour_entry.pack(side='left')
        
        #create and pack tips widgets
        self.tip_label = tkinter.Label(self.tip_frame,
                                       text='Enter total tips earned:',
                                       font = myfont)
        self.tip_entry = tkinter.Entry(self.tip_frame,
                                       width = 10)

        self.tip_label.pack(side='left')
        self.tip_entry.pack(side='left')

        #create middle frame widgets
        self.descr_label = tkinter.Label(self.mid_frame,
                                         text='Tips Per Hour:',
                                         font = myfont)

        #create stringvar object to associate with an output label
        self.value = tkinter.StringVar()

        #create label and associate it with the stringvar object
        self.tph_label = tkinter.Label(self.mid_frame,
                                       textvariable=self.value)

        #pack middle frame widgets
        self.descr_label.pack(side='left')
        self.tph_label.pack(side='left')

        #create button widgets for bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Calculate',
                                          font = myfont,
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          font = myfont,
                                          command=self.main_window.destroy)

        #pack the buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        #pack the frames
        self.top_frame.pack()
        self.hr_frame.pack()
        self.tip_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        #enter tkinter main loop
        tkinter.mainloop()

    #convert method is a callback function for the calculate button
    def convert(self):
        #get value entered by user
        hours = float(self.hour_entry.get())
        tips = float(self.tip_entry.get())

        #calculate tips per hour
        tph = format( tips / hours, '.2f')
        
        #convert tph to a string and store in the stringvar object.
        self.value.set(tph)

#create instance of TipsGUI class
tph_conv = TipsGUI()
