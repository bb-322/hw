class Worker:
    def __init__(self, name: str, surname: str, department: str, start_year: int):

        self._name = name
        self._surname = surname
        self._department = department
        self._start_year = start_year


workers = []

while True:
    act = int(input())
    match act:
        case 1:
            name = input("name: ")
            if not name.isalpha():
                raise TypeError("must be a str")

            surname = input("surname: ")
            if not surname.isalpha():
                raise TypeError("must be a str")

            department = input("department: ")
            if not department.isalpha():
                raise TypeError("must be a str")

            year = input("year: ")
            if not year.isdigit():
                raise TypeError('must be int')
            
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
