# Bike Sharing Dashboard 🚲

## Deskripsi
Dashboard ini dibuat untuk menganalisis pola penyewaan sepeda berdasarkan waktu (jam) dan hari (hari kerja vs hari libur).

---

## Setup Environment

### 1. Install Python
Pastikan Python sudah terinstall di komputer.

### 2. Install Library
Jalankan perintah berikut di CMD / Terminal:

pip install -r requirements.txt

---

## Menjalankan Dashboard

Masuk ke folder project:

cd submission

Jalankan Streamlit:

python -m streamlit run dashboard.py

---

## Struktur Folder

submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── hour.csv
├── day.csv
├── notebook.ipynb
├── requirements.txt
└── README.md

---

## Insight
- Penyewaan sepeda meningkat pada jam sibuk (pagi dan sore)
- Hari kerja memiliki jumlah penyewaan lebih tinggi dibanding hari libur
