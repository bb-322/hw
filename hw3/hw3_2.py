class Language:
    def greeting(self):
        pass

class English(Language):
    def greeting(self):
        return 'Hello'

class Spanish(Language):
    def greeting(self):
        return 'Hola'


greet_en = English.greeting()
greet_sp = Spanish.greeting()

def hello_friend():
    print(greet_en)
    print(greet_sp)

hello_friend()