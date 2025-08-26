import streamlit as st

import teori_dan_konsep
import simulasi_jangka_sorong
import simulasi_micrometer
import kuis_angka_penting
import analisis_data

st.set_page_config(page_title="Lab Pengukuran Virtual - Cahyadi Ariansah", page_icon="⚙️",layout="wide")

# Sidebar menu
menu = st.sidebar.radio("📌 Menu Utama", [
    "🏠 Home",
    "📏 Teori dan Konsep",
    "📐 Simulasi jangka sorong",
    "📐 Simulasi micrometer"
    "🔢 Kuis angka penting",
    "📊 Analisis data"
])

# Halaman utama
if menu == "🏠 Home":
    st.title("⚙️ Lab Pengukuran Virtual")
    st.markdown("""
    Selamat datang di **Lab Pengukuran Virtual by Cahyadi Ariansah** 🎓  

    Gunakan menu di sebelah kiri untuk mengakses:
    - 📏 Teori dan Konsep  
    - 📐 Simulasi jangka sorong
    - 📐 Simulasi micrometer  
    - 🔢 Kuis angka penting
    - 📊 Analisis Data  

    ✍️ *Didesain dan dikembangkan oleh* **Cahyadi Ariansah**
    """)

elif menu == "📏 Teori dan Konsep":
    teori_dan_konsep.show()

elif menu == "📐 Simulasi jangka sorong ":
    simulasi_jangka_sorong.show()

elif menu == "📐 Simulasi micrometer":
    simulasi_micrometer.show()

elif menu == "🔢 Kuis":
    kuis_angka_penting.show()

elif menu == "📊 Analisis Data":
    analisis_data.show()