import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font

co0 = "#444466" #preto
co1 = "#feffff" #branco
co2 = "#6f9fbd" #azul
co3 = "#38576b" #valor
co4 = "#403d3d" #letra
co5 = "#e89613" #laranja

janela = Tk()
janela.title('')
janela.geometry('400x300')
janela.configure(bg=co1)

style = ttk.Style()
style.theme_use('clam')
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=190)


#dividindo a janela

frame_cima = Frame(janela, width=400, height=60, bg=co1, pady=0, padx=0)
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=400, height=300, bg=co1, pady=12, padx=20)
frame_baixo.grid(row=2, column=0, sticky=NW)


#frame cima

app_name = Label(frame_cima, text="Calculadora de bases", relief=FLAT, anchor='center', font=('System 20'), bg=co2, fg=co1)
app_name.place(x=10, y=15)

#frame baixo

bases = ['BINARIO', 'OCTAL', 'DECIMAL', 'HEXADECIMAL']
combo = ttk.Combobox(frame_baixo, width=12, justify=CENTER, font=('Ivy 12 bold'))
combo['values'] = (bases)
combo.place(x=35, y=10)

janela.mainloop()

