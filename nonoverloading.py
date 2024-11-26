# Definisi class Calculator tanpa overloading
class Calculator:
    def add_one(self, a):
        # Penjumlahan dengan satu argumen
        return a

    def add_two(self, a, b):
        # Penjumlahan dengan dua argumen
        return a + b

    def add_three(self, a, b, c):
        # Penjumlahan dengan tiga argumen
        return a + b + c

# Membuat instance dari Calculator
calc = Calculator()

# Memanggil metode sesuai jumlah argumen
print(calc.add_one(10))         # Menggunakan satu argumen, output: 10
print(calc.add_two(10, 20))     # Menggunakan dua argumen, output: 30
print(calc.add_three(10, 20, 30)) # Menggunakan tiga argumen, output: 60
