# Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    def PrintList(self):
        temp = self.head
        if temp is None:
            print("List empty")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
            if temp:
                print("->", end="")
        print()

    def insert_at_start(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def insert_at_end(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = temp

    def insert_after_data(self, x, data):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print("item not in the list")
        else:
            temp = Node(data)
            temp.next = n.next
            n.next = temp

    def insert_before_data(self, x, data):
        if self.head is None:
            print("list has no element")
            return
        if x == self.head.data:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("item not in the list")
        else:
            temp = Node(data)
            temp.next = n.next
            n.next = temp

    def del_front(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp = None

    def del_back(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next is not None:
                    temp = temp.next
                lastNode = temp.next
                temp.next = None
                lastNode = None

    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def search_data(self, data):
        index = 0
        temp = self.head
        while temp:
            if temp.data == data:
                return f"Data found at index {index}"
            temp = temp.next
            index += 1
        return "Data not found"

    def delete_all_nodes(self):
        self.head = None


# Example usage
mylist = LinkedList()
mylist.insert_at_start(10)
mylist.insert_at_end(20)
mylist.insert_at_end(30)
mylist.PrintList()

# 1. Count nodes
print("Number of nodes:", mylist.count_nodes())

# 2. Search data
search_result = mylist.search_data(20)
print(search_result)

# 3. Delete all nodes
mylist.delete_all_nodes()
print("List after deleting all nodes:")
mylist.PrintList()
