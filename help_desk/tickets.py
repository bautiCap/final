"""Gestión de tickets para el sistema de Help Desk.

Este módulo maneja la creación y almacenamiento de tickets en un archivo JSON
ubicado en el mismo directorio que el módulo.
"""

import json
import os
import uuid
from datetime import datetime

# Ruta absoluta al archivo tickets.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TICKETS_FILE = os.path.join(BASE_DIR, "tickets.json")


def cargar_tickets() -> list:
    """Carga los tickets desde el archivo JSON.

    Returns:
        Lista de tickets. Si el archivo no existe, crea uno vacío y retorna una lista vacía.
    """
    if not os.path.exists(TICKETS_FILE):
        with open(TICKETS_FILE, "w") as f:
            json.dump([], f)
    with open(TICKETS_FILE, "r") as f:
        return json.load(f)


def guardar_tickets(tickets: list) -> None:
    """Guarda los tickets en el archivo JSON.

    Args:
        tickets: Lista de tickets a guardar.
    """
    with open(TICKETS_FILE, "w") as f:
        json.dump(tickets, f, indent=4)


def crear_ticket(name: str, email: str, title: str, description: str) -> tuple[bool, dict | str]:
    """Crea un nuevo ticket y lo guarda.

    Args:
        name: Nombre del usuario.
        email: Correo electrónico del usuario.
        title: Título del ticket.
        description: Descripción del ticket.

    Returns:
        Tupla con (éxito, resultado). Si éxito es True, resultado es el ticket creado;
        si False, resultado es un mensaje de error.
    """
    if not name or not email or not title or not description:
        return False, "Todos los campos son obligatorios"

    ticket = {
        "id": str(uuid.uuid4()),
        "user": name,
        "email": email,
        "title": title,
        "description": description,
        "status": "Abierto",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    tickets = cargar_tickets()
    tickets.append(ticket)
    guardar_tickets(tickets)
    return True, ticket