from game import Game
from player import Player
from menu_ import Menu
from os import system
import random_word
import test_game
system("clear")

def title():
    system("clear")
    '''Titulo del juego'''
    title = ""
    path = "guess_word/data/title.txt"
    with open(path,"r") as t:
        for line in t:
            title += line
    print(title)
    title = ""

def run():
    
    
    name = 'Lucas'#input("Ingrese su nombre >")
    gamer = Player()
    menu = Menu()
   
    
    init_option = menu.init_menu()
    while init_option == 1:
        gamer.set_life(3)
        init_word,init_encryp_word,init_len_word = random_word.get()
        guess_word = Game(init_word,init_encryp_word,init_len_word)
        guess_word.init_encryp_word()
        unencryp_word = guess_word.get_word()
        status_encryp_word = guess_word.get_encryp_word()
        status_life = gamer.get_life() 
        tracking_letters = guess_word.get__tracking_letter()
        flag = True
        while flag:  
             
            #title()
            print("Lifes:",("♥️"*status_life))
            print("Letters:",tracking_letters)
            print(status_encryp_word)
            letter = input("Ingrese una letra >")#validar
            match_letter = guess_word.find_letter(letter.upper())
            if (not(match_letter)):
                gamer.life_lose()
                continue_game = guess_word.look_life(gamer.get_life())
                if (not(continue_game)):
                    flag = False
            if(guess_word.complete_word()):
                flag = False
            status_encryp_word = guess_word.get_encryp_word()
            status_life = gamer.get_life() 
            tracking_letters = guess_word.get__tracking_letter()

        print("GANO?: ",guess_word.complete_word())
        if (guess_word.complete_word()):
            print(status_encryp_word)
            print ("Ganaste!")
            print()
            input("Press Enter to continue ")
        else:
            flag = False
            #title()
            print(status_encryp_word)
            print()
            print ("Perdiste")
            print()
            print("La palabra era:",unencryp_word)
            print()
            init_option = menu.init_menu()
                
    print("Chau")

if __name__ == "__main__":
    run()
    