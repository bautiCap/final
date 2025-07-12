import tkinter as tk  # Importamos tkinter explícitamente
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

import tickets
import servicio_smtp

# Crear la ventana principal con un tema de ttkbootstrap
root = ttk.Window(themename="flatly")  # Puedes cambiar a "darkly", "superhero", etc.
root.geometry("300x450")  # Ajustamos el tamaño para mejor estética
root.title("Help Desk")

def mostrar_menu():
    """Muestra el formulario principal."""
    for widget in root.winfo_children():
        widget.destroy()
    ttk.Label(root, text="Envie su consulta:", font=("Arial", 16, "bold")).pack(pady=10)
    
    ttk.Label(root, text="Nombre:").pack()
    name_entry = ttk.Entry(root, bootstyle=PRIMARY)
    name_entry.pack(pady=5)
    
    ttk.Label(root, text="Correo:").pack()
    email_entry = ttk.Entry(root, bootstyle=PRIMARY)
    email_entry.pack(pady=5)
    
    ttk.Label(root, text="Asunto:").pack()
    title_entry = ttk.Entry(root, bootstyle=PRIMARY)
    title_entry.pack(pady=5)
    
    ttk.Label(root, text="Descripción:").pack()
    desc_entry = tk.Text(root, height=5, width=30)
    desc_entry.pack(pady=5)
    
    ttk.Button(
        root,
        text="Crear Ticket",
        bootstyle=SUCCESS,
        command=lambda: crear_ticket(
            name_entry, email_entry, title_entry, desc_entry
        ),
    ).pack(pady=10)
    ttk.Button(root, text="Salir", bootstyle=DANGER, command=root.quit).pack(pady=5)


def crear_ticket(name_entry, email_entry, title_entry, desc_entry):
    """Crea un ticket, envía un correo y limpia los campos."""
    name = name_entry.get()
    email = email_entry.get()
    title = title_entry.get()
    description = desc_entry.get("1.0", tk.END).strip()  # Corregimos tk.END
    
    success, result = tickets.crear_ticket(name, email, title, description)
    if success:
        ticket = result
        email_result = servicio_smtp.send_email(ticket)
        if email_result is True:
            messagebox.showinfo("Éxito", "En breve será contactado por un administrador")
            # Limpiar los campos del formulario
            name_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            title_entry.delete(0, tk.END)
            desc_entry.delete("1.0", tk.END)
        else:
            messagebox.showerror("Error", f"Ticket creado, pero no se pudo enviar el correo: {email_result}")
    else:
        messagebox.showerror("Error", result)

# Iniciar el programa
mostrar_menu()
root.mainloop()