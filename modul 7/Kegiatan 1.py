top=0
mymax=eval(input("Masukkan jumlah maksimum stack:"))
def createStack():
    stack=[]
    return stack
def isEmpty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
    print("--Memasukkan", item, "Ke stack--")
def pop(stack):
    if isEmpty(stack):
        return "**Maff, stack sudah kosong**"
    return stack.pop()
stack=createStack()
while True:
    print("1.Push")
    print("2.Pop")
    print("3.Tampilkan")
    print("4.Keluar")
    ch=int(input("Masukkan Pilihan:"))
    if ch==1:
        if top<mymax:
            item=input("Masukkan item yang ingin di masuk")
            push(stack,item)
            top+=1
        else:
            print("--Maff, stack sudah penuh--")
    elif ch==2:
        print(pop(stack))
    elif ch==3:
        print(stack)
    else:
        print("Keluar..Sampai Jumpa Lagi...")
        break