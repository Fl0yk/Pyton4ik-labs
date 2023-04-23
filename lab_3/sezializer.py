import re
import inspect
import types
import builtins
from constans import CODE, BASE_TYPE, BASE_COLLECTION


def serialize(obj):
    ser = dict()
    obj_type = type(obj)
    def get_base_type():
        return re.search(r"\'(\w+)\'", str(obj_type))[1]
    
    if (isinstance(obj, (list, tuple, set, frozenset, bytearray, bytes))):
        ser["type"] = get_base_type()
        ser["value"] = [serialize(ser_obj) for ser_obj in obj]
        
    elif (isinstance(obj, dict)):
        ser["type"] = get_base_type()
        ser["value"] = [[serialize(key), serialize(value)] for (key, value) in obj.items()]
    
    elif (isinstance(obj, (str, int, float, bool, complex))):
        ser["type"] = get_base_type()
        ser["value"] = obj
        
    elif (inspect.isfunction(obj)):
        ser["type"] = "function"
        ser["value"] = ser_func(obj)
        
    elif (inspect.iscode(obj)):
        ser["type"] = "code"
        args = dict()
        for (k, v) in inspect.getmembers(obj):
            #print(k, v, type(v))
            if (k in CODE):
                args[k] = serialize(v)
        ser["value"] = args
        
    elif (not obj):
        ser["type"] = "NoneType"
        ser["value"] = None
        
    
    
    return ser



def ser_func(func):
    if (not inspect.isfunction(func)):
        return
    
    ser_value_func = dict()
    
    ser_value_func["__name__"] = func.__name__
    
    ser_value_func["__globals__"] = get_globals(func)
    
    args = dict()
    
    for (k, v) in inspect.getmembers(func.__code__):
        #print(k, v, type(v))
        if (k in CODE):
            args[k] = serialize(v)
            
    ser_value_func["__code__"] = args
    
    return ser_value_func
        

def get_globals(func):
    glob = dict()
    
    for glob_var in func.__code__.co_names:
        if (glob_var in func.__globals__):
            if (isinstance(func.__globals__[glob_var], types.ModuleType)):
                glob["module " + glob_var] = serialize(func.__globals__[glob_var].__name__)
                
            elif (glob_var != func.__code__.co_name):
                glob[glob_var] = serialize(func.__globals__[glob_var])
            
            else:
                glob[glob_var] = serialize(func.__name__)
                
    return glob


def deserialize(obj : dict):
    if (obj["type"] in BASE_TYPE):
        return generator_type(obj["type"], obj["value"])
    
    elif (obj["type"] in BASE_COLLECTION):
        return gener_collection(obj["type"], obj["value"])
    
    elif (obj["type"] == "function"):
        return deser_func(obj["value"])
    
    elif (obj["type"] == "code"):
        code = obj["value"]
        return types.CodeType(deserialize(code["co_argcount"]),
                              deserialize(code["co_posonlyargcount"]),
                              deserialize(code["co_kwonlyargcount"]),
                              deserialize(code["co_nlocals"]),
                              deserialize(code["co_stacksize"]),
                              deserialize(code["co_flags"]),
                              deserialize(code["co_code"]),
                              deserialize(code["co_consts"]),
                              deserialize(code["co_names"]),
                              deserialize(code["co_varnames"]),
                              deserialize(code["co_filename"]),
                              deserialize(code["co_name"]),
                              #deserialize(code["co_qualname"]),
                              deserialize(code["co_firstlineno"]),
                              deserialize(code["co_lnotab"]),
                              #deserialize(code["co_exeptiontable"]),
                              deserialize(code["co_freevars"]),
                              deserialize(code["co_cellvars"]))
    
    
    
def generator_type(_type, obj):
    if (_type == "int"):
        return int(obj)
    elif (_type == "float"):
        return float(obj)
    elif (_type == "complex"):
        return complex(obj)
    elif (_type == "str"):
        return str(obj)
    elif (_type == "bool"):
        return bool(obj)
    
def gener_collection(_type, obj):
    if (_type == "list"):
        return list(deserialize(o) for o in obj)
    elif (_type == "tuple"):
        return tuple(deserialize(o) for o in obj)
    elif (_type == "set"):
        return set(deserialize(o) for o in obj)
    elif (_type == "frozenset"):
        return frozenset(deserialize(o) for o in obj)
    elif (_type == "bytearray"):
        return bytearray(deserialize(o) for o in obj)
    elif (_type == "bytes"):
        return bytes(deserialize(o) for o in obj)
    
    
def deser_func(obj):
    code = obj["__code__"]
    globs = obj["__globals__"]
    res_globs = dict()
    
    for k in obj["__globals__"]:
        #print(k, type(k), "   ", globs[k], type(globs[k]))
        if ("module" in k):
            #print("IMPORT", globs[k]["value"])
            res_globs[globs[k]["value"]] = __import__(globs[k]["value"])
            
        
        elif (globs[k] != obj["__name__"]):
            #print(k, "aba", globs[k])
            res_globs[k] = deserialize(globs[k])
       
    codeType = types.CodeType(deserialize(code["co_argcount"]),
                              deserialize(code["co_posonlyargcount"]),
                              deserialize(code["co_kwonlyargcount"]),
                              deserialize(code["co_nlocals"]),
                              deserialize(code["co_stacksize"]),
                              deserialize(code["co_flags"]),
                              deserialize(code["co_code"]),
                              deserialize(code["co_consts"]),
                              deserialize(code["co_names"]),
                              deserialize(code["co_varnames"]),
                              deserialize(code["co_filename"]),
                              deserialize(code["co_name"]),
                              #deserialize(code["co_qualname"]),
                              deserialize(code["co_firstlineno"]),
                              deserialize(code["co_lnotab"]),
                              #deserialize(code["co_exeptiontable"]),
                              deserialize(code["co_freevars"]),
                              deserialize(code["co_cellvars"]))
    
    funcRes = types.FunctionType(code=codeType, globals=res_globs)
    funcRes.__globals__.update({funcRes.__name__ : funcRes})
    
    return funcRes