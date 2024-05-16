#1
class Animal:
    pass

animal = Animal()

#2
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass
    
     
# Creating an instance of the Animal class
animal = Animal("Simon", 10)


#3
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass
    
    def change_weight(self, new_weight):
        self.weight = new_weight
     
# Creating an instance of the Animal class
animal = Animal("Simon", 10)

# Change in animal weight
animal.change_weight(12)

# Output the new weight value
print(animal.weight)  # Повинно вивести 12

#4
class Animal:
    color = 'white'  # Color class variable

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, new_weight):
        self.weight = new_weight

    @classmethod
    def change_color(cls, new_color):
        cls.color = new_color

# Creating an instance of the Animal class
first_animal = Animal("Simon", 10)
second_animal = Animal("Bars", 8)

# Color change for the first instance
Animal.change_color("red")

# Outputting the values of the class variables for the first and second instances
print("The first copy:")
print("Nickname:", first_animal.nickname)
print("Weight:", first_animal.weight)
print("Color:", first_animal.color)

print("\nThe second copy:")
print("Nickname:", second_animal.nickname)
print("Weight:", second_animal.weight)
print("Color:", second_animal.color)

# The first copy:
# Nickname: Simon
# Weight: 10
# Color: red

# The second copy:
# Nickname: Bars
# Weight: 8
# Color: red

#5
class Animal:
    color = 'white'

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, new_weight):
        self.weight = new_weight

    @classmethod
    def change_color(cls, new_color):
        cls.color = new_color


class Cat(Animal):
    def say(self):
        return "Meow"


# Creating an instance of the Cat class
cat = Cat("Simon", 10)

# Display information about the cat
print("The name of the cat:", cat.nickname)
print("The weight of the cat:", cat.weight)
print("The color of the cat:", cat.color)
print("The sound that a cat makes:", cat.say())

# The name of the cat: Simon
# The weight of the cat: 10
# The color of the cat: white
# The sound that a cat makes: Meow



#6
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight
        

class Dog(Animal):
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed = breed

    def say(self):
        return "Woof"
    
# Creating an instance of the Dog class
dog = Dog("Barbos", 23, "labrador")

# Output of information about the dog
print("The name of the dog:", dog.nickname)
print("The weight of the dog:", dog.weight)
print("Dog breed:", dog.breed)
print("The sound a dog makes:", dog.say())

# The name of the dog: Barbos
# The weight of the dog: 23
# Dog breed: labrador
# The sound a dog makes: Woof


#7
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return {'name': self.name, 'age': self.age, 'address': self.address}


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()


# Creating an instance of the Owner class
owner = Owner("John", 35, "123 Main St")

# Creating an instance of the Dog class with an owner
dog = Dog("Barbos", 23, "labrador", owner)

# Output of information about the owner of the dog
print(dog.who_is_owner())


#8
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"

    def info(self):
        return f"{self.nickname}-{self.weight}"


class Dog(Animal):
    def say(self):
        return "Woof"

    def info(self):
        return f"{self.nickname}-{self.weight}"


class CatDog(Cat, Dog):
    def say(self):
        return super().say()

    def info(self):
        return super().info()


class DogCat(Dog, Cat):
    def say(self):
        return super().say()

    def info(self):
        return super().info()


# Example of use
catdog = CatDog("Tom", 5)
dogcat = DogCat("Buddy", 10)

print(catdog.say())  # "Meow"
print(dogcat.say())  # "Woof"

print(catdog.info())  # "Tom-5"
print(dogcat.info())  # "Buddy-10"


#9
from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data:
            if self.data[key] == value:
                keys.append(key)
        return keys


# Example of use
lookup_dict = LookUpKeyDict({'a': 1, 'b': 2, 'c': 1, 'd': 3})
print(lookup_dict.lookup_key(1))  # ['a', 'c']
print(lookup_dict.lookup_key(2))  # ['b']
print(lookup_dict.lookup_key(3))  # ['d']
print(lookup_dict.lookup_key(4))  # []

#10
from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        total = 0
        for value in self.data:
            if value > 0:
                total += value
        return total


# Example of use
payment = AmountPaymentList([1, -3, 4])
print(payment.amount_payment())  # 5

#11
from collections import UserString

class NumberString(UserString):
    def number_count(self):
        count = 0
        for char in self.data:
            if char.isdigit():
                count += 1
        return count


# Example of use
ns = NumberString("Hello12345World")
print(ns.number_count())  # 5


#12
class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if not employee_id.startswith('01'):
        raise IDException("Employee ID must start with '01'")
    id_list.append(employee_id)
    return id_list


# Example of use
ids = ['0101', '0110', '0201']
try:
    ids = add_id(ids, '0303')
    print(ids)  # This throws an error, so this line will not be executed
except IDException as e:
    print("Error:", e)  # Will throw an error: "Employee ID must start with '01'"
    
#13
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    def __init__(self, nickname=None, weight=None):
        self.nickname = nickname
        self.weight = weight
        self.cat = Cat(nickname, weight)

    def change_weight(self, weight):
        self.weight = weight

    def say(self):
        return self.cat.say()

# Example of use
dog = CatDog()
print(dog.say())  # "Meow"

#14
class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        contact = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite
        }
        self.contacts.append(contact)
        Contacts.current_id += 1

# Example of use
contacts = Contacts()
contacts.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
contacts.add_contacts("Cyrus Jackson", "(501) 472-5218", "nibh@semsempererat.com", False)
print(contacts.list_contacts())


# Will display a list of contacts with the added contact
#[{'id': 1, 'name': 'Wylie Pope', 'phone': '(692) 802-2949', 'email': 'est@utquamvel.net', 'favorite': True}, 
# {'id': 2, 'name': 'Cyrus Jackson', 'phone': '(501) 472-5218', 'email': 'nibh@semsempererat.com', 'favorite': False}]


#15
class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        contact = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite
        }
        self.contacts.append(contact)
        Contacts.current_id += 1

    def get_contact_by_id(self, contact_id):
        for contact in self.contacts:
            if contact["id"] == contact_id:
                return contact
        return None

# Приклад використання
contacts = Contacts()
contacts.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
contacts.add_contacts("Cyrus Jackson", "(501) 472-5218", "nibh@semsempererat.com", False)

# Отримання контакту за id
print(contacts.get_contact_by_id(1))  # Виведе контакт з id=1
print(contacts.get_contact_by_id(2))  # Виведе контакт з id=2
print(contacts.get_contact_by_id(3))  # Виведе None, бо контакту з id=3 немає в списку

#16
class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        contact = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite
        }
        self.contacts.append(contact)
        Contacts.current_id += 1

    def get_contact_by_id(self, contact_id):
        for contact in self.contacts:
            if contact["id"] == contact_id:
                return contact
        return None

    def remove_contacts(self, contact_id):
        for i in range(len(self.contacts)):
            if self.contacts[i]["id"] == contact_id:
                del self.contacts[i]
                break

# Приклад використання
contacts = Contacts()
contacts.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
contacts.add_contacts("Cyrus Jackson", "(501) 472-5218", "nibh@semsempererat.com", False)

# Видалення контакту за id
contacts.remove_contacts(1)
print(contacts.list_contacts())  # Виведе список контактів без контакту з id=1

