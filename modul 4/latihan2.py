def selection_sort(arr):
    n = len(arr)
    print("Sebelum Pengurutan:")
    print(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print("Setelah Pengurutan:")
    print(arr)

data = [64, 25, 12, 22, 11]
selection_sort(data)
