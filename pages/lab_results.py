import pandas as pd
import streamlit as st
from data import TEXTS

texts = TEXTS[st.session_state.get("language", "en")]

@st.cache_data #on lit et stocke en mémoire le csv la premiere fois, puis on utlise la version en mémoire pour éviter de le lire a partir de disque a chauqe fois
def load_datas():

    return pd.read_csv("assets/search_timings.csv")
    

try:
    df_timings = load_datas()

    st.subheader(texts["labs"]["search_title"])
    st.write(
        texts["labs"]["search_description"]
    )

    df_search = df_timings[df_timings["benchmark"] == "search"]
    df_search_pivot = df_search.pivot(
        index="size", columns="algorithm", values="average_time_seconds"
    )
    st.line_chart(df_search_pivot)

    st.subheader(texts["labs"]["bst_title"])
    st.write(texts["labs"]["bst_description"])

    df_bst = df_timings[df_timings["benchmark"] == "bst_shape_comparison"]

    st.bar_chart(
        df_bst,
        x="algorithm",
        y="average_time_seconds",
    )

except FileNotFoundError:
    
    st.error(
        texts["labs"]["missing_file"]
    )