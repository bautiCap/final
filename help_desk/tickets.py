import json
import os
import uuid
from datetime import datetime

# Ruta absoluta al directorio donde está tickets.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TICKETS_FILE = os.path.join(BASE_DIR, "tickets.json")

def load_tickets():
    """Carga el archivo tickets.json o crea uno vacío si no existe."""
    if not os.path.exists(TICKETS_FILE):
        with open(TICKETS_FILE, "w") as f:
            json.dump([], f)
    with open(TICKETS_FILE, "r") as f:
        return json.load(f)

def guardar_tickets(tickets):
    """Guarda los tickets en tickets.json."""
    with open(TICKETS_FILE, "w") as f:
        json.dump(tickets, f, indent=4)

def crear_ticket(name, email, title, description):
    """Crea un nuevo ticket."""
    if not name or not email or not title or not description:
        return False, "Todos los campos son obligatorios"
    ticket = {
        "id": str(uuid.uuid4()),
        "user": name,  # Usamos 'name' en lugar de 'username'
        "email": email,
        "title": title,
        "description": description,
        "status": "Abierto",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    tickets = load_tickets()
    tickets.append(ticket)
    guardar_tickets(tickets)
    return True, ticket