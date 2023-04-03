"""
Creational :
    Singleton
"""


class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Db(metaclass=Singleton):
    pass

db1 = Db()
db2 = Db()

print((id(db1)))
print((id(db2)))

print(db1 == db2)





