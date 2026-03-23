import tkinter as tk
from tkinter import messagebox

compras = []

def calcular_descuento(mes, importe):
    mes = mes.strip().lower()
    descuento = 0.0
    
    if mes == "octubre":
        descuento = 0.15
    elif mes == "diciembre":
        descuento = 0.20
    elif mes == "julio":
        descuento = 0.10
        
    monto_descuento = importe * descuento
    total_final = importe - monto_descuento
    return monto_descuento, total_final

def validar_mes(mes):
    meses_validos = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    return mes.strip().lower() in meses_validos

def abrir_ventana(parent):
    top = tk.Toplevel(parent)
    top.title("Ejercicio 3 - Descuentos")
    top.geometry("350x200")
    
    tk.Label(top, text="Nombre Cliente:").grid(row=0, column=0, padx=10, pady=10)
    entry_nombre = tk.Entry(top)
    entry_nombre.grid(row=0, column=1, padx=10, pady=10)
    
    tk.Label(top, text="Mes de la compra:").grid(row=1, column=0, padx=10, pady=10)
    entry_mes = tk.Entry(top)
    entry_mes.grid(row=1, column=1, padx=10, pady=10)
    
    tk.Label(top, text="Importe ($):").grid(row=2, column=0, padx=10, pady=10)
    entry_importe = tk.Entry(top)
    entry_importe.grid(row=2, column=1, padx=10, pady=10)
    
    def registrar():
        nombre = entry_nombre.get().strip()
        mes = entry_mes.get().strip()
        
        if not nombre or not mes:
            messagebox.showerror("Error", "Faltan datos por ingresar", parent=top)
            return
            
        if not validar_mes(mes):
            messagebox.showerror("Error", "El mes ingresado no es válido", parent=top)
            return
            
        try:
            importe = float(entry_importe.get())
            if importe < 0:
                raise ValueError
                
            descuento, total = calcular_descuento(mes, importe)
            compras.append((nombre, mes, importe, descuento, total))
            
            messagebox.showinfo("Ticket de Compra", f"Cliente: {nombre}\nMes: {mes.capitalize()}\nImporte Original: ${importe:.2f}\nDescuento: ${descuento:.2f}\nTotal Final: ${total:.2f}", parent=top)
            
            entry_nombre.delete(0, tk.END)
            entry_mes.delete(0, tk.END)
            entry_importe.delete(0, tk.END)
            entry_nombre.focus()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un importe válido", parent=top)
            
    def ver_total_dia():
        total_vendido = sum(compra[4] for compra in compras)
        messagebox.showinfo("Total Vendido", f"El total vendido en el día (con descuentos aplicados) es: ${total_vendido:.2f}", parent=top)
        
    tk.Button(top, text="Registrar Compra", command=registrar).grid(row=3, column=0, pady=15)
    tk.Button(top, text="Consultar Total Día", command=ver_total_dia).grid(row=3, column=1, pady=15)
