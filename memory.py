# memory.py by rucury

import simplegui
import random

def new_game():
    global state, card1, card2, expose1, expose2, checkState, counter, cards, exposed
   
    counter = 0
    label.set_text("Turns = " + str(counter))
    state = 0
    card1 = None
    card2 = None
    expose1 = None
    expose2 = None
    checkState = None
    
    l1 = range(8)
    l2 = range(8)
    cards = l1 + l2

    exposed= []
    for i in range(len(cards)):
        exposed.append(False)

    random.shuffle(cards)
     
def mouseclick(pos):
 
    global idx, state, card1, card2, checkState, expose1, expose2, counter
    idx = pos[0] // 50
    
    if exposed[idx] == False and state == 0:
        exposed[idx]= True
        card1 = cards[idx]
        expose1 = idx
        checkState = True
        state = 1
        
    elif exposed[idx] == False and state == 1:
        exposed[idx]= True
        card2 = cards[idx]   
        expose2 = idx
        state = 2
        
    elif exposed[idx] == False and state == 2:
        exposed[idx]= True
        if checkState == True:
            if cards[card1]!= cards[card2]:
                exposed[expose1]= False
                exposed[expose2]= False
                checkState = False
                card1 = cards[idx]
                expose1 = idx
                counter += 1
                label.set_text("Turns = " + str(counter))
        else:
            if card1 != card2:
                exposed[expose1]= False
                exposed[expose2]= False
                card1 = cards[idx]
                expose1 = idx
            else:
                card1 = cards[idx]
                expose1 = idx
            counter += 1
            label.set_text("Turns = " + str(counter))
        state = 1
    
def draw(canvas):
    global cards
    card_pos= [20, 60]
    line_pos= [25, 0, 100]
    
    for c in range(len(cards)):
        if exposed[c] == False:
            canvas.draw_line((line_pos[0], line_pos[1]),(line_pos[0], line_pos[2]), 30, 'Green')
        elif exposed[c] == True:
            canvas.draw_text(str(cards[c]), card_pos, 25, "White")
        line_pos[0]+= 50
        card_pos[0]+= 50

frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()
