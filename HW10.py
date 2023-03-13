from collections import UserDict
from string import digits


print("hello")
print("test commit github")

test_commit = "github bla bla bla"

class Field:
    def __init__(self, value):
        self.value = value
    
class Name(Field):
    pass
    
class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone) -> None:
        self.name  = name
        self.phones = []
        if phone:
            self.phones.append(phone)
            
    def add_phone(self, phone: Phone):
        self.phones.append(phone) 
        
    
    def remove_phone(self, phone: Phone):
        for p in self.phones:
            if p == phone.value:
                self.phones.remove(p)
    
    def change_phone(self, old_phone: Phone, new_phone: Phone):
        for phone in self.phones:
            if old_phone.value == phone.value:
                self.phones.remove(phone)
                self.phones.append(new_phone)
        
        
class AdressBook(UserDict):
    def dict_info(self, word):
        return word 
    
    def add_record(self, rec : Record):
        self.data[rec.name.value] = rec
        
