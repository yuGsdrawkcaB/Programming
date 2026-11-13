import random

#Program that creates a deck of playing cards

class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        rank_name = ''
        if self.rank == 1:
            rank_name = 'Ace'
        else:
            rank_name = str(self.rank)
        return rank_name + ' of ' + self.suit

class deck:

    def __init__(self):
        self.cards = [card(suit, rank) for rank in range(1, 10) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']] + [card(suit, rank) for rank in ['King', 'Queen', 'Jack'] for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)
    