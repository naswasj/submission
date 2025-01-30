tujuan menggunakan analisis lanjutan dengan menggunakan time series analysis yaitu agar dapat melihat pola penyewaan berdasarkan musim. Kemudian untuk Clustering Manual yaitu untuk membagi hari menjadi rendah, sedang, dan tinggi berdasarkan jumlah penyewaan. Lalu ada kombinasi kedua analisis yaitu untuk menampilkan jumlah hari dalam tiap kategor penyewaan berdasarkan musim

# Cara menjalankan 
# Setup Environment - Anaconda
conda create --name main-ds python=3.12.7
conda activate main-ds
pip install -r requirements.txt

# Setup Environment - Shell/Terminal
mkdir submission
cd submission
pipenv install
pipenv shell
pip install -r requirements.txt

# Run steamlit app
streamlit run submission/dashboard/dashboard.py

