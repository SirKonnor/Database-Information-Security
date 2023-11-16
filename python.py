Площадь треугольника
a = float(input())
b = float(input())
print(0.5 * a * b)

Две старушки
S = float(input())
V1 = float(input())
V2 = float(input())
print(S / (V1 + V2))

Обратное число
a = float(input())
if a == 0:
    print('Обратного числа не существует')
else:
    print(1 / a)

451 градус по Фаренгейту
F = float(input())
print((5 / 9) * (F - 32))

Dog age
n = int(input())
if n <= 2:
    print(n * 10.5)
else:
    print((2 * 10.5) + (n - 2) * 4)

Первая цифра после точки
a = float(input())
print(int(a * 10) % 10)

Дробная часть
a = float(input())
print(a - int(a))

Наибольшее и наименьшее
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print('Наименьшее число = ', min(a, b, c, d, e))
print('Наибольшее число = ', max(a, b, c, d, e))

Сортировка трех
a = int(input())
b = int(input())
c = int(input())
print(max(a,b,c))
print((a + b + c) - max(a,b,c) - min(a,b,c))
print(min(a,b,c))

Интересное число
x = int(input())
a = x % 10
b = x // 10 % 10
c = x // 100
if a + b + c == 2 * max(a, b, c):
    print('Число интересное')
else:
    print('Число неинтересное')

Абсолютная сумма
a1 = float(input())
a2 = float(input())
a3 = float(input())
a4 = float(input())
a5 = float(input())
print(abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5))

Манхэттенское расстояние
p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())
print(abs(p1 - p2) + abs(q1 - q2))

Текст
print('"Python is a great language!" said Fred.' '"I do not ever remember having this much fun before"')

Whats'your name?
Name = input()
Surname = input()
print('Hello', Name, Surname+'!', 'You have just delved into Python.')

Футбольная команда
x = input()
print('Футбольная команда', x, 'имеет длину', str(len(x)), 'символов')

Три города
a = input()
b = input()
c = input()
if min(len(a), len(b), len(c)) == len(a):
    print(a)
elif min(len(a), len(b), len(c)) == len(b):
    print(b)
else:
    print(c)
if max(len(a), len(b), len(c)) == len(a):
    print(a)
elif max(len(a), len(b), len(c)) == len(b):
    print(b)
else:
    print(c)

Цвет настроения синий
x = input()
if 'синий' in x:
    print('YES')
else:
    print('NO')

Отдыхаем ли?
x = input()
if 'суббота' in x or 'воскресенье' in x:
    print('YES')
else:
    print('NO')

Корректный email
email = input()
if '@' not in email or '.' not in email:
    print('NO')
else:
    print('YES')

Евклидово расстояние
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5)
