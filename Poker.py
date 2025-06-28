import random

global deck
def choose_random(choices):
    picked = random.choice(choices)
    choices.remove(picked)
    return picked
def deal(choices, cards):
    location = []
    for i in range(cards):
        location.append(choose_random(choices))
    return location

def reshuffle_deck():
    deck = [('A', 'S'), ('K', 'S'), ('Q', 'S'), ('J', 'S'), ('T', 'S'), ('9', 'S'), ('8', 'S'), ('7', 'S'), ('6', 'S'), ('5', 'S'), ('4', 'S'), ('3', 'S'), ('2', 'D'), ('A', 'D'), ('K', 'D'), ('Q', 'D'), ('J', 'D'), ('T', 'D'), ('9', 'D'), ('8', 'D'), ('7', 'D'), ('6', 'D'), ('5', 'D'), ('4', 'D'), ('3', 'D'), ('2', 'D'), ('A', 'C'), ('K', 'C'), ('Q', 'C'), ('J', 'C'), ('T', 'C'), ('9', 'C'), ('8', 'C'), ('7', 'C'), ('6', 'C'), ('5', 'C'), ('4', 'C'), ('3', 'C'), ('2', 'C'), ('A', 'H'), ('K', 'H'), ('Q', 'H'), ('J', 'H'), ('T', 'H'), ('9', 'H'), ('8', 'H'), ('7', 'H'), ('6', 'H'), ('5', 'H'), ('4', 'H'), ('3', 'H'), ('2', 'H')]
      
def evaluate(hand):
    values = {'A': 14, 'K':13, 'Q':12, 'J':11, 'T':10, '9': 9, '8':8, '7':7, '6':6, '5':5, '4': 4, '3':3, '2':2}
    sorted_hand = []
    for j in range(len(hand)):
        flag = 15
        low_card = ()
        for i, e in hand:
            if values[i] < flag:
                flag = values[i]
                low_card = (i , e)         
        sorted_hand.append(low_card)
        hand.remove(low_card)
    
    print(sorted_hand)
    #Straight Flush
    
        
    #4 of a Kind
    #Full House
    #Flush
    flush_count = 0
    for i in range(len(sorted_hand)-1):
        if (sorted_hand[i][1]==sorted_hand[i+1][1]):
            flush_count += 1
    #Straight
    
    straight_count = 0
    for i in range(len(sorted_hand)-1):
        if (values[sorted_hand[i][0]] + 1 != values[sorted_hand[i+1][0]]):
            break
        straight_count += 1
    if (sorted_hand[0][0]=='2' and sorted_hand[1][0]=='3' and sorted_hand[2][0]=='4' and sorted_hand[3][0]=='5' and sorted_hand[4][0]=='A'):
        straight_count = 4
    
    if ((flush_count == 4) and (straight_count == 4)):
        print("I'm Straight Flushed with Poker on My Face")
    elif (straight_count == 4):
        print("You're Straight Not Gay") 
    elif (flush_count == 4):
        print("You're Flushed Bruv")
        

    #3 of a Kind
    #Two Pair
    #One Pair
    #High Card     
      
def main():
    deck = [('A', 'S'), ('K', 'S'), ('Q', 'S'), ('J', 'S'), ('T', 'S'), ('9', 'S'), ('8', 'S'), ('7', 'S'), ('6', 'S'), ('5', 'S'), ('4', 'S'), ('3', 'S'), ('2', 'D'), ('A', 'D'), ('K', 'D'), ('Q', 'D'), ('J', 'D'), ('T', 'D'), ('9', 'D'), ('8', 'D'), ('7', 'D'), ('6', 'D'), ('5', 'D'), ('4', 'D'), ('3', 'D'), ('2', 'D'), ('A', 'C'), ('K', 'C'), ('Q', 'C'), ('J', 'C'), ('T', 'C'), ('9', 'C'), ('8', 'C'), ('7', 'C'), ('6', 'C'), ('5', 'C'), ('4', 'C'), ('3', 'C'), ('2', 'C'), ('A', 'H'), ('K', 'H'), ('Q', 'H'), ('J', 'H'), ('T', 'H'), ('9', 'H'), ('8', 'H'), ('7', 'H'), ('6', 'H'), ('5', 'H'), ('4', 'H'), ('3', 'H'), ('2', 'H')]
    p1 = deal(deck, 5)
    p2 = deal(deck, 5)
    straight_ex = [('2', 'S'), ('2', 'C'), ('4', 'S'), ('5', 'S'), ('A', 'S')]
    print(p1)
    print(p2)
    evaluate(p1)
    evaluate(straight_ex)
    
    reshuffle_deck()
    
main()
    