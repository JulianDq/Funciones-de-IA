import customtkinter as ctk
import os

from app_gui import AppVentanaPrincipal

def cargar_usuarios():
    # Leer el archivo txt
    ruta_txt = os.path.join(os.path.dirname(__file__), "data", "usuarios.txt")
    credenciales = {}
    try:
        with open(ruta_txt, "r", encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if ":" in linea:
                    usr, pwd = linea.split(":", 1)
                    credenciales[usr] = pwd
    except Exception as e:
        print(f"Error al cargar usuarios: {e}")
    return credenciales

class VentanaLogin(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Inicio de Sesión - 2do Parcial")
        self.geometry("400x350")
        self.resizable(False, False)
        
        # Centrar
        self.eval('tk::PlaceWindow . center')
        
        self.credenciales = cargar_usuarios()
        
        ctk.CTkLabel(self, text="Bienvenido", font=("Arial", 24, "bold")).pack(pady=(40, 20))
        
        self.entry_user = ctk.CTkEntry(self, placeholder_text="Usuario", width=250)
        self.entry_user.pack(pady=10)
        
        self.entry_pass = ctk.CTkEntry(self, placeholder_text="Contraseña", width=250, show="*")
        self.entry_pass.pack(pady=10)
        
        self.lbl_error = ctk.CTkLabel(self, text="", text_color="red")
        self.lbl_error.pack(pady=5)
        
        self.btn_ingresar = ctk.CTkButton(self, text="Ingresar", command=self.validar_login, width=250)
        self.btn_ingresar.pack(pady=10)
        
        self.bind('<Return>', lambda e: self.validar_login())
        
    def validar_login(self):
        user = self.entry_user.get().strip()
        pwd = self.entry_pass.get().strip()
        
        if not user or not pwd:
            self.lbl_error.configure(text="Por favor, complete ambos campos")
            return
            
        if user in self.credenciales and self.credenciales[user] == pwd:
            self.destroy() # Cierra la ventana actual
            app = AppVentanaPrincipal()
            app.mainloop()
        else:
            self.lbl_error.configure(text="Usuario o contraseña incorrectos")

if __name__ == "__main__":
    app = VentanaLogin()
    app.mainloop()
