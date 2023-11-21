# Class untuk merepresentasikan objek Kucing
class Kucing:
    def __init__(self, umur, warna_bulu):
        self.umur = umur
        self.warna_bulu = warna_bulu

    def meong(self):
        print("Meong!")

    def get_umur(self):
        return self.umur

# Contoh penggunaan class Kucing
kucing1 = Kucing(3, "Putih")
kucing1.meong()  # Memanggil method meong()
print("Umur kucing:", kucing1.get_umur())  # Memanggil method get_umur()
