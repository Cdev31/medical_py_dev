#__new__,__init__,__str__,__repr__

class Persona():
    def __init__(self,name,surname,age,description):
        self.name = name
        self.surname = surname
        self.age = age
        self.description = description

    def __new__(cls,*args,**kwargs):
         print("se creo una instancia")
         return super().__new__(cls)
    
    def __str__(self) -> str:
        return f'Su nombre es: {self.name , self.surname}, edad: {self.age} '

    def __repr__(self) -> str:
        return f'Object pesona 00 {self.name}'    


user1 = Persona("kalet","chavez",23,"ojos verdes")
print(user1)
print(repr(user1))

