class Mobil:
    def __init__(self):
        self.warna = 'Hitam'
        self.tipe = 'Sedan'
        self.pintu = '2 pintu'
        print ('Objek telah dibuat')

    def maju(self):
        print ('maju')

    def mundur(self):
        print ('mundur')

    def melaju(self, speed):
        print ('Melaju dengan kecepatan %s km/jam' % speed)

#membuat objek pertama
mobil1 = Mobil()
print (mobil1.warna)
print (mobil1.maju())
print (mobil1.melaju(100))

#membuat objek kedua
mobil2 = Mobil()
print (mobil2.tipe)
print (mobil2.mundur())
print (mobil2.melaju(150))

#membuat objek ketiga
mobil3 = Mobil()
print (mobil3.pintu)
print (mobil3.mundur())
print (mobil3.melaju(250))
