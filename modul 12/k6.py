hash_table = [[] for _ in range (10)]
print (hash_table)

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