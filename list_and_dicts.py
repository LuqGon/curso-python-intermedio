

def main():
    my_list = [1,"Hello",True,4.5]
    my_dict ={"firstname":"Lucas","lastname":"Gonzalez"}

    super_list = [
        {"firstname":"Lucas","lastname":"Gonzalez"},
        {"firstname":"Miguel","lastname":"Torres"},
        {"firstname":"Pepe","lastname":"Rodelo"},
        {"firstname":"Susana","lastname":"Martinez"},
        {"firstname":"Juan","lastname":"Gonzalez"}
    ]

    super_dict ={
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1,4.5,6.43]
    }

    # for key,value in super_dict.items():
    #     print(key,"-",value)
    for list_value in super_list:
        for key,value in list_value.items():
            print(key+":",value)
            if key == 'lastname':
                print()
if __name__ == '__main__':
    main()