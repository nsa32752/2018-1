def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
    deck = []
    for x in suits:
        for y in ranks:
            deck += [{"suit":x, "rank":y}]
    import random
    random.shuffle(deck)
    return deck



def hit(deck):
    if deck == []:
         deck = fresh_deck()
    return (deck[0], deck[1:]) # (맨 앞의 카드 한장 , 남은 deck)

hit(fresh_deck())

def count_score(cards):
    score = 0
    number_of_ace = 0
    for card in cards:
        num = card["rank"]
        if num == 'A':
            if number_of_ace > 0 :
                if score + 11 > 21:
                    score = score - 10
                    number_of_ace += 1
                    if score + 11 > 21:
                        score += 1
                    elif score + 11 <= 21:
                        score += 11
                elif score + 11 <= 21:
                    number_of_ace += 1
                    score = score + 11
            elif number_of_ace == 0:
                if score + 11 <= 21:
                    number_of_ace += 1
                    score += 11
                else:
                    score += 1
        elif (num == 'J') or (num == 'K') or (num == 'Q'):
             if number_of_ace == 0:
                 score += 10
             else:
                 if number_of_ace > 1:
                     score = score
                 elif number_of_ace == 1:
                     if score + 10 <= 21:
                         score = score + 10
                 number_of_ace = 0
        elif 2 <= int(num) <= 10:
            if score + int(num) > 21 and number_of_ace > 0:
                score = score - 10 + int(num)
                number_of_ace -= 1
            else:
                score = score + int(num)
    return score

#print(count_score(fresh_deck()))
print(count_score([{"suit": "Heart", "rank": '3'},{"suit": "Heart", "rank": 'A'},{"suit": "Heart", "rank": 'K'}]))
#print(count_score([{"suit": "Heart", "rank": 'Q'},{"suit": "Heart", "rank": 'K'},{"suit": "Heart", "rank": 'A'},{"suit": "Heart", "rank": "A"}]))
#print(count_score([{"suit": "Heart", "rank": 'A'},{"suit": "Heart", "rank": 'A'},{"suit": "Heart", "rank": 'A'},{"suit": "Heart", "rank": "A"}]))

def show_cards(cards,message):
    print(message)
    for card in cards:
        suit = card["suit"]
        rank = card["rank"]
        print(" ",suit,rank)

#show_cards([{"suit": "Heart", "rank": 4},{"suit": "Heart", "rank": 'A'},{"suit": "Heart", "rank": 'A'},{"suit": "Heart", "rank": 4}],"My cards are:" )



def more(message):
    answer = input(message)
    while not (answer.isdigit() == False and (answer == 'y' or answer =='n')):#(반복 조건):
        answer = input(message)
    return (answer == 'y' and True) or (answer == 'n' and False)

#message = 'Play more? (y/n) '
#more(message)


