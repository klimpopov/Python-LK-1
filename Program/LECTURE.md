# Переменные
В python используются переменые: int, float, boolean, str, list, None и др.

Эти переменные имеют **динамическое представление**, то есть их не надо объявлять специально через указания типа переменной.

a = 123  # Переменная int типа. Не нужно объявлять.

b = 1.23 # Переменная float типа. Не нужно объявлять.

s = 'hellow world' # Переменная str типа. Не нужно объявлять.

f = True # Булевая переменная

Переменная None позволяет объявить переменную в одной части кода и использовать в другой части кода.

# Списка - массивы

В python нет массивов, есть что-то похожее: list.

 **Объявление массива:** 
 
 + list = []
 + list = [1, 2 , 3]                        # С заполненным массивом
 + list = ['1', '2' , '3', 'hellow world']  # Лист строк
 + list = ['1', '2' , '3', 'hellow world', 1, 2, 4.5, True] # Можно "миксовать" типы переменных, записанных в лист, за счёт динамического представления в языке. ***Но так делать не нужно!!!***, лучше пусть данные будут одного типа.

  **Вывод массива:** print (list)


  **Список** – пронумерованная, изменяемая коллекция
объектов произвольных типов

+ numbers = [1, 2, 3, 4, 5]

  print(numbers) # [1, 2, 3, 4, 5]

+ numbers = list(range(1, 6))
  
  print(numbers) # [1, 2, 3, 4, 5]
  
  numbers[0] = 10
  
  print(numbers) # [10, 2, 3, 4, 5]
  
  for i in numbers:
  
  i *= 2
  
  print(i) # [20, 4, 6, 8, 10]
  
  print(numbers) # [10, 2, 3, 4, 5]


+ colors = ['red', 'green', 'blue']
  
  for e in colors:
 
  print(e) # red green blue
  
  for e in colors:
 
  print(e*2) # redred greengreen blueblue

  colors.append('gray') # добавить в конец

  print(colors == ['red', 'green', 'blue', 'gray']) # True

  colors.remove('red') #del colors[0] # удалить элемент 


  # Пробел 

  Пробел может поломать программу в этом языке.


# Ввод данных

print('Введите a');

a = input()

print('Введите b');

b = input()

print(a,b)

print(a, ' + ', b, ' = ', a+b) # По умолчанию печатается в строковом формате, то есть, например если а = 10 и b = 20, то выведется 1020, а не 30.

**Используем функцию int, то посчитается правильно, выведется значение 30.**

print('Введите a');

a = int(input()) # Запись в переменную значения в формате int

print('Введите b');

b = int(input())
print(a, ' + ', b, ' = ', a+b)

**Для других типов данных, пишем соответвующие название типа данны**

Например 

a = float(input()) # Запись в переменную значения в формате float

# Вывод данных
print ()

print(type(b)) - узнать тип переменной

Обрамеления:

Можно несколькими вариантами:

1) s = "hello 'world'"

2) s = 'hello "world"'

3) s = 'hello \'world'

s = 'hello \nworld'  \n - переход на новую строку


Вывод нескольких значений:

1) print (a,b,s)

2) print(a,' - ',b,' - ', s)

3) print('{} - {} - {}'.format(a,b,s))

4) print(f'{a} - {b} - {s}')

5) print('{1} - {2} - {0}'.format(a,b,s))  Расположение переменных черех {}


# Арифметические операции
+ Стандартные операторы

+ Унарные -, то есть, например -321
+ c=a//b # Деление в целых числах
+ c=a%b # Остаток от деления
+ c=a**b # Возведение в степень
+ c=round(a/b,1) # Округление до нужного кол-ва знаков по правилам математики

# Логические операции
+ Как в других языках: >, >=, <, <=, ==, !=

a=1>4

print(a) Выведет true или false 

a = 'qwe'

b = 'qwe'

print(a==b) Выведет true (false)


a=[1,2]

b=[1,2]

print(a==b) Выведет true (false)
+ Можно использовать 3-ые или 4-ые неравенства

a=1<3<5

print(a) Выведет true (false)

a=1<3<5<10

print(a) Выведет true (false)

+ Проверка элемента в списке

f=[1,2,3,4]

print(f)

print(2 in f) Выведет true (false)

print(not 2 in f) Выведет false (true)

+ Проверка на четность

is_odd = f[0] % 2 ==0

print(is_odd) Выведет false (true)

# Операторы if, if-else
+ Важны отсутпы, иначе может поломаться ветвление
+ if, if-else

a = int(input('a = '))

b = int(input('b = '))

if a > b:

    print(a)

else:

    print(b)

+ if, elif

username = input('Введите имя: ')

if username == 'Маша':

    print('Условие с Машей')

elif username == 'Клим':

    print('Условие с Климом')

else:

    print('Привет, ',username)

+ while 

original = 23

inverted = 0

while original !=0:

    inverted = inverted * 10 + (original % 10)

    original //=10

print(inverted)

+ while - else

original = 23

inverted = 0

while original !=0:

    inverted = inverted * 10 + (original % 10)

    original //=10

else: # Выполняется, когда основное тело цикла отработало

    print('Пожалуй')

    print('хватит')

print(inverted)

+ for

list = [1,2,3,4,10,5]

for i in list:

    print(i*2)

# Справка по методам

help(название метода). Выйдет описание функции

Например: 

text = 'Слова'

help(text.istitle)


# Операции со строками

text = 'съешь ещё этих мягких французских булок'

print(text[0]) # c

print(text[1]) # ъ

print(text[len(text)-1]) # к

print(text[-5]) # б

print(text[:]) # print(text)

print(text[:2]) # съ

print(text[len(text)-2:]) # ок

print(text[2:9]) # ешь ещё

print(text[6:-18]) # ещё этих мягких

print(text[0:len(text):6]) # сеикакл

print(text[::6]) # сеикакл

text = text[2:9] + text[-5] + text[:2] # 

# Функции 

def f(x): # Описание функции, можно миксовать типы переменных 

    if x == 1:

        return 'Целое'

    elif x == 2.3:

        return 23

    else:

        return

arg = 1

print(f(arg)) # Вызов функции с передачей значения аргумента

print(type(f(arg))) # Тип данных будет изменяться в зависимости от выводимого элемента