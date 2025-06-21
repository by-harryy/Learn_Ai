"""
Program Utilitas dengan Berbagai Fungsi Analisis Data

Program ini berisi beberapa fungsi utilitas untuk:
1. Memberikan sapaan berdasarkan waktu
2. Menghitung statistik dasar
3. Menganalisis data penjualan
4. Analisis data game

Dependencies:
- datetime: untuk operasi waktu
- numpy: untuk perhitungan numerik
- pandas: untuk manipulasi data
"""

from datetime import datetime
import numpy as np
import pandas as pd

def sapaan():
    """
    Mengembalikan sapaan berdasarkan waktu saat ini
    
    Returns:
        str: "Selamat pagi" (jam 00-10)
             "Selamat siang" (jam 11-17)
             "Selamat malam" (jam 18-23)
    """
    waktu = datetime.now().hour
    if waktu < 11:
        return "Selamat pagi"
    elif waktu < 18:
        return "Selamat siang"
    else:
        return "Selamat malam"


def sapa(nama):
    """
    Memberikan salam personal dengan menyertakan nama
    
    Args:
        nama (str): Nama orang yang disapa
        
    Returns:
        str: Salam dengan format "halo [nama] [waktu]"
    """
    return f"halo {nama} {sapaan()}"

# Contoh penggunaan fungsi sapa
print(sapa("Harry"))


print("\n---Hitung statistik-----------------------")

def hitung_statistik(data):
    """
    Menghitung statistik dasar dari sekumpulan data numerik
    
    Args:
        data (list): List berisi angka-angka
        
    Returns:
        str: String berisi rata-rata, nilai maksimum, dan minimum
    """
    rata_rata = np.mean(data)
    maksimum = np.max(data)
    minimum = np.min(data)
    return f"Rata-rata: {rata_rata} \nMax: {maksimum} \nMin: {minimum}"

# Data contoh skor
skor = [77, 20, 40, 88, 95]
print(hitung_statistik(skor))


print("\n---Analisis data--------------------------")

# Data penjualan produk alat tulis
# Format data:
# - produk: Nama produk
# - harga: Harga satuan dalam Rupiah
# - stok: Jumlah stok tersedia
# - terjual: Jumlah unit terjual
data = {
    "produk": ["Buku", "Pensil", "Pulpen", "Spidol", "Penghapus"],
    "harga": [5_000, 2_000, 3_000, 4_000, 2_000],
    "stok": [50, 10, 10, 100, 5],    
    "terjual": [30, 3, 2, 80, 1]
}

# Membuat DataFrame dari dictionary
df = pd.DataFrame(data)
print("Data penjualan")
print(df)

# Menghitung pendapatan untuk setiap produk (harga * terjual)
df["pendapatan"] = df["harga"] * df["terjual"]
print("\nData dengan pendapatan:")
print(df)

# Menampilkan statistik ringkas
print("\nRata-rata harga:", df["harga"].mean())
print("Total pendapatan:", df["pendapatan"].sum())

# Analisis produk laris (terjual > 25 unit)
print("\nProduk laris (terjual > 25):")
for index, row in df.iterrows():
    if row["terjual"] > 25:
        print(f"{row['produk']} terjual {row['terjual']} unit!")  # Produk laris
    else:
        print(f"{row['produk']} hanya terjual {row['terjual']} unit")  # Produk kurang laku


# Tugas: Analisis Data Game
print("\n---Tugas-----------------------------")

# Data game populer dengan ranking dan skor
data_game = {
    "daftar_game": ["Genehin Impact", "Pubg Mobile", "Honor of Kings", "CarX Street"],
    "Top": [1, 2, 3, 4],
    "skor": [95, 90, 88, 90]
}

# Membuat DataFrame game
df_game = pd.DataFrame(data_game)
print("Data game:")
print(df_game)

# Menghitung rata-rata skor
rate_skor = df_game["skor"].mean()
print(f"\nRata-rata rate:", rate_skor)

# Menampilkan game dengan skor di atas rata-rata
print("\nGame dengan skor diatas rata rata")
for index, row in df_game.iterrows():
    if row["skor"] > rate_skor:
        print(f"{row['daftar_game']} skor {row['skor']}")  # Game dengan performa baik