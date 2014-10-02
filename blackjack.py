# blackjack.py by rucury

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        
        canvas.draw_image(card_images, card_loc, CARD_SIZE, 
                         [pos[0] + CARD_CENTER[0], pos[1] + 
                         CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        global in_play
        
        self.cards = []	
        in_play = True

    def __str__(self):
        string = "Hand contains"
        for i in range(len(self.cards)):
            string += " " + str(self.cards[i])
        return string
    
    
    def add_card(self, card):
        self.cards.append(card)	

    def get_value(self):
        global hand_value
        hand_value = 0
        flag = False
        
        for card in self.cards:
            rank = card.get_rank()
            if rank in RANKS:
                if rank == 'A':
                    flag = True
                hand_value += VALUES[rank]
        if flag == False:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
            
    def draw(self, canvas, pos):
        for c in self.cards:
            c.draw(canvas, pos)
            pos[0] += 80
        
# define deck class 
class Deck:
    def __init__(self):
        self.deckCards = []
        for suit in SUITS: 
            for rank in RANKS:
                self.newCard = Card(suit, rank)
                self.deckCards.append(self.newCard)                
        self.shuffle()      

    def shuffle(self):
        random.shuffle(self.deckCards)

    def deal_card(self):
        return random.choice(self.deckCards)
    
    def __str__(self):
        string = "Deck contains"
        for i in range(len(self.deckCards)):
            string += " " + str(self.deckCards[i])
        return string

#define event handlers for buttons
def deal():
    global outcome, in_play, my_deck, my_hand, dealer_hand, score, outcome
    
    if in_play:
        score -= 1

    my_deck = Deck()
    my_hand = Hand()
    dealer_hand = Hand()
    
    my_hand.add_card(my_deck.deal_card())
    my_hand.add_card(my_deck.deal_card())
    
    dealer_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card())
    
    my_hand.get_value()
    in_play = True
    outcome = "Hit or stand?"

def hit():
    global in_play, hand_value, outcome, score
    if in_play:
        if hand_value <= 21:
            my_hand.add_card(my_deck.deal_card())
            if my_hand.get_value() > 21:
                outcome = "You busted! Click the Deal button to restart"
                in_play = False
                score -= 1
    else:
        outcome = "The game is already over!"
      
def stand():
    global outcome, score, in_play
    
    if not in_play:
        outcome = "The game is already over!"
    else:
        while dealer_hand.get_value() <= 17:
            dealer_hand.add_card(my_deck.deal_card())
            
        if dealer_hand.get_value() >= my_hand.get_value() \
        and dealer_hand.get_value() <= 21:
            outcome = "You lose! Click the Deal button to restart."
            score -= 1
            in_play = False
            
        else:
            outcome = "You win! Click the Deal button to restart."
            score += 1
            in_play = False
            
# draw handler    
def draw(canvas):
    global score
	# game canvas text
    canvas.draw_text("Blackjack", [235, 40], 46, "Black")
    canvas.draw_text(outcome, [75, 460], 26, "Black")
    canvas.draw_text("Value: " + str(my_hand.get_value()), [100, 290], 16, "Black")
    
    if not in_play:
        canvas.draw_text("Value: " + str(dealer_hand.get_value()), [100, 90], 16, "Black") # draw the true value string
    else:
        canvas.draw_text("Value: ?", [100, 90], 16, "Black") # draw the hidden value string  
		
    canvas.draw_text("Score: " + str(score), [470, 590], 26, "Black")
	
    # draw the cards on the canvas
	my_hand.draw(canvas, [100, 300])
    if not in_play:
        dealer_hand.draw(canvas, [100, 100]) # draw all of the dealer's cards
    else:
        dealer_hand.draw(canvas, [100, 100]) # draw all of the dealer's cards...
		# but place the image of a flipped card on top of the hole card, to hide it
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (136.5, 148.5), CARD_BACK_SIZE)
        


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

deal()
frame.start()
