"""
Creational:
    factory-method:
        3component: 1.creator 2.product 3.client

"""

# class A:
#     def __init__(self , name , format):
#         self.name = name
#         self.format = format
#
#
# class B:
#     def edit(self , file):
#         edit = self._get_edit(file)
#         edit(file)
#
#
#     def _get_edit(self , file):
#         if file.format == 'json':
#             return self.edit_json
#         elif file.format == 'xml':
#             return self.edit_xml
#         else:
#             raise ValueError('sorry...')
#
#     def edit_json(self , file):
#         print(f"editing json file{file.name}")
#     def edit_xml(self , file):
#         print(f"editing xml file {file.name}")
#
# a1 = A('first' , 'json')
#
# b1 = B()
# b1.edit(a1)

#################################################################

from abc import ABC , abstractmethod

class Creator(ABC):
    @abstractmethod
    def make(self):
        pass
    def call_edit(self):
        product = self.make()
        result = product.edit()
        return result

class JsonCreator(Creator):
    def make(self):
        return Json()

class XmlCreator(Creator):
    def make(self):
        return Xml()


#_______________________________________________________

class Product(ABC):
    @abstractmethod
    def edit(self):
        pass


class Json(Product):
    def edit(self):
        return 'editing Json file ...'

class Xml(Product):
    def edit(self):
        return 'Editing Xml file ...'

#_________________________________________________________________________

def client(format):
    return format.call_edit()

print(client(JsonCreator()))