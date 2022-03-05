# Modos de apertura

# r -> Solo lectura
# r+ -> Lectura y escritura
# w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# a -> Añadido (agregar contenido). Crea el archivo si éste no existe
# a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

# palabra clave
# with -> manejador contextual, controla el flujo del archivo. Impide que el archivo se rompa si el programa se cierra
def read():
    numbers =[]
    with open("./files/numbers.txt",'r',encoding="UTF-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)
def write():
    names = ["Lucas","Coco","Stella","Denise","Alejandra"]
    with open("./files/names.txt","w",encoding="UTF-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
def append():
    names = ["Pepe","Pepita la pistolera"]
    with open("./files/names.txt","a",encoding="UTF-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def main():
    append()

if __name__ == '__main__':
    main()