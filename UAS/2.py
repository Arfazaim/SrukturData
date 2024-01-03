class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class FamilyTree:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node:
            elems.append(cur_node.data)
            cur_node = cur_node.next
        print(elems)


# contoh penggunaan
family_tree = FamilyTree()
family_tree.append("Suhidi & Sadiyem")
family_tree.append("Samsul hadi")
family_tree2 = FamilyTree()
family_tree2.append("Sukini & Yarju")
family_tree2.append("Suwarti")
family_tree3 = FamilyTree()
family_tree3.append("Suprapto & Siti Supinah")
family_tree3.append("Sutrisno")
family_tree4 = FamilyTree()
family_tree4.append("Samadi & Sumini")
family_tree4.append("Sakiyem")
family_tree5 = FamilyTree()
family_tree5.append("Samsul Hadi & Suwarti")
family_tree5.append("Khumaidi")
family_tree6 = FamilyTree()
family_tree6.append("Sutrisno & Sakiyem")
family_tree6.append("Yusnaini")
family_tree7 = FamilyTree()
family_tree7.append("Khumaidi & Yusnaini")
family_tree7.append("Arfa Zaim Al Murtadlo")

family_tree.display()
family_tree2.display()
family_tree3.display()
family_tree4.display()
family_tree5.display()
family_tree6.display()
family_tree7.display()