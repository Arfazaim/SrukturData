class Hewan:
    def __init__(self, nama, jumlah_kaki, makanan, pemakan):
        self.nama = nama
        self.jumlah_kaki = jumlah_kaki
        self.makanan = makanan
        self.pemakan = pemakan

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Jumlah Kaki: {self.jumlah_kaki}")
        print(f"Makanan: {self.makanan}")
        print(f"Pemakan: {self.pemakan}")

# Membuat objek hewan
harimau = Hewan("Harimau", 4, "Daging", "Karnivora")
kerbau = Hewan("Kerbau", 4, "Rumput", "Herbivora")

# Memanggil metode info() untuk menampilkan informasi hewan
harimau.info()
kerbau.info()
