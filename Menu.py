from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Catabullet")
window.geometry("500x800")
window.wm_iconbitmap('images\\SpaceshipIcon.ico')

startb = ttk.Button(window)
startb.pack()

window.mainloop() 