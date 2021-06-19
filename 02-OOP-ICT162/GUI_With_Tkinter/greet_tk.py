import tkinter as tk
from tkinter import ttk

def main():

    #makes it more clearer focuses on dpi resolution
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

    #contains unique set of greeted names
    name_array = set()

    def greet(master, username, name_array):
        """
        Function to greet username that is of atleast length 3
        """
        name = username.get()
        length = len(name_array)

        if name and len(name) > 2:
            name_array.add(name)
            if len(name_array) != length:
                ttk.Label(master, text=f"Hello {username.get()}! ",
                          background='orange', foreground='black'
                          ).pack(pady='5 5')

    def clear(master):
        """
        Clears out the entire frame
        """
        for widget in master.winfo_children():
            widget.destroy()

    #main window
    win = tk.Tk()
    win.columnconfigure(0, weight=1)

    #frame1 contains name and input
    f1 = ttk.Frame(win, padding=(10, 20))
    f1.grid(row=0, column=0)

    #-> frame1 widget creation and placing
    nameHolder = tk.StringVar(f1)
    nameLabel = ttk.Label(f1, text='Name: ')
    nameEntry = ttk.Entry(f1, textvariable=nameHolder)
    nameLabel.grid(row=0, column=0)
    nameEntry.grid(row=0, column=1)

    #frame2 contains buttons
    f2 = ttk.Frame(win, padding=(150, 5))
    f2.grid(row=1, column=0, sticky='EW')
    f2.columnconfigure((0, 1, 2), weight=1)

    #-> frame2 widget creation and placing
    greetBtn = ttk.Button(f2, text='Greet')
    quitBtn = ttk.Button(f2, text='Quit!', command=win.destroy)
    clearBtn = ttk.Button(f2, text='Clear')
    greetBtn.grid(row=0, column=0, sticky='EW')
    quitBtn.grid(row=0, column=1, sticky='EW')
    clearBtn.grid(row=0, column=2, sticky='EW')

    #frame3 contains area for placing greetings
    f3 = ttk.Frame(win, padding=(5, 10))
    f3.grid(row=3, column=0)

    #->config greetBtn and clearBtn of frame 2
    greetBtn.config(command=lambda: greet(f3, nameHolder, name_array))
    clearBtn.config(command=lambda: clear(f3))

    win.mainloop()

if __name__ == '__main__':    
    main()