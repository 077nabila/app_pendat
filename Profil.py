import pandas as pd
import streamlit as st
# import plotly.express as px
import numpy as np
from sklearn.utils.validation import joblib

# intial template
# px.defaults.template = "plotly_dark"
# px.defaults.color_continuous_scale = "reds"

# create content
st.title('Prediksi harga perumahan berdasarkan latitude, longitude, dan house age')
st.write("========================================================================================")
st.write("""
Selamat datang di aplikasi Prediksi Harga perumahan berdasarkan latitude, longitude, dan house age
\nAplikasi ini untuk memprediksi harga perumahan berdasarkan latitude, longitude, dan house age
""")

# create content
# create content
st.markdown("#Profil")
st.title("Profil Saya")
st.container()
st.write(''' 
                \nSaya Nabila Regitasyari Irmawan dengan nomor induk mahasiswa 200411100077.  
                \nKali ini saya akan mencoba melakukan penambangan data dan harga perumahan berdasarkan latitude, longitude, dan house age
                \nApakah yang dimaksud dengan Data Mining???
                \nData Mining adalah proses pengumpulan dan pengolahan data yang bertujuan untuk mengekstrak informasi penting pada data.
                
                \nUntuk pertanyaan lebih lanjut bisa menghubungi saya melalui :
                \nEmail : nabilaregitasya@gmail.com  
                \nInstagram : @nabillaaree 
                \nSemoga bermanfaat:>
            ''')
           





