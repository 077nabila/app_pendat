import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import streamlit as st
# import plotly.express as px
import numpy as np
from sklearn.utils.validation import joblib
from io import StringIO, BytesIO
import urllib.request
import joblib
import time
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
import os,sys
from scipy import stats

# intial template
# px.defaults.template = "plotly_dark"
# px.defaults.color_continuous_scale = "reds"

st.markdown("# 3. Modeling Data")
    st.write("""
    <h5>modeling<h5>
    """, unsafe_allow_html=True)
    st.container()
    X=df_new.iloc[:,0:11].values
    y=df_new.iloc[:,11].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,stratify=y, random_state=42)
    algoritma = st.radio(
    "Pilih model yang anda inginkan untuk cek akurasi",
    ('KNN','Naive Bayes','Random Forest','Ensemble Stacking'))
    if algoritma=='KNN':
        model = KNeighborsClassifier(n_neighbors=3)
        filename='knn.pkl'
        st.write("""
        <h5>Pengertian</h5>
        """, unsafe_allow_html=True)
        st.write('''Algoritma KNN (K-Nearest Neighbour) mengasumsikan bahwa sesuatu yang mirip akan ada dalam jarak yang berdekatan atau bertetangga. 
        Artinya data-data yang cenderung serupa akan dekat satu sama lain. KNN menggunakan semua data yang tersedia dan 
        mengklasifikasikan data atau kasus baru berdasarkan ukuran kesamaan atau fungsi jarak. Data baru kemudian ditugaskan ke kelas 
        tempat sebagian besar data tetangga berada.''')
    elif algoritma=='Naive Bayes':
        model = GaussianNB()
        filename='naivebayes.pkl'
        st.write("""
        <h5>Pengertian</h5>
        """, unsafe_allow_html=True)
        st.write(''' Metode yang juga dikenal sebagai Naive Bayes Classifier ini menerapkan teknik supervised klasifikasi objek di masa depan dengan menetapkan
        label kelas ke instance/catatan menggunakan probabilitas bersyarat. Probabilitas bersyarat adalah ukuran peluang suatu peristiwa yang terjadi berdasarkan 
        peristiwa lain yang telah (dengan asumsi, praduga, pernyataan, atau terbukti) terjadi Rumus: P(A│B) = P(B│A)P(A)P(B). Adapun salah satu jenis naive bayes adalah gausian. 
        Distribusi Gaussian adalah asumsi pendistribusian nilai kontinu yang terkait dengan setiap fitur berisi nilai numerik. Ketika diplot, akan muncul kurva berbentuk lonceng
        yang simetris tentang rata-rata nilai fitur.''')
    elif algoritma=='Random Forest':
        model = RandomForestClassifier(n_estimators = 100)
        filename='randomforest.pkl'
        st.write("""
        <h5>Pengertian</h5>
        """, unsafe_allow_html=True)
        st.write(''' Random forest adalah kombinasi dari  masing – masing tree yang baik kemudian dikombinasikan ke dalam satu model. Random Forest bergantung pada sebuah
        nilai vector random dengan distribusi yang sama pada semua pohon yang masing masing decision tree memiliki kedalaman yang maksimal. Random forest adalah classifier 
        yang terdiri dari classifier yang berbentuk pohon {h(x, θ k ), k = 1, . . .} dimana θk adalah random vector yang diditribusikan secara independen dan masing masing 
        tree pada sebuah unit kan memilih class yang paling popular pada input x. Berikut ini karakteristik akurasi pada random forest.''')
    elif algoritma=='Ensemble Stacking':
        estimators = [
            ('rf_1', RandomForestClassifier(n_estimators=10, random_state=42)),
            ('knn_1', KNeighborsClassifier(n_neighbors=10))             
        ]
        model = StackingClassifier(estimators=estimators, final_estimator=GaussianNB())
        filename='stacking.pkl'
        st.write("""
        <h5>Pengertian</h5>
        """, unsafe_allow_html=True)
        st.write(''' Metode ensemble adalah algoritma dalam pembelajaran mesin (machine learning) dimana algoritma ini sebagai pencarian solusi prediksi terbaik dibandingkan dengan
        algoritma yang lain karena metode ensemble ini menggunakan beberapa algoritma pembelajaran untuk pencapaian solusi prediksi yang lebih baik daripada algoritma yang bisa diperoleh 
        dari salah satu pembelajaran algoritma kosituen saja. Stacking merupakan cara untuk mengkombinasi beberapa model, dengan konsep meta learner yang dipakai setelah bagging dan boosting. 
        Tidak seperti bagging dan boosting, stacking memungkinkan mengkombinasikan model dari tipe yang berbeda.''')
    model.fit(X_train, y_train)
    Y_pred = model.predict(X_test) 
    score=metrics.accuracy_score(y_test,Y_pred)
    loaded_model = pickle.load(open(filename, 'rb'))
    st.write("""
        <h5>Hasil Akurasi</h5>
        """, unsafe_allow_html=True)
    st.write(f"Akurasi : {score*100} %")

