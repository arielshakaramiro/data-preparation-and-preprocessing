import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from scipy import stats

# Membaca dataset
data = pd.read_csv("hasil/data.csv")

# Menangani data yang hilang (hanya pada kolom numerik)
numeric_cols = data.select_dtypes(include=[np.number]).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].median())

# Menghapus data duplikat
data.drop_duplicates(inplace=True)

# Mengatasi outlier menggunakan Z-score hanya untuk kolom numerik
z_scores = np.abs(stats.zscore(data[numeric_cols]))
data = data[(z_scores < 3).all(axis=1)]

# Encoding variabel kategori
categorical_cols = ["gender", "city"]
encoder = OneHotEncoder(
    sparse_output=False, drop="first"
)  # drop="first" untuk menghindari dummy variable trap
categorical_encoded = encoder.fit_transform(data[categorical_cols])
encoded_df = pd.DataFrame(
    categorical_encoded, columns=encoder.get_feature_names_out(categorical_cols)
)

# Gabungkan kembali dataset
data = data.drop(columns=categorical_cols).reset_index(drop=True)
data = pd.concat([data, encoded_df], axis=1)

# Normalisasi fitur numerik
scaler = StandardScaler()
data[numeric_cols] = scaler.fit_transform(data[numeric_cols])

# Membagi data menjadi training, validation, dan test set
train_data, temp_data = train_test_split(data, test_size=0.3, random_state=42)
val_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=42)

# Reduksi Dimensi dengan PCA setelah split
pca = PCA(n_components=2)
train_pca = pca.fit_transform(train_data)
val_pca = pca.transform(val_data)
test_pca = pca.transform(test_data)

print("Shape of Training Data:", train_data.shape)
print("Shape of Validation Data:", val_data.shape)
print("Shape of Test Data:", test_data.shape)
