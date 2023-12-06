#configurar el espacio.Y luego ver como era para hacerlo un archivo ejecutable
#Y luego anotar que quiero hacer un programa de contraseñas randoms

import tkinter as tk

def calcular():
    try:
        num1 = float(digito1a.get())
        num2 = float(digito2a.get())
        operacion = combo_operaciones.get()

        if operacion == 'Sumar':
            resultado.set(num1 + num2)
        elif operacion == 'Resta':
            resultado.set(num1 - num2)
        elif operacion == 'Multiplicacion':
            resultado.set(num1 * num2)
        elif operacion == 'Divison':
            resultado.set(num1 / num2)
        elif operacion == 'Porcentaje':
            resultado.set((num1 * num2) / 100)
    except ValueError:
        resultado.set('Error')


#Pantalla y titulo
Pantalla = tk.Tk()
Pantalla.title("Calculadora super mega pro")

#Tamaño de la pantalla. Con tk.Tk se crea la pantalla y con .geometry se decide el tamaño

Pantalla.geometry("250x120")

#Variables para que se veean los numeros
resultado = tk.StringVar() #Stringvar es barra de texto
resultado.set('Resultado')

#Digitos
digito1= tk.Label(Pantalla, text="Digito: ")  
digito1.grid(row=3, column=2)
digito1a=tk.Entry(Pantalla)
digito1a.grid(row=3, column=3)

digito2=tk.Label(Pantalla, text='Digito: ')
digito2.grid(row=5,column=2)
digito2a=tk.Entry(Pantalla)
digito2a.grid(row=5, column=3)


#Operadores
operadores= tk.Label(Pantalla, text="Operadores")
operadores.grid(row=4,column=2)
operaciones=["Sumar", "Divison", "Resta", "Multiplicacion", "Porcentaje"]
combo_operaciones=tk.StringVar()
combo_operaciones.set(operaciones[0])
menu_operaciones= tk.OptionMenu(Pantalla,combo_operaciones, *operaciones) #.OptionMenu desplega un menu de opciones
menu_operaciones.grid(row=4, column=3)
#Boton para calcular
btn_calcular= tk.Button(Pantalla, text="Calcular", command=calcular)
btn_calcular.grid(row=6, column=3, columnspan=1)

#Boton para el resultado
etiqueta_resultado = tk.Label(Pantalla, textvariable=resultado) #Aqui habia puesto el texto, pero en realidad era la variable
etiqueta_resultado.grid(row=7, column=3, columnspan=2)


Pantalla.mainloop()