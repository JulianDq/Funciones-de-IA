import tkinter as tk
from tkinter import messagebox

historial_pago = []

def calcular_pago_trabajador(h_normales, pago_hn, h_extras, hijos):
    # Regla: El pago por hora extra es 50% mayor que la hora normal (es decir, pago_hn * 1.5)
    pago_he = pago_hn * 1.5
    
    # Cálculos
    pago_por_hn = h_normales * pago_hn
    pago_por_he = h_extras * pago_he
    
    # Bonificación: 0.5 por hijo (asumimos que la unidad es una cantidad fija, ej. 0.5 soles/dolares por hijo)
    # Releyendo: "Cada hijo recibe una bonificación de 0.5". En este contexto puede ser 0.5 de bonificación porcentual 
    # o una cantidad 0.5 al total... Lo tomaré como 0.5 adicional.
    bonificacion_hijos = hijos * 0.5
    
    pago_total = pago_por_hn + pago_por_he + bonificacion_hijos
    
    return pago_por_hn, pago_por_he, bonificacion_hijos, pago_total

def abrir_ventana(parent):
    top = tk.Toplevel(parent)
    top.title("Ejercicio 10 - Pago de Trabajadores")
    top.geometry("350x300")
    
    tk.Label(top, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
    entry_nombre = tk.Entry(top)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(top, text="Horas Normales:").grid(row=1, column=0, padx=10, pady=5)
    entry_h_normales = tk.Entry(top)
    entry_h_normales.grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(top, text="Pago x Hora Normal:").grid(row=2, column=0, padx=10, pady=5)
    entry_p_hora = tk.Entry(top)
    entry_p_hora.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Label(top, text="Horas Extras:").grid(row=3, column=0, padx=10, pady=5)
    entry_h_extras = tk.Entry(top)
    entry_h_extras.grid(row=3, column=1, padx=10, pady=5)
    
    tk.Label(top, text="Cantidad de Hijos:").grid(row=4, column=0, padx=10, pady=5)
    entry_hijos = tk.Entry(top)
    entry_hijos.grid(row=4, column=1, padx=10, pady=5)
    
    def procesar():
        nombre = entry_nombre.get().strip()
        if not nombre:
            messagebox.showerror("Error", "Ingrese nombre del trabajador", parent=top)
            return
            
        try:
            hn = float(entry_h_normales.get())
            ph = float(entry_p_hora.get())
            he = float(entry_h_extras.get())
            hijos = int(entry_hijos.get())
            
            p_hn, p_he, bonif, total = calcular_pago_trabajador(hn, ph, he, hijos)
            
            historial_pago.append((nombre, p_hn, p_he, bonif, total))
            
            msg = f"Trabajador: {nombre}\n"
            msg += f"Pago Horas Normales: ${p_hn:.2f}\n"
            msg += f"Pago Horas Extras: ${p_he:.2f}\n"
            msg += f"Bonificación por Hijos: ${bonif:.2f}\n"
            msg += f"-----------------------\n"
            msg += f"PAGO TOTAL: ${total:.2f}"
            
            messagebox.showinfo("Boleta de Pago", msg, parent=top)
            
            for ent in (entry_nombre, entry_h_normales, entry_p_hora, entry_h_extras, entry_hijos):
                ent.delete(0, tk.END)
            entry_nombre.focus()
            
        except ValueError:
            messagebox.showerror("Error", "Verifique que los datos numéricos sean correctos.", parent=top)

    def reporte():
        if not historial_pago:
            messagebox.showinfo("Reporte", "No hay pagos registrados.", parent=top)
            return
            
        texto = "=== Reporte de Pagos ===\n\n"
        gt = 0
        for p in historial_pago:
            texto += f"• {p[0]}: Total ${p[4]:.2f} (Norm: ${p[1]:.2f}, Ext: ${p[2]:.2f}, Hijos: ${p[3]:.2f})\n"
            gt += p[4]
            
        texto += f"\nTOTAL PLANILLA: ${gt:.2f}"
        messagebox.showinfo("Reporte General", texto, parent=top)

    tk.Button(top, text="Procesar Pago", command=procesar).grid(row=5, column=0, pady=15)
    tk.Button(top, text="Ver Reporte", command=reporte).grid(row=5, column=1, pady=15)
