def binary_search(arr, target):
    arr.sort(reverse=True)  # Mengurutkan dalam urutan terbalik (dari terbesar ke terkecil)
    left, right = 0, len(arr) - 1
    indices = []

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            original_index = arr[::-1].index(target)  # Mendapatkan indeks asli dari data terurut terbalik
            indices.append(len(arr) - 1 - original_index)
            break
        elif arr[mid] < target:
            right = mid - 1
        else:
            left = mid + 1

    return indices

# Contoh penggunaan:
data = [5, 2, 7, 1, 9, 3, 5]
target = 5
result = binary_search(data, target)
if result:
    print(f"Data {target} ditemukan di indeks: {result}")
else:
    print(f"Data {target} tidak ditemukan.")