# Kelas Induk: Kendaraan
class Kendaraan:
    def berjalan(self):
        # Fungsi berjalan() di kelas induk
        print("Kendaraan berjalan..")

# Kelas Turunan: Mobil, mewarisi Kendaraan
class Mobil(Kendaraan):
    def berjalan(self, kecepatan, satuan='km/j'):
        # Fungsi berjalan() di-*override* dari kelas induk
        # Menambahkan perilaku baru dan tetap memanggil fungsi induk
        super().berjalan()  # Memanggil fungsi berjalan() dari kelas induk
        print(f"  -> Mobil berjalan dengan kecepatan {kecepatan} {satuan}")

# Kelas Turunan: Sepeda, mewarisi Kendaraan
class Sepeda(Kendaraan):
    def berjalan(self):
        # Fungsi berjalan() di-*override* dari kelas induk
        # Mengganti implementasi tanpa memanggil fungsi induk
        print("Sepeda berjalan dengan santai..")

# Membuat instance dari masing-masing kelas
kendaraan_umum = Kendaraan()  # Objek dari kelas Kendaraan
mobil_balap = Mobil()         # Objek dari kelas Mobil
sepeda_lipat = Sepeda()       # Objek dari kelas Sepeda

# Memanggil method berjalan() dari objek Kendaraan
print("Contoh Kendaraan:")
kendaraan_umum.berjalan()  # Output: Kendaraan berjalan..

# Memanggil method berjalan() dari objek Mobil
print("\nContoh Mobil:")
mobil_balap.berjalan(150)  # Output:
# Kendaraan berjalan..  (Dari kelas induk, dipanggil menggunakan super())
#   -> Mobil berjalan dengan kecepatan 150 km/j (Implementasi override di kelas Mobil)

# Memanggil method berjalan() dari objek Sepeda
print("\nContoh Sepeda:")
sepeda_lipat.berjalan()  # Output:
# Sepeda berjalan dengan santai.. (Implementasi override di kelas Sepeda)
