class Editor:
    def view_document(self):
        return 'document' 

    def edit_document(self):
        return 'Document editing is only available with Pro version'
    

class ProEditor(Editor):
    def edit_document(self):
        return 'Editing document'

key_input = int(input("Enter key: "))
key = 982534892

if key_input == key:
    user = ProEditor()
else:
    user = Editor()

print(user.view_document())
print(user.edit_document())