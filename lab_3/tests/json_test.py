import unittest
import sys
sys.path.append("/home/floyk/Рабочий стол/IGI-Labs/Pyton4ik-labs/lab_3")
from data_test import my_func, my_decorator, for_dec, A, B, C
from SerKosach153501.json_ser import JsonSerializer

class JsonTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.js = JsonSerializer()
        
    def test_int(self):
        ser_obj = self.js.dumps(12)
        des_obj = self.js.loads(ser_obj)
        
        self.assertEqual(des_obj, 12)
        
    def test_list(self):
        ser_obj = self.js.dumps([1, 2, [3, 5, "blue"], "pup"])
        des_obj = self.js.loads(ser_obj)
        
        self.assertEqual(des_obj, [1, 2, [3, 5, "blue"], "pup"])
        
    def test_func(self):
        ser_obj = self.js.dumps(my_func)
        des_obj = self.js.loads(ser_obj)
        
        self.assertEqual(des_obj(5), my_func(5))

    def test_decorator(self):
        answ = my_decorator(for_dec)
        ser_obj = self.js.dumps(my_decorator)
        des_obj = self.js.loads(ser_obj)
        dec = des_obj(for_dec)
        
        self.assertEqual(answ(3), dec(3))
        
    def test_lambda(self):
        l = lambda b: b + 25
        ser_obj = self.js.dumps(l)
        des_ob = self.js.loads(ser_obj)
        
        self.assertEqual(l(2), des_ob(2))
        
    def test_static_method(self):
        ser_obj = self.js.dumps(A)
        des_obj = self.js.loads(ser_obj)
        
        self.assertEqual(des_obj.ret_bob(), A.ret_bob())
        
    def test_decorated_static_method(self):
        obj = B()
        ser_obj = self.js.dumps(obj)
        des_obj = self.js.loads(ser_obj)
        
        self.assertEqual(obj.another_method(5),des_obj.another_method(5))
        
    def test_method(self):
        obj = C()
        ser_obj = self.js.dumps(obj)
        des_obj = self.js.loads(ser_obj)
        
        self.assertEqual(obj.abobus(12), des_obj.abobus(12))
        
    def test_init(self):
        obj = C()
        ser_obj = self.js.dumps(obj)
        des_obj = self.js.loads(ser_obj)
        
        self.assertEqual(obj.coca, des_obj.coca)
        
if __name__ == "__main__":
    unittest.main()