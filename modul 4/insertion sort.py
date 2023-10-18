def insertionSort(mylist):
    for index in range(1, len(mylist)):
        Kanan = mylist[index]
        Kiri = index - 1
        while Kiri >=0 and mylist[Kiri] > Kanan:
            mylist[Kiri + 1] = mylist[Kiri]
            Kiri -= 1
        mylist[Kiri + 1] = Kanan
        
index = 0
panjangList = int(input("Panjang data yang diinginkan = "))
mylist=[]
for i in range(1,panjangList+1):
    angka = int(input("Masukkan data yang ke %i untuk List = " %i))
    mylist.append(angka)
    
print("sebelum di insertion sort =")
print(mylist)
insertionSort(mylist)
print("setelah di insertion sort")
print(mylist)