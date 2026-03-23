import tkinter as tk
from tkinter import messagebox

numeros_limite = []

def abrir_ventana(parent):
    global numeros_limite
    numeros_limite = []
    
    top = tk.Toplevel(parent)
    top.title("Ejercicio 9 - Suma límite > 100")
    top.geometry("350x250")
    
    tk.Label(top, text="Ingrese un número (se detendrá al superar 100):").pack(pady=10)
    entry_num = tk.Entry(top)
    entry_num.pack(pady=5)
    
    lbl_estado = tk.Label(top, text="Suma actual: 0", font=("Arial", 12, "bold"))
    lbl_estado.pack(pady=10)
    
    def agregar():
        try:
            num = int(entry_num.get())
            numeros_limite.append(num)
            
            suma_actual = sum(numeros_limite)
            lbl_estado.config(text=f"Suma actual: {suma_actual}")
            
            if suma_actual > 100:
                finalizar(suma_actual)
            else:
                entry_num.delete(0, tk.END)
                entry_num.focus()
                
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número entero válido.", parent=top)
            entry_num.delete(0, tk.END)
            
    def finalizar(suma_final):
        cantidad = len(numeros_limite)
        lista_str = ", ".join(str(x) for x in numeros_limite)
        
        msg = f"¡Límite de 100 superado!\n\n"
        msg += f"Cantidad ingresados: {cantidad}\n"
        msg += f"Números: [{lista_str}]\n"
        msg += f"Suma Final: {suma_final}"
        
        messagebox.showinfo("Resultados", msg, parent=top)
        top.destroy()
        
    tk.Button(top, text="Agregar", command=agregar, width=20).pack(pady=5)
    top.bind('<Return>', lambda e: agregar())
