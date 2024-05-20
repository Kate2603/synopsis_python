#1
import pickle

def write_contacts_to_file(filename, contacts):
    with open(filename, 'wb') as file:
        pickle.dump(contacts, file)

def read_contacts_from_file(filename):
    with open(filename, 'rb') as file:
        contacts = pickle.load(file)
    return contacts

#2
import json

def write_contacts_to_file(filename, contacts):
    with open(filename, 'w') as file:
        json.dump({"contacts": contacts}, file, indent=2)

def read_contacts_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data["contacts"]
    
#3
import csv

def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email", "phone", "favorite"])
        writer.writeheader()
        writer.writerows(contacts)

def read_contacts_from_file(filename):
    contacts = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["favorite"] = row["favorite"] == 'True'
            contacts.append(row)
    return contacts

#4
import pickle

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __eq__(self, other):
        if isinstance(other, Person):
            return (
                self.name == other.name
                and self.email == other.email
                and self.phone == other.phone
                and self.favorite == other.favorite
            )
        return False

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts

    def save_to_file(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self, f)

    def read_from_file(self):
        with open(self.filename, "rb") as f:
            loaded_contacts = pickle.load(f)
        return Contacts(self.filename, loaded_contacts.contacts)

    def __eq__(self, other):
        if isinstance(other, Contacts):
            return self.filename == other.filename and self.contacts == other.contacts
        return False

# Example usage
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
persons.save_to_file()
person_from_file = persons.read_from_file()

print(persons == person_from_file)  # True
print(persons.contacts[0] == person_from_file.contacts[0])  # True
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True

#5
