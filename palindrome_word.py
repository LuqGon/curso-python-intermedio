def is_palindrome(word_ev):
    palindrome = lambda word : word == word[::-1]
    word_input = word_ev.lower().replace(" ","")
    return palindrome(word_input)

def main():
    word_input = input("Ingrese una palabra: ")

    if(is_palindrome(word_input)):
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == '__main__':
    main()