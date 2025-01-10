import streamlit as st
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from rules import create_rules
from info_page import show_info_page

# Tambahkan pilihan halaman di sidebar
page = st.sidebar.selectbox("Pilih Halaman", ["Informasi AQI", "Kalkulator AQI"])

if page == "Kalkulator AQI":
    # 1. Definisi variabel input dan output
    pm25 = ctrl.Antecedent(np.arange(0, 446, 1), 'PM2.5')
    pm10 = ctrl.Antecedent(np.arange(0, 551, 1), 'PM10')
    co = ctrl.Antecedent(np.arange(0, 54166, 1), 'CO')
    no2 = ctrl.Antecedent(np.arange(0, 551, 1), 'NO2')
    o3 = ctrl.Antecedent(np.arange(0, 1502, 1), 'O3')
    so2 = ctrl.Antecedent(np.arange(0, 3001, 1), 'SO2')

    # Output AQI sebagai Consequent dengan nilai konstanta
    aqi = ctrl.Consequent(np.arange(0, 551, 1), 'AQI')

    # 2. Definisi fungsi keanggotaan untuk input
    pm25['baik'] = fuzz.trapmf(pm25.universe, [0, 0, 15, 45])
    pm25['sedang'] = fuzz.trimf(pm25.universe, [15, 45, 75])
    pm25['buruk'] = fuzz.trimf(pm25.universe, [45, 75, 105])
    pm25['tidak_sehat'] = fuzz.trimf(pm25.universe, [75, 105, 135])
    pm25['parah'] = fuzz.trimf(pm25.universe, [105, 185, 265])
    pm25['berbahaya'] = fuzz.trapmf(pm25.universe, [185, 315, 445, 445])

    pm10['baik'] = fuzz.trapmf(pm10.universe, [0, 0, 25, 75])
    pm10['sedang'] = fuzz.trimf(pm10.universe, [25, 75, 125])
    pm10['buruk'] = fuzz.trimf(pm10.universe, [75, 175, 275])
    pm10['tidak_sehat'] = fuzz.trimf(pm10.universe, [210, 300, 390])
    pm10['parah'] = fuzz.trimf(pm10.universe, [310, 390, 470])
    pm10['berbahaya'] = fuzz.trapmf(pm10.universe, [390, 470, 550, 550])

    co['baik'] = fuzz.trapmf(co.universe, [0, 0, 4165, 12500])
    co['sedang'] = fuzz.trimf(co.universe, [4165, 12500, 20835])
    co['buruk'] = fuzz.trimf(co.universe, [12505, 20835, 29165])
    co['tidak_sehat'] = fuzz.trimf(co.universe, [20835, 29165, 37495])
    co['parah'] = fuzz.trimf(co.universe, [29165, 37500, 45835])
    co['berbahaya'] = fuzz.trapmf(co.universe, [37505, 45835, 54165, 54165])

    no2['baik'] = fuzz.trapmf(no2.universe, [0, 0, 20, 60])
    no2['sedang'] = fuzz.trimf(no2.universe, [20, 60, 100])
    no2['buruk'] = fuzz.trimf(no2.universe, [75, 130, 185])
    no2['tidak_sehat'] = fuzz.trimf(no2.universe, [130, 185, 240])
    no2['parah'] = fuzz.trimf(no2.universe, [185, 295, 405])
    no2['berbahaya'] = fuzz.trapmf(no2.universe, [350, 450, 550, 550])

    o3['baik'] = fuzz.trapmf(o3.universe, [0, 0, 25, 75])
    o3['sedang'] = fuzz.trimf(o3.universe, [25, 75, 100])
    o3['buruk'] = fuzz.trimf(o3.universe, [80, 134, 188])
    o3['tidak_sehat'] = fuzz.trimf(o3.universe, [148, 188, 228])
    o3['parah'] = fuzz.trimf(o3.universe, [188, 470, 752])
    o3['berbahaya'] = fuzz.trapmf(o3.universe, [497, 999, 1501, 1501])

    so2['baik'] = fuzz.trapmf(so2.universe, [0, 0, 20, 60])
    so2['sedang'] = fuzz.trimf(so2.universe, [20, 60, 100])
    so2['buruk'] = fuzz.trimf(so2.universe, [60, 230, 400])
    so2['tidak_sehat'] = fuzz.trimf(so2.universe, [230, 590, 950])
    so2['parah'] = fuzz.trimf(so2.universe, [590, 1200, 1810])
    so2['berbahaya'] = fuzz.trapmf(so2.universe, [1200, 2100, 3000, 3000])

    # 3. Definisi fungsi keanggotaan untuk output AQI
    aqi['baik'] = fuzz.trapmf(aqi.universe, [0, 0, 25, 75])
    aqi['sedang'] = fuzz.trimf(aqi.universe, [25, 75, 125])
    aqi['buruk'] = fuzz.trimf(aqi.universe, [75, 150, 225])
    aqi['tidak_sehat'] = fuzz.trimf(aqi.universe, [150, 250, 350])
    aqi['parah'] = fuzz.trimf(aqi.universe, [250, 350, 450])
    aqi['berbahaya'] = fuzz.trapmf(aqi.universe, [350, 450, 550, 550])

    # 4. Membuat Aturan
    rules = create_rules(pm25, pm10, co, no2, o3, so2, aqi)

    # 5. Sistem kontrol Sugeno
    aqi_ctrl = ctrl.ControlSystem(rules)
    aqi_system = ctrl.ControlSystemSimulation(aqi_ctrl)

    # 6. Streamlit User Interface
    st.header("Air Quality Index (AQI) dengan Fuzzy Inference System Sugeno")
    st.caption("Silakan masukan nilai enam faktor polutan udara.")

    # Input fields
    pm25_input = st.number_input("Nilai PM2.5 (µg/m³)", min_value=0, max_value=445, step=1, value=None)
    pm10_input = st.number_input("Nilai PM10 (µg/m³)", min_value=0, max_value=550, step=1, value=None)
    co_input = st.number_input("Nilai CO (ppb)", min_value=0, max_value=54165, step=1, value=None)
    no2_input = st.number_input("Nilai NO2 (ppb)", min_value=0, max_value=550, step=1, value=None)
    o3_input = st.number_input("Nilai O3 (ppb)", min_value=0, max_value=1501, step=1, value=None)
    so2_input = st.number_input("Nilai SO2 (ppb)", min_value=0, max_value=3000, step=1, value=None)

    # Custom CSS for button color
    st.markdown("""
        <style>
        .stButton>button {
            background-color: #D32F2F;
            color: white;
            border: none;
        }
        .stButton>button:hover {
            background-color: #C62828;
        }
        </style>
        """, unsafe_allow_html=True)

    if st.button("Hitung AQI"):
        if pm25_input is not None and pm10_input is not None and co_input is not None and no2_input is not None and o3_input is not None and so2_input is not None:
            aqi_system.input['PM2.5'] = pm25_input
            aqi_system.input['PM10'] = pm10_input
            aqi_system.input['CO'] = co_input
            aqi_system.input['NO2'] = no2_input
            aqi_system.input['O3'] = o3_input
            aqi_system.input['SO2'] = so2_input

            # Proses inferensi
            aqi_system.compute()

            # Output AQI
            aqi_value = aqi_system.output['AQI']
            st.subheader(f"Indeks Kualitas Udara (AQI): {aqi_value:.1f}")

            # Tentukan kategori berdasarkan AQI
            if aqi_value <= 50:
                category = "Baik"
                recommendation = "Kualitas udara memuaskan dan polusi udara menimbulkan risiko kecil atau tidak ada risiko."
            elif aqi_value <= 100:
                category = "Sedang"
                recommendation = "Kualitas udara dapat diterima, namun mungkin ada risiko kesehatan kecil bagi kelompok sensitif."
            elif aqi_value <= 150:
                category = "Tidak Sehat bagi Kelompok Sensitif"
                recommendation = "Anggota kelompok sensitif mungkin mengalami efek kesehatan. Publik umum tidak mungkin terpengaruh."
            elif aqi_value <= 200:
                category = "Tidak Sehat"
                recommendation = "Setiap orang dapat mulai mengalami efek kesehatan. Anggota kelompok sensitif mungkin mengalami efek yang lebih serius."
            elif aqi_value <= 300:
                category = "Sangat Tidak Sehat"
                recommendation = "Peringatan kondisi darurat. Risiko kesehatan meningkat bagi semua orang."
            else:
                category = "Berbahaya"
                recommendation = "Kondisi kesehatan darurat. Semua orang lebih mungkin terpengaruh."

            # Tampilkan kategori dan rekomendasi
            st.subheader(f"Kategori: {category}")
            st.info(f"Rekomendasi: {recommendation}")
        else:
            st.error("Semua nilai harus diisi untuk menghitung AQI.")

else:
    # Tampilkan halaman informasi
    show_info_page()
