class MyException(BaseException):
    def __init__(self, *args):
        super().__init__(*args)
        self.message = args[0]

    def __str__(self):
        return f'{self.message}'

class Worker:
    def __init__(self, name: str, surname: str, department: str, start_year: str):

        self._name = name
        self._surname = surname
        self._department = department
        self._start_year = start_year

        if not self._name.isalpha():
            raise MyException("name must be letters")
        if not self._surname.isalpha():
            raise MyException("surname must be letters")
        if not self._department.isalpha():
            raise MyException("department must be letters")
        if not self._start_year.isdigit():
            raise MyException('year must be numbers')


workers = []

while True:
    act = int(input())
    match act:
        case 1:
            name = input("name: ")

            surname = input("surname: ")

            department = input("department: ")

            year = input("year: ")
            
            new_worker = Worker(name, surname, department, year)
            workers.append(new_worker)

        case 2:
            since_year = int(input("year: "))
            workers_since_year = []
            for worker in workers:
                if worker._start_year >= since_year:
                    workers_since_year.append(worker._name)
            print(workers_since_year)

        case 3:
            break
