hash_table = ["Hello"] * 10

def hash_func(key):
    return key % len(hash_table)

# Memanggil fungsi hash_func dengan angka 10, 20, dan 25
result_10 = hash_func(10)
result_20 = hash_func(20)
result_25 = hash_func(25)

print("Hasil hash untuk angka 10:", result_10)
print("Hasil hash untuk angka 20:", result_20)
print("Hasil hash untuk angka 25:", result_25)

def insert(hash_table, key, value):
    hash_key = hash_func(key)
    hash_table[hash_key] = value

# Contoh penggunaan fungsi insert untuk menambahkan data ke dalam tabel hash
insert(hash_table, 10, 'Solo')
insert(hash_table, 20, 'Wonogiri')
insert(hash_table, 25, 'Sragen')

# Tampilkan hasil pada tabel hash yang telah diisi
print("\nTabel hash setelah diisi:")
print(hash_table)

# Apakah data pada tabel terisi sesuai inputan?
print("\nApakah data pada tabel terisi sesuai inputan?")
print("Data untuk kunci 10:", hash_table[hash_func(10)])
print("Data untuk kunci 20:", hash_table[hash_func(20)])
print("Data untuk kunci 25:", hash_table[hash_func(25)])