# Bike Sharing Dashboard 🚲

## Deskripsi
Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda berdasarkan waktu (jam) dan jenis hari (hari kerja vs hari libur) menggunakan dataset Bike Sharing.

---

## Setup Environment

### 1. Membuat Virtual Environment (Opsional tapi Direkomendasikan)

Buka CMD / Terminal:

python -m venv venv

Aktifkan virtual environment:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

### 2. Install Dependencies

Install semua library yang dibutuhkan:

pip install -r requirements.txt

---

## Menjalankan Dashboard

Masuk ke folder project:

cd submission

Jalankan aplikasi:

streamlit run dashboard/dashboard.py

Jika terjadi error:

python -m streamlit run dashboard/dashboard.py

---

## Struktur Direktori

submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── data/
│   ├── hour.csv
│   └── day.csv
├── notebook.ipynb
├── requirements.txt
├── README.md
└── url.txt

---

## Insight Analisis

### Berdasarkan Jam
- Penyewaan tertinggi terjadi pada jam 07.00–09.00 dan 16.00–18.00.
- Pola ini menunjukkan penggunaan sepeda sebagai transportasi kerja.

### Berdasarkan Hari
- Hari kerja memiliki penyewaan lebih tinggi dibanding hari libur.
- Hal ini menunjukkan penggunaan sepeda lebih dominan untuk aktivitas rutin.

---

## Dashboard
Dashboard dibuat menggunakan Streamlit untuk memvisualisasikan:
- Pola penyewaan berdasarkan jam
- Perbandingan hari kerja dan hari libur

---

## URL Dashboard
https://bike-sharing-dashboard-wdukgzee4dyryfrgdxxbfu.streamlit.app/

---

## Author
Nama: [Rapika Dahlan]  
Dicoding ID: [CDCC220D6X1867]
