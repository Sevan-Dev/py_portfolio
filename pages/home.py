import streamlit as st

from data import PROFILE, TEXTS, DATA

texts = TEXTS[st.session_state.get("language", "en")]
data = DATA[st.session_state.get("language", "en")]
profile = data["profile"]
projects = data["projects"]
skills = data["skills"]

st.title(texts["home"]["greeting"].format(name=PROFILE["name"]))
st.subheader(profile["title"])
left, right = st.columns([1, 2])

"""
Sur un écran mobile, Streamlit gère automatiquement le responsive design : au lieu d'afficher les colonnes (st.columns) côte à côte ce qui les rendrait beaucoup trop étroites et illisibles, l'interface les réorganise et les empile verticalement les unes sous les autres pour s'adapter à la largeur de l'écran.
"""
with left:
    st.image("assets/photo.png", width=220)
with right:
    st.write(profile["about"])
#TODO: city and e-mail, then a button to download assets/cv.pdf

with open("assets/cv.pdf", "rb") as f:
    st.download_button(texts["home"]["download_cv"], f, file_name="cv.pdf")

st.divider()

st.metric(label=texts["home"]["project_count"], value=len(projects))
st.metric(label=texts["home"]["skill_count"], value=len(skills))



best_skill = max(skills, key=skills.get)


col_metric, col_valeur = st.columns([3, 1])

with col_metric:
    st.metric(label=texts["home"]["best_skill"], value=best_skill)

with col_valeur:
    st.metric(label=texts["home"]["level"], value=(skills[best_skill]))

st.progress(skills.get(best_skill) / 100)

