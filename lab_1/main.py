from functions import hello_world, doOperfirstNumtion, evenNumbers
from utilties import check_integer, check_list

hello_world()

print("\nТеперь второй пункт.\n Введите первое целое число:")
num1=check_integer(input())

print("Введите второе целое число:")
num2=check_integer(input())

print("Введите операцию(add, sub, mult, div):")
operation=str(input())

print(doOperfirstNumtion(num1, num2, operation))

print("\nТеперь третий пункт. Введите список целых чисел(тут лучше не ошибаться:) вводите через пробел):")

listNum=check_list(input().split())

if(listNum):
    print(evenNumbers(listNum))
else:
    print("Ввели плохой список. Теперь все заново")
