import sys


class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


lst_in = list(map(str.strip, sys.stdin.readlines()))

# head_obj = ListObject(lst_in[0])
for i, data in enumerate(lst_in):
    obj = None
    if i == 0:
        head_obj = ListObject(data)
        head_obj.link(ListObject(lst_in[i + 1]))
        obj = head_obj
    elif i != len(lst_in) - 1:
        current_obj = ListObject(data)
        obj.link(ListObject(lst_in[i + 1]))
    else:
        current_obj = ListObject(data)
        obj.link(current_obj)

print(head_obj.data, head_obj.next_obj.next_obj)

# import sys
#
#
# class ListObject:
#    def __init__(self, data, next_object=None):
#        self.data = data
#        self.next_object = next_object
#
#    def link(self, obj):
#        self.next_object = obj
#
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
#
# lst_out = []
# head_obj = None
# for i, data in enumerate(lst_in):
#    if i == 0:
#        head_obj = ListObject(data)
#        head_obj.next_object = head_obj.link(ListObject(lst_in[i + 1]))
#        lst_out.append(head_obj)
#    elif i != len(lst_in) - 1:
#        lst_out.append(ListObject(data, ListObject(lst_in[i + 1])))
#    elif i == len(lst_in) - 1:
#        lst_out.append(ListObject(data))
#
#
# for i in lst_out:
#    print(f"{i.data}                                      {i.next_object}")
