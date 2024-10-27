class SingletonFive:
    __instance_list = []
    __instance_count = 0

    def __new__(cls, *args, **kwargs):
        if cls.__instance_count <= 4:
            cls.instance = super().__new__(cls)
            cls.__instance_list.append(cls.instance)
            cls.__instance_count += 1
            return cls.instance
        else:
            return cls.__instance_list[-1]

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять

for i in objs:
    print(i)
