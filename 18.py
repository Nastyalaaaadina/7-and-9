def hello(name = "World!"):
 print("Hello", name)
hello()
hello("dear user! Nice to meet you!")
n=int(input('Введите число, содержащее нечетные цифры(например, 1,3,5,7,9):'))
if not [x for x in str(n) if int(x) % 2]:
 print('Ошибка,ваше число НЕ содержит нечетные цифры,попробуйте еще раз.')
else: 
 print("Наименьшая нечетная цифра: ", min(int(x) for x in str(n) if int(x) % 2))