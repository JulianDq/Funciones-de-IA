import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Configurar apariencia inicial de customtkinter
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Gráfica de Línea Recta: f(x) = mx + b")
        self.geometry("800x600")
        
        # Frame izquierdo para los controles
        self.frame_controles = ctk.CTkFrame(self, width=250)
        self.frame_controles.pack(side="left", fill="y", padx=10, pady=10)
        
        # Frame derecho para la gráfica
        self.frame_grafica = ctk.CTkFrame(self)
        self.frame_grafica.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        # --- Controles ---
        ctk.CTkLabel(self.frame_controles, text="Función Lineal", font=("Arial", 20, "bold")).pack(pady=20)
        ctk.CTkLabel(self.frame_controles, text="f(x) = mx + b", font=("Arial", 16)).pack(pady=5)
        
        # Entrada para la pendiente 'm'
        ctk.CTkLabel(self.frame_controles, text="Pendiente (m):").pack(pady=(20, 0))
        self.entry_m = ctk.CTkEntry(self.frame_controles, placeholder_text="Ejemplo: 2")
        self.entry_m.pack(pady=5)
        
        # Entrada para el término independiente 'b'
        ctk.CTkLabel(self.frame_controles, text="Término indep. (b):").pack(pady=(10, 0))
        self.entry_b = ctk.CTkEntry(self.frame_controles, placeholder_text="Ejemplo: 5")
        self.entry_b.pack(pady=5)
        
        # Botón para graficar
        self.btn_graficar = ctk.CTkButton(self.frame_controles, text="Generar Gráfica", command=self.generar_grafica)
        self.btn_graficar.pack(pady=30)
        
        # Variables para mantener el lienzo de matplotlib
        self.canvas = None
        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        
        # Mostrar una gráfica vacía al inicio
        self.mostrar_grafica_en_interfaz()
        
    def generar_grafica(self):
        # 1. Validar si los datos son incorrectos
        try:
            m = float(self.entry_m.get())
            b = float(self.entry_b.get())
        except ValueError:
            # Si no se puede convertir a número, mostramos error y no graficamos
            tk.messagebox.showerror("Error de Datos", "Por favor ingresa números válidos para 'm' y 'b'.")
            return
            
        # 2. Generar datos para la gráfica si la validación fue exitosa
        # Limpiar la gráfica anterior
        self.ax.clear()
        
        # Generar valores de x (desde -10 hasta 10, 100 puntos en total)
        x = np.linspace(-10, 10, 100)
        
        # Calcular los valores de y: f(x) = mx + b
        y = (m * x) + b
        
        # 3. Dibujar la línea recta
        self.ax.plot(x, y, color='blue', label=f'f(x) = {m}x + {b}')
        
        # Personalizar la gráfica
        self.ax.set_title("Gráfica de la Función Lineal")
        self.ax.set_xlabel("Eje X")
        self.ax.set_ylabel("Eje Y")
        self.ax.grid(True) # Mostrar la cuadrícula
        self.ax.axhline(0, color='black', linewidth=1) # Línea horizontal en 0
        self.ax.axvline(0, color='black', linewidth=1) # Línea vertical en 0
        self.ax.legend() # Mostrar la leyenda
        
        # Actualizar el lienzo en la interfaz
        self.canvas.draw()
        
    def mostrar_grafica_en_interfaz(self):
        # Configuración inicial del widget para incrustar matplotlib en tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_grafica)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
