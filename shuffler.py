import random
while True:
    deck=list(range(0,int(input("no of cards"))))
    random.shuffle(deck)
    players=int(input("no of players"))
    for i in range(len(deck)):
        input(i,deck[i]%players+1)
