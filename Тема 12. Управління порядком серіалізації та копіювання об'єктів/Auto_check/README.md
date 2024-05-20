1. import pickle
class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
    def save_to_file(self):
    def read_from_file(self):
Розробіть клас Person. Він має чотири властивості: ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.
Приклад створення екземпляра класу:
   Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

Розробіть клас Contacts. Він повинен ініціалізувати через конструктор дві властивості: filename - ім'я файлу для пакування об'єкта класу Contacts, contacts - список контактів, екземплярів класу Person.
Приклад створення екземпляра класу:
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

persons = Contacts("user_class.dat", contacts)

Розробіть два методи для серіалізації та десеріалізації екземпляра класу Contacts за допомогою пакету pickle та зберігання даних у бінарному файлі.
Перший метод save_to_file зберігає екземпляр класу Contacts у файл, використовуючи метод dump пакету pickle. Ім'я файлу зберігається в атрибуті filename.
Другий метод read_from_file читає та повертає екземпляр класу Contacts з файлу filename, використовуючи метод load пакету pickle.
Приклад роботи:
persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # False
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True

----------------------------------------------------------------------------------------

2. import pickle


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
        
Продовжуємо розширювати приклад із попереднього завдання. Додайте до класу Contacts атрибут is_unpacking, за замовчуванням він повинен мати значення False. Реалізуйте магічний метод __setstate__ для класу Contacts. При розпаковуванні екземпляра класу метод повинен змінювати значення атрибута is_unpacking на значення True. Таким чином, ця властивість визначатиме, що екземпляр класу отримано внаслідок розпакування.
Приклад роботи коду:
persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons.is_unpacking)  # False
print(person_from_file.is_unpacking)  # True

------------------------------------------------------------------------------------

3. import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):

Для копіювання екземпляра класу Person із попереднього прикладу реалізуйте функцію copy_class_person. Як параметр вона приймає екземпляр класу person, та повертає "поверхневу" копію об'єкта за допомогою функції copy із пакета copy.

Приклад коду:

person = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

copy_person = copy_class_person(person)

print(copy_person == person)  # False
print(copy_person.name == person.name)  # True
...

------------------------------------------------------------------------

4. import copy
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

Як ви вже зрозуміли, для класу Contacts створення поверхневої копії екземпляра класу не увінчається успіхом через те, що ми маємо атрибут contacts, який є списком екземплярів об'єктів класу Person, а отже, всі вони будуть передані за посиланням. Тому необхідно використовувати глибоке копіювання методом deepcopy з пакета copy

Для класу Contacts реалізуйте функцію copy_class_contacts. Як параметр вона приймає екземпляр класу Contacts і повертає глибоку копію об'єкта за допомогою функції deepcopy з пакета copy.

Приклад коду:

persons = Contacts("user_class.dat", contacts)

new_persons = copy_class_contacts(persons)

new_persons.contacts[0].name = "Another name"

print(persons.contacts[0].name)  # Allen Raymond
print(new_persons.contacts[0].name)  # Another name

----------------------------------------------------------------------------

5. import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        
            
            
            
            
        
        


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
        
        

    def __deepcopy__(self, memo):
        
Реалізуйте метод __copy__ для класу Person.
Реалізуйте методи __copy__ та __deepcopy__ для класу Contacts.

--------------------------------------------------------------------------------------------

6. 