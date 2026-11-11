import pandas as pd
import streamlit as st
from data import DATA, TEXTS

texts = TEXTS[st.session_state.get("language", "en")]
data = DATA[st.session_state.get("language", "en")]
skills = data["skills"]
timeline = data["timeline"]

tab1, tab2 = st.tabs([texts["skills"]["tab"], texts["skills"]["education_tab"]])
with tab1:
    st.metric(label=texts["skills"]["skill_count"], value=len(skills))


    for skill in skills:
        col_metric, col_valeur = st.columns([3, 1])
        
        with col_metric:
            st.metric(label=texts["skills"]["skill"], value=skill)

        with col_valeur:
            st.metric(label=texts["skills"]["level"], value=(skills[skill]))

        st.progress(skills.get(skill) / 100)

    st.subheader(texts["skills"]["overview"])
    df = pd.DataFrame(list(skills.items()), columns=["skill", "level"])
    st.bar_chart(df, x="skill", y="level")


with tab2:
    st.subheader(texts["skills"]["education"])
    for period, degree in timeline:
        with st.container(border=True):
            st.markdown(f"**{period}**")
            st.write(degree)
    
