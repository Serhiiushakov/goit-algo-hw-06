from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # Клас для зберігання імені контакту

    def __init__(self, value):
        super().__init__(value)  # Ініціалізуємо клас
        

class Phone(Field):
    # Клас для зберігання номера телефону. Має валідацію формату (10 цифр)

    def __init__(self, value):
        super().__init__(value)  # Ініціалізуємо клас
        if not self.validate_phone(value):
            raise ValueError("Неправильний формат номера телефону")

    def validate_phone(self, phone):
        return len(phone) == 10 and phone.isdigit()

class Record:
    # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.

    def __init__(self, name):
        self.name = Name(name)  # Створюємо об'єкт класу Name для зберігання імені
        self.phones = []  # Пустий список для зберігання телефонів

    def add_phone(self, phone):
        # Додаємо новий телефон до списку
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        # Видаляємо телефон зі списку
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        # Редагуємо номер телефону
        for idx, phone in enumerate(self.phones):
            if str(phone) == old_phone:
                self.phones[idx] = Phone(new_phone)
                break

    def find_phone(self, phone):
        # Пошук телефону у записі
        for p in self.phones:
            if str(p) == phone:
                return p
        return None

    def __str__(self):
        # Перевизначаємо метод для зручного виводу
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    # Клас для зберігання та управління записами.

    def add_record(self, record):
        # Додаємо запис до адресної книги
        self.data[record.name.value] = record

    def find(self, name):
        # Знаходимо запис за ім'ям
        return self.data.get(name, None)

    def delete(self, name):
        # Видаляємо запис за ім'ям
        if name in self.data:
            del self.data[name]

############## Приклад використання з ДЗ #####################

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phone: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
