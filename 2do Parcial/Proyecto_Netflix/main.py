from login_gui import VentanaLogin
import customtkinter as ctk

# Configuración global del tema de CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

if __name__ == "__main__":
    # Arrancar la aplicación desde la ventana de login
    app = VentanaLogin()
    app.mainloop()
