import tkinter as tk
from tkinter import messagebox

historial_intentos = []
intentos_incorrectos = 0

def validar_rango(numero, min_val, max_val):
    return min_val < numero < max_val

def abrir_ventana(parent):
    global intentos_incorrectos, historial_intentos
    intentos_incorrectos = 0
    historial_intentos = []
    
    top = tk.Toplevel(parent)
    top.title("Ejercicio 6 - Historial de Validaciones")
    top.geometry("300x200")
    
    tk.Label(top, text="Ingrese un número entre (0, 20):").grid(row=0, column=0, columnspan=2, pady=10)
    entry_num = tk.Entry(top)
    entry_num.grid(row=1, column=0, columnspan=2, pady=10)
    
    def verificar():
        global intentos_incorrectos
        try:
            num = int(entry_num.get())
            historial_intentos.append(num)
            
            if validar_rango(num, 0, 20):
                msg = f"¡Número {num} aceptado!\n"
                msg += f"Intentos incorrectos previos: {intentos_incorrectos}\n"
                msg += f"Número correcto: {num}"
                messagebox.showinfo("Éxito", msg, parent=top)
                
                # Reset for next run
                intentos_incorrectos = 0
                entry_num.delete(0, tk.END)
            else:
                intentos_incorrectos += 1
                messagebox.showerror("Error", f"El número {num} NO está en el rango (0, 20).", parent=top)
                entry_num.delete(0, tk.END)
                entry_num.focus()
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número entero.", parent=top)
            entry_num.delete(0, tk.END)
            entry_num.focus()
            
    def ver_historial():
        if not historial_intentos:
            messagebox.showinfo("Historial", "No se han registrado intentos.", parent=top)
            return
            
        texto = "Historial de todos los números ingresados:\n\n"
        texto += ", ".join(str(x) for x in historial_intentos)
        messagebox.showinfo("Historial Completo", texto, parent=top)
        
    tk.Button(top, text="Verificar", command=verificar, width=15).grid(row=2, column=0, pady=15, padx=5)
    tk.Button(top, text="Ver Historial", command=ver_historial, width=15).grid(row=2, column=1, pady=15, padx=5)
