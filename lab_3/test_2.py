from sezializer import *

def ser_test(obj):
    ser_obj = serialize(obj)
    
    print(ser_obj)
    print()
    
    des_obj = deserialize(ser_obj)
    
    print(des_obj)
    print("===========================")

ser_test(12)

ser_test(1.5)

ser_test([1, 2, 3, 4, "aboba"])

ser_test((5, 7, 9, "pup", 25))

ser_test(bytes([104, 101, 108, 108, 111]))

ser_test(bytearray(b'hello world!'))