#!/usr/bin/python3
"""
    A game of blackjack, or at least my take on it:
        1. Aces are soft (i.e 1 or 11).
        2. Dealer stands on 17, hits up to 16.
        3. Blackjacks behave as expected.
        4. We have a shoe with 5 decks that gets shuffled if there
        are less than 10 cards remaining, so you can count cards ;)
        5. You also have a bank of 1000, in future I can make that a starting
        argument. Once you reach 0$ game is over and you can't bet more than what you have, no
        borrowing on this table.
        6. It pays everything double, i.e. a bet of 100 returns 200 if you win, since I can't
        bother with 3:2, 6:5 etc.
        7. Standard blackjack rules apply otherwise, e.g if dealer & player
        bust, player looses.
"""
import random
from os import system
from usefulstuff import flatten_list

system('clear')
print("I made my own! There are no hookers, but at least we have blackjack!")

base_deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
DECKS = 5

def shuffle(d, n):
    """
      This creates a new clean deck where d is the list
      of cards, n is the number of decks. Returns list
      with the cards
    """
    d = []
    for _ in range(n):

        for card in base_deck:

            d.append(card)

    return d


def draw_card(d, n):
    """
      Function to draw a random card from a deck and discard it.
      d is the deck to use. n is number of cards to draw. Card
      is then removed from the list.
    """
    drawn_card = []

    for _ in range(n):
        card = random.choice(d)
        d.remove(card)
        drawn_card.append(card)

    return drawn_card


def calc_score(_hand):
    """
       Take current hand and return score value taking aces into account.
    """
    total = 0
    named_cards = ['J', 'Q', 'K']
    values = []
    hand = flatten_list(_hand)

    for i in hand:
        if any(substr in str(i) for substr in named_cards):
            values.append(10)
        elif i == 'A':
            values.append(11)
        else:
            values.append(i)

    for val in values:
        while total + val > 21 and 11 in values:
            pos = values.index(11)
            values[pos] = 1
        total += val

    return total


def game(bank):
    """
        Main game function
    """
    shoe = (shuffle(d=base_deck, n=DECKS))
    print(f"Player bank is {bank}$")
    bet = int(input("Place your bet:\n"))

    if bank - bet < 0:
        print("Sorry, you need money to play at this table!")
        return bank

    bank -= bet

    if len(shoe) <= 10:
        print("Less than 10 cards, shuffling...")
        shuffle(shoe, DECKS)

    d_hand = draw_card(shoe, 1)
    p_hand = draw_card(shoe, 2)

    print(f"Dealer hand is:\n {d_hand}")
    print(f"Player hand is:\n {p_hand}")
    print(f"Player: {calc_score(p_hand)} Dealer: {calc_score(d_hand)}")

    # Dealer moves

    d_blackjack = False
    d_bust = False

    # Draw second card:

    new_card = draw_card(shoe, 1)
    d_hand.append(new_card)
    d_score = calc_score(d_hand)

    if d_score == 21:
        d_blackjack = True

    while d_score < 16:
        new_card = draw_card(shoe, 1)
        d_hand.append(new_card)
        d_score = calc_score(d_hand)

        if d_score > 21:
            d_bust = True

# End of dealer moves

# Player moves
    p_score = calc_score(p_hand)
    p_blackjack = False
    p_bust = False

    if p_score == 21:

        p_blackjack = True
        print("Player has blackjack!")

    else:
        choice = input("Hit, double or stay? (h/d/s)\n")

        match choice:

            case 'h':
                hit = True

                while hit:

                    print("Hit!")
                    new_card = draw_card(shoe, 1)
                    p_hand.append(new_card)
                    p_score = calc_score(p_hand)
                    print(f"Hand is: \n {p_hand}\n score: {p_score}")

                    if p_score > 21:
                        print("Player busts!")
                        hit = False
                        p_bust = True
                    else:
                        if p_score != 21:
                            hit_again = input("Hit again? (y/n)\n")
                            if not hit_again.lower() == 'y':
                                hit = False

            case 'd':
                bet += bet
                new_card = draw_card(shoe, 1)
                p_hand.append(new_card)
                p_score = calc_score(p_hand)
                print(f"Double! Bet is now {bet}")
                print(f"Player hand:\n{p_hand}\n Score:{p_score}")
                if p_score > 21:
                    p_bust = True

            case 's':
                print("Staying...")

# End of player moves

# Time to reveal our cards

    print(f"Dealer hand is: {d_hand}\n Dealer score is: {d_score}")

# Deal with possible blackjacks

    if d_blackjack and p_blackjack:
        print("Dealer has blackjack!")
        print("Player also has blackjack!")
        bank += bet
        return bank

    if d_blackjack:
        print("Dealer blackjack!")
        print("Dealer wins!")
        return bank

    if p_blackjack:
        bank += bet * 2
        return bank

# Deal with busts:

    if p_bust:
        print("Player busts, sorry!")
        return bank

    if d_bust:
        print("Dealer busts, player wins!")
        bank += bet * 2
        return bank

# If all is normal do regular score comparisons:

    if d_score > p_score:
        print("Dealer wins!")
        return bank

    if d_score < p_score:
        print("Player wins!")
        bank += bet * 2
        print(f"Player bank:\n {bank}")
        return bank

    if d_score == p_score:
        print("Push!")
        bank += bet
        return bank


player_bank = 1000
play = True

while play:

    player_bank = game(player_bank)

    if player_bank <= 0:
        play = False
        break
    _play = input(f"Current bank is {player_bank}$\n Keep playing? (y/n)\n")
    system('clear')
    if not _play.lower() == 'y':
        play = False

print(f"You've ended the game with {player_bank}$!")
