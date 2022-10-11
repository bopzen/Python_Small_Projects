import random
from collections import deque
import pyfiglet


def build_deck(deck_cards):
    for i in range(2, 15):
        for suit in suits:
            if i == 11:
                deck.append(f'J {suit}')
            elif i == 12:
                deck.append(f'Q {suit}')
            elif i == 13:
                deck.append(f'K {suit}')
            elif i == 14:
                deck.append(f'A {suit}')
            else:
                deck.append(f'{i} {suit}')
    return deck_cards


def shuffle_deck(deck_cards):
    random.shuffle(deck_cards)
    return deck_cards


def deal_cards(deck_cards):
    while deck_cards:
        player1_cards.append(deck_cards.pop())
        player2_cards.append(deck_cards.pop())


def play_turn():
    global turns
    player1_war_cards = deque([])
    player2_war_cards = deque([])
    turns += 1
    while True:
        player1_war_cards.append(player1_cards.pop())
        player2_war_cards.append(player2_cards.pop())
        player1_card = player1_war_cards[-1]
        print(f"Player 1 hand: |{'|'.join(player1_war_cards)}|")
        player2_card = player2_war_cards[-1]
        print(f"Player 2 hand: |{'|'.join(player2_war_cards)}|")
        player1_card_number = player1_card.split()[0]
        player2_card_number = player2_card.split()[0]
        if player1_card_number == 'J':
            player1_card_number = 11
        elif player1_card_number == 'Q':
            player1_card_number = 12
        elif player1_card_number == 'K':
            player1_card_number = 13
        elif player1_card_number == 'A':
            player1_card_number = 14
        else:
            player1_card_number = int(player1_card_number)

        if player2_card_number == 'J':
            player2_card_number = 11
        elif player2_card_number == 'Q':
            player2_card_number = 12
        elif player2_card_number == 'K':
            player2_card_number = 13
        elif player2_card_number == 'A':
            player2_card_number = 14
        else:
            player2_card_number = int(player2_card_number)

        if player1_card_number > player2_card_number:
            print('Player 1 takes the hand.')
            while player1_war_cards:
                player1_cards.insert(0, player1_war_cards.popleft())
            while player2_war_cards:
                player1_cards.insert(0, player2_war_cards.popleft())
            print(f'Player 1 cards {len(player1_cards)} - Player 2 cards {len(player2_cards)} Turns {turns}')
            break
        elif player1_card_number < player2_card_number:
            print('Player 2 takes the hand.')
            while player1_war_cards:
                player2_cards.insert(0, player1_war_cards.popleft())
            while player2_war_cards:
                player2_cards.insert(0, player2_war_cards.popleft())
            print(f'Player 1 cards {len(player1_cards)} - Player 2 cards {len(player2_cards)} Turns {turns}')
            break
        else:
            print('WAR!')
            if len(player1_cards) == 0 or len(player2_cards) == 0:
                break
            elif len(player1_cards) > 2 and len(player2_cards) > 2:
                player1_war_cards.append(player1_cards.pop())
                player2_war_cards.append(player2_cards.pop())
                player1_war_cards.append(player1_cards.pop())
                player2_war_cards.append(player2_cards.pop())


def print_deck(deck_cards):
    print(f'Cards {len(deck_cards)}')
    print("|".join(deck_cards))


def play_another_game():
    print('The game takes too long, the players got bored!')
    another_game = input('Do you want to shuffle the deck and play another game Y/N: ')
    if another_game.upper() == 'Y':
        return True
    elif another_game.upper() == 'N':
        return False
    else:
        print('Enter Y or N!')
        return play_another_game()


title = pyfiglet.figlet_format('* War Game *')
print(title)
print('****************************************************************')
print()

deck = []
suits = ['\u2660', '\u2665', '\u2666', '\u2663']
player1_cards = []
player2_cards = []
turns = 0
build_deck(deck)
shuffle_deck(deck)
deal_cards(deck)
print('Player 1: ', end="")
print_deck(player1_cards)
print('Player 2: ', end="")
print_deck(player2_cards)
print()

while player1_cards and player2_cards:
    play_turn()
    print()
    if turns == 1000:
        if play_another_game():
            deck = []
            player1_cards = []
            player2_cards = []
            turns = 0
            build_deck(deck)
            shuffle_deck(deck)
            deal_cards(deck)
            print('Player 1: ', end="")
            print_deck(player1_cards)
            print('Player 2: ', end="")
            print_deck(player2_cards)
            print()
        else:
            break

if len(player1_cards) > len(player2_cards):
    print('Player 1 Wins!')
else:
    print('Player 2 Wins!')
