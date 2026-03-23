import tkinter as tk
from tkinter import messagebox

intentos = 0

def validar_rango(numero, min_val, max_val):
    return min_val < numero < max_val

def abrir_ventana(parent):
    global intentos
    intentos = 0
    
    top = tk.Toplevel(parent)
    top.title("Ejercicio 5 - Validar (0, 20)")
    top.geometry("300x150")
    
    tk.Label(top, text="Ingrese un número entre (0, 20):").grid(row=0, column=0, columnspan=2, pady=10)
    entry_num = tk.Entry(top)
    entry_num.grid(row=1, column=0, columnspan=2, pady=10)
    
    def verificar():
        global intentos
        intentos += 1
        
        try:
            num = int(entry_num.get())
            if validar_rango(num, 0, 20):
                messagebox.showinfo("Éxito", f"¡Número {num} aceptado!\nCantidad de intentos que tomó: {intentos}", parent=top)
                intentos = 0
                entry_num.delete(0, tk.END)
            else:
                messagebox.showerror("Error", f"El número {num} NO está en el rango (0, 20).", parent=top)
                entry_num.delete(0, tk.END)
                entry_num.focus()
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número entero.", parent=top)
            entry_num.delete(0, tk.END)
            entry_num.focus()
            
    tk.Button(top, text="Verificar Rango", command=verificar, width=20).grid(row=2, column=0, columnspan=2, pady=10)
