import streamlit as st

# halaman utama
st.title('Aplikasi Perhitungan Luas Bangun Datar')
st.header('ini buatan anak Sistem Informasi')

# sidebar
menu = st.sidebar.selectbox('Menu', ['Luas Persegi', 'Luas Segitiga', 'Luas Lingkaran'])

if menu == 'Luas Persegi' :
    st.write('ini halaman untuk menghitung luas persegi')
    st.image('https://www.doyanblog.com/wp-content/uploads/2021/12/rumus-persegi.jpg.webp', caption='gambar persegi')
    def LuasPersegi(a):
        return a*a
    sisi = st.number_input('Silahkan masukkan nilai sisi', min_value=0)
    if st.button('Hitung'):
        luas = LuasPersegi(sisi)
        st.success(f'luas persegi adalah {luas}')
    
elif menu == 'Luas Segitiga':
    st.write('ini halaman untuk menghitung Luas segitiga')
    st.image('https://fti.ars.ac.id/img-blog/cara-mengitung-luas-segitiga-dengan-bahasa-pemograman-c', caption="gambar luas segitiga")
    def LuasSegitiga(a,t):
        return a*t/2
    a = st.number_input('Silahkan masukkan  nilai alas segitiga', min_value=0)
    t = st.number_input('Masukkan nilai tinggi segitiga', min_value=0)
    if st.button('Hitung'):
        luas = LuasSegitiga(a,t)
        st.success(f'Luas Segitiga adalah {luas}')
        
elif menu == 'Luas Lingkaran':
    st.write('ini halaman untuk menghitung nilai luas lingkaran')
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQc7ssoaLPi5AGwYVy1xXurNA9WC34XxY5VnQ&s', caption='gambar rumus lingkaran')
    def LuasLingkaran(r):
        return 22/7*r*r
    r = st.number_input('Silahkan masukkan jari-jari lingkaran', min_value=0)
    if st.button('Hitung'):
        luas = LuasLingkaran(r)
        st.success(f'luas Lingkaran adalah {luas}')
