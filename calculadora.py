# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk


co0 = "#444466" #preto
co1 = "#feffff" #branco
co2 = "#6f9fbd" #azul
co3 = "#38576b" #valor
co4 = "#403d3d" #letra
co5 = "#e89613" #laranja
cobutton = "#87CEFA" #lightskyblue

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
app_name.place(x=50, y=15)


#funcão para determinacao do numero
def converter():
    def numero_para_decimal(numero, base):
        decimal = int(numero, base)

        binario = bin(decimal)
        octal = oct(decimal)
        hexa = hex(decimal)

        l_binario['text'] = str(binario[2:])
        l_octal['text'] = str(octal[2:])
        l_decimal['text'] = str(decimal)
        l_hexadecimal['text'] = str(hexa[2:].upper())

    numero = e_valor.get()
    base = combo.get()

    #valor da base
    if base == 'BINÁRIO':
        base = 2
    elif base == 'OCTAL':
        base = 8
    elif base == 'DECIMAL':
        base = 10
    else:
        base = 16

    numero_para_decimal(numero, base)

#frame baixo

bases = ['BINÁRIO', 'OCTAL', 'DECIMAL', 'HEXADECIMAL']
combo = ttk.Combobox(frame_baixo, width=12, justify=CENTER, font=('Ivy 12 bold'))
combo['values'] = (bases)
combo.place(x=35, y=10)

e_valor = Entry(frame_baixo, width=9, justify='center', font=("", 13), highlightthickness=1, relief='solid')
e_valor.place(x=160, y=10)

b_converter = Button(frame_baixo, command=converter, text="Calcular", relief=RAISED, overrelief=RIDGE, font=('Ivy 9'), bg=cobutton, fg=co4)
b_converter.place(x=247, y=10)




#=====================resultados=================
#binario
l_binario = Label(frame_baixo, text="BINÁRIO",width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=co5, fg=co1)
l_binario.place(x=35, y=60)
l_binario = Label(frame_baixo, text="",width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=co4)
l_binario.place(x=170, y=60)


#ocatal
l_octal = Label(frame_baixo, text="OCTAL",width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=co5, fg=co1)
l_octal.place(x=35, y=100)
l_octal = Label(frame_baixo, text="",width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=co4)
l_octal.place(x=170, y=100)


#decimal
l_decimal = Label(frame_baixo, text="DECIMAL",width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=co5, fg=co1)
l_decimal.place(x=35, y=140)
l_decimal = Label(frame_baixo, text="",width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=co4)
l_decimal.place(x=170, y=140)


#hexadecimal
l_hexadecimal = Label(frame_baixo, text="HEXADECIMAL",width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=co5, fg=co1)
l_hexadecimal.place(x=35, y=180)
l_hexadecimal = Label(frame_baixo, text="",width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=co4)
l_hexadecimal.place(x=170, y=180)

janela.mainloop()

