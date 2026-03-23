import tkinter as tk
from tkinter import messagebox

historial_visitantes = []

def calcular_pago(edad, juegos):
    COSTO_JUEGO = 50
    total = juegos * COSTO_JUEGO
    descuento = 0.0
    
    if edad < 10:
        descuento = 0.25
    elif 10 <= edad <= 17:
        descuento = 0.10
        
    total_pagar = total * (1 - descuento)
    return total, descuento * total, total_pagar

def abrir_ventana(parent):
    top = tk.Toplevel(parent)
    top.title("Ejercicio 2 - Parque Diversiones")
    top.geometry("350x250")
    
    tk.Label(top, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
    entry_nombre = tk.Entry(top)
    entry_nombre.grid(row=0, column=1, padx=10, pady=10)
    
    tk.Label(top, text="Edad:").grid(row=1, column=0, padx=10, pady=10)
    entry_edad = tk.Entry(top)
    entry_edad.grid(row=1, column=1, padx=10, pady=10)
    
    tk.Label(top, text="Cant. Juegos:").grid(row=2, column=0, padx=10, pady=10)
    entry_juegos = tk.Entry(top)
    entry_juegos.grid(row=2, column=1, padx=10, pady=10)
    
    def registrar():
        nombre = entry_nombre.get().strip()
        if not nombre:
            messagebox.showerror("Error", "Ingrese el nombre", parent=top)
            return
            
        try:
            edad = int(entry_edad.get())
            juegos = int(entry_juegos.get())
            if edad < 0 or juegos < 0:
                raise ValueError
                
            sub, desc, total = calcular_pago(edad, juegos)
            historial_visitantes.append((nombre, edad, juegos, sub, desc, total))
            
            msg = f"Visitante: {nombre}\nJuegos: {juegos}\nSubtotal: {sub:.2f}\nDescuento: {desc:.2f}\nTotal a Pagar: {total:.2f}"
            messagebox.showinfo("Ticket", msg, parent=top)
            
            entry_nombre.delete(0, tk.END)
            entry_edad.delete(0, tk.END)
            entry_juegos.delete(0, tk.END)
            entry_nombre.focus()
        except ValueError:
            messagebox.showerror("Error", "Ingrese edad y cantidad de juegos válidos (números enteros)", parent=top)
            
    def ver_recaudacion():
        if not historial_visitantes:
            messagebox.showinfo("Recaudación", "No hay visitantes registrados.", parent=top)
            return
        
        recaudacion = sum(visita[5] for visita in historial_visitantes)
        texto = f"Total Recaudado por el Parque: {recaudacion:.2f} soles\n\nVisitantes:\n"
        for v in historial_visitantes:
            texto += f"- {v[0]}: Pagó {v[5]:.2f}\n"
            
        messagebox.showinfo("Recaudación", texto, parent=top)
        
    tk.Button(top, text="Registrar", command=registrar).grid(row=3, column=0, pady=15)
    tk.Button(top, text="Total Recaudado", command=ver_recaudacion).grid(row=3, column=1, pady=15)
