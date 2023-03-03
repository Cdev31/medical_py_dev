
def suma(*args) -> int:
    total:int = 0
    for arg in args:
        total = total + arg
    return total    
    
resultado = suma(10,2)
print(resultado)

def dics(**kwargs):
    for key, value in kwargs.items():
       print(f'{key} es {value}')  

dics(nombre="Gaston", edad=23,sexo='M')

