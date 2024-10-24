class AbstactClass:
    def __new__(cls):
        return "Ошибка: нельзя создавать объекты абстрактного класса"


obj123 = AbstactClass()
print(obj123)
