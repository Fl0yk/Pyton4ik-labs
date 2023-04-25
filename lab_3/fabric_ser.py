from json_ser import JsonSerializer
from xml_ser import XMLSerializer

class Fabric:
    
    @staticmethod
    def create_serializer(format_name : str):
        format_name = format_name.lower()
        
        if (format_name == "json"):
            return JsonSerializer()
        elif (format_name == "xml"):
            return XMLSerializer()
        else:
            raise ValueError