#primer ejercicio.

def rmSensitiveData(func):
    def wrapper(self,id):
        user = func(self,id)
        if user:
            dataUser = user.copy()
            del dataUser['email']
            del dataUser['password']
            return dataUser
        else:
            return False
    return wrapper    

# def rmSensitiveData():
#     def superUser(cls):
#         class superUser(cls):
#             def findUser(self,id):
#                 print("lo sobreescribi pelotudo")
#         return superUser
#     return superUser        

# @rmSensitiveData()
class User:
    users = [{
        "id":1,
        "name": 'kalet',
        "age": 23,
        "email": "kal@gmail.com",
        "password":"secreto1"
    },
    {
        "id": 2,
        "name": 'Ana',
        "age": 26,
        "email": "ana@gmail.com",
        "password": "secreto2"
    }
    ]
    @rmSensitiveData
    def findUser(self,id):
        for user in self.users:
            if user['id'] == id:
                return user
        return False    
    
user1 = User()

#decorador que da mayor seguridad con las propiedades privadas
def protectedProperties():
    def superAutos(cls):
        class superAuto(cls):
            attrProperty =[]

            def __setattr__(self, name,value):
                print(name)
                self.attrProperty.append(value)
                if name.startswith('__') or name.startswith(f'_{cls.__name__}'):
                    raise AttributeError("No puedes sobreesribir la propiedad privada")
                else:
                    return super().__setattr__(name, value)

           
        return superAuto
    return superAutos


@protectedProperties()
class Auto:
    __llantas=4
    __ancho=23
    __largo=25
    def __init__(self,modelo,color):
        self.__llantas  
        self.__ancho  
        self.__largo 
        self.modelo =modelo
        self.color = color

    def __str__(self):
        return f"""
        el auto{self.modelo} de color: {self.color}
        tiene un ancho:  y largo:  y
        llantas {self.__llantas}
        """
    def get_llantas(self):
        return self.__llantas
    
    def getAncho(self):
        return self.__ancho
    
auto1 = Auto("nissan","blue")

print(auto1.get_llantas())
print(auto1.getAncho())
