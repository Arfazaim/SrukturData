class Perpustakaan:
    def _init_(self):
        self.data_buku = {}

    def tambah_buku(self, kode, judul, pengarang, penerbit, nomor_buku):
        if kode not in self.data_buku:
            self.data_buku[kode] = {
                'Judul': judul,
                'Pengarang': pengarang,
                'Penerbit': penerbit,
                'Nomor Buku': nomor_buku
            }
        else:
            print("Kode buku sudah ada. Gunakan kode yang berbeda.")

    def cari_nomor_rak(self, nomor_buku):
        for kode, buku in self.data_buku.items():
            if buku['Nomor Buku'] == nomor_buku:
                return kode
        return None


perpustakaan = Perpustakaan()

# Menambahkan data buku ke perpustakaan
perpustakaan.tambah_buku('A', 'Pemrograman Dasar', 'Abdul Kadir', 'Andi', 35)
perpustakaan.tambah_buku('B', 'Belajar Python', 'Budi Raharjo', 'Graha Ilmu', 20)
perpustakaan.tambah_buku('C', 'Struktur Data', 'Chomaria', 'Informatika', 64)
perpustakaan.tambah_buku('D', 'Internet', 'Deni Santoso', 'Biobses', 131)
perpustakaan.tambah_buku('E', 'Database', 'Eko Cahyanto', 'Cemerlang', 78)

# Mencari nomor rak berdasarkan nomor buku
nomor_buku_cari = 64
kode_buku_ditemukan = perpustakaan.cari_nomor_rak(nomor_buku_cari)

if kode_buku_ditemukan is not None:
    print(f"Nomor rak buku dengan Nomor Buku {nomor_buku_cari}: {kode_buku_ditemukan}")
else:
    print(f"Buku dengan Nomor Buku {nomor_buku_cari} tidak ditemukan.")