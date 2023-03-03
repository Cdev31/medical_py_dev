

def Hola(function):
    def wrapper(*args,**kwargs):
        function(*args,**kwargs)
        print("como estas")
    return wrapper    

@Hola
def saludar():
    print("hola")

# saludar()    

def rolePermiss(roles):
    def decorator(function):
        def wrapper(*args,**kwargs):
            perfil = {
                "role": "admin"
            }
            if perfil['role'] in roles:
                return function(*args,**kwargs)
            else:
                print("no esta permitido")
        return wrapper
    return decorator        


@rolePermiss(roles=["admin","cliente"])
def isAdmin(nombre):
    print(f"hola {nombre}")

isAdmin("Gaston")

