from tkinter import *


root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()
    def tela(self):
        self.root.title("cadastro de cliente")
        self.root.configure(bg='#708090')
        self.root.geometry('500x250')
        self.root.resizable(True, True)
        self.root.maxsize(width= 500, height= 250)
        self.root.minsize(width=250, height=150)
Application()
