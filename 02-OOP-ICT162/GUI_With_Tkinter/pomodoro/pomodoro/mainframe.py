import tkinter as tk
from tkinter import ttk

class MainFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)
        self.__container = container
        self.rowconfigure((0, 2), weight=1)
        self.rowconfigure(1, weight=2)
        self.columnconfigure((0, 1), weight=1)
        
        self.__pomodoro = [0, 1, 0, 2]
        self.__pomodoroMapping = {0:['25:00','Pomodoro'],
                                  1: ['03:30', 'Short Break'],
                                  2:['10:30','Long Break']}
        self.__index = -1
        self.__currentStatus = None
        self.create_widgets()
        self.place_widgets()
        self.rotate_status()

    @property
    def root(self):
        return self.__container

    @property
    def timeHolder(self):
        return self.__timeHolder

    def reset_index(self):
        self.__index = -1

    @property
    def pomodoroMapping(self):
        return self.__pomodoroMapping
    
    @property
    def buttonFrame(self):
        return self.__buttonFrame

    def create_widgets(self):
        self.__headerFrame = HeaderFrame(self)  # add padding for frames
        self.__title = ttk.Label(self)
        self.__timeHolder = tk.StringVar(self)
        self.__timerLabel = ttk.Label(self, textvariable=self.__timeHolder)
        self.__buttonFrame = ButtonFrame(self)

    def place_widgets(self):
        self.__headerFrame.grid(row=0, column=0, columnspan=2, sticky='NSEW')
        self.__title.grid(row=1, column=0)
        self.__timerLabel.grid(row=1, column=1)
        self.__buttonFrame.grid(row=2, column=0, columnspan=2, sticky='NSEW')

    def rotate_status(self):
        self.__index = (self.__index + 1) % len(self.__pomodoro)
        self.__currentStatus = self.__pomodoro[self.__index]
        self.__title.config(
            text=f'{self.__pomodoroMapping[self.__currentStatus][1]}')
        self.__timeHolder.set(
            value=self.__pomodoroMapping[self.__currentStatus][0])


class HeaderFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)
        self.__container = container
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.config(style='me.TFrame')

        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        self.__title = ttk.Label(self, text='Pomodoro Timer !')
        self.__settingBtn = ttk.Button(self, text='Setting',
                                       command=self.update_settings)

    def place_widgets(self):
        self.__title.grid(row=0, column=0)
        self.__settingBtn.grid(row=0, column=2)

    def update_settings(self):
        self.__container.root.title('Settings')
        self.__container.root.geometry('400x300')
        self.__container.root.resizable(False,False)
        self.__container.root.switch_frames(self.__container.root.settingFrame)


class ButtonFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)
        self.__container = container
        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure(0, weight=1)
        self.config(style='me.TFrame')
        self.create_widgets()
        self.place_widgets()
        self.__id = None

    def create_widgets(self):
        self.__startBtn = ttk.Button(self, text='Start',
                                     command=self.start_timer)
        self.__pauseBtn = ttk.Button(
            self, text='Pause', command=self.pause_timer)
        self.__resetBtn = ttk.Button(self, text='Reset',
                                     command=self.reset_timer)

    def place_widgets(self):
        self.__startBtn.grid(row=0, column=0, sticky='E')
        self.__pauseBtn.grid(row=0, column=1)
        self.__resetBtn.grid(row=0, column=2, sticky='W')

    def start_timer(self):
        timer = self.__container.timeHolder
        minutes, seconds = map(lambda v: int(v), timer.get().split(':'))
        if (minutes + seconds) != 0:
            if seconds > 0:
                seconds -= 1
            else:
                seconds = 59
                minutes -= 1
            timer.set(value=f"{minutes:02d}:{seconds:02d}")
            self.__id = self.after(1000, self.start_timer)
        else:
            self.__container.rotate_status()
            self.__id = self.after(1000, self.start_timer)

    def pause_timer(self):
        self.after_cancel(self.__id)

    def reset_timer(self):
        if self.__id:
            self.pause_timer()
        self.__container.reset_index()
        self.__container.rotate_status()
