import streamlit as st


st.set_page_config(page_title="Escape Room", page_icon="🗝️")
st.title("🗝️ Escape Room Puzzle - Streamlit")
st.write("Pecahkan teka-teki untuk keluar dari ruangan!")

# ------------------------ State ------------------------
if "stage" not in st.session_state:
    st.session_state.stage = 1
if "inventory" not in st.session_state:
    st.session_state.inventory = []
if "message" not in st.session_state:
    st.session_state.message = ""

st.subheader(f"Stage {st.session_state.stage}")
st.write(st.session_state.message)

# ------------------------ Stage 1 ------------------------
if st.session_state.stage == 1:
    st.write("Kamu berada dalam ruangan gelap. Ada **meja**, **lemari**, dan **pintu terkunci**.")
    choice = st.radio("Apa yang ingin kamu periksa?", ["Meja", "Lemari", "Pintu"], index=0)

    if st.button("Periksa"):
        if choice == "Meja":
            st.session_state.message = "Kamu menemukan **kunci kecil** di dalam laci!"
            if "kunci" not in st.session_state.inventory:
                st.session_state.inventory.append("kunci")
        elif choice == "Lemari":
            st.session_state.message = "Lemari terkunci dengan kode 3 digit. Kamu butuh petunjuk."
        elif choice == "Pintu":
            st.session_state.message = "Pintu terkunci rapat. Kamu butuh **kunci** untuk membukanya."

    if "kunci" in st.session_state.inventory and st.button("Gunakan kunci pada pintu"):
        st.session_state.stage = 2
        st.session_state.message = "Kamu membuka pintu dan masuk ke ruangan berikutnya."

# ------------------------ Stage 2 ------------------------
elif st.session_state.stage == 2:
    st.write("Ruangan ini memiliki **brankas angka**, **lukisan**, dan **kertas sobek** di lantai.")

    choice = st.radio("Apa yang ingin kamu lakukan?", ["Periksa kertas", "Lihat lukisan", "Coba buka brankas"])

    if st.button("Aksi"):
        if choice == "Periksa kertas":
            st.session_state.message = "Kertas itu bertuliskan: 'Jumlah sudut pada sebuah persegi'."
        elif choice == "Lihat lukisan":
            st.session_state.message = "Lukisan itu menunjukkan sebuah **persegi** besar berwarna merah."
        elif choice == "Coba buka brankas":
            st.session_state.message = "Masukkan kode di bawah."

    if choice == "Coba buka brankas":
        code = st.number_input("Masukkan kode 3 digit", value=0, min_value=0, max_value=999)
        if st.button("Buka brankas"):
            if code == 4:
                st.session_state.stage = 3
                st.session_state.message = "Brankas terbuka! Kamu menemukan **kartu akses**."
                st.session_state.inventory.append("kartu akses")
            else:
                st.session_state.message = "Kode salah!"

# ------------------------ Stage 3 ------------------------
elif st.session_state.stage == 3:
    st.write("Di ruangan terakhir, ada **pintu elektronik** dengan pemindai kartu.")

    if "kartu akses" in st.session_state.inventory:
        if st.button("Gunakan kartu akses"):
            st.session_state.stage = 4
            st.session_state.message = "Pintu terbuka! Kamu berhasil melarikan diri! 🎉"
    else:
        st.write("Kamu butuh kartu akses untuk keluar.")

# ------------------------ Stage 4 (End) ------------------------
elif st.session_state.stage == 4:
    st.success("🎉 Kamu berhasil menyelesaikan Escape Room!")
    if st.button("Main Lagi"):
        st.session_state.stage = 1
        st.session_state.inventory = []
        st.session_state.message = ""
        st.experimental_rerun()

# ------------------------ Inventory ------------------------
st.markdown("---")
st.subheader("Inventory Kamu")
st.write(st.session_state.inventory)

def run_simulator_interactive():
    print("Simulator berjalan...")