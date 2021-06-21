import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

class Window(tk.Tk):
    
    def __init__(self):
        super().__init__()
        #sets dpi
        self.set_dpi_awareness()
        #confiure the root window
        self.geometry('250x250')
        self.resizable(False, False)
        self.title('Convert Meter to Feet!')
        self.columnconfigure((0, 1), weight=1)
        #--> Default font
        defaultFont = tkfont.nametofont('TkDefaultFont')
        defaultFont.configure(family="Arial", size=16, weight=tkfont.NORMAL)        
        self.create_widgets()
        self.bind_events()
        self.place_widgets()        

    def create_widgets(self):
        self.__title = ttk.Label(self, text='Convert Meter to Feet!',
                        font=('Corbel', 18, 'italic bold'))
        #meter
        self.__meterLabel = ttk.Label(self, text='Meter: ', padding=5, width=5,
                            background='blue', foreground='white')
        self.__meterHolder= tk.StringVar(self, value=0)
        self.__meterInput = ttk.Entry(self, width=6, textvariable=self.__meterHolder,
                            font=("Arial", 16))
        #feet
        self.__feetLabel  = ttk.Label(self, text='Feet: ', padding=5, width=5,
                            background='green', foreground='white')
        self.__feetHolder = tk.StringVar(self, value=0)
        self.__answer     = ttk.Label(self, textvariable=self.__feetHolder,
                                      font=("Arial", 16))
        #btn
        self.__calculateBtn = ttk.Button(self, text='Calculate', padding=2,
                                command=lambda: self.convertToFeet())

    def place_widgets(self):
        self.__title.grid(row=0, column=0, columnspan=2)
        self.__meterLabel.grid(row=1, column=0, sticky='W')
        self.__meterInput.grid(row=1, column=1, sticky='EW')
        self.__meterInput.focus()
        self.__feetLabel.grid(row=2, column=0, sticky='W')
        self.__answer.grid(row=2, column=1, sticky='EW')
        self.__calculateBtn.grid(row=3, column=0, columnspan=2)

        for i, child in enumerate(self.winfo_children()):
            child.grid_configure(pady=10)
            if i == 0:
                continue
            elif i % 2 != 0:
                child.grid_configure(padx=(25, 0))  # helps to configure
            else:
                child.grid_configure(padx=(0, 25))  # helps to configure
    
    def bind_events(self):        
        self.__meterInput.bind('<Return>', lambda event: self.convertToFeet())

    def convertToFeet(self):
        try:
            value = float(self.__meterHolder.get().strip())
            feet = round(328084 * value, 2)
            color = 'green'
        except:
            feet = 'Invalid Input'
            color = 'red'
        finally:
            self.__feetHolder.set(feet)
            self.__answer.configure(foreground=color)

    def set_dpi_awareness(self,level=1):
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(level)
        except:
            pass

if __name__ == '__main__':
    window = Window()
    window.mainloop()