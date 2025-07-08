import pandas as pd
import numpy as np

# Set seed untuk memastikan hasil yang sama setiap kali dijalankan
np.random.seed(42)

# Menentukan jumlah sampel
num_samples = 1000

# Membuat fitur numerik
age = np.random.randint(18, 65, num_samples)  # Usia antara 18 hingga 65 tahun
salary = np.random.randint(30000, 150000, num_samples).astype(
    float
)  # Gaji antara 30k hingga 150k (diubah ke float untuk menangani NaN)

# Membuat fitur kategori
gender = np.random.choice(["Male", "Female"], num_samples)  # Jenis kelamin
city = np.random.choice(
    ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"], num_samples
)  # Kota asal

# Menambahkan nilai yang hilang pada fitur salary
missing_indices = np.random.choice(
    num_samples, size=50, replace=False
)  # Memilih indeks secara acak
salary[missing_indices] = np.nan  # Menetapkan NaN pada indeks terpilih

# Membuat DataFrame utama
data = pd.DataFrame({"age": age, "salary": salary, "gender": gender, "city": city})

# Menambahkan data duplikat
duplicate_indices = np.random.choice(
    num_samples, size=20, replace=False
)  # Memilih beberapa sampel secara acak
duplicates = data.iloc[
    duplicate_indices
].copy()  # Membuat salinan dari data yang akan diduplikasi

data = pd.concat(
    [data, duplicates], ignore_index=True
)  # Menggabungkan data asli dengan duplikat

# Menyimpan dataset ke dalam file CSV
file_path = "hasil/data.csv"
data.to_csv(file_path, index=False)
