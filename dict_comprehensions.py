def main():
    my_dict={}
    # for num in range(1,101):
    #     if num % 3 != 0 :
    #         my_dict[num]=num**3
    # print(my_dict)
    #Otra forma de hacer esto es haciendo dctionary comprehensions:
    my_dict = {num: num**3 for num in range(1, 101) if num % 3 != 0}
    print(my_dict)
if __name__ == '__main__':
    main()