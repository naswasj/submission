import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
@st.cache_data
def load_data():
    day_df = pd.read_csv("https://raw.githubusercontent.com/naswasj/submission/main/data/day.csv")
    hour_df = pd.read_csv("https://raw.githubusercontent.com/naswasj/submission/main/data/hour.csv")
    
    # Mapping season and day type
    season_mapping = {1: "Musim Dingin", 2: "Musim Semi", 3: "Musim Panas", 4: "Musim Gugur"}
    day_df["season"] = day_df["season"].map(season_mapping)
    day_df["day_type"] = day_df["holiday"].map({1: "Hari Libur", 0: "Hari Kerja"})
    hour_df["season"] = hour_df["season"].map(season_mapping)
    hour_df["day_type"] = hour_df["holiday"].map({1: "Hari Libur", 0: "Hari Kerja"})
    
    # Kategorisasi jumlah penyewaan
    def categorize_rentals(cnt):
        if cnt < 2000:
            return "Low"
        elif 2000 <= cnt < 5000:
            return "Medium"
        else:
            return "High"
    
    day_df["rental_category"] = day_df["cnt"].apply(categorize_rentals)
    
    # Kategorisasi waktu per jam
    def categorize_hour(hr):
        if 0 <= hr < 6:
            return "Malam"
        elif 6 <= hr < 12:
            return "Pagi"
        elif 12 <= hr < 18:
            return "Siang"
        else:
            return "Sore"
    
    hour_df["time_category"] = hour_df["hr"].apply(categorize_hour)
    
    return day_df, hour_df

# Load data
day_df, hour_df = load_data()

# Streamlit App
st.title("Dashboard Penyewaan Sepeda")

# Sidebar untuk memilih dataset
dataset_option = st.sidebar.radio("Pilih Dataset:", ["Harian (day_df)", "Jam (hour_df)"])

# Sidebar untuk memilih jenis visualisasi
st.sidebar.header("Pilih Visualisasi")
option = st.sidebar.radio("Pilih grafik:", ["Pengaruh Musim", "Hari Kerja vs Hari Libur", "Distribusi Penyewaan", "Distribusi Kategori Waktu"])

# Menentukan dataset yang digunakan
if dataset_option == "Harian (day_df)":
    df = day_df
else:
    df = hour_df

# Menampilkan grafik berdasarkan pilihan pengguna
if option == "Pengaruh Musim":
    st.subheader("Pengaruh Musim terhadap Penyewaan Sepeda")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="season", y="cnt", data=df, hue="season", palette="Blues_d", errorbar=None, ax=ax)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Jumlah Penyewaan")
    ax.set_title("Pengaruh Musim terhadap Penyewaan Sepeda")
    st.pyplot(fig)

elif option == "Hari Kerja vs Hari Libur":
    st.subheader("Jumlah Penyewaan Sepeda pada Hari Kerja vs Hari Libur")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="day_type", y="cnt", data=df, hue="holiday", palette="coolwarm", errorbar=None, ax=ax)
    ax.set_xlabel("Tipe Hari")
    ax.set_ylabel("Jumlah Penyewaan")
    ax.set_title("Hari Kerja vs Hari Libur")
    st.pyplot(fig)

elif option == "Distribusi Penyewaan":
    st.subheader("Distribusi Penyewaan berdasarkan Musim dan Hari")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x="season", hue="day_type", data=df, palette="coolwarm", ax=ax)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Jumlah Hari")
    ax.set_title("Distribusi Penyewaan berdasarkan Musim")
    st.pyplot(fig)

elif option == "Distribusi Kategori Waktu":
    if dataset_option == "Jam (hour_df)":
        st.subheader("Distribusi Penyewaan berdasarkan Kategori Waktu")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.countplot(x="time_category", hue="season", data=df, palette="coolwarm", ax=ax)
        ax.set_xlabel("Kategori Waktu")
        ax.set_ylabel("Jumlah Penyewaan")
        ax.set_title("Distribusi Penyewaan berdasarkan Kategori Waktu")
        st.pyplot(fig)
    else:
        st.warning("Visualisasi ini hanya tersedia untuk dataset jam (hour_df).")
