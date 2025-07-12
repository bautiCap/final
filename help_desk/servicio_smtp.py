"""sgyi dqbx hpwh bzzo bellapazprol@gmail.com"""

import smtplib
from email.mime.text import MIMEText

# Configuración de correo
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "bellapazprol@gmail.com"  # Cambia por tu correo
SMTP_PASS = "sgyi dqbx hpwh bzzo"  # Cambia por tu contraseña de aplicación
ADMIN_EMAIL = "bellapazprol@gmail.com"  # Cambia por el correo del administrador

def send_email(ticket):
    """Envía un correo al administrador con los detalles del ticket."""
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