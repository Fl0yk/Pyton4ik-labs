import re


def serialize(obj):
    ser = dict()
    obj_type = type(obj)
    def get_base_type():
        return re.search(r"\'(\w+)\'", str(obj_type))[1]
    
    if isinstance(obj, (list, tuple, set, frozenset, bytearray, bytes)):
        ser["type"] = get_base_type()
        ser["value"] = [serialize(ser_obj) for ser_obj in obj]
        
    elif isinstance(obj, dict):
        ser["type"] = get_base_type()
        ser["value"] = [[serialize(key), serialize(value)] for (key, value) in obj.items()]
    
    elif (isinstance(obj, (str, int, float, bool, complex))):
        ser["type"] = get_base_type()
        ser["value"] = obj
    
    
    
    return ser