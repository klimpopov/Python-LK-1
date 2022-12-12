# print ('hello world')

value = None
a = 123  # Переменная int типа. Не нужно объявлять.
b = 1.23 # Переменная float типа. Не нужно объявлять.
print (a)
print(type(a))
print(b)
print(type(b))
value = 12334
print(value)
print(type(value))

s = 'hello world'
print (s)  # Вывод строки
s = 'hello \nworld'
print (s)
s = "hello 'world'"
print (s)
s = 'hello "world"'
print (s)
s = 'hello \'world'
print (s)


print(a,b,s)
print(a,'-',b,'-', s)
print('{} - {} - {}'.format(a,b,s))
print(f'{a} - {b} - {s}')
print('{1} - {2} - {0}'.format(a,b,s))

f = True # Булевая переменная
print(f)

list = [] # Объявление массива
print(list)
list = [1, 2 , 3]
print(list)
list = ['1', '2' , '3', 'hellow world']
print(list)
list = ['1', '2' , '3', 'hellow world', 1, 2, 4.5, True]
print(list)

col = ['hellow world', 1, 2, 4.5, True] #  Пробел может поломать программу в этом языке
print (col)

#print('Введите a');
#a = input()
#print('Введите b');
#b = input()
#print(a,b)
#print('{} {}'.format(a,b))
#print(f'{a} {b}')
#print(a, ' + ', b, ' = ', a+b) # По умолчанию печатается в строковом формате, то есть, например если а = 10 и b = 20, то выведется 1020, а не 30.
#print('Введите a');
#a = int(input()) # Запись в переменную значения в формате int
#print('Введите b');
#b = int(input())
#print(a, ' + ', b, ' = ', a+b)

#print('Введите a');
#a = float(input()) # Запись в переменную значения в формате int
#print('Введите b');
#b = float(input())
#print(a, ' + ', b, ' = ', a+b)

a=2
b=8
c=a+b
print(c)
c=a-b
print(c)
c=a*b
print(c)
c=a/b
print(c)
c=a//b # Деление в целых числах
print(c)
c=a%b # Остаток от деления
print(c)
c=a**b # Возведение в степень
print(c)
c=round(a/b,1) # Округление до нужного кол-ва знаков по правилам математики
print(c)
a=3
a=a+5
print(a)
a+=5
print(a)

a=1>4
print(a)
a = 'qwe'
b = 'qwe'
print(a==b)
a=[1,2]
b=[1,2]
print(a==b)

a=1<3<5
print(a)

a=1<3<5<10
print(a)

f=[1,2,3,4]
print(f)
print(2 in f)
print(not 2 in f)

is_odd = f[0] % 2 ==0
print(is_odd)

#a = int(input('a = '))
#b = int(input('b = '))
#if a > b:
    #print(a)
#else:
    #print(b)

#username = input('Введите имя: ')
#if username == 'Маша':
#    print('Условие с Машей')
#elif username == 'Клим':
#    print('Условие с Климом')
#else:
#    print('Привет, ',username)

original = 23
inverted = 0
while original !=0:
    inverted = inverted * 10 + (original % 10)
    original //=10
print(inverted)

original = 23
inverted = 0
while original !=0:
    inverted = inverted * 10 + (original % 10)
    original //=10
else:
    print('Пожалуй')
    print('хватит')
print(inverted)

list = [1,2,3,4,10,5]
for i in list:
    print(i*2)

for i in range(1,5, 2): # Пробегаемся от 1 до 4 c приращением в 2
    print(i)

text = 'Слова'
help(text.istitle)

def f(x): # Описание функции, можно миксовать типы переменных 
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
arg = 1
print(f(arg))
print(type(f(arg)))
