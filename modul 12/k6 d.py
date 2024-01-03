# Inisialisasi hash_table
hash_table = [[] for _ in range(10)]
print("Hash Table Awal:", hash_table)

# Definisi operasi insert, search, dan delete

def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    
    if key_exists:
        bucket[i] = (key, value)
    else:
        bucket.append((key, value))

def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    
    for kv in bucket:
        k, v = kv
        if key == k:
            return v

def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    
    if key_exists:
        del bucket[i]
        print('Key ({}) deleted'.format(key))
    else:
        print('Key ({}) not found'.format(key))

# Operasi Insert
insert(hash_table, 'apple', 10)
insert(hash_table, 'banana', 20)
insert(hash_table, 'orange', 30)
print("\nSetelah operasi insert:")
print("Hash Table:", hash_table)

# Operasi Search
print("\nHasil Pencarian 'banana':", search(hash_table, 'banana'))

# Operasi Delete
delete(hash_table, 'apple')
print("\nSetelah operasi delete:")
print("Hash Table:", hash_table)