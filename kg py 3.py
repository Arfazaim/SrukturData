class Orang:
    total = 0

    def _init_(self, nama):
        self.nama = nama
        Orang.total += 1

    def _del_(self):
        Orang.total -= 1

    def katakanHalo(self):
        print("Halo, nama saya", self.nama, ", apa kabar?")

    @classmethod
    def total_populasi(cls):
        print('Total Orang adalah', cls.total)

org = Orang('Quraisy')
org.katakanHalo()
Orang.total_populasi()

org2 = Orang('Ibrani')
org2.katakanHalo()
Orang.total_populasi()

print('Obyek dihapus')
del org
del org2

Orang.total_populasi()