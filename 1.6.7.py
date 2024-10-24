class SingletonFive:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять

a = SingletonFive("data")

print(a.name)
