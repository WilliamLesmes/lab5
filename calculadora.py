#Suma
def sumar(a, b): 
    return a + b

#Resta

def restar(a, b):
    return a - b

#Multipicacion

def multiplicar(a, b):
    return a * b

#division

def dividir(a, b):
    if b == 0:
        raise ValueError("Error, no se puede dividir por cero")
    return a / b

if __name__ == "__main__":
    print(sumar(5, 3))
    print(restar(9, 4))
    print(multiplicar(2, 8))
    print(dividir(6, 2))
    print(dividir(7, 0))