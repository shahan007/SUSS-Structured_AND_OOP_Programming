import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        #sets dpi
        self.set_dpi_awareness()
        #confiure the root window
        self.geometry('250x300')
        self.resizable(False, False)
        self.title('Convert Meter to Feet!')
        self.columnconfigure((0, 1), weight=1)
        #--> Default font
        defaultFont = tkfont.nametofont('TkDefaultFont')
        defaultFont.configure(family="Arial", size=16, weight=tkfont.NORMAL)
        self.__f = 'Meter'
        self.__t = 'Feet'
        self.create_widgets()
        self.bind_events()
        self.place_widgets()

    def create_widgets(self):
        f = self.__f
        t = self.__t
        self.__title = ttk.Label(self, text=f'Convert {f} to {t}!',
                                 font=('Corbel', 18, 'italic bold'))
        #from
        self.__fLabel = ttk.Label(self, text=f'{f}: ', padding=5, width=5,
                                  background='blue', foreground='white')
        self.__fHolder = tk.StringVar(self, value=0.0)
        self.__fInput = ttk.Entry(self, width=6, textvariable=self.__fHolder,
                                  font=("Arial", 16))
        #to
        self.__tLabel = ttk.Label(self, text=f'{t}: ', padding=5, width=5,
                                  background='green', foreground='white')
        self.__tHolder = tk.StringVar(self, value=0.0)
        self.__answer = ttk.Label(self, textvariable=self.__tHolder,
                                  font=("Arial", 16),foreground='green')
        #btns
        self.__calculateBtn = ttk.Button(self, text='Calculate', padding=2,
                                         command=lambda: self.convert())
        self.__switchBtn = ttk.Button(self, text='Switch',
                                      padding=2, command=lambda: self.overWrite(t, f))

    def place_widgets(self):
        self.__title.grid(row=0, column=0, columnspan=2)
        self.__fLabel.grid(row=1, column=0, sticky='W')
        self.__fInput.grid(row=1, column=1, sticky='EW')
        self.__fInput.focus()
        self.__tLabel.grid(row=2, column=0, sticky='W')
        self.__answer.grid(row=2, column=1, sticky='EW')
        self.__calculateBtn.grid(row=3, column=0, columnspan=2)
        self.__switchBtn.grid(row=4, column=0, columnspan=2)

        for i, child in enumerate(self.winfo_children()):
            child.grid_configure(pady=10)
            if i == 0:
                continue
            elif i >= 5:
                break
            elif i % 2 != 0:
                child.grid_configure(padx=(25, 0))  # helps to configure
            else:
                child.grid_configure(padx=(0, 25))  # helps to configure

    def overWrite(self, f, t):
        
        """
        Called when switch button is selected. It updates the Meter and Feet
        """
        
        self.__f = f
        self.__t = t
        self.title(f'Convert {self.__f} to {self.__t}!')
        self.__title.config(text=f'Convert {f} to {t}!')
        self.__fLabel.config(text=f'{f}: ')
        self.__tLabel.config(text=f'{t}: ')        
        self.__fHolder.set(value=0.0)
        self.__tHolder.set(value=0.0)      
        self.__answer.config(foreground='green')
        self.__switchBtn.config(command=lambda: self.overWrite(t, f))

    def convert(self):
        try:
            value = float(self.__fHolder.get().strip())
            if self.__f == 'Meter':
                answer = round(3.28084 * value, 2)

            else:
                answer = round(value / 3.28084, 2)
            color = 'green'
        except:
            answer = 'Invalid Input'
            color = 'red'
        finally:
            self.__tHolder.set(answer)
            self.__answer.configure(foreground=color)

    def bind_events(self):
        self.__fInput.bind('<Return>', lambda event: self.convert())

    def set_dpi_awareness(self, level=1):
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(level)
        except:
            pass

if __name__ == '__main__':
    window = Window()
    window.mainloop()