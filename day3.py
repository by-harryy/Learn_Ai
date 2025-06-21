import pandas as pd 
import matplotlib.pyplot as plt 

# Data toko online
data = {
    "produk": ["Laptop", "Mouse", "Monitor", "Handphone", "Keyboard", "Headset"],
    "kategori": ["Elektronik", "Aksesoris", "Aksesoris", "Elektronik", "Aksesoris", "Aksesoris"],
    "harga": [6_000_000, 100_00, 1_000_000, 4_000_000, 350_00, 60_00],
    "terjual": [77, 20, 30, 360, 100, 900]
}

df = pd.DataFrame(data)
print("Data toko:")
print(df)

# Filter: produk yang terjual > 30
print("\nProduk laris:")
laris = df[df["terjual"] > 30]
print(laris)

# Sortir: Dari harga termahal
print("\nProduk diurutkan dari termahal:")
sorted_df = df.sort_values(by="harga", ascending=False)
print(sorted_df)

# Sortir: Dari harga termurah
print("\nProduk diurutkan dari termurah:")
sorted_df = df.sort_values(by="harga", ascending=True)
print(sorted_df)

# Plot bar chart
print("\n---Bar chart-----------------")
plt.plot(df["produk"], df["terjual"]) # Kalo mau bar gunakan plt.bar
plt.title("Penjualan per Produk")
plt.xlabel("Produk")
plt.ylabel("Terjual")
plt.show()

# Tambah Kolom psndapatan
df["pendapatan"] = df["harga"] * df["terjual"]
print("Data dengan pendapatan")
print(df)

# Analisis per kategori
print("\nTotal pendapatan per kategori:")
kategori_pendapatan = df.groupby("kategori")["pendapatan"].sum()
print(kategori_pendapatan)

# Visualisasi
plt.bar(kategori_pendapatan.index, kategori_pendapatan.values, color="green")
plt.title("Pendapatan per kategori")
plt.xlabel("Kategori")
plt.ylabel("Pendapatan (Rupiah)")
plt.show()


# Tugass
# Ga dlu deh :v