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