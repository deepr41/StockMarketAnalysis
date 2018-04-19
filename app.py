import tkinter
from Window.utilities import *
#initializations
window = tkinter.Tk()
window.geometry("1000x600")
window.title("Stock Market Analysis")

#add elements
quitButton = tkinter.Button(window, text="Exit",command = myQuit)
quitButton.pack()

#run event loop
window.mainloop()
