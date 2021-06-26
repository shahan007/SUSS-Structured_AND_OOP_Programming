from tkinter import ttk

class SettingFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)
        self.__container = container

        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        self.__gobackBtn = ttk.Button(
            self, text='<- Go back', command=self.go_back)

    def place_widgets(self):
        self.__gobackBtn.grid(row=0, column=0)

    def go_back(self):
        self.__container.title('Pomodoro')
        self.__container.switch_frames(self.__container.mainFrame)