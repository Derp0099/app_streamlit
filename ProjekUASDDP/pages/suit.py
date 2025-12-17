import streamlit as st
import random
import time

st.set_page_config(page_title="Gunting Batu Kertas", page_icon="✊")

# ===== CSS SEDERHANA =====
st.markdown("""
<style>
.choice {
    font-size: 60px;
    animation: pop 0.4s ease;
    text-align: center;
}

@keyframes pop {
    from {transform: scale(0.3); opacity:0;}
    to {transform: scale(1); opacity:1;}
}

.center {
    text-align: center;
    font-size: 40px;
    animation: fade 0.5s ease;
}

@keyframes fade {
    from {opacity:0;}
    to {opacity:1;}
}
</style>
""", unsafe_allow_html=True)

# ===== GAME LOGIC =====
emoji = {"Gunting":"✌️", "Batu":"✊", "Kertas":"✋"}
pilihan = list(emoji.keys())

def cek(p1, p2):
    if p1 == p2:
        return "🤝 Seri"
    if (p1=="Gunting" and p2=="Kertas") or (p1=="Batu" and p2=="Gunting") or (p1=="Kertas" and p2=="Batu"):
        return "🏆 Player 1 Menang"
    return "🏆 Player 2 Menang"

# ===== UI =====
st.title("✊✋✌️ Gunting Batu Kertas")
mode = st.radio("Pilih Lawan:", ["🖥️ Komputer", "👥 Player 2"])

p1 = st.selectbox("Player 1", pilihan)
p2 = random.choice(pilihan) if mode=="🖥️ Komputer" else st.selectbox("Player 2", pilihan)

if st.button("🔥 Mainkan"):
    st.markdown("<div class='center'>3... 2... 1...</div>", unsafe_allow_html=True)
    time.sleep(0.8)

    st.markdown(
        f"<div class='choice'>{emoji[p1]} VS {emoji[p2]}</div>",
        unsafe_allow_html=True
    )

    st.success(cek(p1, p2))

