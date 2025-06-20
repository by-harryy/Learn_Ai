import numpy as np

# Menampilkan pesan pembuka
print("Hello,i'am a Ai Engineer!")

# Inisialisasi list nilai dan menampilkannya
nilai = [75, 80, 95, 90, 98] # list berisi nilai-nilai
print("Value Variable nilai:", nilai)
print("Length nilai:", len(nilai)) # menghitung jumlah elemen dalam list

# Menghitung total dan rata-rata
total = sum(nilai) # menjumlahkan semua nilai dalam list
print("Hasil total:", total)

rata_rata = total / len(nilai) # menghitung nilai rata-rata
print("Rata rata nilai:", rata_rata)

"""
Analisis Statistik Menggunakan NumPy
------------------------------------
Bagian ini menggunakan library NumPy untuk menghitung
statistik dasar dari sekumpulan nilai
"""
print("\n---NumPy----------------------")
nilai = np.array([76, 88, 90, 98, 77])
rata_rata = np.mean(nilai)
median = np.median(nilai)
standar_deviasi = np.std(nilai)
print("Rata-rata (NumPy):", rata_rata)
print("Median (NumPy):", median)
print("Standar (NumPy):", standar_deviasi)

# Program input nilai interaktif
print("\n---Loop NumPy------------------")
jumlah = int(input("Mau masukin berapa nilai?: "))
nilai = []

# Loop untuk mengumpulkan input dari pengguna
for i in range(jumlah):
    n = float(input(f"Masukan nilai ke {i + 1}: "))
    nilai.append(n)

# Menghitung dan menampilkan statistik
nilai_array = np.array(nilai)
print("Rata-rata:", np.mean(nilai_array))
print("Nilai tertinggi:", np.max(nilai_array))
print("Nilai terendah:", np.min(nilai_array))
print("Nilai median:", np.median(nilai_array))

# Tugas: Menghitung rata-rata skor game
nilai = []
for i in range(3):
    n = float(input(f"Masukan angka ke {i + 1}: "))
    nilai.append(n)

print("Rata rata skor game lu segini cuy:", np.mean(nilai))

# End of program