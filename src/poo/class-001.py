from abc import ABC

class User(ABC):
    name:str = ""
    surname: str = ""
    age:int = 0
    role: str = ""

    def __init__(self,name:str,surname:str,age:int,role:str):
        self.name = name
        self.surname = surname
        self.age = age
        self.role = role
    
    @classmethod
    def __new__(cls,*args,**kwargs):
        if cls == User:
            raise TypeError("La clase no puede ser instanciada ")
        return super().__new__(cls)

    def viewInventory(self):
        return "puedes ver el inventario"  


class UserNormal(User):
    role = "Normal"
    def __init__(self,name,surname,age):
        super().__init__(name,surname,age,self.role)

    def viewOnly(self):
        response = super().viewInventory()
        print(f"{response} pero solamente eso")

class UserAdmin(User):
    role = "Admin"
    def __init__(self,name,surname,age):
        super().__init__(name,surname,age,self.role)

    def updateInventoru(self):
        print("puedes actualizar el inventario")

    def createInventory(self):
        print("puedes crear productos en el inventario")

    def deleteInventory(self):
        print("puedes eliminar un producto del inventario")

 
user1 = UserAdmin("kalet","chavez",23)
print(user1.age)
print(user1.role)
user1.viewInventory()

user2 = UserNormal("Ana","Barrientos",21)
print(user2.name)
print(user2.role)
user2.viewOnly()
