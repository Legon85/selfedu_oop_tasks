class SingletonFive:
    __instance = None
    instance_count = 0

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None and cls.instance_count <= 5:
            cls.instance_count =+ 1
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять

a = SingletonFive("data")

print(a.name)
