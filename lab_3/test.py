from tests.data_test import my_func, my_decorator, for_dec, A, B, C
from SerKosach153501.xml_ser import XMLSerializer

js = XMLSerializer()

def ser_test(obj):
    with open("xmlformat.xml", "w") as file:
        js.dump(obj, file)
    
    with open("xmlformat.xml", "r") as file:
        des_obj = js.load(file)
    
    print(des_obj)
    print("===========================")
    
def ser_test_func(obj, arg):
    print(obj(arg))
    with open("xmlformat.xml", "w") as file:
        js.dump(obj, file)
    
    #print(ser_obj)
    print()
    
    with open("xmlformat.xml", "r") as file:
        des_obj = js.load(file)
    
    print(des_obj(arg))
    print("===========================")
    
x = 10    
    

ser_test(12)

ser_test(1.5)

ser_test([1, 2, 3, 4, "aboba"])

ser_test({1 : 1, 2 : 2, 3 : 3, "pip" : 4})

ser_test((5, 7, 9, "pup", 25))

ser_test(bytes([104, 101, 108, 108, 111]))

ser_test(bytearray(b'hello world!'))

ser_test_func(my_func, 3)

#сериализация самого декоратора
with open("xmlformat.xml", "w") as file:
        js.dump(my_decorator, file)

for_dec(25)    
#print(ser_obj)
print()
    
with open("xmlformat.xml", "r") as file:
        des_obj = js.load(file)

df = des_obj(for_dec)
    
df(25)
print("===========================")

#сериализация декорированной функции

df = my_decorator(for_dec)

ser_test_func(df, 25)

#сериализация анонимной функции
l = lambda b: b + 25

ser_test_func(l, 10)

with open("xmlformat.xml", "w") as file:
        js.dump(A, file)
#print(cl)

with open("xmlformat.xml", "r") as file:
        des_cl = js.load(file)
a = des_cl()


print(des_cl.ret_bob())
print(a.my_method(5))

print("===============================")

#Сериализация объекта
o = C()
print("Изначальные значения")
print(o.abobus(5))
print("Переменная объекта: ", o.coca)
print("Статический метод класса А: ", o.ret_bob())
print("Статический декорированный метод класса B: ", o.another_method(10))


with open("xmlformat.xml", "w") as file:
    js.dump(o, file)
#o_ser = serialize(o)
#print(o_ser)

#des_o = deserialize(o_ser)
with open("xmlformat.xml", "r") as file:
    des_o = js.load(file)

print("Десериализованные значения")
print(des_o.abobus(5))
print("Переменная объекта: ", des_o.coca)
print("Статический метод класса А: ", des_o.ret_bob())
print("Статический декорированный метод класса B: ", des_o.another_method(10))


