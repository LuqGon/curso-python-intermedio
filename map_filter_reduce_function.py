from functools import reduce

def master_functions(func):
    func()
def map_function():
    # my_list = [1,2,3,4,5,7]

    # squares = [num**2 for num in my_list]

    #print(squares)

    #Misma logica con map
    my_list = [1,2,3,4,5,7]

    squares = list(map(lambda num: num**2,my_list))

    print(squares)

def filter_function():
    # my_list = [1,4,5,6,9,13,19,21]

    # odd = [num for num in my_list if num % 2 != 0]

    # print(odd)

    # Misma logica con filter
    my_list = [1,4,5,6,9,13,19,21]

    odd = list(filter(lambda num: num % 2 != 0,my_list))

    print(odd)
def reduce_function():
    # my_list = [2,2,2,2,2]

    # all_multiplied = 1

    # for num in my_list:
    #     all_multiplied *= num
    
    # print(all_multiplied)

    # Misma logica con reduce, hay que hacer import del modulo fanctools
    my_list = [2,2,2,2,2]

    all_multiplied = reduce(lambda a,b: a*b,my_list)

    print(all_multiplied)

def main():
    master_functions(reduce_function)

if __name__ == '__main__':
    main()