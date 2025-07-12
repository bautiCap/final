"""Interfaz gráfica para un sistema de Help Desk básico.

Este módulo crea una ventana con ttkbootstrap para que los usuarios ingresen
tickets de soporte con nombre, correo, asunto y descripción. Los tickets se
gestionan mediante el módulo `tickets` y se envían al administrador por correo
usando `servicio_smtp`.
"""

import tkinter as tk
from tkinter import messagebox

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import servicio_smtp
import tickets


def main():
    """Inicia la aplicación creando la ventana principal."""
    root = ttk.Window(themename="flatly")
    root.geometry("300x500")
    root.title("Help Desk")
    mostrar_menu(root)
    root.mainloop()


def mostrar_menu(root: ttk.Window) -> None:
    """Muestra el formulario principal para crear tickets.

    Args:
        root: Ventana principal de la aplicación.
    """
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
        command=lambda: crear_ticket(name_entry, email_entry, title_entry, desc_entry),
    ).pack(pady=10)

    ttk.Button(root, text="Salir", bootstyle=DANGER, command=root.quit).pack(pady=5)


def crear_ticket(name_entry: ttk.Entry, email_entry: ttk.Entry, title_entry: ttk.Entry, desc_entry: tk.Text) -> None:
    """Crea un ticket, envía un correo y limpia los campos.

    Args:
        name_entry: Campo de entrada para el nombre.
        email_entry: Campo de entrada para el correo.
        title_entry: Campo de entrada para el asunto.
        desc_entry: Campo de texto para la descripción.
    """
    name = name_entry.get()
    email = email_entry.get()
    title = title_entry.get()
    description = desc_entry.get("1.0", tk.END).strip()

    success, result = tickets.crear_ticket(name, email, title, description)
    if success:
        ticket = result
        email_result = servicio_smtp.send_email(ticket)
        if email_result is True:
            messagebox.showinfo("Mensaje enviado con exito", "En breve será contactado por un administrador")
            name_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            title_entry.delete(0, tk.END)
            desc_entry.delete("1.0", tk.END)
        else:
            messagebox.showerror("Error", f"Ticket creado, pero no se pudo enviar el correo: {email_result}")
    else:
        messagebox.showerror("Error", result)

#Inicio del programa
if __name__ == "__main__":
    main()