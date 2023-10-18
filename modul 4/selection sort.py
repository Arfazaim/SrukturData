def bubble(listku):
    perubahan = True
    sesi = len(listku)
    while sesi > 1 and perubahan:
        perubahan = False
        j = 1
        while j < sesi:
            if listku[j] < listku[j - 1]:
                perubahan = True
                tukar(listku, j, j - 1)
            j += 1
        print(listku)
        if not perubahan:
            print("hasil akhir = %s" % str(listku))
        sesi -= 1

print("====================================================================")
print("Bubble sort")
input_string = input("Masukkan angka-angka yang akan diurutkan (pisahkan dengan spasi): ")
mylist = [int(x) for x in input_string.split()]
print("Sebelum Bubble sort")
print(mylist)
print("Setelah Bubble Sort")
bubble(mylist)