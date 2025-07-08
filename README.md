
# 📊 Data Preprocessing & PCA Project

Proyek ini menunjukkan alur kerja *data preprocessing* menggunakan `pandas`, `scikit-learn`, dan `scipy`, serta penerapan **Principal Component Analysis (PCA)** untuk reduksi dimensi. Dataset yang digunakan bersifat sintetis dan dihasilkan secara otomatis.

---

## 📁 Struktur Proyek

```
.
├── data_generator.py    # Menghasilkan data simulasi dan menyimpannya dalam CSV
├── main.py              # Script utama untuk preprocessing dan PCA
└── hasil/
    └── data.csv         # Dataset hasil generate
```

---

## ⚙️ Fitur Utama

### `data_generator.py`
- Membuat 1.000 data sampel dengan fitur:
  - `age` (numerik)
  - `salary` (numerik, dengan sebagian data missing)
  - `gender` (kategori)
  - `city` (kategori)
- Menambahkan 50 data `salary` dengan nilai NaN.
- Menambahkan 20 data duplikat.
- Menyimpan dataset ke `hasil/data.csv`.

### `main.py`
- **Cleaning Data**:
  - Mengisi nilai hilang di kolom numerik dengan median.
  - Menghapus duplikat.
  - Menghapus outlier menggunakan Z-score (> 3).
- **Encoding**:
  - One-hot encoding kolom `gender` dan `city`.
- **Normalisasi**:
  - Standarisasi data numerik.
- **Data Splitting**:
  - Train (70%), Validation (15%), Test (15%).
- **Reduksi Dimensi**:
  - Menggunakan PCA (2 komponen utama).

---

## ▶️ Cara Menjalankan

### 1. Persiapkan Lingkungan
Pastikan Python dan `pip` sudah terpasang.

> 💡 Gunakan virtual environment jika diperlukan:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 2. Install Dependencies

```bash
pip install pandas numpy scikit-learn scipy
```

### 3. Generate Dataset

Jalankan script untuk membuat data:
```bash
python data_generator.py
```

Dataset `data.csv` akan disimpan di folder `hasil/`.

### 4. Jalankan Proses Preprocessing + PCA

```bash
python main.py
```

Output akan menampilkan dimensi dari training, validation, dan test set.

---

## 📦 Output

Contoh output di terminal:

```
Shape of Training Data: (679, 9)
Shape of Validation Data: (146, 9)
Shape of Test Data: (146, 9)
```

> 📉 Data asli: 1000 sampel  
> ➕ Ditambah duplikat: 1020 sampel  
> 🔍 Setelah preprocessing (missing, duplikat, outlier): ~971 sampel  
> 📦 Setelah split: 70% train, 15% val, 15% test

---

## 📌 Catatan
- PCA dilakukan setelah pembagian data agar tidak terjadi *data leakage*.
- Outlier hanya dihapus dari kolom numerik.
- One-hot encoding menghindari *dummy variable trap* (`drop="first"`).

---

## 🧠 Cocok Untuk Belajar
- Data wrangling & cleaning
- Encoding & normalisasi
- Train/test split
- Reduksi dimensi (PCA)

---
Created with by Ariel Shakaramiro
