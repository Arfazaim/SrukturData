def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    indices = []
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            indices.append(mid)
            left = mid + 1
        elif arr[mid] < target:
            right = mid - 1
        else:
            left = mid + 1
    return indices

# Mengurutkan data terbalik
data.sort(reverse=True)

# Contoh penggunaan
target = 5
result_binary = binary_search(data, target)
print(f"Indeks data {target} menggunakan pencarian biner: {result_binary}")
