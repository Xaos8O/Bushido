import tkinter as tk
import random
import string

def randomizador():

    #----------------------------------------------
    simbol = ('+','-','%','?','¿','#','!','.','}')
    simbo = random.choice(simbol)
    simbo2 = random.choice(simbol)
    simbo3 = random.choice(simbol)
    simbo4 = random.choice(simbol)
    simbo5= random.choice(simbol)
    simbo6 =random.choice(simbol)
    simbo7 = random.choice(simbol)
    simbo8 = random.choice(simbol)
    simbo9 = random.choice(simbol)
    simbo10 = random.choice(simbol)
    simbo11 = random.choice(simbol)
    simbo12 = random.choice(simbol)
    #----------------------------------------------
    num=random.randint(1,9)
    num2=random.randint(1,9)
    num3=random.randint(1,9)
    num4=random.randint(1,9)
    num5=random.randint(1,9)
    num6=random.randint(1,9)
    num7 = random.randint(1,9)
    num8 = random.randint(1,9)
    num9 = random.randint(1,9)
    num10 = random.randint(1,9)
    num11 = random.randint(1,9)
    num12 = random.randint(1,9)
    #----------------------------------------------
    minus=random.choice(string.ascii_lowercase)
    minus2=random.choice(string.ascii_lowercase)
    minus3=random.choice(string.ascii_lowercase)
    minus4=random.choice(string.ascii_lowercase)
    minus5=random.choice(string.ascii_lowercase)
    minus6=random.choice(string.ascii_lowercase)
    minus7=random.choice(string.ascii_lowercase)
    minus8=random.choice(string.ascii_lowercase)
    minus9=random.choice(string.ascii_lowercase)
    minus10=random.choice(string.ascii_lowercase)
    minus11=random.choice(string.ascii_lowercase)
    minus12=random.choice(string.ascii_lowercase)
    #----------------------------------------------
    mayus= random.choice(string.ascii_uppercase)
    mayus2=random.choice(string.ascii_uppercase)
    mayus3=random.choice(string.ascii_uppercase)
    mayus4=random.choice(string.ascii_uppercase)
    mayus5=random.choice(string.ascii_uppercase)
    mayus6=random.choice(string.ascii_uppercase)
    mayus7=random.choice(string.ascii_uppercase)
    mayus8=random.choice(string.ascii_uppercase)
    mayus9=random.choice(string.ascii_uppercase)
    mayus10=random.choice(string.ascii_uppercase)
    mayus11=random.choice(string.ascii_uppercase)
    mayus12=random.choice(string.ascii_uppercase)
    #-----------------------------------------------
    contraseña = combo_simbolos.get()
    
    if contraseña == "Mayusculas":
        resultado.set(mayus + mayus2 + mayus3 + mayus4 + mayus5 + mayus6 + mayus7 + mayus8 + mayus9 + mayus10 + mayus11 + mayus12)
    elif contraseña == "Numeros":
        resultado.set(str(num) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6) + str(num7) + str(num9) + str(num10) + str(num11) + str(num12))
    elif contraseña == "Minusculas":
        resultado.set(minus + minus2 + minus3 + minus4 + minus5 + minus6 + minus7 + minus8 + minus9 + minus10 + minus11 + minus12)
    elif contraseña == "Simbolos":
        resultado.set(simbo + simbo2 + simbo3 + simbo4 + simbo5 + simbo6 + simbo7 + simbo8 +simbo9 + simbo10 + simbo11 + simbo12)
    elif contraseña == "Todos":
        resultado.set(str(num) + minus + mayus + simbo + mayus2 + simbo2 + minus2 + str(num2) + minus3 + simbo8 + mayus11 + str(num10))

def copiar():
    resultado_text = resultado.get() #Lo que consiga del .set(), lo invocara el .get()
    pantalla.clipboard_clear
    pantalla.clipboard_append(resultado_text)
    pantalla.update

#Crear la pantalla
pantalla = tk.Tk()
pantalla.title("Contraseña random XwX")

pantalla.geometry("240x120")

#Para que se muestre el resultado
resultado=tk.StringVar(pantalla)
resultado.set("Contraseña generada")

#Boton para generar la contraseña
btn_contra = tk.Button(pantalla, text= "Generar contraseña", command= randomizador)
btn_contra.grid(row=3, column=4)

#Aqui aparecera el resultado que salga
etq_resultado =tk.Label(pantalla, textvariable=resultado)
etq_resultado.grid(row=3, column=5, columnspan=8) 

#Boton para copiar 
btn_copiar = tk.Button(pantalla, text="Copiar", command=copiar) 
btn_copiar.grid(row=5, column=5)

texto_simbolos = tk.Label(pantalla, text="Simbolos")
simbolos = "Mayusculas", "Minusculas", "Numeros", "Simbolos", "Todos"
combo_simbolos=tk.StringVar(pantalla)
combo_simbolos.set(simbolos[0])
menu_simbolos = tk.OptionMenu(pantalla, combo_simbolos, *simbolos )
menu_simbolos.grid(row=5, column=4)

pantalla.mainloop()