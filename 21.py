from random import shuffle
koloda = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]*4
shuffle(koloda)

your_points = 0
dealer_points = 0
min_dealer_points = 17
move = 1

more = 'да'

while your_points < 21 and dealer_points < 17:
    dealer_card = koloda.pop()
    dealer_points += dealer_card
    print(1111)
    if move == 1:
        cards = []
        for i in range(2):
            your_card = koloda.pop()
            your_points += your_card
            cards.append(your_card)
    else:
        your_card = koloda.pop()
        your_points += your_card

    print(f"""
    =============
    ОЧКИ:
    Крупье: {dealer_points}
    Вы: {your_points}
    =============    
        """)
    print(f"    Вам выпали карты номиналом {cards[0]} и {cards[1]}")
    print("Ещё? (да/нет)\n")
    
    choice = input()
    while choice not in ["да", "нет"]:
        print("Введи да или нет")
        choce  = input()
    if choice == ""


    move+=1
    
    