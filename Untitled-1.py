from tkinter import *

menu_inicial = Tk()
menu_inicial.title('primeiro app')

largura = 500
altura = 300

largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenwidth()

posx = largura_screen/4 - largura/4
posy = altura_screen/4 - altura/4

menu_inicial.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

menu_inicial.mainloop()