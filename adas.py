import streamlit as st

st.title('Aplikasi perhitungan normalitas dan persentase kadar')

st.write('Oleh Kelompok 9')
st.write('Ali Akbar Mustaqim (2219030)')
st.write('Jecly Nur Fauzan (2219088)')
st.write('Mafhum Shihab Khalwany (2219102)')
st.write('Muhammad Dzaki Pratama Putra (2219114)')
st.write('Rai Aria Yudistira (2219148)')


massa = st.number_input('Masukkan nilai massa',format='%.4f')
volume = st.number_input('Masukkan nilai volume')
BE1 = st.number_input('Masukkan nilai BE')
FP1 = st.number_input('Masukkan nilai F Pengali')

tombol = st.button('Hitung nilai normalitasnya')

nilai_normalitas1=massa/(BE1*volume*FP1)
if tombol:
    nilai_normalitas = massa/(BE1*volume*FP1)
    st.success(f'Nilai normalitas adalah {nilai_normalitas}')


Vtitran = st.number_input('Masukkan nilai volume titran (mL)')
Ntitran = st.number_input('Masukkan nilai normalitas titran',format='%.4f', value=(nilai_normalitas1))
BE2 = st.number_input('Masukkan nilai BEnya')
FP2 = st.number_input('Masukkan nilai F Pengalinya')
Vtitrat = st.number_input('Masukkan nilai volume titrat (mL)')

tombol = st.button('Hitung nilai kadarnya')



if tombol:
    nilai_kadar = (Vtitran*Ntitran*BE2*10**-3*FP2*100)/Vtitrat 
    st.success(f'Persentase kadarnya adalah {nilai_kadar}%')
    