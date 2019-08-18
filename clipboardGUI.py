import Tkinter as tk # use tkinter instead of Tkinter for python3
from Tkinter import *
import pyautogui as pya

# GUI using Tkinter

def clipboardNotFoundGUI():
    msg = "Word Not Found"
    pya.alert(msg, "My Dictionary")

def clipboardGUI(msg):
    def on_configure(event):
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        canvas.configure(scrollregion=canvas.bbox('all'))

    root = tk.Tk()
    root.title("My Dictionary")
    # --- create canvas with scrollbar ---
    root.geometry("500x700+"+str(root.winfo_screenwidth()/2)+"+"+str(root.winfo_screenheight()/2))
    canvas = tk.Canvas(root,width=490, height=690)
    # canvas.pack(side=tk.LEFT)
    canvas.grid(row=0, column=0)

    scrollbary = tk.Scrollbar(root, command=canvas.yview)
    # scrollbary.pack(side=tk.LEFT, fill='y')
    scrollbary.grid(row=0, column=1, sticky="ns")

    scrollbarx = tk.Scrollbar(root, orient = tk.HORIZONTAL, command=canvas.xview)
    # scrollbarx.pack(side=tk.RIGHT, fill='x')
    scrollbarx.grid(row=1, column=0, sticky="ew")

    canvas.configure(xscrollcommand = scrollbarx.set, yscrollcommand = scrollbary.set)

    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.bind('<Configure>', on_configure)
    root.bind_all('<MouseWheel>', lambda event: root.yview_scroll(int(-1*(event.delta/120)), "units"))
    root.bind_all('<Shift-MouseWheel>', lambda event: root.xview_scroll(int((event.delta/120)), "units"))
    # --- put frame in canvas ---

    frame = tk.Frame(canvas)
    canvas.create_window((0,0), window=frame, anchor='nw')

    # --- add widgets in frame ---

    l = tk.Label(frame, text=msg, font=("Helvetica", 11), anchor='nw', justify=LEFT)
    l.pack()

    def close_window(): 
        root.destroy()

    button = tk.Button(frame, text = "Ok", command = close_window)
    button.pack(side="left", padx=100, pady=4)


    root.bind('<Return>', (lambda e, button=button: button.invoke())) # invoke return as close window by calling close_window of button
    root.mainloop()