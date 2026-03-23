import tkinter as tk
from tkinter import messagebox

historial = []

def calcular_aumento(sueldo):
    if sueldo < 7000:
        return sueldo * 1.08
    return sueldo

def abrir_ventana(parent):
    top = tk.Toplevel(parent)
    top.title("Ejercicio 1 - Aumento de Sueldo")
    top.geometry("300x200")
    
    tk.Label(top, text="Nombre Trabajador:").grid(row=0, column=0, padx=10, pady=10)
    entry_nombre = tk.Entry(top)
    entry_nombre.grid(row=0, column=1, padx=10, pady=10)
    
    tk.Label(top, text="Sueldo Actual:").grid(row=1, column=0, padx=10, pady=10)
    entry_sueldo = tk.Entry(top)
    entry_sueldo.grid(row=1, column=1, padx=10, pady=10)
    
    def procesar():
        nombre = entry_nombre.get().strip()
        if not nombre:
            messagebox.showerror("Error", "Ingrese el nombre", parent=top)
            return
            
        try:
            sueldo = float(entry_sueldo.get())
            if sueldo < 0:
                raise ValueError
            nuevo_sueldo = calcular_aumento(sueldo)
            historial.append((nombre, sueldo, nuevo_sueldo))
            messagebox.showinfo("Resultado", f"Trabajador: {nombre}\nSueldo Original: {sueldo:.2f}\nNuevo Sueldo: {nuevo_sueldo:.2f}", parent=top)
            entry_nombre.delete(0, tk.END)
            entry_sueldo.delete(0, tk.END)
            entry_nombre.focus()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un sueldo numérico válido", parent=top)
            
    def ver_historial():
        if not historial:
            messagebox.showinfo("Historial", "No hay trabajadores procesados.", parent=top)
            return
        
        texto = "Historial de Trabajadores:\n\n"
        for n, s, ns in historial:
            texto += f"{n}: {s:.2f} -> {ns:.2f}\n"
        messagebox.showinfo("Historial", texto, parent=top)
        
    tk.Button(top, text="Procesar", command=procesar).grid(row=2, column=0, pady=15)
    tk.Button(top, text="Ver Historial", command=ver_historial).grid(row=2, column=1, pady=15)
