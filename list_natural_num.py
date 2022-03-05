def main():
    # list_squares = []
    # for num_append in range(1,101):
    #     if num_append % 3 != 0:
    #         list_squares.append(num_append**2)
    #Otra forma de hacer esto es haciendo list comprehensions:
    list_squares = [num**2 for num in range(1,101) if num % 3 != 0]
    print(list_squares)


if __name__ == '__main__':
    main()