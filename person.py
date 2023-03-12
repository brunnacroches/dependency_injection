# Injection Dependency

from typing import Type

class House:
    
    def __init__(self) -> None:
        self.__address = "Street of Lemon Trees"
    
    def turn_the_lights(self) -> None:
        print('I am turning on the lights')
    
    def get_address(self) -> str:
        return self.__address

class Person:
    def __init__(self, name: str, local: Type[House]) -> None:
        self.__local = local
        self.__name = name
    
    def into_local(self) -> None:
        self.__local.turn_the_lights()
    
    def show_local(self) -> None:
        address = self.__local.get_address()
        print(address)


friends_house = House()
maria = Person('Maria',friends_house)


maria.into_local()
maria.show_local()


# class House:
    
#     def __init__(self) -> None:
#         self.__address = "Street of lemon trees"
    
#     def turn_the_lights(self) -> None:
#         print('I am turning on the lights')
    
#     def get_address(self) -> str:
#         return self.__address

# class Person:
#     def __init__(self, name: str) -> None:
#         self.__name = name
    
#     def into_local(self, local: any) -> None:
#         local.turn_the_lights()
    
#     def show_local(self, local: any) -> None:
#         address = local.get_address()
#         print(address)


# friends_house = House()
# maria = Person('Maria')


# maria.into_local(friends_house)
# maria.show_local(friends_house)