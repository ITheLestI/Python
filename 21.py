from random import shuffle, choice
from time import sleep
from lib import check_digit, check_input

play_again = "да"
balance = 100

def get_deck():
    deck = []

    for suit in ("черви", "пики", "бубны", "трефы"):
        for card in range(2,11):
            deck.append(f"{card} {suit}")
        for card in ("дама", "валет", "король", "туз"):
            deck.append(f"{card} {suit}")
    shuffle(deck)
    return deck

def get_card_weight(requested_card, dealer=False):
    card_name = requested_card.split()

    card_weights = {}
    for card in range(2,11):
        card_weights[f"{card}"] = card
    for card in ("дама", "валет", "король"):
        card_weights[f"{card}"] = 10

    if card_name[0] == "туз":
        if dealer:
            weight = choice([1, 11])
        else:
            weight = input("Туз - это 1 или 11?\n")
    else:
        weight = card_weights[card_name[0]]
    return int(weight)

while play_again == "да":
    if not balance:
        break  
    
    koloda = get_deck()
    your_points = 0
    dealer_points = 0
    min_dealer_points = 17
    move = 1
    pick_card_again = 'да'
    print(f"Ваш баланс: {balance}$")
    
    bet = check_digit(input("Введите ставку "))
    while int(bet) > balance:
        
        bet = input(f"Ставка слишком большая, баланс {balance}$\n")
        bet = check_digit(input("Введите ставку "))
    bet = int(bet)
    

    while pick_card_again == "да":
        sleep(1)
        if move == 1:
            dealer_card = koloda.pop()
            dealer_points += get_card_weight(dealer_card, True)

            cards = []
            for i in range(2):
                your_card = koloda.pop()
                your_points += get_card_weight(your_card)
                cards.append(your_card)
        else:
            your_card = koloda.pop()
            your_points += get_card_weight(your_card)

        print(f"""
        =============
        ОЧКИ:
        Крупье: {dealer_points}
        Вы: {your_points}
        =============    
            """)
        if move == 1:
            print(f"Вам выпали карты {cards[0]} и {cards[1]}")
        else:
            print(f"Вам выпала карта {your_card}")

        if your_points > 21:
            print(f"""
        =============
        ОЧКИ:
        Крупье: {dealer_points}
        Вы: {your_points}
        =============    
            """)
            print("Вы проиграли")
            balance-=bet
            print(f"Ваш баланс: {balance}$")
            break

        elif your_points == 21:
            pick_card_again = "нет"
        else:
            pick_card_again = check_input(input("Ещё? (да/нет)\n"), ["да","нет"])
        
        move+=1
        
    else:
        while dealer_points <= 17:
            dealer_card = koloda.pop()
            dealer_points += get_card_weight(dealer_card, True)
            print(f"Крупье вытянул карту  {dealer_card}")
            sleep(2)

        if your_points == dealer_points:
            print(f"""
        =============
        ОЧКИ:
        Крупье: {dealer_points}
        Вы: {your_points}
        =============    
            """)
            print("Ничья")
            print(f"Ваш баланс: {balance}$")
        elif dealer_points > 21:
            print(f"""
        =============
        ОЧКИ:
        Крупье: {dealer_points}
        Вы: {your_points}
        =============    
            """)
            print("Вы выиграли")
            balance+=bet
            print(f"Ваш баланс: {balance}$")
        else:
            if your_points > dealer_points:
                print(f"""
        =============
        ОЧКИ:
        Крупье: {dealer_points}
        Вы: {your_points}
        =============    
            """)
                print("Вы выиграли")
                balance+=bet
                print(f"Ваш баланс: {balance}$")
            else:
                print(f"""
        =============
        ОЧКИ:
        Крупье: {dealer_points}
        Вы: {your_points}
        =============    
            """)
                print("Вы проиграли")
                balance-=bet
                print(f"Ваш баланс: {balance}$")
    play_again = check_input(input("Сыграем еще? Да/нет\n"), ["да","нет"])
    
    