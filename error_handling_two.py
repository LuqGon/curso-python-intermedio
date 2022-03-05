'''
Manejo de errores con assert statements
'''

def divisor(num):
    divisors =[i for i in range(1, num + 1) if num % i == 0]
    return divisors
  


def main():
    num = input('Ingrese un número: ')    
    assert num.isnumeric(),"El valor ingresado no es valido. Debe ingresar un numero"
    print(divisor(int(num)))
    print("Termino mi programa")
    
        
if __name__ =='__main__':
    main()