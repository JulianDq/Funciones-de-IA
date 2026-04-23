import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import queries
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AppVentanaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Panel de Consultas Complejas - Netflix Data")
        self.geometry("1100x650")
        
        # Grid layout (1 row, 2 cols)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # Frame Izquierdo (Menú)
        self.frame_menu = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.frame_menu.grid(row=0, column=0, sticky="nsew")
        self.frame_menu.grid_rowconfigure(len(queries.QUERIES) + 2, weight=1)
        
        ctk.CTkLabel(self.frame_menu, text="Menú de Consultas", font=("Arial", 18, "bold")).grid(row=0, column=0, padx=20, pady=20)
        
        # Generar botones dinámicamente según queries.py
        for i, (nombre, func) in enumerate(queries.QUERIES):
            btn = ctk.CTkButton(self.frame_menu, text=nombre, command=lambda f=func: self.ejecutar_consulta(f), anchor="w")
            btn.grid(row=i+1, column=0, padx=20, pady=10, sticky="ew")
            
        # Botón extra de salir
        btn_salir = ctk.CTkButton(self.frame_menu, text="Cerrar Sesión", fg_color="red", hover_color="darkred", command=self.destroy)
        btn_salir.grid(row=len(queries.QUERIES) + 2, column=0, padx=20, pady=20, sticky="s")
        
        # Frame Derecho (Resultados y Justificación)
        self.frame_main = ctk.CTkFrame(self, corner_radius=0)
        self.frame_main.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.frame_main.grid_rowconfigure(0, weight=3) # Treeview
        self.frame_main.grid_rowconfigure(1, weight=1) # Justification
        self.frame_main.grid_columnconfigure(0, weight=1)
        
        # Estilos aplicados al Treeview para que combine con CustomTkinter
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", 
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
        
        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat")
        style.map("Treeview.Heading", background=[('active', '#3484F0')])

        # Componente Treeview
        # Se envuelve en un frame normal para poder agregar los scrollbars de forma fácil
        tree_frame = ctk.CTkFrame(self.frame_main)
        tree_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        scroll_y = ctk.CTkScrollbar(tree_frame, orientation="vertical")
        scroll_y.grid(row=0, column=1, sticky="ns")
        
        scroll_x = ctk.CTkScrollbar(tree_frame, orientation="horizontal")
        scroll_x.grid(row=1, column=0, sticky="ew")
        
        self.tree = ttk.Treeview(tree_frame, yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        
        scroll_y.configure(command=self.tree.yview)
        scroll_x.configure(command=self.tree.xview)
        
        # Area de justificación
        self.frame_just = ctk.CTkFrame(self.frame_main)
        self.frame_just.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        self.frame_just.grid_rowconfigure(1, weight=1)
        self.frame_just.grid_columnconfigure(0, weight=1)
        
        lbl_titulo = ctk.CTkLabel(self.frame_just, text="Justificación del Análisis", font=("Arial", 16, "bold"))
        lbl_titulo.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        
        self.btn_grafica = ctk.CTkButton(self.frame_just, text="Ver Gráfico", command=self.mostrar_grafica, fg_color="green", hover_color="darkgreen", width=120)
        self.btn_grafica.grid(row=0, column=1, sticky="e", padx=10, pady=5)
        self.btn_grafica.grid_remove() # Ocultar por defecto
        
        self.fig_actual = None
        
        self.textbox_just = ctk.CTkTextbox(self.frame_just, wrap="word", fg_color="#1E1E1E", text_color="white", font=("Arial", 14))
        self.textbox_just.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        self.textbox_just.insert("0.0", "Selecciona una consulta del menú izquierdo para comenzar...")
        self.textbox_just.configure(state="disabled")
        
    def ejecutar_consulta(self, func):
        try:
            # Ahora func() retorna 4 elementos
            columnas, filas, justificacion, fig = func()
            
            self.fig_actual = fig
            if fig is not None:
                self.btn_grafica.grid()
            else:
                self.btn_grafica.grid_remove()
            
            # Limpiar treeview existente
            self.tree.delete(*self.tree.get_children())
            
            # Configurar nuevas columnas
            self.tree["columns"] = columnas
            self.tree["show"] = "headings"
            
            for col in columnas:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=150, anchor="center")
            
            # Insertar filas
            for row in filas:
                self.tree.insert("", "end", values=row)
                
            # Actualizar Justificación
            self.textbox_just.configure(state="normal")
            self.textbox_just.delete("0.0", "end")
            self.textbox_just.insert("0.0", justificacion)
            self.textbox_just.configure(state="disabled")
            
        except Exception as e:
            self.textbox_just.configure(state="normal")
            self.textbox_just.delete("0.0", "end")
            self.textbox_just.insert("0.0", f"Ocurrió un error al ejecutar la consulta:\n{repr(e)}")
            self.textbox_just.configure(state="disabled")

    def mostrar_grafica(self):
        if self.fig_actual:
            top = ctk.CTkToplevel(self)
            top.title("Gráfico Analítico")
            top.geometry("700x500")
            canvas = FigureCanvasTkAgg(self.fig_actual, master=top)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = AppVentanaPrincipal()
    app.mainloop()
