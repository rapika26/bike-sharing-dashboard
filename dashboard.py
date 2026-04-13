
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('main_data.csv')

st.title('Dashboard Bike Sharing 🚲')

# Filter
hour_range = st.slider('Pilih Jam', 0, 23, (0, 23))

filtered_df = df[(df['hr'] >= hour_range[0]) & (df['hr'] <= hour_range[1])]

# Grafik jam
st.subheader('Penyewaan per Jam')
hour_data = filtered_df.groupby('hr')['cnt'].mean()

fig, ax = plt.subplots()
hour_data.plot(ax=ax)
st.pyplot(fig)

# Grafik hari
st.subheader('Hari Kerja vs Libur')
day_data = filtered_df.groupby('workingday')['cnt'].mean()

fig2, ax2 = plt.subplots()
day_data.plot(kind='bar', ax=ax2)
ax2.set_xticklabels(['Libur', 'Kerja'], rotation=0)
st.pyplot(fig2)
