from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Primeiro app')

menu_inicial.geometry("500x250+200+200")
menu_inicial.resizable(True, True)

#menu_inicial.minsize(width = 500, height = 250)
#menu_inicial.maxsize(700, 400)
#menu_inicial.state('iconic')

def btn():
    print('hello world')

menu_inicial["bg"] = "blue"
btn = Button(menu_inicial, text='execultar', command=btn)
btn.pack()

btn2 = Button(menu_inicial, text='clicar', command=lambda: print('OK'))
btn2.pack()
menu_inicial.mainloop()