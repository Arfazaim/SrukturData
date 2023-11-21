def linear_search(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

# Contoh penggunaan
data = [5, 2, 7, 1, 9, 3, 5, 2]
target = 5
result_linear = linear_search(data, target)
print(f"Indeks data {target} menggunakan pencarian linear: {result_linear}")