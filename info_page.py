import streamlit as st
import pandas as pd

def show_info_page():
    st.title("Informasi Sistem Indeks Kualitas Udara (AQI)")
    
    # Penjelasan Sistem
    st.header("Tentang Sistem AQI")
    st.write("""
    Sistem Indeks Kualitas Udara (AQI) adalah sistem yang digunakan untuk mengukur dan 
    melaporkan tingkat polusi udara. Sistem ini menggunakan metode Fuzzy Logic dengan 
    mempertimbangkan 6 parameter polutan utama:
    
    1. **PM2.5** - Particulate Matter ≤ 2.5 µm
    2. **PM10** - Particulate Matter ≤ 10 µm
    3. **CO** - Karbon Monoksida
    4. **NO2** - Nitrogen Dioksida
    5. **O3** - Ozon
    6. **SO2** - Sulfur Dioksida
    
    Setiap parameter ini diukur dan dievaluasi menggunakan logika fuzzy untuk menghasilkan 
    nilai AQI yang mencerminkan kualitas udara secara keseluruhan.
    """)
    
    # Tabel Kategori
    st.header("Kategori Kualitas Udara")
    
    # Data untuk tabel kategori
    data = {
        'Kategori': ['Baik', 'Sedang', 'Buruk', 'Tidak Sehat', 'Sangat Tidak Sehat', 'Berbahaya'],
        'Rentang AQI': ['0-50', '50-100', '100-200', '200-300', '300-400', '400->500'],
        'Penjelasan': [
            'Kualitas udara memuaskan dan polusi udara menimbulkan risiko kecil atau tidak ada risiko.',
            'Kualitas udara dapat diterima namun beberapa polutan dapat menimbulkan masalah kesehatan ringan bagi sebagian kecil orang yang sangat sensitif.',
            'Anggota kelompok sensitif mungkin mengalami dampak kesehatan. Masyarakat umum cenderung tidak terpengaruh.',
            'Setiap orang mungkin mulai mengalami dampak kesehatan; anggota kelompok sensitif mungkin mengalami dampak kesehatan yang lebih serius.',
            'Peringatan kesehatan yang mengindikasikan bahwa setiap orang dapat mengalami dampak kesehatan yang lebih serius.',
            'Peringatan kesehatan darurat. Seluruh populasi kemungkinan terkena dampak.'
        ],
        'Rekomendasi': [
            'Lakukan aktivitas di luar ruangan seperti biasa',
            'Kurangi aktivitas fisik yang berkepanjangan di luar ruangan bagi kelompok sensitif',
            'Kurangi aktivitas fisik yang berkepanjangan di luar ruangan',
            'Hindari aktivitas fisik yang berkepanjangan di luar ruangan',
            'Hindari semua aktivitas fisik di luar ruangan',
            'Tetap di dalam ruangan dan tutup semua jendela'
        ]
    }
    
    df = pd.DataFrame(data)
    
    # Styling untuk tabel
    st.markdown("""
    <style>
    .dataframe {
        font-size: 14px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Menampilkan tabel dengan warna yang sesuai
    st.dataframe(df.style.apply(lambda x: ['background-color: #9EFF9E' if x.name == 0
                                         else 'background-color: #FFFF9E' if x.name == 1
                                         else 'background-color: #FFB84D' if x.name == 2
                                         else 'background-color: #FF9E9E' if x.name == 3
                                         else 'background-color: #FF69B4' if x.name == 4
                                         else 'background-color: #FF4D4D' for i in range(len(x))], axis=1))
    
    # Informasi Tambahan
    st.header("Informasi Parameter Polutan")
    
    # Expand/collapse sections untuk setiap polutan
    with st.expander("PM2.5 (Particulate Matter ≤ 2.5 µm)"):
        st.write("""
        Partikel halus dengan diameter 2.5 mikrometer atau lebih kecil. 
        Sumber: Pembakaran, kendaraan bermotor, industri.
        Dampak: Dapat masuk ke dalam paru-paru dan aliran darah.
        """)
    
    with st.expander("PM10 (Particulate Matter ≤ 10 µm)"):
        st.write("""
        Partikel dengan diameter 10 mikrometer atau lebih kecil.
        Sumber: Debu jalan, konstruksi, industri.
        Dampak: Dapat mengganggu sistem pernapasan.
        """)
    
    with st.expander("CO (Karbon Monoksida)"):
        st.write("""
        Gas tidak berwarna dan tidak berbau.
        Sumber: Kendaraan bermotor, pembakaran tidak sempurna.
        Dampak: Mengurangi kemampuan darah mengangkut oksigen.
        """)
    
    with st.expander("NO2 (Nitrogen Dioksida)"):
        st.write("""
        Gas berwarna kecoklatan dan berbau tajam.
        Sumber: Kendaraan bermotor, pembangkit listrik.
        Dampak: Iritasi saluran pernapasan, memperburuk asma.
        """)
    
    with st.expander("O3 (Ozon)"):
        st.write("""
        Gas tidak berwarna dengan bau tajam.
        Sumber: Reaksi kimia polutan di udara dengan sinar matahari.
        Dampak: Iritasi mata dan saluran pernapasan, memperburuk asma.
        """)
    
    with st.expander("SO2 (Sulfur Dioksida)"):
        st.write("""
        Gas tidak berwarna dengan bau tajam.
        Sumber: Pembangkit listrik, industri, kendaraan diesel.
        Dampak: Iritasi saluran pernapasan, memperburuk asma.
        """)

if __name__ == "__main__":
    show_info_page()