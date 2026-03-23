import tkinter as tk
from ejercicios import ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5
from ejercicios import ejercicio_6, ejercicio_7, ejercicio_8, ejercicio_9, ejercicio_10

def abrir():
    ventana = tk.Tk()
    ventana.title("Menú Principal")
    
    tk.Label(ventana, text="Menu Principal", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, padx=20, pady=15)
    
    # Fila 1
    tk.Button(ventana, text="Ejercicio 1 - Aumento", width=25, command=lambda: ejercicio_1.abrir_ventana(ventana)).grid(row=1, column=0, padx=10, pady=5)
    tk.Button(ventana, text="Ejercicio 2 - Parque", width=25, command=lambda: ejercicio_2.abrir_ventana(ventana)).grid(row=1, column=1, padx=10, pady=5)
    # Fila 2
    tk.Button(ventana, text="Ejercicio 3 - Descuentos", width=25, command=lambda: ejercicio_3.abrir_ventana(ventana)).grid(row=2, column=0, padx=10, pady=5)
    tk.Button(ventana, text="Ejercicio 4 - Validar < 10", width=25, command=lambda: ejercicio_4.abrir_ventana(ventana)).grid(row=2, column=1, padx=10, pady=5)
    # Fila 3
    tk.Button(ventana, text="Ejercicio 5 - Validar 0-20", width=25, command=lambda: ejercicio_5.abrir_ventana(ventana)).grid(row=3, column=0, padx=10, pady=5)
    tk.Button(ventana, text="Ejercicio 6 - Historial", width=25, command=lambda: ejercicio_6.abrir_ventana(ventana)).grid(row=3, column=1, padx=10, pady=5)
    # Fila 4
    tk.Button(ventana, text="Ejercicio 7 - Suma Enteros", width=25, command=lambda: ejercicio_7.abrir_ventana(ventana)).grid(row=4, column=0, padx=10, pady=5)
    tk.Button(ventana, text="Ejercicio 8 - Suma Acumulativa", width=25, command=lambda: ejercicio_8.abrir_ventana(ventana)).grid(row=4, column=1, padx=10, pady=5)
    # Fila 5
    tk.Button(ventana, text="Ejercicio 9 - Suma límite 100", width=25, command=lambda: ejercicio_9.abrir_ventana(ventana)).grid(row=5, column=0, padx=10, pady=5)
    tk.Button(ventana, text="Ejercicio 10 - Trabajadores", width=25, command=lambda: ejercicio_10.abrir_ventana(ventana)).grid(row=5, column=1, padx=10, pady=5)
    
    tk.Button(ventana, text="Salir", command=ventana.destroy, bg="red", fg="white", font=("Arial", 10, "bold"), width=52).grid(row=6, column=0, columnspan=2, pady=20)
    
    ventana.mainloop()

if __name__ == "__main__":
    abrir()

