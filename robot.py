import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Tajuk App
st.set_page_config(page_title="AI Data Robot", layout="wide")
st.title("🤖 Robot Analisis Database Syarikat")
st.write("Sila upload fail Excel anda di bawah untuk analisis automatik.")

# 2. Bahagian Upload Fail
uploaded_file = st.file_uploader("Pilih fail Excel (.xlsx) atau CSV", type=['csv', 'xlsx'])

if uploaded_file is not None:
    try:
        # Membaca data mengikut jenis fail
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.success("✅ Fail berjaya dibaca!")

        # 3. Analisis Statistik (Robot Kira Automatik)
        st.subheader("📊 Rumusan Statistik (Robot Calc)")
        st.write(df.describe())

        # 4. Paparan Data Penuh
        with st.expander("Lihat Data Penuh"):
            st.dataframe(df)

        # 5. Graf Automatik (Jika ada data nombor)
        st.subheader("📈 Visualisasi Data")
        kolum_nombor = df.select_dtypes(include=['number']).columns.tolist()
        
        if kolum_nombor:
            pilihan = st.selectbox("Pilih kolum untuk dibuat graf:", kolum_nombor)
            fig = px.bar(df, y=pilihan, title=f"Analisis Kolum: {pilihan}")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Tiada kolum bernombor dikesan untuk buat graf.")

    except Exception as e:
        st.error(f"Alamak, ada masalah: {e}")
else:
    st.info("💡 Menunggu fail diupload untuk memulakan analisis.")