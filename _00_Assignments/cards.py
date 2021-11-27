"""
Requirement:
-------------
-->create pack of cards, distribute to 2 players.count the numbers on the cards.count decides the winner. do it without using
the random module.
"""
# solution:
# -----------
values_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'K': 12, 'Q': 13,
               'A': 14}
total_dict = {}
shapes_dict = {'D': 4, 'H': 3, 'S': 2, 'C': 1}
deck = {}

for i in shapes_dict.keys():
    for j in values_dict.keys():
        deck[j + i] = values_dict[j] + shapes_dict[i]

for i, j in deck.items():
    # print(i, ' : ', j)
    pass

cards = set(deck.keys())

cards_list = list(cards)
# print(cards_list)

player_A_cards = []
player_B_cards = []

first = input('enter which player starts first, enter A or B :')
if first == 'A':
    for i, j in zip([i for i in cards_list[0: 26]], [j for j in cards_list[26:]]):
        player_A_cards.append(i)
        player_B_cards.append(j)

elif first == 'B':
    for i, j in zip([i for i in cards_list[0: 26]], [j for j in cards_list[26:]]):
        player_A_cards.append(j)
        player_B_cards.append(i)

print(f'\n-----------player A cards are-----------\n {player_A_cards}')
print(f'\n-----------player B cards are-----------\n {player_B_cards}')

player_A_count = 0
player_B_count = 0

for i in player_A_cards:
    player_A_count += deck[i]

for j in player_B_cards:
    player_B_count += deck[j]

if player_A_count > player_B_count:
    print('player A count is :', player_A_count)
    print('player B count is : ', player_B_count)
    print('player A wins')

elif player_A_count < player_B_count:
    print('player A count is :', player_A_count)
    print('player B count is : ', player_B_count)
    print('player B wins')

else:
    print('player A count is :', player_A_count)
    print('player B count is : ', player_B_count)
    print('the count is equal')
