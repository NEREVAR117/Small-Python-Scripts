# Written October 12th to test land spacing



import random




# Top of deck < ---------- > Bottom of deck

first_25_cards = ['8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8']

second_25_cards = ['8', '8', '8', '8', '8', '8', '8', '8', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

third_25_cards = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

fourth_25_cards = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


# Merges the sub-structure lists into a main deck list
combined_deck = first_25_cards + second_25_cards + third_25_cards + fourth_25_cards

# Asks the user if the deck should be shuffled
shuffle_answer = input("Shuffle the list? ")

if shuffle_answer == "yes":
    print("derp")
    random.shuffle(combined_deck)

print(combined_deck)

# Establishes the piles we'll sort into
pile_1 = []
pile_2 = []
pile_3 = []

pile_4 = []
pile_5 = []
pile_6 = []

# Sets the shuffle loops
loop_again = True

while loop_again == True:
    while len(combined_deck) > 0:

        try:
            pile_1.append(combined_deck[0])
            combined_deck.pop(0)
        except:
            print("")

        try:
            pile_2.append(combined_deck[0])
            combined_deck.pop(0)
        except:
            print("")

        try:
            pile_3.append(combined_deck[0])
            combined_deck.pop(0)
        except:
            print("")

        try:
            pile_4.append(combined_deck[0])
            combined_deck.pop(0)
        except:
            print("")

        try:
            pile_5.append(combined_deck[0])
            combined_deck.pop(0)
        except:
            print("")

        try:
            pile_6.append(combined_deck[0])
            combined_deck.pop(0)
        except:
            print("")


    # Prints out the piles of the deck
    print(pile_1)
    print(pile_2)
    print(pile_3)

    print(pile_4)
    print(pile_5)
    print(pile_6)

    # Rebuilds the compiled desk list
    combined_deck = pile_1 + pile_2 + pile_3 + pile_4 + pile_5 + pile_6

    # Empties the piles to be reused
    pile_1.clear()
    pile_2.clear()
    pile_3.clear()

    pile_4.clear()
    pile_5.clear()
    pile_6.clear()


    # Asks the user if they want to shuffle again
    answer = input("Shuffle again? ")

    if answer == "no":
        loop_again = False


print("Ended script")