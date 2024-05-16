##############1

name = "Kiti"
age = 25

##############2

rate = 1.68
value = 1568
payment = rate * value

##############3

rate = 1.68
value_day = 200
value_night = 200 
payment = rate*value_day + rate/2*value_night

##############4

first_name = "Katya"
last_name = "Gaf"

##############5

first_name = "Katya"
last_name = "Gaf"
full_name = "Katya" + " " + "Gaf"
print(full_name)

##############6

length = 2.75
width = 1.75
area = length * width
show = f"With width {width} and length {length} of the room, its area is equal to {area}"
print(show)

##############7

is_active = True
is_delete = False

##############8

name = "K"
age = 23
is_active = True
subscription = None

##############9

length = "2.75"
width = "1.75"
area = float(length) *float(width)
print(area)
show = f"With width {width} and length {length} of the room, its area is equal to {area}"
print(show)

##############10

name = input("Your name? ")
email = input("Your email? ")
age = int(input("Your email? "))
height = float(input("Your height? "))
is_active = True

##############11

length = float(input('Enter the value length'))
width = float(input('Enter the value width'))
area = length*width

##############12

my_list = []
my_list.insert(0, 2024)
my_list.insert(1, 'Python')
my_list.insert(2, 3.12)
print(my_list)

##############13

my_list = [2024, 3.12]
some_data = ['Python']
my_list.extend(some_data)
my_list.insert(1, 'Python')
my_list.reverse()
print(my_list)

##############14

data = {}
data = {"year": 2024, "lang": "Python", "version" : 3.12}
print(data)

##############15

cat = {}
info = {"status": "vaccinated", "breed": True}
cat["nick"] = "Simon"
cat["age"] = 7
cat["characteristics"] = ["лагідний", "кусається"]
age = cat.get("age")
cat.update(info)
print(cat)



