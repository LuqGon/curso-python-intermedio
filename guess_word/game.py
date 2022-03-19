class Game:

    def __init__(self,word,encryp_word,length_word):
        self.__word = word
        self.__encryp_word = encryp_word 
        self.__length_word = length_word
        self.__tracking_letter = []


    def get_word(self):
        return " ".join(self.__word)


    def set_word(self,word):
        self.__word = word


    def get_encryp_word(self):
        return " ".join(self.__encryp_word)


    def set_encryp_word(self,encryp_word):
        self.__encryp_word = encryp_word


    def get__tracking_letter(self):
        return "-".join(self.__tracking_letter)


    def find_letter(self,letter):
        encryp_position = [i for i, l in enumerate(self.__encryp_word) if l == letter]
        if encryp_position == []: 
            position = [i for i, l in enumerate(self.__word) if l == letter] 

            if position != []:
                for i in position:
                    self.__encryp_word[i] = self.__word[i]
                result = True
                self.__tracking_letter.append(letter)
            else:
                result = False

        else:
            result = False
        return result

    def init_encryp_word(self):
        i = len(self.__word)-1
        self.find_letter(self.__word[0])
        if i > 3 :
            self.find_letter(self.__word[i])
        if i > 5 :
            self.find_letter(self.__word[i//2])

    def complete_word(self):
        result = False

        if self.__encryp_word == self.__word:
            result = True
        
        return result


    def look_life(self, life):
        result = False

        if life > 0:
            result = True

        return result
