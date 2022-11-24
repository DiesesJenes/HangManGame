import random

def build_game_field():
    global blank_word_list, fails
    blank_word = "".join(blank_word_list)
    if fails == 0:
        print(blank_word)
    elif fails == 1:
        print(blank_word)
        print("/")
    elif fails == 2:
        print(blank_word)
        print("/\ ")
    elif fails == 3:
        print(blank_word)
        print("""
        |
        |
        |
        |
        /\ """)
    elif fails == 4:
        print(blank_word)
        print("""
        ______
        |
        |
        |
        |
        /\ """)
    elif fails == 5:
        print(blank_word)
        print("""
        ______
        |/
        |
        |
        |
        /\ """)
    elif fails == 6:
        print(blank_word)
        print("""
        ______
        |/   |
        |
        |
        |
        /\ """)
    elif fails == 7:
        print(blank_word)
        print("""
        ______
        |/   |
        |    o
        |
        |
        /\ """)
    elif fails == 8:
        print(blank_word)
        print("""
            ______
            |/   |
            |    o
            |    O
            |
            /\ """)
    elif fails == 9:
        print(blank_word)
        print("""
            ______
            |/   |
            |    o /
            |    O
            |
            /\ """)
    elif fails == 10:
        print(blank_word)
        print("""
            ______
            |/   |
            |  \ o /
            |    O
            |
            /\ """)
    elif fails == 11:
        print(blank_word)
        print("""
            ______
            |/   |
            |  \ o /
            |    O
            |   /
            /\ """)
    elif fails == 12:
        print(blank_word)
        print("""
            ______
            |/   |
            |  \ o /
            |    O
            |   / \  
            /\ """)
        print("Du hast das Spiel verloren...")
        print("Das gesuchte Wort war: " + word)

def game_loop():
    global world
    if "".join(blank_word_list).upper() == word.upper():
        build_game_field()
        print("Du hast das Spiel gewonnen!!!")
        return False
    if fails < 12:
        return True
    if fails == 12:
        build_game_field()
        return False

def set_letter():
    global fails, blank_word_list
    counter = 0
    letter = input("Bitte geben sie einen Buchstaben ein: ")    #Es muss noch überprüft werden, ob wirklich ein Buchstabe eingegeben wurde!
    for i in range(len(word)):
        if word[i] == letter or word[i] == letter.upper() or word[i] == letter.lower:
            blank_word_list[i+1] = letter
        else:
            counter += 1
    if counter == len(word):
        fails += 1

def random_word():
    word_list = ["Kraftfahrzeugtechniker", "Ettikettiergeraet", "Kuhpfladen", "Buecherwurm"]
    return random.choice(word_list)


word = random_word()
fails = 0
blank_word_list = [""]
for i in range(0, len(word)):
    blank_word_list.append("_")


print(len(word))
while game_loop() == True:
    blank_word = "".join(blank_word_list)
    build_game_field()
    set_letter()
    print(len(word))






