class Contact:
    def __init__(self, surname: str, name: str, age: int, mob_phone: int, email: str):
        self._surname = surname
        self._name = name
        self._age = age
        self._mob_phone = mob_phone
        self._email = email
        mob_phones[f"{self._name} {self._surname}"] = self._mob_phone
        contacts.append(self)

    def get_contact(self):
        print(
            f"Contact's data:\n\tSurname: {self._surname}\n\tName: {self._name}\n\tAge: {self._age}\n\tMobile phone: {self._mob_phone}\n\tEmail: {self._email}\n"
        )

    @classmethod
    def send_message(cls):
        cls._text = input("Message text: ")
        phone_number = int(input("Enter reciever's phone number: "))
        try:
            reciever = next(r for r in contacts if r._mob_phone == phone_number)
            reciever_info = [reciever._name, reciever._surname]
            reciever = " ".join(reciever_info)
            print(f"Sent: \n\t'{cls._text}'\nto {reciever}")
        except StopIteration:
            print("No contact with this number in contacts")


class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self._job = job

    def get_contact(self):
        print(
            f"Contact's data:\n\tSurname: {self._surname}\n\tName: {self._name}\n\tAge: {self._age}\n\tMobile phone: {self._mob_phone}\n\tEmail: {self._email}\n\tJob: {self._job}\n"
        )

    @classmethod
    def get_message(cls):
        phone_number = int(input("Enter sender's phone number: "))
        try:
            sender = next(s for s in contacts if s._mob_phone == phone_number)
            sender_info = [sender._name, sender._surname]
            sender = " ".join(sender_info)
            print(f"Recieved: \n\t'{cls._text}'\nfrom {sender}")
        except StopIteration:
            print("No contact with this number in contacts")


mob_phones = {}
contacts = []

per1 = Contact("Woodman", "James", "99", 1234567890, "email1@gmail.com")
per2 = Contact("Hooman", "Jon", "20", 9876543210, "email2@gmail.com")
per3 = Contact("Goober", "Goober", "40", 5555555555, "email3@gmail.com")

per2_upd = UpdateContact(
    "Per2_s", "Per2_n", 100, 1234512345, "email2upd@gmail.com", "job"
)

per1.get_contact()
per2_upd.get_contact()
# per1.send_message()
# per2_upd.get_message()

print(hasattr(per1, "_job"))
print(hasattr(per1, "_name"))
print(getattr(per1, "_name"))
setattr(per1, "_name", "new_per1_name")
print(getattr(per1, "_name"))
delattr(per1, "_name")
print(hasattr(per1, "_name"))

print(hasattr(per2_upd, "_job"))
print(hasattr(per2_upd, "_name"))
print(getattr(per2_upd, "_name"))
setattr(per2_upd, "_name", "new_per2_upd_name")
print(getattr(per2_upd, "_name"))
delattr(per2_upd, "_name")
print(hasattr(per2_upd, "_name"))

print(isinstance(per1, Contact))
print(isinstance(per1, UpdateContact))
print(isinstance(per2_upd, Contact))
print(isinstance(per2_upd, UpdateContact))

print(issubclass(Contact, type))
print(issubclass(UpdateContact, type))
print(issubclass(Contact, UpdateContact))
print(issubclass(UpdateContact, Contact))

print(Contact.__dict__)
print(UpdateContact.__dict__)
print(Contact.__base__)
print(UpdateContact.__base__)
print(Contact.__bases__)
print(UpdateContact.__bases__)

print(per2_upd.__dict__)
delattr(per2_upd, "_job")
print(per2_upd.__dict__)
print(per1.__dict__)

print(dir(Contact))
print(dir(UpdateContact))
