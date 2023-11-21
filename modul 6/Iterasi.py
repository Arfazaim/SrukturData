def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print("masukkan list data:")
numList=[int(x)for x in input() .split()]
print("Hasil penjumlahan:",listsum(numList))