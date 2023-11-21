def quick_sort_by_nim(mahasiswa):
    if len(mahasiswa) <= 1:
        return mahasiswa
    else:
        pivot = mahasiswa[0]["nim"]
        less = [m for m in mahasiswa[1:] if m["nim"] < pivot]
        greater = [m for m in mahasiswa[1:] if m["nim"] >= pivot]
        return quick_sort_by_nim(less) + [mahasiswa[0]] + quick_sort_by_nim(greater)

def merge_sort_by_alamat(mahasiswa):
    if len(mahasiswa) > 1:
        mid = len(mahasiswa) // 2
        left_half = mahasiswa[:mid]
        right_half = mahasiswa[mid:]

        merge_sort_by_alamat(left_half)
        merge_sort_by_alamat(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i]["alamat"] < right_half[j]["alamat"]:
                mahasiswa[k] = left_half[i]
                i += 1
            else:
                mahasiswa[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            mahasiswa[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            mahasiswa[k] = right_half[j]
            j += 1
            k += 1

mahasiswa = [
    {"nama": "Arfa Zaim", "nim": 202207004, "alamat": "Boyolali"},
    {"nama": "Rimba Jati", "nim": 202207006, "alamat": "karanganyar"},
    {"nama": "Ammar zky", "nim": 202207009, "alamat": "Surakarta"},
    {"nama": "Prameswari", "nim": 202207003, "alamat": "Boyolali"},
    {"nama": "Adit", "nim": 202207001, "alamat": "Sragen"},
    {"nama": "Hanif Prabowo", "nim": 202207010, "alamat": "Surakarta"},
    {"nama": "Ari Putra", "nim": 202207005, "alamat": "Sukoharjo"},
    {"nama": "Akmalsyah", "nim": 202207002, "alamat": "Surakarta"},
    {"nama": "Nida", "nim": 202207008, "alamat": "Surakarta"},
    {"nama": "Hania", "nim": 202207007, "alamat": "Sragen"},
]

mahasiswa_sorted_nim = quick_sort_by_nim(mahasiswa.copy())

merge_sort_by_alamat(mahasiswa)

print("Pengurutan NIM:")
for m in mahasiswa_sorted_nim:
    print(f"Nama: {m['nama']}, NIM: {m['nim']}, Alamat: {m['alamat']}")

print("\nPengurutan Alamat:")
for m in mahasiswa:
    print(f"Nama: {m['nama']}, NIM: {m['nim']}, Alamat: {m['alamat']}")
