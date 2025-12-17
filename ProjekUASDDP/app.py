import streamlit as st

st.set_page_config(
    page_title="Menu Utama",
    page_icon="📂",
    layout="centered"
    
)

st.title("🎮 GAME Streamlit")
st.header("Welcome to the Game!")
st.write("Silakan pilih game yang ada di sidebar")

st.sidebar.success("Pilih games di sini")
