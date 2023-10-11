def l_search(a, x, l, n):
    if l < n:
        if a[l] == x:
            return l + 1
        else:
            return l_search(a, x, l + 1, n)
    else:
        return -1

arr = [114, 234, 347,147, 1348, 34,23,123,333,444]
x = 234
n = len(arr)

result = l_search(arr, x, 0, n)

if result != -1:
    print("Data di temukan pada posisi", result)
else:
    print("Data tidak ditemukan")