import re
import streamlit as st
import csv
from datetime import datetime
import os
from data import TEXTS

texts = TEXTS[st.session_state.get("language", "en")]

st.title(texts["nav"]["contact"])

def check(name, email, message, contact_texts):
    name = name.strip()
    email = email.strip()
    message = message.strip()

    if not name:
        return contact_texts["empty_name"]

    email_regle = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_regle, email):
        return contact_texts["invalid_email"]
    if len(message) < 10:
        return contact_texts["short_message"]
    return ""

"""On utilise le mode "a" (append) parce qu'il permet d'ajouter les nouveaux messages directement à la fin du fichier CSV sans toucher à ceux qui sont déjà enregistrés. Si on utilisait le mode "w" (write), le fichier serait complètement réinitialisé et écrasé à chaque fois qu'un visiteur envoie un nouveau formulaire, et on perdrait tous les anciens messages."""

def save(name, email, message):
    file_existe = os.path.exists("messages.csv")
    with open("messages.csv", mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_existe:
            writer.writerow(["date", "name", "email", "message"])

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([now, name, email, message])

st.subheader(texts["contact"]["title"])

with st.form("contact_form"):
    name = st.text_input(texts["contact"]["name"])
    email = st.text_input(texts["contact"]["email"])
    message = st.text_area(texts["contact"]["message"])
    submited = st.form_submit_button(texts["contact"]["send"])

if submited:
    erreur = check(name, email, message, texts["contact"])
    if erreur == "":
        save(name, email, message)
        st.success(texts["contact"]["success"])
    else:
        st.error(erreur)
