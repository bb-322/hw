class Editor:
    def __init__(self, key:int):
        self.key = key
        self.key_pro = 982534892
    
    def view_document(self):
        return 'document' 

    def edit_document(self):
        if self.key != self.key_pro:
            return 'Document editing is only available with Pro version'
        else:
            return ProEditor(Editor).edit_document()
    

class ProEditor(Editor):
    def edit_document(self):
        super().edit_document()
        return 'Editing document'


user = Editor(1)
admin = Editor(982534892)

print(user.edit_document())
print(admin.edit_document())

print(user.view_document())
print(admin.view_document())