from sezializer import *
import math

def ser_test(obj):
    ser_obj = serialize(obj)
    
    print(ser_obj)
    print()
    
    des_obj = deserialize(ser_obj)
    
    print(des_obj)
    print("===========================")
    
def ser_test_func(obj, arg):
    print(obj(arg))
    ser_obj = serialize(obj)
    
    #print(ser_obj)
    print()
    
    des_obj = deserialize(ser_obj)
    
    print(des_obj(arg))
    print("===========================")
    
x = 10    
def my_func(a):
    return math.sin(a + x)

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("func start")
        res = func(*args, **kwargs)
        print("Func end")
        return res
        
    return wrapper

#@my_decorator
def for_dec(a):
    print("Hello World!", a)
    
X = 12
class A:
    bob = "sinii"
    
    
    @staticmethod
    def ret_bob():
        return A.bob
    
    def my_method(self, x):
        return x + 5

class B:
    @staticmethod
    @my_decorator
    def another_method(k):
        print("Hi:)")
        return math.sin(k * X)

class C(A, B):
    def __init__(self):   
        self.coca = "Cola"
    
    

ser_test(12)

ser_test(1.5)

ser_test([1, 2, 3, 4, "aboba"])

ser_test({1 : 1, 2 : 2, 3 : 3, "pip" : 4})

ser_test((5, 7, 9, "pup", 25))

ser_test(bytes([104, 101, 108, 108, 111]))

ser_test(bytearray(b'hello world!'))

ser_test_func(my_func, 3)

#сериализация самого декоратора
ser_obj = serialize(my_decorator)

for_dec(25)    
#print(ser_obj)
print()
    
des_obj = deserialize(ser_obj)

df = des_obj(for_dec)
    
df(25)
print("===========================")

#сериализация декорированной функции

df = my_decorator(for_dec)

ser_test_func(df, 25)

#сериализация анонимной функции
l = lambda b: b + 25

ser_test_func(l, 10)

cl = serialize(A)
#print(cl)

des_cl = deserialize(cl)
a = des_cl()


print(des_cl.ret_bob())
print(a.my_method(5))

print("===============================")

#Сериализация объекта
o = C()
print("Изначальные значения")
print("Переменная объекта: ", o.coca)
print("Статический метод класса А: ", o.ret_bob())
print("Статический декорированный метод класса B: ", o.another_method(10))

o_ser = serialize(o)
#print(o_ser)
des_o = deserialize(o_ser)

print("Десериализованные значения")
print("Переменная объекта: ", des_o.coca)
print("Статический метод класса А: ", des_o.ret_bob())
print("Статический декорированный метод класса B: ", des_o.another_method(10))


