import streamlit as st
from data import PROFILE, TEXTS

st.set_page_config(page_title=PROFILE["name"], page_icon=":briefcase:", layout="wide")

language_labels = {"en": TEXTS["en"]["english"], "fr": TEXTS["fr"]["french"]}
language = st.session_state.get("language", "en")

with st.sidebar:

    selected_language = st.radio(
        TEXTS[language]["language"],
        options=list(language_labels),
        format_func=language_labels.get,
        index=list(language_labels).index(language),
    )

    st.session_state["language"] = selected_language


    language = selected_language
    texts = TEXTS[language]

    st.image("assets/photo.png", width=120)
    st.markdown(f"### {PROFILE['name']}")
    st.link_button(texts["github"], PROFILE["github"], icon=":material/code:")
    st.link_button(texts["linkedin"], PROFILE["linkedin"], icon=":material/code:")

pages = [st.Page("pages/home.py", title=texts["nav"]["about"], icon=":material/person:", default=True),
st.Page("pages/projects.py", title=texts["nav"]["projects"], icon=":material/code:"),
st.Page("pages/skills.py", title=texts["nav"]["skills"], icon=":material/bar_chart:"),
st.Page("pages/contact.py", title=texts["nav"]["contact"], icon=":material/mail:"),
st.Page("pages/lab_results.py", title=texts["nav"]["labs"], icon=":material/science:")]

st.navigation(pages).run()