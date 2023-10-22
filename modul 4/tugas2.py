nilai_basis_data = [
    ("Mahasiswa1", 85),
    ("Mahasiswa2", 90),
    ("Mahasiswa3", 75),
    ("Mahasiswa4", 80),
    ("Mahasiswa5", 95),
]

nilai_sistem_operasi = [
    ("Mahasiswa1", 80),
    ("Mahasiswa2", 95),
    ("Mahasiswa3", 70),
    ("Mahasiswa4", 75),
    ("Mahasiswa5", 85),
]

nilai_struktur_data = [
    ("Mahasiswa1", 75),
    ("Mahasiswa2", 85),
    ("Mahasiswa3", 95),
    ("Mahasiswa4", 80),
    ("Mahasiswa5", 90),
]

def bubble_sort(nilai):
    n = len(nilai)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if nilai[j][1] < nilai[j+1][1]:
                nilai[j], nilai[j+1] = nilai[j+1], nilai[j]

bubble_sort(nilai_basis_data)
bubble_sort(nilai_sistem_operasi)
bubble_sort(nilai_struktur_data)

print("5 Mahasiswa Terbaik Basis Data:")
for i in range(5):
    print(f"Nama: {nilai_basis_data[i][0]}, Nilai: {nilai_basis_data[i][1]}")

print("\n5 Mahasiswa Terbaik Sistem Operasi:")
for i in range(5):
    print(f"Nama: {nilai_sistem_operasi[i][0]}, Nilai: {nilai_sistem_operasi[i][1]}")

print("\n5 Mahasiswa Terbaik Struktur Data:")
for i in range(5):
    print(f"Nama: {nilai_struktur_data[i][0]}, Nilai: {nilai_struktur_data[i][1]}")
