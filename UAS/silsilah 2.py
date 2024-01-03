class Family:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, name):
        self.children.append(Family(name))

    def display(self, level=0):
        print(" "*level + self.name)
        for child in self.children:
            child.display(level+4)


# contoh penggunaan
keluarga = Family("Suhidi & Sadiyem")
keluarga2 = Family("Sukini & Yarju")
keluarga.add_child("Samsul Hadi")
keluarga2.add_child("Suwarti")
keluarga.children[0].add_child("Khumaidi")


keluarga.display()
keluarga2.display()