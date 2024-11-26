import tkinter as tk  # Import modul tkinter untuk membuat antarmuka GUI
from tkinter import ttk  # Import ttk untuk widget yang lebih modern
from tkinter import messagebox  # Import messagebox untuk menampilkan pesan peringatan atau informasi

# Fungsi untuk menambahkan barang ke tabel
def tambah_barang():
    # Mengambil data dari input (Nama Barang, Jumlah, Harga)
    nama_barang = entry_nama.get()
    jumlah = entry_jumlah.get()
    harga = entry_harga.get()
    
    # Validasi input untuk memastikan semua kolom telah diisi
    if not nama_barang or not jumlah or not harga:
        messagebox.showwarning("Input Error", "Semua kolom harus diisi!")  # Tampilkan peringatan jika ada kolom kosong
        return

    # Validasi tipe data untuk memastikan Jumlah adalah integer dan Harga adalah float
    try:
        jumlah = int(jumlah)
        harga = float(harga)
    except ValueError:
        messagebox.showwarning("Input Error", "Jumlah harus angka dan harga harus angka desimal!")  # Peringatan jika format salah
        return
    
    # Menambahkan data ke tabel dengan format: ID, Nama Barang, Jumlah, Harga
    tree.insert("", "end", values=(len(tree.get_children()) + 1, nama_barang, jumlah, harga))
    
    # Membersihkan input setelah menambahkan data ke tabel
    entry_nama.delete(0, tk.END)
    entry_jumlah.delete(0, tk.END)
    entry_harga.delete(0, tk.END)

# Fungsi untuk menghapus barang yang dipilih dari tabel
def hapus_barang():
    # Mendapatkan item yang dipilih di tabel
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Delete Error", "Pilih barang yang akan dihapus!")  # Tampilkan pesan jika tidak ada barang yang dipilih
        return
    
    # Menghapus item yang dipilih satu per satu
    for item in selected_item:
        tree.delete(item)

# Fungsi untuk merefresh data tabel (placeholder untuk fitur tambahan)
def refresh_data():
    # Tampilkan informasi bahwa fitur belum tersedia
    messagebox.showinfo("Refresh", "Fitur refresh data belum tersedia.")

# Membuat jendela utama aplikasi
root = tk.Tk()
root.title("Aplikasi Inventori Barang")  # Judul jendela
root.geometry("600x400")  # Ukuran jendela (lebar x tinggi)

# Frame untuk form input (bagian atas)
frame_form = tk.Frame(root)
frame_form.pack(pady=10, padx=10, fill="x")  # Memberikan jarak dan menyesuaikan lebar frame

# Label dan Entry untuk input Nama Barang
tk.Label(frame_form, text="Nama Barang:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_nama = tk.Entry(frame_form)
entry_nama.grid(row=0, column=1, padx=5, pady=5)

# Label dan Entry untuk input Jumlah Barang
tk.Label(frame_form, text="Jumlah:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_jumlah = tk.Entry(frame_form)
entry_jumlah.grid(row=1, column=1, padx=5, pady=5)

# Label dan Entry untuk input Harga Barang
tk.Label(frame_form, text="Harga:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_harga = tk.Entry(frame_form)
entry_harga.grid(row=2, column=1, padx=5, pady=5)

# Tombol untuk menambahkan barang ke tabel
btn_tambah = tk.Button(frame_form, text="Tambah Barang", command=tambah_barang)
btn_tambah.grid(row=3, column=1, pady=10)

# Frame untuk tabel (bagian tengah)
frame_table = tk.Frame(root)
frame_table.pack(padx=10, fill="both", expand=True)  # Tabel memenuhi area tengah

# Membuat tabel menggunakan Treeview
columns = ("ID", "Nama Barang", "Jumlah", "Harga")
tree = ttk.Treeview(frame_table, columns=columns, show="headings")
tree.heading("ID", text="ID")  # Judul kolom pertama
tree.heading("Nama Barang", text="Nama Barang")  # Judul kolom kedua
tree.heading("Jumlah", text="Jumlah")  # Judul kolom ketiga
tree.heading("Harga", text="Harga")  # Judul kolom keempat

# Menyesuaikan lebar setiap kolom tabel
tree.column("ID", width=50, anchor="center")  # Kolom ID
tree.column("Nama Barang", width=150, anchor="w")  # Kolom Nama Barang
tree.column("Jumlah", width=100, anchor="center")  # Kolom Jumlah
tree.column("Harga", width=100, anchor="e")  # Kolom Harga

# Menampilkan tabel di jendela
tree.pack(fill="both", expand=True)

# Frame untuk tombol aksi (bagian bawah)
frame_action = tk.Frame(root)
frame_action.pack(pady=10, padx=10, fill="x")

# Tombol untuk menghapus barang
btn_hapus = tk.Button(frame_action, text="Hapus Barang", command=hapus_barang)
btn_hapus.pack(side="left", padx=5)

# Tombol untuk merefresh data
btn_refresh = tk.Button(frame_action, text="Refresh Data", command=refresh_data)
btn_refresh.pack(side="left", padx=5)

# Menjalankan loop utama aplikasi (agar jendela tetap terbuka)
root.mainloop()
