import re
import streamlit as st
import csv
from datetime import datetime
import os

def check(name, email, message):
    name = name.strip()
    email = email.strip()
    message = message.strip()

    if not name:
        return "Le nom ne peut pas être vide."

    email_regle = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_regle, email):
        return "L'adresse email n'est pas valide."
    if len(message) < 10:
        return "Le message doit contenir au moins 10 caractères."
    return ""

def save(name, email, message):
    file_existe = os.path.exists("messages.csv")
    with open("messages.csv", mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_existe:
            writer.writerow(["date", "name", "email", "message"])

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([now, name, email, message])

st.subheader("Me contacter")

with st.form("contact_form"):
    name = st.text_input("Nom")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submited = st.form_submit_button("Envoyer")

if submited:
    erreur = check(name, email, message)
    if erreur == "":
        save(name, email, message)
        st.success("Merci ! Votre message a bien été envoyé.")
    else:
        st.error(erreur)
