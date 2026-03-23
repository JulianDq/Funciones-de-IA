import tkinter as tk
from tkinter import messagebox

numeros_ingresados = []

def abrir_ventana(parent):
    global numeros_ingresados
    numeros_ingresados = []
    
    top = tk.Toplevel(parent)
    top.title("Ejercicio 8 - Suma Acumulativa")
    top.geometry("350x250")
    
    tk.Label(top, text="Ingrese un número (0 para detener):").pack(pady=10)
    entry_num = tk.Entry(top)
    entry_num.pack(pady=5)
    
    lbl_estado = tk.Label(top, text="Suma actual: 0", font=("Arial", 12, "bold"))
    lbl_estado.pack(pady=10)
    
    def agregar():
        try:
            num = int(entry_num.get())
            if num == 0:
                finalizar()
                return
                
            numeros_ingresados.append(num)
            suma_actual = sum(numeros_ingresados)
            lbl_estado.config(text=f"Suma actual: {suma_actual}")
            entry_num.delete(0, tk.END)
            entry_num.focus()
            
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número entero válido.", parent=top)
            entry_num.delete(0, tk.END)
            
    def finalizar():
        if not numeros_ingresados:
            messagebox.showinfo("Resultados", "No se ingresaron números.", parent=top)
            top.destroy()
            return
            
        suma_total = sum(numeros_ingresados)
        cantidad = len(numeros_ingresados)
        lista_str = ", ".join(str(x) for x in numeros_ingresados)
        
        msg = f"Proceso finalizado.\n\n"
        msg += f"Números ingresados: [{lista_str}]\n"
        msg += f"Cantidad de números: {cantidad}\n"
        msg += f"Suma Total: {suma_total}"
        
        messagebox.showinfo("Resumen Final", msg, parent=top)
        top.destroy()
        
    tk.Button(top, text="Agregar", command=agregar, width=20).pack(pady=5)
    
    # Permitir usar Enter para agregar
    top.bind('<Return>', lambda e: agregar())
