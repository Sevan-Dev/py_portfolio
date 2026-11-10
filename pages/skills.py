import pandas as pd
import streamlit as st
from data import SKILLS, TIMELINE

tab1, tab2 = st.tabs(["Skills", "Education"])
with tab1:
    st.metric(label="Nombre de skills", value=len(SKILLS))


    for skill in SKILLS:
        col_metric, col_valeur = st.columns([3, 1])
        
        with col_metric:
            st.metric(label="Compétence", value=skill)

        with col_valeur:
            st.metric(label="Niveau", value=(SKILLS[skill]))

        st.progress(SKILLS.get(skill) / 100)

    st.subheader("Vue d'ensemble")
    df = pd.DataFrame(list(SKILLS.items()), columns=["skill", "level"])
    st.bar_chart(df, x="skill", y="level")


with tab2:
    st.subheader("Parcours académique")
    for period, degree in TIMELINE:
        with st.container(border=True):
            st.markdown(f"**{period}**")
            st.write(degree)
    

