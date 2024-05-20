#1

import pickle

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

class Contacts:
    def __init__(self, filename: str, contacts: list['Person'] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0  
        
    def save_to_file(self):
        # Зберегти поточне значення count_save
        current_count_save = self.count_save
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)
        # Повернути значення count_save до початкового стану
        self.count_save = current_count_save + 1

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        # Тимчасово зберегти значення count_save
        current_count_save = self.count_save
        # Змінити значення count_save до поточного стану
        self.count_save += 1
        state = self.__dict__.copy()
        # Повернути значення count_save до початкового стану
        self.count_save = current_count_save
        return state

# Приклад використання
contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

# Створити екземпляр класу Contacts
persons = Contacts("user_class.dat", contacts)

# Зберегти у файл
persons.save_to_file()

# Прочитати з файлу
first = persons.read_from_file()

# Зберегти у файл
first.save_to_file()

# Прочитати з файлу
second = first.read_from_file()

# Зберегти у файл
second.save_to_file()

# Прочитати з файлу
third = second.read_from_file()

# Вивести значення count_save
print(persons.count_save)  # 0
print(first.count_save)  # 1
print(second.count_save)  # 2
print(third.count_save)  # 3


#2
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0
        self.is_unpacking = False  # Доданий атрибут is_unpacking

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
            content.is_unpacking = True  # Встановлюємо is_unpacking як True при розпакуванні
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] += 1
        return attributes

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.is_unpacking = True  # Позначаємо, що екземпляр був розпакований

# Приклад використання
contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

# Створити екземпляр класу Contacts
persons = Contacts("user_class.dat", contacts)

# Зберегти у файл
persons.save_to_file()

# Прочитати з файлу
person_from_file = persons.read_from_file()

# Вивести значення is_unpacking
print(persons.is_unpacking)  # False
print(person_from_file.is_unpacking)  # True

#3

import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)

# Приклад використання
person = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

copy_person = copy_class_person(person)

print(copy_person == person)  # False
print(copy_person.name == person.name)  # True


#4

import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True


def copy_class_contacts(contacts):
    return copy.deepcopy(contacts)

# Створення екземплярів класу Person
person1 = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)
person2 = Person(
    "Chaim Lewis",
    "dui.in@egetlacus.ca",
    "(294) 840-6685",
    False,
)

# Додавання екземплярів до списку contacts
contacts = [person1, person2]

# Створення екземпляра класу Contacts
persons = Contacts("user_class.dat", contacts)

# Копіювання об'єкту класу Contacts
new_persons = copy_class_contacts(persons)

# Зміна імені першого контакту у новому списку
new_persons.contacts[0].name = "Another name"

# Виведення імені першого контакту у початковому та копійованому списку
print(persons.contacts[0].name)  # Allen Raymond
print(new_persons.contacts[0].name)  # Another name

#5
import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        return Person(self.name, self.email, self.phone, self.favorite)   
            
class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        return Contacts(self.filename)

    def __deepcopy__(self, memo):
        copied_contacts = Contacts(self.filename)
        copied_contacts.is_unpacking = copy.deepcopy(self.is_unpacking, memo)
        copied_contacts.count_save = copy.deepcopy(self.count_save, memo)
        copied_contacts.contacts = copy.deepcopy(self.contacts, memo)
        return copied_contacts
    
#6

