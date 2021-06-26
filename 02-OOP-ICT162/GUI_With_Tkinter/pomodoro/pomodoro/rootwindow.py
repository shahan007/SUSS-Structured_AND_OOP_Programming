import tkinter as tk
from tkinter import ttk
from pomodoro.mainframe import MainFrame
from pomodoro.settingsframe import SettingFrame

class RootWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Pomodoro')
        self.geometry('250x250')
        self.style = ttk.Style(self)                
        self.style.theme_use('clam')
        self.style.configure('me.TFrame', bordercolor='red',
                             borderwidth=20, relief='ridge')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.create_frames()
        self.place_frames()

    @property
    def mainFrame(self):
        return self.__mainFrame

    @property
    def settingFrame(self):
        return self.__settingFrame

    def create_frames(self):
        self.__mainFrame = MainFrame(self)
        self.__settingFrame = SettingFrame(self)

    def place_frames(self):
        self.__mainFrame.grid(row=0, column=0,
                              sticky='NSEW')
        self.__settingFrame.grid(row=0, column=0, sticky='NSEW')
        self.__mainFrame.tkraise()

    def switch_frames(self, frame):
        frame.tkraise()

if __name__ == '__main__':
    rw = RootWindow()
    rw.mainloop()
