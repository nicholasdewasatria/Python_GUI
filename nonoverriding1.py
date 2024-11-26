# Kelas Induk
class Kendaraan:
    def berjalan(self):
        # Fungsi berjalan() di kelas induk
        print("Kendaraan berjalan..")

# Kelas Turunan: Mobil (tidak ada overriding)
class Mobil(Kendaraan):
    pass

# Kelas Turunan: Sepeda (tidak ada overriding)
class Sepeda(Kendaraan):
    pass

# Membuat instance dari masing-masing kelas
kendaraan_umum = Kendaraan()
mobil_balap = Mobil()
sepeda_lipat = Sepeda()

# Memanggil method berjalan() dari semua objek
print("Tanpa Overriding:")
kendaraan_umum.berjalan()  # Output: Kendaraan berjalan..
mobil_balap.berjalan()     # Output: Kendaraan berjalan..
sepeda_lipat.berjalan()    # Output: Kendaraan berjalan..
