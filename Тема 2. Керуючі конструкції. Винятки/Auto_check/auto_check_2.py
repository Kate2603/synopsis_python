################1

is_next = None
num = int(input("Enter the number of points: "))
if num >= 83:
    is_next = True
else: 
    is_next = False

################2

work_experience = int(input("Enter your full work experience in years: "))

if work_experience > 1 and work_experience <= 5 :
    developer_type = "Middle"
elif work_experience <= 1:
    developer_type = "Junior"
else :
    developer_type = "Senior"
print(work_experience)
print(developer_type)

################3

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 1:
        result = "Positive odd number"
    else:
        result = "Positive even number"
elif num < 0:
    result = "Negative number"
else :
    result = "It is zero"
print(num)

################4

num = int(input("Enter the integer (0 to 100): "))
sum = 0
print(num)

while num < 101:
    sum += num
    num -= 1
    print(sum)
    if num <=0:
        break

print(sum)


################5

message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for symbol in message:
    if symbol == "r": 
        result += 1
        continue
    
print(result)

################6

pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool // quantity
    print(chunk)
except ZeroDivisionError:
    print('Division by zero is not possible!')

################7

def greeting():
    print("Hello world!")

greeting()

################8

def invite_to_event(username):
    return f'Dear {username}, we have the honour to invite you to our event'

################9

def discount_price(price: int, discount: float = 0) -> float:
    def apply_discount():
        nonlocal price 
        price = price * (1 - discount)
    apply_discount() 
    return price

################10

def get_fullname(first_name: str, last_name: str, middle_name: str = "") -> str:
    if middle_name == "":
        return f'{first_name} {last_name}'
    else:
        return f'{first_name} {middle_name} {last_name}'
    
################11

def format_string(string, length):
    if len(string) < length:
        spaces = ((length - len(string)) // 2) * ' '
        return f'{spaces}{string}'
    else:
        return f'{string}'

################12

def first(size, *args):
    sum = size + len(args)
    return sum


def second(size, **kwargs):
    sum = size + len(kwargs)
    return sum

################13

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    return factorial (n) // (factorial (k) * factorial (n - k))




