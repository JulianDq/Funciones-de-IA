import tkinter as tk
from tkinter import messagebox

def abrir_ventana(parent):
    top = tk.Toplevel(parent)
    top.title("Ejercicio 7 - Suma de Enteros")
    top.geometry("350x250")
    
    tk.Label(top, text="Ingrese un número n positivo:").pack(pady=10)
    entry_n = tk.Entry(top)
    entry_n.pack(pady=5)
    
    lbl_resultado = tk.Label(top, text="", justify=tk.LEFT, wraplength=320)
    lbl_resultado.pack(pady=10)
    
    def calcular():
        try:
            n = int(entry_n.get())
            if n <= 0:
                messagebox.showerror("Error", "El número debe ser positivo y mayor a 0.", parent=top)
                return
                
            secuencia = list(range(1, n + 1))
            suma = sum(secuencia)
            
            texto_secuencia = " + ".join(str(x) for x in secuencia)
            if len(texto_secuencia) > 200:
                texto_secuencia = texto_secuencia[:197] + "..."
                
            resultado_texto = f"Secuencia: {texto_secuencia}\n\nSuma Total: {suma}"
            lbl_resultado.config(text=resultado_texto)
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número entero.", parent=top)
            
    tk.Button(top, text="Calcular", command=calcular, width=20).pack(pady=10)
