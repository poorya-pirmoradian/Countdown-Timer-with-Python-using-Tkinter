import tkinter as tk
from tkinter import messagebox

# Definning class:
class Application(tk.Frame):
    def __init__(self, window=None):
        super().__init__(window)

        # Defining hour, minute and second changer labels: 
        self.lbl_hour_changer = tk.Label(
            self,
            text= 0,
            font=('Arial', 25),
            bg='#ffffff',
            borderwidth=2,
            relief='solid',
            width=3,
        )
        self.lbl_minute_changer = tk.Label(
            self,
            text= 0,
            font=('Arial', 25),
            bg='#ffffff',
            borderwidth=2,
            relief='solid',
            width=3,
        )
        self.lbl_second_changer = tk.Label(
            self,
            text= 0,
            font=('Arial', 25),
            bg='#ffffff',
            borderwidth=2,
            relief='solid',
            width=3,
        )
        
        # Defining attributes:
        self.window= window
        self.update_time = ''
        self.running = False
        self.hours = self.lbl_hour_changer['text']
        self.minutes = self.lbl_minute_changer['text']
        self.seconds = self.lbl_second_changer['text']
        self.new_hours = 0
        self.new_minutes = 0
        self.new_seconds = 0
        self.grid()
        self.create_widget()

    # Definning arrows functions:    
    def encrease_hour(self):
        if self.lbl_hour_changer['text'] < 999:
            self.lbl_hour_changer['text'] += 1
            self.new_hours = self.lbl_hour_changer['text']
            self.all_sec()
    def decrease_hour(self):
        if self.lbl_hour_changer['text'] > 0:
            self.lbl_hour_changer['text'] -= 1
            self.new_hours = self.lbl_hour_changer['text']
            self.all_sec()
    def encrease_minute(self):
        if self.lbl_minute_changer['text'] < 59:
            self.lbl_minute_changer['text'] += 1
            self.new_minutes = self.lbl_minute_changer['text']
            self.all_sec()
    def decrease_minute(self):
        if self.lbl_minute_changer['text'] > 0:
            self.lbl_minute_changer['text'] -= 1
            self.new_minutes = self.lbl_minute_changer['text']
            self.all_sec()
    def encrease_second(self):
        if self.lbl_second_changer['text'] < 59:
            self.lbl_second_changer['text'] += 1
            self.new_seconds = self.lbl_second_changer['text']
            self.all_sec()
    def decrease_second(self):
        if self.lbl_second_changer['text'] > 0:
            self.lbl_second_changer['text'] -= 1
            self.new_seconds = self.lbl_second_changer['text']
            self.all_sec()

    # Defining a function to convert the selected time duration to just seconds:
    def all_sec(self):    
        self.all_seconds = self.new_hours*3600 + self.new_minutes*60 + self.new_seconds

    # Definning app buttons and labels:
    def create_widget(self):

        # Defining main label:
        self.lbl_stopwatch = tk.Label(
            self,
            text= "00 : 00 : 00",
            font=('Arial', 60),
            width=8,
            bg='#ffffff',
            borderwidth=4,
            relief='solid',
        )

        # Defining HH MM SS labels:
        self.lbl_hour = tk.Label(
            self,
            text= 'HH',
            font=('Arial', 20),
        )
        self.lbl_minute = tk.Label(
            self,
            text= 'MM',
            font=('Arial', 20),
        )
        self.lbl_second = tk.Label(
            self,
            text= 'SS',
            font=('Arial', 20),
        )

        # Defining start, stop and reset buttons:
        self.btn_start = tk.Button(
            self,
            text= '     ▶️',
            width=5,
            height=2,
            fg='#000000',
            bg='#e7f320',
            command=self.start,
        )
        self.btn_stop = tk.Button(
            self,
            text= '⏹',
            width=5,
            height=2,
            command=self.stop,
            fg='#ffffff',
            bg='#52aa12'
        )
        self.btn_reset = tk.Button(
            self,
            text='⟲',
            width=5,
            height=2,
            fg='#ffffff',
            bg='#aa3712',
            command=self.reset,
        )

        # Defining arrow buttons:
        self.btn_hour_up = tk.Button(
            self,
            text= '▲',
            fg='#ffffff',
            bg='#696969',
            width=4,
            height=2,
            command= self.encrease_hour
        )
        self.btn_hour_down = tk.Button(
            self,
            text= '▼',
            fg='#ffffff',
            bg='#696969',
            width=4,
            height=2,
            command= self.decrease_hour
        )
        self.btn_minute_up = tk.Button(
            self,
            text= '▲',
            width=4,
            height=2,
            fg='#ffffff',
            bg='#696969',
            command= self.encrease_minute
        )
        self.btn_minute_down = tk.Button(
            self,
            text= '▼',
            fg='#ffffff',
            bg='#696969',
            width=4,
            height=2,
            command= self.decrease_minute
        )
        self.btn_second_up = tk.Button(
            self,
            text= '▲',
            width=4,
            height=2,
            fg='#ffffff',
            bg='#696969',
            command= self.encrease_second
        )
        self.btn_second_down = tk.Button(
            self,
            text= '▼',
            width=4,
            height=2,
            fg='#ffffff',
            bg='#696969',
            command= self.decrease_second
        )

        # Showing app buttons:
            #Showing Main Label:
        self.lbl_stopwatch.grid(row=0,column=0,columnspan=6,sticky='nswe',padx=5,pady=5)
 
            #Showing arrow buttons:
        self.btn_hour_up.grid(row=2, column=1,sticky='nswe',padx=10,pady=6)
        self.btn_hour_down.grid(row=3, column=1,sticky='nswe',padx=10,pady=6)     
        self.btn_minute_up.grid(row=2, column=3,sticky='nswe',padx=10,pady=6)
        self.btn_minute_down.grid(row=3, column=3,sticky='nswe',padx=10,pady=6)
        self.btn_second_up.grid(row=2, column=5,sticky='nswe',padx=10,pady=6)
        self.btn_second_down.grid(row=3, column=5,sticky='nswe',padx=10,pady=6)

            #Showing hour, minute and second changer labels: 
        self.lbl_hour_changer.grid(row=2,rowspan=2, column=0,sticky='nswe',padx=10,pady=6)
        self.lbl_minute_changer.grid(row=2,rowspan=2, column=2,sticky='nswe',padx=10,pady=6)
        self.lbl_second_changer.grid(row=2,rowspan=2, column=4,sticky='nswe',padx=10,pady=6)

            #Showing HH MM SS main labels:
        self.lbl_hour.grid(row=1, column=0,sticky='we')
        self.lbl_minute.grid(row=1, column=2,sticky='we')
        self.lbl_second.grid(row=1, column=4,sticky='we')

            #Showing start, stop and reset buttons:
        self.btn_start.grid(row=4,rowspan=4,column=0,columnspan=2,sticky='nswe',padx=10,pady=6)
        self.btn_stop.grid(row=4,rowspan=4,column=2,columnspan=2,sticky='nswe',padx=10,pady=6)
        self.btn_reset.grid(row=4,rowspan=4,column=4,columnspan=2,sticky='nswe',padx=10,pady=6)

        # Showing app title:
        self.window.title("Countdown Timer")

    # Definning buttons functions:
    def start(self):
        if self.running == False:
            self.lbl_stopwatch.after(1000)
            self.update()
            self.running = True
    def stop(self):
        if self.running == True:
            self.lbl_stopwatch.after_cancel(self.update_time)
            self.running = False
    def reset(self):
        if self.running == True:
            self.running = False
        self.lbl_stopwatch.after_cancel(self.update_time)
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.new_hours = 0
        self.new_minutes = 0
        self.new_seconds = 0
        self.lbl_stopwatch.config(text="00 : 00 : 00")
        self.lbl_hour_changer.config(text=0)
        self.lbl_minute_changer.config(text=0)
        self.lbl_second_changer.config(text=0)
        
    # Definning update functions:
    def update(self):
        if self.all_seconds > 0:
            self.all_seconds -= 1
            self.new_hours = self.all_seconds // 3600
            self.new_min_sec = self.all_seconds % 3600
            self.new_minutes = self.new_min_sec // 60
            self.new_seconds = self.new_min_sec % 60
            self.lbl_stopwatch.config(text=f'{self.new_hours:02} : {self.new_minutes:02} : {self.new_seconds:02}')
            if self.all_seconds == 0:
                messagebox.showinfo("","TIME'S UP")     
        self.update_time = self.lbl_stopwatch.after(1000,self.update)

# Showing app window:
root = tk.Tk()
app = Application(window=root)
app.mainloop()
