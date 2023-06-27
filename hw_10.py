from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone=None):
        self.phones = []
        self.name = name
        if phone:
            self.add_phone(phone)

    def add_phone(self,  phone):
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



class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data.update({record.name.value: record})


if __name__ == "__main__":

    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')
