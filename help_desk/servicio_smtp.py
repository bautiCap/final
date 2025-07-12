# """Envío de correos electrónicos para notificar tickets al administrador.

# Este módulo configura y envía correos usando el protocolo SMTP.

import smtplib
from email.mime.text import MIMEText

# Configuración de correo
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = ""  # Cambia por un correo de Gmail, para que envie los tickets
SMTP_PASS = ""  # Cambia por la contraseña de aplicación TP_USER. ej: "sgyi dqbx hpwh bzzo". para saber como activar esta contraseña ir a README.md
ADMIN_EMAIL = ""  # Cambia por el correo del administrador que recibira el mail(puede ser el mismo que TP_USER)


def send_email(ticket: dict) -> bool | str:
    """Envía un correo al administrador con los detalles del ticket.

    Args:
        ticket: Diccionario con los datos del ticket (id, user, email, title, description, date).

    Returns:
        True si el correo se envía correctamente, o un mensaje de error si falla.
    """
    msg = MIMEText(
        f"Nuevo ticket #{ticket['id'][:8]}:\n"
        f"Usuario: {ticket['user']}\n"
        f"Correo: {ticket['email']}\n"
        f"Título: {ticket['title']}\n"
        f"Descripción: {ticket['description']}\n"
        f"Fecha: {ticket['date']}"
    )
    msg["Subject"] = f"Nuevo Ticket #{ticket['id'][:8]} - Help Desk"
    msg["From"] = SMTP_USER
    msg["To"] = ADMIN_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, ADMIN_EMAIL, msg.as_string())
        return True
    except Exception as e:
        return str(e)