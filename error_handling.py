'''
Manejo de errores con try, except y raise
'''
def divisor(num):
    try:
        if num < 0:
            raise ValueError("ingresa un número positvo")
        divisors =[i for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return False


def main():
    try: 
        num = int(input('Ingrese un número: '))      
        print(divisor(num))
        print("Termino mi programa")
    except ValueError:
        print("El valor ingresado no es valido. Debe ingresar un numero")
    
if __name__ =='__main__':
    main()