# 카드 섞기
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

# 맨 앞의 카드 1장 빼기
def hit(deck):
    if deck == []:
         deck = fresh_deck()
    return (deck[0], deck[1:])

# 점수 계산
def count_score(cards):
    score = 0
    number_of_ace = 0
    for card in cards:
        num = card["rank"]
        if num == 'A':
            if number_of_ace > 0:
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

# 카드 표시
def show_cards(cards,message):
    print(message)
    for card in cards:
        suit = card["suit"]
        rank = card["rank"]
        print(" ",suit,rank)

# 게임 진행 여부
def more(message):
    answer = input(message)
    while not (answer.isdigit() == False and (answer == 'y' or answer =='n')):#(반복 조건):
        answer = input(message)
    return (answer == 'y' and True) or (answer == 'n' and False)

def Blackjack():
    print("Welcome to SMaSH Casino!")
    deck = fresh_deck()
    chips = 0
    num = 0
    while (num == 0) or more("Play more? (y/n) ") == True:
        print("-----")
        dealer = []
        player = []
        card, deck = hit(deck)  # 1장 뽑아서
        player.append(card)  # 손님에게 주고
        card, deck = hit(deck)  # 1장 뽑아서
        dealer.append(card)  # 딜러에게 주고
        card, deck = hit(deck)  # 1장 뽑아서
        player.append(card)  # 손님에게 주고
        card, deck = hit(deck)  # 1장 뽑아서
        dealer.append(card)  # 딜러에게 준다.
        print("My cards are:")
        print(" ", "****", "**")
        print(" ", dealer[1]["suit"], dealer[1]["rank"])
        show_cards(player,"Your cards are")
        score_player = count_score(player)
        score_dealer = count_score(dealer)
        if score_player == 21:
            print("Blackjack! You won.")
            chips += 2
            print("Chips = ",chips)
            num += 1
        elif score_player < 21:
            while score_player < 21 and more("Hit? (y/n) ") == True:
                card, deck = hit(deck)
                player.append(card)
                print(" ", card["suit"], card["rank"])
                score_player = count_score(player)
            if score_player == 21:
                print("Blackjack! You won.")
                chips += 2
                print("Chips = ", chips)
                num += 1
            elif score_player > 21:
                print("You bust! I won.")
                num += 1
                chips -= 1
                print("Chips = ", chips)
            elif score_player < 21:
                if score_dealer > 16:
                    show_cards(dealer, "My cards are:")
                while score_dealer <= 16:
                    card, deck = hit(deck)
                    dealer.append(card)
                    score_dealer = count_score(dealer)
                    show_cards(dealer,"My cards are:")
                if score_dealer > 21:
                    print("I bust! You won.")
                    num += 1
                    chips += 1
                    print("Chips = ", chips)
                elif score_dealer == score_player :
                    print("We draw.")
                    num += 1
                    print("Chips = ", chips)
                elif score_player > score_dealer :
                    print("You won.")
                    num += 1
                    chips += 1
                    print("Chips = ", chips)
                elif score_player < score_dealer:
                    print("I won.")
                    num += 1
                    chips -= 1
                    print("Chips = ", chips)
    print("Bye!")

Blackjack()
