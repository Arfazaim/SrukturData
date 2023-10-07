class Orang:
    total=0
    def __init__ (self, nama) :
#inisiasi data, data yang dibuat pada self merupakan variabel obyek
        self.nama = nama
#ketika ada orang yang dibuat, tambahkan total orang
        Orang.total += 1

    def __del__ (self):
#kurangi total orang jika objek dihapus
        Orang.total -=1
    def katakanHalo (self) :
        print ("Halo, nama saya", self.nama, ", apa kabar?")
    def total_populasi (cls) :
        print( 'Total Orang adalah ', cls.total)
# method class
    total_populasi= classmethod (total_populasi)

org=Orang('budi')
org.katakanHalo ()
print ('total orang', cls.total)

org2=Orang('andi')
org2.katakanHalo ()
print ('total orang', cls.total)

print ('objek dihapus')
del org
del org2

orang.total_populasi()
