warna = ["Merah","Jingga","Kuning","Hijau","Biru"]

#menampilkan semua warna
print("Semua warna:", warna)

#mengakses satu warna ( indeks ke-2)
index = 2
print(f"warna pada indeks ke-(index): (warna[index])")

#menambahkan warna nila dan ungu
warna.append("nila")
warna.append("ungu")

#menampilkan semua warna setelah penambahan
print("Warna setelah penambahan nila dan ungu:", warna)

#menghapus satu warna (misalnya warna jingga)
target_color = "jingga"
if target_color in warna:
    warna.remove(target_color)
    
#menampilkan semua warna setelah penghapusan
print(f"warna setelah dihapus. (target_color):", warna)