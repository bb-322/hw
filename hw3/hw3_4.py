class Base:
    @classmethod
    def method(cls):
        print(f'Hello from {cls.__name__}')

class Child(Base):
    pass

Base.method()
Child.method()