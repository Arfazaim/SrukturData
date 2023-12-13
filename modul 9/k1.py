class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def PrintList(self):
        temp = self.head
        if(temp is None):
            print("Link kososng")
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
            if temp:
                print ("<->", end=" ")
        print()
#k2
    def insert_first(self, data):
        newNode = Node(data)
        if(self.head == None):
            self.head = new
            return
        else:
            self.head.prev = new
            new.next = self.head
            self.head = new
            
    def insert_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        else:
            n = self.head
            while (n.next is not None):
                n = n.next
            n.next = new
            new.prev = n
            
#k3
    def del_first(self):
        if (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
            if(self.head != None):
                self.head.prev = None
                
ll = LinkedList()

while True:
    print("\n1. Insert First")
    print("2. Delete First")
    print("3. Print List")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        data = int(input("Masukkan data untuk dimasukkan di awal: "))
        ll.insert_first(data)
    elif choice == 2:
        ll.del_first()
        print("Elemen pertama telah dihapus.")
    elif choice == 3:
        print("Linked List:")
        ll.PrintList()
    elif choice == 4:
        print("Program berakhir.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1-4.") 