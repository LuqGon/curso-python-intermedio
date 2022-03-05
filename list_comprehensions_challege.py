def main():
    list_nums =[nums for nums in range(1,10000) if nums % 4 == 0 and nums % 6 == 0 and nums % 9 ==0]

    print(list_nums)

if __name__ == '__main__':
    main()