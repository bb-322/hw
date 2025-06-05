import mymodule

while True:
    choice = input('1 - create link\n2 - get original link\n3 - get all names\n4 - break\n')

    match choice:
        case '1':
            mymodule.short_link()
        case '2':
            mymodule.get_old_link()
        case '3':
            mymodule.get_all_names()
        case '4':
            break
        case _:
            continue