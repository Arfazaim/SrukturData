# Fungsi untuk menginisialisasi tabel hash
def inisialisasi_tabel_hash(jumlah_rak):
    tabel_hash = {}
    for i in range(jumlah_rak):
        tabel_hash[i + 1] = {}
    return tabel_hash

# Fungsi untuk menambahkan data buku ke tabel hash
def tambah_buku(tabel_hash, kode, judul, pengarang, penerbit, nomor_buku):
    rak = nomor_buku % len(tabel_hash) + 1
    tabel_hash[rak][nomor_buku] = {'Kode': kode, 'Judul': judul, 'Pengarang': pengarang, 'Penerbit': penerbit}
    return tabel_hash

# Fungsi untuk mencari nomor rak dari nomor buku
def cari_nomor_rak(tabel_hash, nomor_buku):
    rak = nomor_buku % len(tabel_hash) + 1
    if nomor_buku in tabel_hash[rak]:
        return rak
    else:
        return None

# Inisialisasi tabel hash dengan 5 rak buku
jumlah_rak_buku = 5
tabel_buku = inisialisasi_tabel_hash(jumlah_rak_buku)

# Menambahkan data buku ke dalam tabel hash
tabel_buku = tambah_buku(tabel_buku, 'A', 'Pemrograman Dasar', 'Abdul Kadir', 'Andi', 35)
tabel_buku = tambah_buku(tabel_buku, 'B', 'Belajar Python', 'Budi Raharjo', 'Graha Ilmu', 20)
tabel_buku = tambah_buku(tabel_buku, 'C', 'Struktur Data', 'Chomaria', 'Informatika', 64)
tabel_buku = tambah_buku(tabel_buku, 'D', 'Internet', 'Deni Santoso', 'Biobses', 131)
tabel_buku = tambah_buku(tabel_buku, 'E', 'Database', 'Eko Cahyanto', 'Cemerlang', 78)

# Cari nomor rak dari nomor buku
nomor_buku_dicari = 64
nomor_rak = cari_nomor_rak(tabel_buku, nomor_buku_dicari)

# Output nomor rak dari nomor buku
if nomor_rak is not None:
    print(f"Nomor rak dari buku dengan nomor {nomor_buku_dicari} adalah rak nomor {nomor_rak}.")
else:
    print(f"Buku dengan nomor {nomor_buku_dicari} tidak ditemukan.")