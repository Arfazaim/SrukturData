hash_table = [[] for_in range (10)]
print (hash_table)
def hashing_func(key):
    return key % len (hash_table)
print (hashing_func(10))
print (hashing_func(20)) 
print (hashing_func(25))
def insert (hash_table, key, value):
    hash_key = hashing_func(key)
    hash_table[hash_key].append(value)
insert (hash_table, 10, 'Solo')
insert (hash_table, 25, 'Sragen')
insert (hash_table, 20, 'Wonogiri')
print (hash_table)