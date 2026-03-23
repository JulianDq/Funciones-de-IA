import tkinter as tk
import ventana_principal

USUARIO_VALIDO = "admin"
CONTRASENA_VALIDA = "1234"

def login():
    user = entry_user.get()
    pwd = entry_pass.get()
    
    if user == USUARIO_VALIDO and pwd == CONTRASENA_VALIDA:
        root.destroy()
        ventana_principal.abrir()
    else:
        lbl_msg.config(text="Usuario o Contraseña Incorrectos")

root = tk.Tk()
root.title("Login")

# Fila 0: Usuario
tk.Label(root, text="Usuario").grid(row=0, column=0, padx=10, pady=5)
entry_user = tk.Entry(root)
entry_user.grid(row=0, column=1, padx=10, pady=5)

# Fila 1: Contraseña
tk.Label(root, text="Contraseña").grid(row=1, column=0, padx=10, pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.grid(row=1, column=1, padx=10, pady=5)

# Fila 2: Botón Ingresar
tk.Button(root, text="Ingresar", command=login).grid(row=2, column=0, columnspan=2, pady=10)

# Fila 3: Mensaje de Error
lbl_msg = tk.Label(root, text="", fg="red")
lbl_msg.grid(row=3, column=0, columnspan=2)

root.bind('<Return>', lambda e: login())
entry_user.focus()
root.mainloop()
