# Class untuk merepresentasikan objek Persegi Panjang
class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

# Contoh penggunaan class PersegiPanjang
persegi_panjang1 = PersegiPanjang(5, 10)
print("Luas persegi panjang:", persegi_panjang1.luas())
print("Keliling persegi panjang:", persegi_panjang1.keliling())
