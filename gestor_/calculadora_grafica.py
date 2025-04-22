# Funciones de operaciones
import tkinter as tk
from tkinter import messagebox


def sumar():
    try:
        resultado = float(entrada1.get()) + float(entrada2.get())
        mostrar_resultado(resultado)
    except ValueError:
        mostrar_error()

def restar():
    try:
        resultado = float(entrada1.get()) - float(entrada2.get())
        mostrar_resultado(resultado)
    except ValueError:
        mostrar_error()

def multiplicar():
    try:
        resultado = float(entrada1.get()) * float(entrada2.get())
        mostrar_resultado(resultado)
    except ValueError:
        mostrar_error()

def dividir():
    try:
        num2 = float(entrada2.get())
        if num2 == 0:
            messagebox.showwarning("Error", "No se puede dividir por cero")
        else:
            resultado = float(entrada1.get()) / num2
            mostrar_resultado(resultado)
    except ValueError:
        mostrar_error()

def mostrar_resultado(valor):
    etiqueta_resultado.config(text=f"Resultado: {valor}")

def mostrar_error():
    messagebox.showerror("Error", "Por favor ingresa solo números")

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Gráfica")
ventana.geometry("300x250")
ventana.resizable(False, False)

# Entradas de números
tk.Label(ventana, text="Número 1:").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Número 2:").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

# Botones de operaciones
tk.Button(ventana, text="Sumar", command=sumar).pack(pady=2)
tk.Button(ventana, text="Restar", command=restar).pack(pady=2)
tk.Button(ventana, text="Multiplicar", command=multiplicar).pack(pady=2)
tk.Button(ventana, text="Dividir", command=dividir).pack(pady=2)

# Resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.pack(pady=10)

# Iniciar el bucle de la ventana
ventana.mainloop()