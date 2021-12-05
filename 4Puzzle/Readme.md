# Day4
**Now this one was quite a pain in the a ** to solve, nothing fancy or 
elaborated, but because at first, I took a harder way around which ended up in a bunch of spaghetti code, we are going to talk about that attempt later on, but first let's discuss this much simpler solution I came up with**

there are a few considerations we need to take in mind before we start

* *we are dealing with some sort of bingo game, as our input data, we have our calls or the numbers that were played and our bingo boards, these ones we are going to call them cards*

* *another lifesaver is that we only care about rows and columns, NOT diagonals in our cards*
* *last but most important, we NEED a way to know when a specific number has been called or not  for that we are going to take advantage of the fact that all numbers range from 0 to 99 so we can use 100 as a way to mark called number positions*

start by reading the calls from the .txt file

```python
with open("4Puzzle/data.txt", "r") as file:
    calls = [int(number) for number in file.readline().strip('\n').split(',')]
```
now we get our cards
once we get rid of the calls we focus on the cards we are going to build an array that contains arrays with all the numbers included in the card
we know that our cards are 5x5 
so every 5 numbers we have a line and for every 5 lines we know we have an entire card
excluding of course empty lines  

```python
with open("4Puzzle/data.txt", "r") as file:
    cards = []
    while file.readline():
        card = []
        for i in range(5):
            card.extend([int(number) for number in file.readline().strip(
                '\n').split(' ') if number != ''])
        cards.append(card)
```

now we need a way to know if a certain card have won, here is where the 100 thing comes in handy

*offset* will help us move row wise or column wise, we know that every 5 numbers we have a line, so we have to compare 4 postion ahead of offset to consider an entire line, we are comparing it´s sum to 500 because of the 100 trick explained before
same goes for the row, but now we move using multiples of 5 to make it row wise
```python
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
    
```
Finally, we iterate through the cards, taking the first call  and adjusting the calls list
and converting to 100every instance of that number on every card 
after a move, we need to check if we have a winner so we again iterate through the cards
The last part is just adding all the number that are NOT 100 so we can multiply them later 
```python
have_winner = False
    while not have_winner:
        number = calls[0]
        calls = calls[1:]
        for card in cards:
            for i in range(len(card)): #25
                if card[i] == number:
                    card[i] = 100
        for card in cards:
            if is_winner(card):
                total = sum(number for number in card if number != 100)
                print(f"the card that won is: {card}")
                print(f"the total is :{total*number}")
                have_winner = True
```

## Second part!

**now the twist is we need the LAST card that won**

everything remains the same, we are just going to pop out the winning cards until only one remains
```python
have_winner = False
    while not have_winner:
        number = calls[0]
        calls = calls[1:]
        for card in cards:
            for i in range(len(card)): #25
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
```
now let's take a look at my first attempt
first i thought of removing the calls list from the input file and treating it like a hardcoded list

```python
calls=[92,12,94,64,14,4,99,71...]
```

then I started the process of getting what I thought was the ideal data structure, a list that contained matrixes each one of these matrixes was a card

```python
data = [board.strip() for board in data]
    dirty_boards=[]
    for lines in data:
        dirty_boards.append(lines.split(" "))
        
    new_board=[]
    Boards=[]
    for line in dirty_boards:
        if line == ['']:
            Boards.append(new_board)
            new_board=[]
        else:
            new_board.append(line)      
    
    for board in Boards:
        for lines in board:
            try:
                lines.remove('')
            except(ValueError):
                pass
 ```
 to finally came up with this 
 ```python
 ED=[[[bingo_number(number) for number in lines] for lines in board] for board in Boards]
 ```
 *bingo_number* was my first approach to solve the "called number" thing 
  ```python
 class bingo_number():
    def __init__(self,number):
        self.number = number
        self.is_called = False
    def call(self):
        self.is_called = True
```
my helper functions 
 ```python
def is_bingo(board):
    for i in range(5):
        won=True
        for j in range(5):
            if board[i][j].is_called==False:
                won=False
        if won==True:
            return True
    for j in range(5):
        won=True
        for i in range(5):
            if board[i][j].is_called==False:
                won=False
        if won==True:
            return True
    return False
            
def sum_unmarked_numbers(board):
    counter=0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j].is_called==False:
                counter+=board[i][j].number
    return counter
 ```
and finally the algorithm
  ```python
for call in calls:
        for boards in ED:
            for lines in boards:
                for numbers in lines:
                    if numbers.number == call:
                        print(f"called{call}")
                        numbers.call()
        for b in ED:
            if(is_bingo(b)):
                print(b)
                total=sum_unmarked_numbers(b)
                print(f"Score: {total*call}")
                break
```
clearly I was overcomplicating things a little bit, that's why it is always nice to take a coffee break when you are stuck, and attack the problem alter with a new mind set
