from typing import Final

class User:
  
    def __init__(self,name:str,surname:str,Dui:str) -> None:
        self.name = name
        self.surname = surname
        self.__Dui:Final[str] = Dui

    def __setattr__(self,name,value):
        if name == '_User__Dui':
            raise AttributeError("no puedes modificar el Dui")
        else: 
            super().__setattr__(name,value)



user1 = User("kalet","chavez","123450-6") 
user1._User__Dui= "234321-2"

print(user1.__Dui)