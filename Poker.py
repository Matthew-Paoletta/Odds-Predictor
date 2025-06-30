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
    SF = 0
    FK = 0
    FH = [0, 0]
    FL = 0
    ST = 0
    TK = 0
    TP = [0, 0]
    OP = 0
    HC = []
    
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
        
        
    flush_count = 0
    straight_count = 0
    for i in range(len(sorted_hand)-1):
        if (values[sorted_hand[i][0]] + 1 == values[sorted_hand[i+1][0]]):
            straight_count += 1
        if (sorted_hand[i][1]==sorted_hand[i+1][1]):
            flush_count += 1
    #print(sorted_hand)    
    if (sorted_hand[0][0]=='2' and sorted_hand[1][0]=='3' and sorted_hand[2][0]=='4' and sorted_hand[3][0]=='5' and sorted_hand[4][0]=='A'):
        straight_count = 4
    
    if ((flush_count == 4) and (straight_count == 4)):
        SF = values[sorted_hand[-1][0]]
    elif (straight_count == 4):
        ST = values[sorted_hand[-1][0]] 
    elif (flush_count == 4):
        FL = values[sorted_hand[-1][0]]
        
        
    multiples = {}
    types = []
    for i, e in sorted_hand:
        types.append(values[i]) 
    for i in types:
        multiples[i] = types.count(i)
    for val, num in multiples.items():
        if num == 2 and OP == 0:
            OP = val
        elif num == 2 and OP != 0:
            TP = (OP, val)
            OP = 0
        elif num == 3:
            TK = val
        elif num == 4:
            FK = val
        elif num == 1:
            HC.insert(0, val)
    if TK != 0 and OP != 0:
        FH = [TK, OP]
        TK = 0
        OP = 0
    return [SF, FK, FH, FL, ST, TK, TP, OP, HC]
def compare(hand1, hand2):
    count1 = 0
    count2 = 0
    for i in range(len(hand1)):
        if (hand1[i]!=hand2[i]):
            
            if i==2 or i == 6:
                if hand1[i][0] > hand2[i][0]:
                    return hand1
                elif hand1[i][0] < hand2[i][0]:
                    return hand2
                else:
                    if hand1[i][1] > hand2[i][1]:
                        return hand1
                    elif hand1[i][1] < hand2[i][1]:
                        return hand2
            elif i==8:
                for e in range(len(hand1[i])):
                    if hand1[i][e] > hand2[i][e]:
                        return hand1
                    elif hand1[i][e] < hand2[i][e]:
                        return hand2
                return None
            else:
                if hand1[i] > hand2[i]:
                    return hand1
                elif hand1[i] < hand2[i]:
                    return hand2
                return None
            break
            
def find_best_hand(community, hole):
    best_hand = evaluate(community + hole)
    if len(community)==0:
        return evaluate(hole)
    elif len(community)==3:
        return best_hand
    elif len(community)==4:
        print(community[1:] + hole)
        return compare(best_hand, evaluate(community[1:] + hole))
    elif len(community) == 5:
        return compare(compare(best_hand, evaluate(community[1:4] + hole)), evaluate(community[2:] + hole))
    else:
        return None
            
            
      
def main():
    deck = [('A', 'S'), ('K', 'S'), ('Q', 'S'), ('J', 'S'), ('T', 'S'), ('9', 'S'), ('8', 'S'), ('7', 'S'), ('6', 'S'), ('5', 'S'), ('4', 'S'), ('3', 'S'), ('2', 'D'), ('A', 'D'), ('K', 'D'), ('Q', 'D'), ('J', 'D'), ('T', 'D'), ('9', 'D'), ('8', 'D'), ('7', 'D'), ('6', 'D'), ('5', 'D'), ('4', 'D'), ('3', 'D'), ('2', 'D'), ('A', 'C'), ('K', 'C'), ('Q', 'C'), ('J', 'C'), ('T', 'C'), ('9', 'C'), ('8', 'C'), ('7', 'C'), ('6', 'C'), ('5', 'C'), ('4', 'C'), ('3', 'C'), ('2', 'C'), ('A', 'H'), ('K', 'H'), ('Q', 'H'), ('J', 'H'), ('T', 'H'), ('9', 'H'), ('8', 'H'), ('7', 'H'), ('6', 'H'), ('5', 'H'), ('4', 'H'), ('3', 'H'), ('2', 'H')]
    p1 = deal(deck, 2)
    p2 = deal(deck, 2)
    board = []
    ex1 = [('A', 'S'), ('A', 'D'), ('J', 'S'), ('K', 'S'), ('K', 'S')]
    ex2 = [('A', 'S'), ('J', 'C'), ('K', 'D'), ('T', 'H'), ('Q', 'S')]
    print("Preflop:")
    print(board)
    print("Player 1 Hand:")
    print(p1)
    print("Player 1 Best Hand:")
    print(find_best_hand(board, p1))
    print("Player 2 Hand: ")
    print(p2)
    print("Player 2 Best Hand:")
    print(find_best_hand(board, p2))
    print("\n\nFlop:")
    board += deal(deck, 3)
    print(board)
    print("Player 1 Hand:")
    print(p1)
    print("Player 1 Best Hand:")
    print(find_best_hand(board, p1))
    print("Player 2 Hand: ")
    print(p2)
    print("Player 2 Best Hand:")
    print(find_best_hand(board, p2))
    print("\n\nTurn:")
    board += deal(deck, 1)
    print(board)
    print("Player 1 Hand:")
    print(p1)
    print("Player 1 Best Hand:")
    print(find_best_hand(board, p1))
    print("Player 2 Hand: ")
    print(p2)
    print("Player 2 Best Hand:")
    print(find_best_hand(board, p2))
    print("\n\nRiver:")
    board += deal(deck, 1)
    print(board)
    print("Player 1 Hand:")
    print(p1)
    print("Player 1 Best Hand:")
    print(find_best_hand(board, p1))
    print("Player 2 Hand: ")
    print(p2)
    print("Player 2 Best Hand:")
    print(find_best_hand(board, p2))
    
    
    
    '''ev_ex1 = evaluate(ex1)
    ev_ex2 = evaluate(ex2)
    print("Example Hand #1: ")
    print(ev_ex1)
    print("Example Hand #2: ")
    print(ev_ex2)
    print("Better One: ")
    print(compare(ev_ex1, ev_ex2))'''
    
    
    
    reshuffle_deck()
    
main()
    