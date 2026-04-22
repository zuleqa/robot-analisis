import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Tajuk App
st.set_page_config(page_title="AI Data Robot", layout="wide")
st.title("🤖 Robot Analisis Database Universal")
st.write("Upload sebarang fail Excel/CSV untuk analisis mengikut kolum pilihan anda.")

# 2. Bahagian Upload Fail
uploaded_file = st.file_uploader("Pilih fail Excel (.xlsx) atau CSV", type=['csv', 'xlsx'])

if uploaded_file is not None:
    try:
        # Membaca data mengikut jenis fail
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file, low_memory=False)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.success(f"✅ Fail '{uploaded_file.name}' berjaya dibaca!")

        # --- BAHAGIAN BARU: ANALISIS MENGIKUT PILIHAN ---
        st.divider()
        st.subheader("🎯 Analisis Spesifik Kolum")
        
        all_columns = df.columns.tolist()
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Pilihan untuk 'Country' atau Kolum Pertama
            pilihan_1 = st.selectbox("Pilih Kolum Utama (cth: Country/Negara):", all_columns)
            if pilihan_1:
                stats1 = df[pilihan_1].value_counts().reset_index()
                stats1.columns = [pilihan_1, 'Jumlah']
                st.write(f"**Top 10 {pilihan_1}:**")
                st.table(stats1.head(10))
                
                fig1 = px.pie(stats1.head(10), values='Jumlah', names=pilihan_1, hole=0.4,
                             title=f"Agihan Top 10 {pilihan_1}")
                st.plotly_chart(fig1, use_container_width=True)

        with col2:
            # Pilihan untuk 'Part Number' atau Kolum Kedua
            pilihan_2 = st.selectbox("Pilih Kolum Kedua (cth: Part Number):", all_columns)
            if pilihan_2:
                stats2 = df[pilihan_2].value_counts().reset_index()
                stats2.columns = [pilihan_2, 'Jumlah']
                st.write(f"**Top 10 {pilihan_2}:**")
                st.table(stats2.head(10))
                
                fig2 = px.bar(stats2.head(10), x=pilihan_2, y='Jumlah', 
                             title=f"Kekerapan Top 10 {pilihan_2}", color='Jumlah')
                st.plotly_chart(fig2, use_container_width=True)

        # 3. Analisis Statistik (Robot Kira Automatik)
        st.divider()
        st.subheader("📊 Ringkasan Statistik Data")
        st.write(df.describe(include='all').fillna(''))

        # 4. Paparan Data Penuh
        with st.expander("🔍 Lihat Data Penuh (Raw Data)"):
            st.dataframe(df)

    except Exception as e:
        st.error(f"Alamak, ada masalah: {e}")
else:
    st.info("💡 Menunggu fail diupload. Anda boleh gunakan fail TOTO atau sebarang data lain.")
