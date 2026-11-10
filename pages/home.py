import streamlit as st

from data import PROFILE, PROJECTS, SKILLS


st.title(f"Hi, I'm {PROFILE['name']}")
st.subheader(PROFILE["title"])
left, right = st.columns([1, 2])
with left:
    st.image("assets/photo.png", width=220)
with right:
    st.write(PROFILE["about"])
#TODO: city and e-mail, then a button to download assets/cv.pdf

with open("assets/cv.pdf", "rb") as f:
    st.download_button("Download my CV", f, file_name="cv.pdf")

st.divider()

st.metric(label="Nombre de projets", value=len(PROJECTS))
st.metric(label="Nombre de skills", value=len(SKILLS))



best_skill = max(SKILLS, key=SKILLS.get)


col_metric, col_valeur = st.columns([3, 1])

with col_metric:
    st.metric(label="Meilleure compétence", value=best_skill)

with col_valeur:
    st.metric(label="Niveau", value=(SKILLS[best_skill]))


st.progress(SKILLS.get(best_skill) / 100) 



