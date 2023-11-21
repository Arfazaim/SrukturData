def toStr(n,base):
    convertString = "012345678ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]
n = int(input("masukkan bilangan integer:"))
base = int(input("Masukkan basis bilangan (2 atau 16):"))
print("hasil konversi bilangan",n,"dengan basis",base,"adalah:",toStr(n,base))