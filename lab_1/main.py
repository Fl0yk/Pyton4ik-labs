from functions import hello_world, doOperfirstNumtion
from utilties import check_float

hello_world()

print("Теперь второй пункт.\n Введите первое целое число:")
num1=check_float(input())

print("Введите второе целое число:")
num2=check_float(input())

print("Введите операцию(add, sub, mult, div):")
operation=str(input())

print(doOperfirstNumtion(num1, num2, operation))