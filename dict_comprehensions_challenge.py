from math import sqrt
def main():
    my_dict = {num : round(sqrt(num),2) for num in range(1,1001)}
    print(my_dict)
if __name__ == '__main__':
    main()