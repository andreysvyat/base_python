from dataclasses import dataclass
import sys


class MyEmptyClass:
    pass


class MyClassWithMethod:
    def call_me(self):
        print(self.__class__.__name__)


mcwm = MyClassWithMethod()
mcwm.call_me()


class MyCreatableClass:
    def __init__(self):
        self.description = 'I set description on ' \
                           'initialization'


class MyClassWithObjFields:
    def __init__(self, val):
        self.obj_val = val


obj_1 = MyCreatableClass()
obj_2 = MyClassWithObjFields('this is val')
print(obj_1)
print(obj_2)
print('--------------------\n')


class MyClassWithClassField:
    common_val = 'This value same for all objects of this class'

    def __init__(self, obj_f):
        self.obj_f = obj_f


obj_4 = MyClassWithClassField('obj_4 object val')
obj_5 = MyClassWithClassField('obj_5 object val')

print(f'object 4 field = {obj_4.obj_f}')
print(f'object 5 field = {obj_5.obj_f}')
obj_5.obj_f = 'new value'
print(f'object 4 field = {obj_4.obj_f}')
print(f'object 5 field = {obj_5.obj_f}')

print(f'object 4 class = {obj_4.common_val}')
print(f'object 5 class = {obj_5.common_val}')
MyClassWithClassField.common_val = 'Set new value for all objects'
print(f'object 4 class = {obj_4.common_val}')
print(f'object 5 class = {obj_5.common_val}')
obj_5.common_val = 'Set new value'
print(f'object 4 class = {obj_4.common_val}')
print(f'object 5 class = {obj_5.common_val}')

obj_4.new_field = 10
print(f'object 4 external added field = {obj_4.new_field}')
# print(f'object 4 external added field = {obj_5.new_field}')
print('--------------------\n')


class MyBaseClass:
    def __init__(self, base_val):
        self.base_field = base_val

    def show_me(self):
        print(f'base_field = {self.base_field}')


class MyChildClass(MyBaseClass):
    def __init__(self):
        super().__init__('I set base_field on init')

    def show_me(self):
        print('I`m fully self-sufficient child.',
              'I can do here all I want',
              f'And {self.base_field}', sep='\n')

    def append_to_filed(self, appendix):
        self.base_field += ' ' + appendix


bc_obj = MyBaseClass('Some value')
cc_obj = MyChildClass()
bc_obj.show_me()
cc_obj.show_me()
cc_obj.append_to_filed('appendix')
print(cc_obj.base_field)


@dataclass
class MyDataClass:
    i_field: int
    s_field: str
    l_field: list


class MyProperties:
    def __init__(self, ip):
        self.__ip = ip
        self.__domain = 'ru'
        self.__port = 80

    def set_port(self, port):
        if port <= 65535:
            self.__port = port
        else:
            print('port should be not greater then 65535')

    def get_port(self):
        return self.__port

    @property
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, dom):
        if not isinstance(dom, str) and len(dom) <= 5:
            self.__domain = dom
        else:
            'Domain should be shorter'

    @property
    def ip(self):
        return self.__ip


server = MyProperties('localhost')
