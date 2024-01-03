data_kota_list = [
    (10, 'Solo'),
    (15, 'Sukoharjo'),
    (20, 'Wonogiri'),
    (25, 'Sragen'),
    (30, 'Karanganyar'),
    (35, 'Boyolali')
]

def insert(item_list, key, value):
    item_list.append((key, value))

def search(item_list, key):
    for item in item_list:
        if item[0] == key:
            return item[1]

# Contoh penggunaan fungsi insert
insert(data_kota_list, 40, 'Klaten')

# Contoh penggunaan fungsi search
result = search(data_kota_list, 25)
print("Nilai untuk kunci 25:", result)