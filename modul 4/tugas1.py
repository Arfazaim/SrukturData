def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key[2] < arr[j][2]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j][2] < arr[min_idx][2]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

data_karyawan = [
    ("kaka", 30, 50000),
    ("kiki", 25, 60000),
    ("kuku", 35, 75000),
    ("keke", 28, 90000)
]

insertion_sort(data_karyawan)

print("Data karyawan setelah diurutkan berdasarkan gaji (Insertion Sort):")
for karyawan in data_karyawan:
    print(f"Nama: {karyawan[0]}, Usia: {karyawan[1]}, Gaji: {karyawan[2]}")

data_karyawan2 = [
    ("Arfa", 23, 50000),
    ("Zaim", 24, 60000),
    ("Al", 25, 75000),
    ("Murtadlo", 28, 80000)
]

selection_sort(data_karyawan)

print("\nData karyawan setelah diurutkan berdasarkan gaji (Selection Sort):")
for karyawan in data_karyawan2:
    print(f"Nama: {karyawan[0]}, Usia: {karyawan[1]}, Gaji: {karyawan[2]}")
