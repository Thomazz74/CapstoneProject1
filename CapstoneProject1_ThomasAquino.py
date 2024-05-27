# Sistem Manajemen Perpustakaan (Peminjaman Buku )

# Koleksi Buku (inisiasi) 
perpustakaan = [
    {
        "id": "A001",
        "judul": "Pemrograman Python",
        "penulis": "John Doe",
        "tahun": "2020",
        "kategori": "Teknologi",
        "ketersediaan": "tersedia"
    },
    {
        "id": "A002",
        "judul": "Dasar-Dasar Jaringan",
        "penulis": "Jane Smith",
        "tahun": "2018",
        "kategori": "Teknologi",
        "ketersediaan": "tersedia"
    },
    {
        "id": "B001",
        "judul": "Sejarah Dunia",
        "penulis": "Michael Johnson",
        "tahun": "2015",
        "kategori": "Sejarah",
        "ketersediaan": "tersedia"
    },
    {
        "id": "C001",
        "judul": "Fiksi Ilmiah",
        "penulis": "Isaac Asimov",
        "tahun": "1995",
        "kategori": "Fiksi",
        "ketersediaan": "tersedia"
    }
]

# Fungsi untuk menambah buku baru (Create)
def tambah_buku():
    id_buku = input("Masukkan ID buku (4 karakter, bisa huruf dan angka): ")
    while len(id_buku) != 4:
        print("ID buku harus terdiri dari 4 karakter.")
        id_buku = input("Masukkan ID buku (4 karakter, bisa huruf dan angka): ")
    
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan penulis buku: ")
    tahun = input("Masukkan tahun terbit: ")
    kategori = input("Masukkan kategori buku: ")
    ketersediaan = "tersedia"
    
    buku = {
        "id": id_buku,
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun,
        "kategori": kategori,
        "ketersediaan": ketersediaan
    }
    
    perpustakaan.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")

# Fungsi untuk melihat buku (Read) 
def lihat_buku():
    if not perpustakaan:
        print("Tidak ada buku di perpustakaan.")
    else:
        print("Katalog Perpustakaan:")
        print("+------+-------------------------------+---------------------------+--------+----------------------+------------+")
        print("| ID   | Judul                         | Penulis                   | Tahun  | Kategori             | Ketersediaan|")
        print("+------+-------------------------------+---------------------------+--------+----------------------+------------+")
        for buku in perpustakaan:
            print(f"| {buku['id']:<4} | {buku['judul']:<29} | {buku['penulis']:<25} | {buku['tahun']:<6} | {buku['kategori']:<20} | {buku['ketersediaan']:<10} |")
            print("+------+-------------------------------+---------------------------+--------+----------------------+------------+")

# Fungsi untuk memperbarui detail buku (Update)
def perbarui_buku():
    id_buku = input("Masukkan ID buku yang ingin diperbarui (4 karakter): ")
    for buku in perpustakaan:
        if buku['id'] == id_buku:
            print("Pilih apa yang ingin diperbarui:")
            print("1. Judul")
            print("2. Penulis")
            print("3. Tahun")
            print("4. Kategori")
            print("5. Ketersediaan")
            pilihan = input("Masukkan pilihan Anda: ")
            if pilihan == "1":
                judul_baru = input("Masukkan judul baru: ")
                buku['judul'] = judul_baru
                print("Judul berhasil diperbarui!")
            elif pilihan == "2":
                penulis_baru = input("Masukkan penulis baru: ")
                buku['penulis'] = penulis_baru
                print("Penulis berhasil diperbarui!")
            elif pilihan == "3":
                tahun_baru = input("Masukkan tahun terbit baru: ")
                buku['tahun'] = tahun_baru
                print("Tahun terbit berhasil diperbarui!")
            elif pilihan == "4":
                kategori_baru = input("Masukkan kategori baru: ")
                buku['kategori'] = kategori_baru
                print("Kategori berhasil diperbarui!")
            elif pilihan == "5":
                ketersediaan_baru = input("Masukkan ketersediaan baru (tersedia/dipinjam): ")
                buku['ketersediaan'] = ketersediaan_baru
                print("Status ketersediaan berhasil diperbarui!")
            else:
                print("Pilihan tidak valid!")
            return
    print("Buku tidak ditemukan!")

# Fungsi untuk menghapus buku (Delete)
def hapus_buku():
    id_buku = input("Masukkan ID buku yang ingin dihapus (4 karakter): ")
    for buku in perpustakaan:
        if buku['id'] == id_buku:
            perpustakaan.remove(buku)
            print(f"Buku '{buku['judul']}' berhasil dihapus!")
            return
    print("Buku tidak ditemukan!")

# Fungsi untuk meminjam buku
def pinjam_buku():
    id_buku = input("Masukkan ID buku yang ingin dipinjam (4 karakter): ")
    for buku in perpustakaan:
        if buku['id'] == id_buku:
            if buku['ketersediaan'] == "tersedia":
                buku['ketersediaan'] = "dipinjam"
                print(f"Buku '{buku['judul']}' berhasil dipinjam!")
            else:
                print(f"Buku '{buku['judul']}' sedang dipinjam!")
            return
    print("Buku tidak ditemukan!")

# Fungsi untuk mengembalikan buku
def kembalikan_buku():
    id_buku = input("Masukkan ID buku yang ingin dikembalikan (4 karakter): ")
    for buku in perpustakaan:
        if buku['id'] == id_buku:
            if buku['ketersediaan'] == "dipinjam":
                buku['ketersediaan'] = "tersedia"
                print(f"Buku '{buku['judul']}' berhasil dikembalikan!")
            else:
                print(f"Buku '{buku['judul']}' tidak sedang dipinjam!")
            return
    print("Buku tidak ditemukan!")

# Loop utama menu program
def utama():
    while True:
        print("\nSistem Manajemen Perpustakaan")
        print("1. Tambah Buku")
        print("2. Lihat Buku")
        print("3. Perbarui Buku")
        print("4. Hapus Buku")
        print("5. Pinjam Buku")
        print("6. Kembalikan Buku")
        print("7. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")
        
        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            lihat_buku()
        elif pilihan == "3":
            perbarui_buku()
        elif pilihan == "4":
            hapus_buku()
        elif pilihan == "5":
            pinjam_buku()
        elif pilihan == "6":
            kembalikan_buku()
        elif pilihan == "7":
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    utama()