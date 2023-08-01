# n = 5

# print (n)

# n = "abcd"
# print (n)

# a = 5
# b = 4.56
# c = "hello"

# print (f" - {a}, - {b}, - {c}")
# print ("{} - {} - {}". format(a, b, c))

# print("Введите данные")
# a = input()
# print (a)

# print("Input 1st number: ")
# a = input()
# b = input("Input 2nd number: ")

# print (a, " + ", b, " = ", a + b)

# c = 5.89
# print (c)
# n = int (c)
# print (n)

# print(type(n))

# print("Input 1st number: ")
# a = int(input())
# b = int(input("Input 2nd number: "))

# print (a, " + ", b, " = ", a + b)

# Округление
# a = 67.56789
# b = 3.56789

# print (a * b)

# a = 67.56789
# b = 3.56789

# print (round(a * b, 2))

# a = 1 > 4
# print (a)

# a = 1 < 4 and 5 > 2
# print (a)

# a = 1 == 2
# print (a)

# a = 1 != 2
# print (a)

# a = "abc"
# b = "abc"
# print (a == b)

# a = 1 < 3 < 5 < 8 < 10
# print (a)

# username = input ("Input name: ")
# if username == "Maria" :
#     print ("Hey Maria!")
# elif username == "Bara" :
#     print ("Fuck off Bara!")
# elif username == "Vara" :
#     print ("Good bye Vara!")
# else: 
#     print ("Hello, " , username)

# n = 123
# sum = 0
# while n > 0:
#     x =  n % 10
#     sum += x
#     n = n // 10
# print (sum)

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i += 1
# else:
#     print ("well")
#     print ("anogh")
# print (i) 

# i = 0
# while i < 5:
   
#     i += 1
# else:
#     print ("well")
#     print ("anogh")
# print (i) 

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# a = "qwerty"
# print (a[0])

# a = "qwerty"
# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)


# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text)) # 39 символов
# print('ещё' in text) # True (строка есть в нашем тексте)
# print(text.lower()) # съешь ещё этих мягких французских булок (все перевели в нижний регистр)
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК (все перевели в верхний регистр)
# print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок (замена в тексте)

#  text = 'съешь ещё этих мягких французских булок'
#  print(text[0]) # c
#  print(text[1]) # ъ
#  print(text[len(text)-1]) # к
#  print(text[-5]) # б
#  print(text[:]) # съешь ещё этих мягких французских булок
#  print(text[:2]) # съ
#  print(text[len(text)-2:]) # ок
#  print(text[2:9]) # ешь ещё
#  print(text[6:-18]) # ещё этих мягких
#  print(text[0:len(text):6]) # сеикакл
#  print(text[::6]) # сеикакл
#  text = text[2:9] + text[-5] + text[:2] # ...