# Bike Sharing Dashboard 🚲

## Deskripsi
Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda menggunakan dataset Bike Sharing. Analisis dilakukan untuk mengetahui pengaruh waktu (jam) dan hari (hari kerja vs hari libur) terhadap jumlah penyewaan sepeda.

---

## Setup Environment

### 1. Install Python
Pastikan Python sudah terinstall di komputer Anda.

### 2. Install Library
Jalankan perintah berikut pada CMD / Terminal:

pip install -r requirements.txt

---

## Menjalankan Dashboard

Masuk ke folder project:

cd submission

Jalankan aplikasi Streamlit:

python -m streamlit run dashboard.py

---

## Struktur Direktori

submission/
├── dashboard/
│   ├── main_data.csv
│   └── dashboard.py
├── data/
│   ├── hour.csv
│   └── day.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt

---

## Insight Analisis

### 1. Berdasarkan Jam
- Penyewaan sepeda meningkat pada jam sibuk, yaitu sekitar pukul 07.00–09.00 dan 16.00–18.00.
- Pola ini menunjukkan aktivitas commuting (berangkat dan pulang kerja).

### 2. Berdasarkan Hari
- Hari kerja memiliki jumlah penyewaan yang lebih tinggi dibandingkan hari libur.
- Hal ini menunjukkan sepeda lebih banyak digunakan untuk aktivitas rutin dibanding rekreasi.

---

## Dashboard
Dashboard interaktif dibuat menggunakan Streamlit untuk memvisualisasikan:
- Tren penyewaan berdasarkan jam
- Perbandingan hari kerja vs hari libur
