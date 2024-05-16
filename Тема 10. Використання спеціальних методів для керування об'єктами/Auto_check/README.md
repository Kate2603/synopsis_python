1. Створіть клас Point, який відповідатиме за відображення геометричної точки на площині.

Реалізуйте через конструктор __init__ ініціалізацію двох атрибутів: координати x та координати y.

Приклад:

point = Point(5, 10)

print(point.x)  # 5
print(point.y)  # 10

-----------------------------------------

2. У класу Point через конструктор __init__ оголошено два атрибути: координати x та y. Приховати доступ до них з допомогою подвійного підкреслення: __x та __y

Реалізуйте для класу Point механізми setter та getter до атрибутів __x та __y за допомогою декораторів property та setter.

Приклад:

point = Point(5, 10)

print(point.x)  # 5
print(point.y)  # 10

-----------------------------------------

3. У класу Point до механізму setter властивостей x і y додайте перевірку на значення, що вводиться. Дозвольте встановлювати значення властивостей x та y для екземпляра класу, тільки якщо вони мають числове значення (int або float).

Приклад:

point = Point("a", 10)

print(point.x)  # None
print(point.y)  # 10


class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        
            

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):

--------------------------------------------

4. class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
     
    def __getitem__(self, index):
        
Реалізуйте клас Vector. Властивість coordinates визначає координати вектора і є екземпляром класу Point. Нагадаємо, що вектором називають спрямований відрізок з початком та кінцем. Початок у нас буде в точці (0, 0), а кінець вектора ми задаватимемо атрибутом coordinates.
Реалізуйте можливість звертатися до координат екземпляра класу Vector через квадратні дужки:
vector = Vector(Point(1, 10))

print(vector.coordinates.x)  # 1
print(vector.coordinates.y)  # 10

vector[0] = 10  # Встановлюємо координату x вектора 10

print(vector[0])  # 10
print(vector[1])  # 10

Щоб отримати значення, використовуючи квадратні дужки об'єкта print(vector[0]), реалізуйте метод __getitem__ у класу Vector.
Для запису значення координат вектора через індекс, як vector[0] = 10, реалізуйте метод __setitem__ у класу Vector.
Звернення до координати x проводиться за індексом 0, а звернення до координати y - за індексом 1.

---------------------------------------------------

5. class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __str__(self):
        
Реалізуйте для класу Point та Vector магічний метод __str__. Для класу Point метод повинен повертати рядок виду Point(x,y), а для класу Vector - рядок Vector(x,y), як у прикладі нижче (замість x,y необхідно підставити значення координат екземпляра класу):
point = Point(1, 10)
vector = Vector(point)

print(point)  # Point(1,10)
print(vector)  # Vector(1,10)

----------------------------------------------------------------

6. class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
    
    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"
Для екземпляра класу Vector реалізуйте функтор. Створіть для класу Vector метод __call__. Він має реалізувати наступну поведінку:
vector = Vector(Point(1, 10))

print(vector())  # (1, 10)

При виклику екземпляра класу як функції він повертає кортеж з координатами вектора.
Якщо при виклику ми передаємо параметр число, ми виконуємо добуток вектора на число — множимо кожну координату на вказане число та повертаємо кортеж з новими координатами вектора.
vector = Vector(Point(1, 10))

print(vector(5))  # (5, 50)
--------------------------------------------------------------

7. class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        
        
        

    def __sub__(self, vector):  
    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"
Реалізуйте для класу Vector операції додавання та віднімання векторів. Тобто перевизначите для нього математичні оператори __add__ та __sub__
Є два вектори: a з координатами (x1, y1) та b з координатами (x2, y2).
Тоді додавання векторів b + a - це новий вектор з координатами (x2 + x1, y2 + y1). Віднімання – зворотна операція, b - a - це новий вектор з координатами (x2 - x1, y2 - y1)
Приклад коду:
vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

vector3 = vector2 + vector1
vector4 = vector2 - vector1

print(vector3)  # Vector(11,20)
print(vector4)  # Vector(9,0)

------------------------------------------------------------------

8. class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"
Реалізуйте для класу Vector операцію скалярного добутку векторів. Тобто перевизначте для нього математичний оператор __mul__
Є два вектори: a з координатами (x1, y1) та вектор b з координатами (x2, y2).
Тоді скалярний добуток векторів b*a - це таке число x2*x1+y2*y1.
Приклад коду:
vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

scalar = vector2 * vector1

print(scalar)  # 110

-----------------------------------------------------------------

9. class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        return (
                self.coordinates.x * vector.coordinates.x
                + self.coordinates.y * vector.coordinates.y
        )

    def len(self):
        

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"
Перш ніж ми приступимо до операцій порівняння векторів, реалізуйте метод визначення довжини вектора - len для класу Vector
Для вектора a з координатами (x1, y1) його довжина визначається за такою формулою:
(x1 ** 2 + y1 ** 2) ** 0.5.
Приклад коду:
vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

print(vector1.len())  # 10.04987562112089
print(vector2.len())  # 14.142135623730951

----------------------------------------------------------

10. class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        return (
                self.coordinates.x * vector.coordinates.x
                + self.coordinates.y * vector.coordinates.y
        )

    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

    def __eq__(self, vector):
        

    def __ne__(self, vector):
        

    def __lt__(self, vector):
        

    def __gt__(self, vector):
        

    def __le__(self, vector):
        

    def __ge__(self, vector):
Реалізуйте всі методи порівняння для класу Vector. З метою спрощення порівнювати екземпляри класу Vector будемо тільки за їх довжиною, використовуючи метод len, не враховуючи напрямок векторів.
Приклад коду:
vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(3, 10))

print(vector1 == vector2)  # False
print(vector1 != vector2)  # True
print(vector1 > vector2)  # False
print(vector1 < vector2)  # True
print(vector1 >= vector2)  # False
print(vector1 <= vector2)  # True

----------------------------------------------------------------

11. from random import randrange


class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        return (
                self.coordinates.x * vector.coordinates.x
                + self.coordinates.y * vector.coordinates.y
        )

    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

    def __eq__(self, vector):
        return self.len() == vector.len()

    def __ne__(self, vector):
        return self.len() != vector.len()

    def __lt__(self, vector):
        return self.len() < vector.len()

    def __gt__(self, vector):
        return self.len() > vector.len()

    def __le__(self, vector):
        return self.len() <= vector.len()

    def __ge__(self, vector):
        return self.len() >= vector.len()


class Iterable:
    def __init__(self, max_vectors, max_points):
        self.current_index = 0
        self.vectors = []
        
            

    def __next__(self):
        
            
            
            
        
            


class RandomVectors:
    def __init__(self, max_vectors=10, max_points=50):
        
        

    def __iter__(self):
Необхідно реалізувати клас RandomVectors, який зможе створювати об'єкт, що ітерується, і дозволяти ітеруватися по випадковим векторам.
Формат класу:
RandomVectors(max_vectors: int, max_points: int) -> Iterable(max_vectors, max_points)

де:
max_vectors — визначає максимальну кількість елементів (примірників класу Vector) в ітерованій послідовності
max_points — визначає максимальне значення для координат x та y (в діапазоні 0...max_points)
Щоб екземпляри класу RandomVectors були об'єктами, що ітеруються, в класі повинен бути реалізований метод __iter__, який повертає ітератор. Ітератор – це будь-який об'єкт, який на кожному кроці ітерації (крок ітерації – це виклик методу next() для цього ітератора) повертає таке значення - і так до вичерпання кількості ітерацій (визначається параметром max_vectors).
У нашому випадку ітератором буде клас Iterable, у якому необхідно реалізувати метод __next__. Він у конструкторі отримує ті ж параметри max_vectors та max_points, що і клас RandomVectors.
Метод __next__ повинен видавати кожне наступне значення зі списку self.vectors. Створіть у конструкторі набір випадкових векторів self.vectors завдовжки max_vectors за допомогою randrange. Атрибут current_index вказівник-індекс на поточний вектор зі списку vectors, необхідний для ітерування.
Приклад роботи класу `RandomVectors:
vectors = RandomVectors(5, 10)

for vector in vectors:
    print(vector)

Вивід має бути схожим на цей:
Vector(7,7)
Vector(0,0)
Vector(8,9)
Vector(1,9)
Vector(6,6)

Деталізуємо наше завдання:
Клас RandomVectors повинен мати метод __iter__, який має повернути об'єкт ітератора (клас Iterable)
Об'єкт ітератора (примірник класу Iterable) повинен мати метод __next__
Метод __next__ стежить за кількістю можливих кроків ітерації, вони визначаються параметром max_vectors
Якщо ми вичерпали можливі кроки, то метод __next__ генерує виняток StopIteration
В іншому випадку метод __next__ повертає вектор з випадковими координатами (примірник класу Vector), розмір координат вектора визначається параметром max_points.

----------------------------------------------------------------------


