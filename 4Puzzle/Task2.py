def is_winner(card):
    offset = 0
    for i in range(5):
        if card[offset] + card[offset+1] + card[offset+2] + card[offset+3] + card[offset+4] == 500:
            return True
        offset += 5
    offset = 0
    for i in range(5):
        if card[offset] + card[offset+5] + card[offset+10] + card[offset+15] + card[offset+20] == 500:
            return True
        offset += 1
    return False

with open("4Puzzle/data.txt", "r") as file:
    calls = [int(number) for number in file.readline().strip('\n').split(',')]
    cards = []
    while file.readline():
        card = []
        for i in range(5):
            card.extend([int(number) for number in file.readline().strip(
                '\n').split(' ') if number != ''])
        cards.append(card)
        
    have_winner = False
    while not have_winner:
        number = calls[0]
        calls = calls[1:]
        for card in cards:
            for i in range(len(card)):
                if card[i] == number:
                    card[i] = 100
        index = 0
        while index < len(cards):
            if is_winner(cards[index]):
                if len(cards) > 1:
                    cards.pop(index)
                else:
                    have_winner = True
                    print(f"the last card to win is: {cards[0]}")
                    break
            else:
                index += 1
    total = sum([number for number in cards[index] if number != 100])
    print(f"the total is {total*number}")
