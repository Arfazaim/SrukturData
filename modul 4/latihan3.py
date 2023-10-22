def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:  # Ubah tanda '<' menjadi '>'
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

data = [12, 11, 13, 5, 6]
insertion_sort_descending(data)
print("Data Terurut Secara Descending:")
print(data)
