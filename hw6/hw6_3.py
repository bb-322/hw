class Iterator:
    def __init__(self, obj:iter):
        self._obj = obj
    
    def __iter__(self):
        self._idx = len(self._obj)
        return self
    
    def __next__(self):
        if self._idx <= 0:
            raise StopIteration
        result = self._obj[self._idx]
        self._idx -= 1
        return result

iterable = [1, 2, 3, 4, 5, 6, 7]

for item in iterable:
    print(item)