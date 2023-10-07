class Mahasiswa:
    def __init__(self, nama, nim, alamat, semester):
        self.nama = nama
        self.nim = nim
        self.alamat = alamat
        self.semester = semester

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Alamat: {self.alamat}")
        print(f"Semester: {self.semester}")

# Membuat objek mahasiswa
mahasiswa1 = Mahasiswa("Arfa zaim", "01202207004", "Boyolali", 3)
mahasiswa2 = Mahasiswa("Ari putra", "01202207005", "Sukoharjo", 3)

# Memanggil metode info() untuk menampilkan informasi mahasiswa
mahasiswa1.info()
mahasiswa2.info()
