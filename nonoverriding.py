# Definisi kelas dasar
class Animal:
    def make_general_sound(self):
        # Metode umum untuk semua hewan
        print("Suara hewan")

# Definisi subclass Dog yang mewarisi dari Animal
class Dog(Animal):
    def make_dog_sound(self):
        # Metode khusus untuk anjing
        print("Guk guk!")

# Definisi subclass Cat yang mewarisi dari Animal
class Cat(Animal):
    def make_cat_sound(self):
        # Metode khusus untuk kucing
        print("Meong meong!")

# Membuat instance dari setiap kelas
animal = Animal()
dog = Dog()
cat = Cat()

# Memanggil metode masing-masing kelas
animal.make_general_sound()  # Output: Suara hewan
dog.make_general_sound()     # Output: Suara hewan (warisan dari kelas dasar)
dog.make_dog_sound()         # Output: Guk guk! (khusus untuk Dog)
cat.make_general_sound()     # Output: Suara hewan (warisan dari kelas dasar)
cat.make_cat_sound()         # Output: Meong meong! (khusus untuk Cat)
