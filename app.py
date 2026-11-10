import streamlit as st
from data import PROFILE

st.set_page_config(page_title=PROFILE["name"], page_icon=":briefcase:", layout="wide")
with st.sidebar: # everything in this block goes to the sidebar
    st.image("assets/photo.png", width=120)
    st.markdown(f"### {PROFILE['name']}")
    st.link_button("GitHub", PROFILE["github"], icon=":material/code:")
    st.link_button("Linkedin", PROFILE["linkedin"], icon=":material/code:")
pages = [st.Page("pages/home.py", title="About me", icon=":material/person:", default=True),
st.Page("pages/projects.py", title="Projects", icon=":material/code:"),
st.Page("pages/skills.py", title="Skills", icon=":material/bar_chart:"),
st.Page("pages/contact.py", title="Contact", icon=":material/mail:")]
st.navigation(pages).run() # shows the menu and runs the chosen page