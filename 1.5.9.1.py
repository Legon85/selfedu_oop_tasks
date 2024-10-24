import sys


class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_out = []
head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):
    obj_new = ListObject(lst_in[i])
    obj.link(obj_new)
    lst_out.append(obj)
    obj = obj_new
lst_out.append(obj)


print(head_obj.next_obj)
print(lst_out[7].data)
print(head_obj.next_obj.next_obj.next_obj.data)
for i in lst_out:
    print(f"{i.data}                                 {i.next_obj.data}")
