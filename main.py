from functools import reduce
from operator import add


class TreeStore:

    def __init__(self, *args):
        if not args:
            self.object = [{'id': 0, 'parent': 0, 'type': []}, ]
        self.object = reduce(add, args)

    def add_obj(self, id_obj: int, parent='root', typer=[]):
        self.object.append({'id': id_obj, 'parent': parent, 'type': typer})

    def getAll(self):
        return self.object

    def getItem(self, id_object: int):
        for item in self.object:
            if item['id'] == id_object:
                return item

    def getChildren(self, id_children: int):
        dict = []
        for item in self.object:
            if item['parent'] == id_children:
                dict.append(item)
        return dict

    def getAllParents(self, id_parent: int):
        dict = []
        prev_parent = self.getItem(id_parent)['parent']
        while prev_parent != 'root':
            for item in self.object:
                if item['id'] == prev_parent:
                    prev_parent = item['parent']
                    dict.append(item)
        return dict


if __name__ == '__main__':
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]
    ojj = TreeStore(items)
    print("ALL", ojj.getAll())
    print("ITEM", ojj.getItem(1))
    print("CHILD", ojj.getChildren(1))
    print("ALL PARENTS: ", ojj.getAllParents(7))
