import deck_of_cards
# Most notes are for eventual integration on to ti-84 calculator
import time

deck = deck_of_cards.deck()
deck.shuffle()

class hand:
    def __init__(self):
        self.cards = []
        self.total = 0

    def show_hand(self):
        for card in self.cards:
            print(card)
            time.sleep(0.75)
    
    def deal_initial_hand(self):
        self.cards.append(deck.deal_card())
        self.cards.append(deck.deal_card())

    def calc_total(self):
        self.total = 0
        for c in self.cards:
            if c.rank != 1:
                if c.rank == 'King':
                    self.total += 10
                elif c.rank == 'Queen':
                    self.total += 10
                elif c.rank == 'Jack':
                    self.total += 10
                else:
                    self.total += c.rank
        for c in self.cards:
            if c.rank == 1:
                if self.total <= 10:
                    self.total += 11
                else:
                    self.total += 1
        

class Dealer:
    def __init__(self):
        self.hand = hand()


class Player:
    def __init__(self):
        self.hand = hand()

def play():
    dealer = Dealer()
    player = Player()
# Sets up hands and calculates values
    dealer.hand.deal_initial_hand()
    dealer.hand.calc_total()
    player.hand.deal_initial_hand()
    player.hand.calc_total()

    bust = False
    dbust = False

    if player.hand.cards[0].rank == player.hand.cards[1].rank:
        split = True

    while player.hand.total < 21:
        print("Your hand is ")
        time.sleep(0.5)
        player.hand.show_hand()
        time.sleep(0.75)
        print('')
        print("Dealer's hand is " + str(dealer.hand.cards[0]) + " and a hidden card.")
        time.sleep(0.75)
        print('')

        ## Add split eventually
        i = input("Press 1 to hit or 2 to stand. ")
        time.sleep(0.5)
        print('')

        if i == "1":
            #Draw a new card and output value
            newcard = deck.deal_card()
            player.hand.cards.append(newcard)
            print("Your new card is " + str(newcard) + ".")
            player.hand.calc_total()
            print('')
            time.sleep(1)
            print("Your hand now totals to " + str(player.hand.total))
            time.sleep(1)
        
        if i == "2":
            print("Your hand totals to " + str(player.hand.total))
            print('')
            time.sleep(1)
            break

        if player.hand.total > 21:
            print("Bust! You lose.")
            bust = True
            break

##      Add blackjack check
        if player.hand.total == 21:
            print("21!")
            break

    while dealer.hand.total < 21 and bust != True:
        print("Dealer's hand is")
        dealer.hand.show_hand()
        time.sleep(0.5)

        if dealer.hand.total <= 17:
            # Tells dealer to hit under 17
            time.sleep(0.5)
            newcard = deck.deal_card()
            dealer.hand.cards.append(newcard)
            print("Dealer flips " + str(newcard) + ".")
            dealer.hand.calc_total()
            print('')
            time.sleep(1)

        if dealer.hand.total >= 17 and dealer.hand.total < 21:
            print("Dealer stands on " + str(dealer.hand.total))
            time.sleep(1)
            break 

        if dealer.hand.total > 21:
            print("Dealer busts!")
            dbust == True
            break
        else:
            dbust == False

##      Add blackjack check
        if dealer.hand.total == 21:
            print("Dealer has 21!")
            break
    
    if bust == False:
        # Game outcomes
        if player.hand.total > dealer.hand.total or dbust == True:
            print('')
            print("You Win!")

        if player.hand.total < dealer.hand.total and dbust == False:
            print("You Lose!")

        if player.hand.total == dealer.hand.total:
            print("Push!")

play()