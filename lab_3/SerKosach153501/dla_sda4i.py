#Почему-то в vsCode как-то странно стала работать видимость файлов
#Эта штука в данном случае добавляет в пути путь к самой папке лабы,
#чтоб нормально видела файлы
import sys
sys.path.append("/home/floyk/Рабочий стол/IGI-Labs/Pyton4ik-labs/lab_3")
from SerKosach153501.json_ser import JsonSerializer
from SerKosach153501.xml_ser import XMLSerializer

ser = XMLSerializer()

class A:
    x = 15
    
    def __init__(self) -> None:
        self.a = 12
        self.b = 10
    
    def my_meth(self):
        return self.a * self.b
    
    
class B:
    def __str__(self):
        return "AAAAAAAAA"
    
    def __repr__(self):
        return "AAAAAAAAA"
    
    
class C(A, B):
    pass


obj = C()
obj_s = ser.dumps(obj)
obj_d = ser.loads(obj_s)


print(obj_d.my_meth()) 
print(obj_d.x)
print(obj_d)








