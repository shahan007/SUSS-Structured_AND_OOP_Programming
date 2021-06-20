import tkinter as tk
from tkinter import ttk

def set_dpi(level=1):

    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(level)
    except:
        pass


def convertToFeet(meterHolder, feetHolder,answer):
    try:
        value = float(meterHolder.get().strip())
        feet  = round(328084 * value,2)
        color = 'green'
        
    except:
        feet = 'Invalid Input'
        color= 'red' 
    finally:        
        feetHolder.set(feet)        
        answer.configure(foreground = color)

def main():
    
    #---window config---
    set_dpi()    
    win = tk.Tk()
    win.geometry('250x250')
    win.resizable(False,False)
    win.title('Convert Meter to Feet!')
    win.columnconfigure((0,1),weight=1)    
    
    #---Creation---
    title = ttk.Label(win,text='Convert Meter to Feet!')
    #meter
    meterLabel = ttk.Label(win,text='Meter: ',padding=5,width=5,
                           background='blue',foreground='white')
    meterHolder= tk.StringVar(win,value=0)
    meterInput = ttk.Entry(win, width=6, textvariable=meterHolder)
    #feet
    feetLabel = ttk.Label(win, text='Feet: ', padding=5, width=5,
                          background='green', foreground='white')
    feetHolder = tk.StringVar(win,value=0)    
    answer     = ttk.Label(win,textvariable=feetHolder)    
    #btn
    calculateBtn = ttk.Button(win, text='Calculate',padding=2,
                              command=lambda: convertToFeet(meterHolder,feetHolder,answer))    
    
    #---binding events---
    #enter key event binding
    meterInput.bind('<Return>', lambda event: convertToFeet(
        meterHolder, feetHolder, answer))
    
    #---Placing----    
    title.grid(row=0,column= 0,columnspan=2) #columnspan allows us to occup the columns in the grid
    meterLabel.grid(row=1,column=0,sticky='W')
    meterInput.grid(row=1,column=1,sticky='EW')
    meterInput.focus()
    feetLabel.grid(row=2, column=0, sticky='W')
    answer.grid(row=2,column=1,sticky='EW')
    calculateBtn.grid(row=3,column = 0,columnspan=2) 
    
    for i, child in enumerate(win.winfo_children()):
        child.grid_configure(pady=10)
        if i == 0:
            continue
        elif i % 2 !=0 :
            child.grid_configure(padx=(25,0)) #helps to configure        
        else:
            child.grid_configure(padx=(0, 25))  # helps to configure
            
    win.mainloop()

if __name__ == "__main__":
    main()