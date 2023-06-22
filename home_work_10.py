from collections import UserDict

class Field:
    pass 

class Name(Field):
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, value):
        self.value = value

class Record:
    def add_phone(self, phone):
        self.phones.append(phone)
        if self.phones[0] == None:
            del self.phones[0]

    def del_phone(self, phone):
        for el in self.phones:
            if el.value == phone:
                 self.phones.remove(el)

    def cha_phone(self, phone, new_phone):
        for el in self.phones:
            if el.value == phone:
                el.value = new_phone

    def __init__(self, name: Name, phone=None):
        self.phones = []
        self.name = name 
        self.add_phone(phone)

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}
        
    def add_record(self, record: Record):
        self.data.update({record.name.value:record.phones})

phone_list = AddressBook()
record = Record(Name("Name 1"), Phone("11111"))
record1 = Record(Name("Name 2"), Phone("00000"))
record2 = Record(Name("Name 3"))
phone_list.add_record(record)
phone_list.add_record(record1)
phone_list.add_record(record2)

record.add_phone(Phone("22222"))
record.add_phone(Phone("33333"))
record.add_phone(Phone("44444"))
record.del_phone("22222")
record.cha_phone("44444", "55555")

record2.add_phone(Phone("44444"))

print(record.name.value)
for el in record.phones:
    print(el.value)
print(record1.name.value)
for el in record1.phones:
    print(el.value)
print(record2.name.value)
for el in record2.phones:
    print(el.value)
