import os
class Iterator:
    def __init__(self, collection):
        self._collection = collection
        print("inicializa iterator")
        self._index = 0

    def __next__(self):
        print("obtiene siguiente elemento")
        try:
            result = self._collection[self._index]
            self._index += 1
            return result
        except IndexError:
            print("<eol>")
            raise StopIteration

class Collection:
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __iter__(self):
        return Iterator(self._items)

    def add_item(self, item):
        print("Agrega item %s" % (item))
        self._items.append(item)


os.system("clear")

#*--------- Crea colección
collection = Collection()
collection.add_item(1)
collection.add_item(2)
collection.add_item(3)

#*-------- La recorre

for item in collection:
    print(item)

