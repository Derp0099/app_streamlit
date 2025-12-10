import streamlit as st

# halaman utama
st.title('Aplikasi Perhitungan Luas Bangun Datar')
st.header('ini buatan anak Sistem Informasi')

# sidebar
menu = st.sidebar.selectbox('Menu', ['Luas Persegi', 'Luas Segitiga', 'Luas Lingkaran'])

if menu == 'Luas Persegi' :
    st.write('ini halaman untuk menghitung luas persegi')
    st.image('https://uptdsmpn3bangkalan.sch.id/wp-content/uploads/2024/01/persegi-bangun-datar.webp', caption='gambar persegi')
    def LuasPersegi(a):
        return a*a
    sisi = st.number_input('Silahkan masukkan nilai sisi', min_value=0)
    if st.button('Hitung'):
        luas = LuasPersegi(sisi)
        st.success(f'luas persegi adalah {luas}')
    
elif menu == 'Luas Segitiga':
    st.write('ini halaman untuk menghitung luas segitiga')