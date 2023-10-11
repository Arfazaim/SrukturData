# membuat list 2 dimensi
siswa = [["Arfa", 11111], ["Zaim", 22222], ["Al", 33333], ["Murtadlo", 44444], ["Azam", 55555]]

# tampilkan isi list indeks nomor 3
print(siswa[3])

# tampilkan semua data dengan perulangan
for i in range(len(siswa)):
    for j in range(len(siswa[i])):
        print(siswa[i][j], end=" ")
    print()

# tampilkan panjang list
print("Panjang list siswa adalah", len(siswa))
