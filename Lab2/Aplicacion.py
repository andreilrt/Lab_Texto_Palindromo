import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import Funciones as Back

##################################################################################
# Configuracion de la raiz 
raiz = Tk()
raiz.title('Lab 2 : Palindromos')
raiz.iconbitmap('./usta.ico')
raiz.geometry('500x500')
raiz.resizable(0,0)
raiz.config(bg='#FFFFFF')
# Variables Globales
colorBotones = '#F54500'
colorFondo = '#FFFFFF'
##################################################################################
# Frame Principal
principal = Frame(raiz)
principal.config(width="500", height="500", bg=colorFondo)
principal.pack()

## Elementos del frame principal
### Textos
textPalindromo = ttk.Label(principal,
                           text='PALINDROMO',
                           background=colorFondo,
                           font=('Calibri', 30, 'bold'))
textPalindromo.place(x=140, y=40)

textIngreso = ttk.Label(principal,
                        text='Ingrese el mensaje palindromo ',
                        background=colorFondo,
                        font=('Calibri', 15, 'bold'))
textIngreso.place(x=120, y=110)
textIngreso2 = ttk.Label(principal,
                        text='Entre 10-20 caracteres, sin caracteres especiales',
                        background=colorFondo,
                        font=('Calibri', 12, 'bold'))
textIngreso2.place(x=88, y=135)
textError = ttk.Label(principal,
                    foreground='#FF0000',
                    font=('Calibri', 16, 'bold'),
                    background=colorFondo
                    )
textError.place_forget()
### Input 
mensaje = Text(principal)
mensaje.config(font=('Calibri', 14, 'bold'), 
            bg='#F59C6B',
            bd=0,
            width=35,
            height=1,
            padx=5,
            pady=15
            )
mensaje.place(x=70, y=170)
### Botones
#### Boton de Calcular
btnCalcular = Canvas(principal)
btnCalcular.config(highlightthickness=0, height=70, bg=colorFondo,)
btnCalcular.create_oval(0,0,200,60,fill=colorBotones,outline=colorBotones)
btnCalcular.create_text(100,30,fill=colorFondo,font="Calibri 16 bold",text="Calcular")
btnCalcular.place(x=140, y=270)
def CambiarResultado(event):
    textMensaje = Back.back(mensaje.get('1.0', 'end-1c'))
    if textMensaje == 1:
        textError.config(text='Error1 : Tamaño del mensaje Invalido')
        textError.place(x=90, y=360)
    elif textMensaje == 2:
        textError.config(text='Error2 : Contiene caracteres Invalidos')
        textError.place(x=90, y=360)
    elif textMensaje == 3:
        textError.config(text='Error3 : No es una frase Palindroma')
        textError.place(x=90, y=360)
    else:
        textR2.config(text=mensaje.get('1.0', 'end-1c'))
        contador = 0
        for x in textMensaje :
            if contador == 0 :
                textRL0.config(text=f'{x} : {textMensaje[x]}')
            if contador == 1 :
                textRL1.config(text=f'{x} : {textMensaje[x]}')
            if contador == 2 :
                textRL2.config(text=f'{x} : {textMensaje[x]}')
            if contador == 3 :
                textRL3.config(text=f'{x} : {textMensaje[x]}')
            if contador == 4 :
                textRL4.config(text=f'{x} : {textMensaje[x]}')
            if contador == 5 :
                textRL5.config(text=f'{x} : {textMensaje[x]}')
            if contador == 6 :
                textRL6.config(text=f'{x} : {textMensaje[x]}')
            if contador == 7 :
                textRL7.config(text=f'{x} : {textMensaje[x]}')
            if contador == 8 :
                textRL8.config(text=f'{x} : {textMensaje[x]}')
            if contador == 9 :
                textRL9.config(text=f'{x} : {textMensaje[x]}')
            contador = contador + 1
        resultados.pack()
        principal.pack_forget()
btnCalcular.bind('<Button-1>', CambiarResultado)
#### Boton de Creditos
btnCreditos = Canvas(principal)
btnCreditos.config(highlightthickness=0, height=70, bg=colorFondo,)
btnCreditos.create_rectangle(0,0,249,50,fill=colorBotones,outline=colorBotones)
btnCreditos.create_text(124,25,fill=colorFondo,font="Calibri 16 bold",text="Creditos")
btnCreditos.place(x=0, y=450)
def CambioCreditos(event):
    principal.pack_forget()
    creditos.pack()
btnCreditos.bind("<Button-1>", CambioCreditos)
#### Boton de Salir
btnSalir = Canvas(principal)
btnSalir.config(highlightthickness=0, height=70, bg=colorFondo,)
btnSalir.create_rectangle(0,0,249,50,fill=colorBotones,outline=colorBotones)
btnSalir.create_text(124,25,fill=colorFondo,font="Calibri 16 bold",text="Salir")
btnSalir.place(x=251, y=450)
def Salir(event):
    raiz.quit()
btnSalir.bind("<Button-1>", Salir)
########################################################################################################
# Frame Creditos
creditos = Frame(raiz)
creditos.config(bg=colorFondo,width="500", height="500")
## Elementos Del Fame
### Textos
textC1 = ttk.Label(creditos, 
                    text="Creditos 2020-2",
                    foreground=colorBotones,
                    font=('Calibri', 24, 'bold'), 
                    background=colorFondo)
textC1.place(x=120, y=40)
textC2 = ttk.Label(creditos, 
                    text="Sistemas De Telecomunicaciones II",
                    font=('Calibri', 16, 'bold'), 
                    background=colorFondo)
textC2.place(x=80, y=90)
textC3 = ttk.Label(creditos, 
                    text="ING. Gustavo Alonzo Chica Pedraza",
                    font=('Calibri', 16, 'bold'), 
                    background=colorFondo)
textC3.place(x=80, y=130)
textC4 = ttk.Label(creditos, 
                    text="Integrantes :",
                    foreground=colorBotones,
                    font=('Calibri', 16, 'bold'), 
                    background=colorFondo)
textC4.place(x=120, y=160)
textC5 = ttk.Label(creditos, 
                    text="Andrei Lizandro Riaño Tuta",
                    font=('Calibri', 16, 'bold'), 
                    background=colorFondo)
textC5.place(x=80, y=190)
textC6 = ttk.Label(creditos, 
                    text="Johann Stev Castellanos Gonzalez",
                    font=('Calibri', 16, 'bold'), 
                    background=colorFondo)
textC6.place(x=80, y=230)
textC7 = ttk.Label(creditos, 
                    text="Andres Nicolas Linares Chaparro",
                    font=('Calibri', 16, 'bold'), 
                    background=colorFondo)
textC7.place(x=80, y=270)
### Boton de Menu
botonMenu = Canvas(creditos)
botonMenu.config(bg=colorFondo, highlightthickness=0)
botonMenu.create_oval(0,0,80,80,fill=colorBotones,outline=colorBotones)
botonMenu.create_text(40,40,fill=colorFondo,font="Calibri 16 bold",text="Menu")
botonMenu.place(x=200, y=350)
def CambioMenu(event):
    textError.place_forget()
    creditos.pack_forget()
    principal.pack()
botonMenu.bind("<Button-1>", CambioMenu)
#########################################################################################################
# Frame De Resultados
resultados = Frame(raiz)
resultados.config(bg=colorFondo,width="500", height="500")
# Elemntos Del Frame
## Textos
textR1 = ttk.Label(resultados,
                    text="El texto :",
                    font=('Calibri', 18, 'bold'), 
                    background=colorFondo)
textR1.place(x=200, y=40)
textR2 = ttk.Label(resultados,
                    font=('Calibri', 16, 'bold'),
                    foreground=colorBotones,
                    background=colorFondo)
textR2.place(x=100, y=80)
textR3 = ttk.Label(resultados,
                    text="Contine :",
                    font=('Calibri', 18, 'bold'),
                    background=colorFondo)
textR3.place(x=200, y=120)
textRL0 = ttk.Label(resultados,
                    text='',
                    font=('Calibri', 16, 'bold'),
                    foreground=colorBotones,
                    background=colorFondo)
textRL0.place(x=100, y=160)
textRL1 = ttk.Label(resultados,
                    text='',
                    font=('Calibri', 16, 'bold'),
                    foreground=colorBotones,
                    background=colorFondo)
textRL1.place(x=100, y=190)
textRL2 = ttk.Label(resultados,
                    text='',
                    font=('Calibri', 16, 'bold'),
                    foreground=colorBotones,
                    background=colorFondo)
textRL2.place(x=100, y=220)
textRL3 = ttk.Label(resultados,
                    text='',
                    font=('Calibri', 16, 'bold'),
                    foreground=colorBotones,
                    background=colorFondo)
textRL3.place(x=100, y=250)
textRL4 = ttk.Label(resultados,
                    text='',
                    font=('Calibri', 16, 'bold'),
                    foreground=colorBotones,
                    background=colorFondo)
textRL4.place(x=100, y=280)
textRL5 = ttk.Label(resultados,
                    text='',
                    font=('Calibri', 16, 'bold'),
                    foreground=colorBotones,
                    background=colorFondo)
textRL5.place(x=300, y=160)
textRL6 = ttk.Label(resultados,
                    text='',
                    font=('Calibri', 16, 'bold'),
                    foreground=colorBotones,
                    background=colorFondo)
textRL6.place(x=300, y=190)
textRL7 = ttk.Label(resultados,
                    text='',
                    font=('Calibri', 16, 'bold'),
                    foreground=colorBotones,
                    background=colorFondo)
textRL7.place(x=300, y=220)
textRL8 = ttk.Label(resultados,
                    text='',
                    font=('Calibri', 16, 'bold'),
                    foreground=colorBotones,
                    background=colorFondo)
textRL8.place(x=300, y=250)
textRL9 = ttk.Label(resultados,
                    text='',
                    font=('Calibri', 16, 'bold'),
                    foreground=colorBotones,
                    background=colorFondo)
textRL9.place(x=300, y=280)
## Botones 
### Boton de Menu
botonMenu = Canvas(resultados)
botonMenu.config(bg=colorFondo, highlightthickness=0)
botonMenu.create_oval(0,0,80,80,fill=colorBotones,outline=colorBotones)
botonMenu.create_text(40,40,fill=colorFondo,font="Calibri 16 bold",text="Menu")
botonMenu.place(x=150, y=400)
def CambioMenu2(event):
    textError.place_forget()
    textRL0.config(text='')
    textRL1.config(text='')
    textRL2.config(text='')
    textRL3.config(text='')
    textRL4.config(text='')
    textRL5.config(text='')
    textRL6.config(text='')
    textRL7.config(text='')
    textRL8.config(text='')
    textRL9.config(text='')
    mensaje.delete('1.0', tk.END)
    resultados.pack_forget()
    principal.pack()
botonMenu.bind("<Button-1>", CambioMenu2)
### Boton De Salir
botonSalir = Canvas(resultados)
botonSalir.config(bg=colorFondo, highlightthickness=0)
botonSalir.create_oval(0,0,80,80,fill=colorBotones,outline=colorBotones)
botonSalir.create_text(40,40,fill=colorFondo,font="Calibri 16 bold",text="Salir")
botonSalir.place(x=250, y=400)
botonSalir.bind("<Button-1>", Salir)

raiz.mainloop()