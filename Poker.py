import random
import copy

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
      
def evaluate(actual_hand):
    if (actual_hand==None):
        print("ERROR")
    hand = copy.deepcopy(actual_hand)
    
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
    #print(actual_hand)
    #print(hand)
    return [SF, FK, FH, FL, ST, TK, TP, OP, HC]
def compare(hand1, hand2):
    hand1_eval = evaluate(copy.deepcopy(hand1))
    hand2_eval = evaluate(copy.deepcopy(hand2))
    rank = 0
    while(rank < 9):
        #HC or TP or FH
        if (rank == 8 or rank == 6 or rank == 2):
            #print(hand1_eval[rank])
            #print(hand2_eval[rank])
            for i in range(len(hand1_eval[rank])):
                if hand1_eval[rank][i] > hand2_eval[rank][i]:
                    #print("hand 1 is higher")
                    return hand1
                elif hand1_eval[rank][i] < hand2_eval[rank][i]:
                    #print("hand 2 is higher")
                    return hand2
                else:
                    continue
            #print("same hand")
            #return hand2
        else: 
            if hand1_eval[rank] > hand2_eval[rank]:
                return hand1
            elif hand1_eval[rank] < hand2_eval[rank]:
                return hand2
        rank += 1        
        #FH and TP
        '''
        elif (rank == 2 or rank == 6):
            if hand1_eval[rank][0] > hand2_eval[rank][0]:
                return hand1
            elif hand1_eval[rank][0] < hand2_eval[rank][0]:
                return hand2
            elif hand1_eval[rank][0] == hand2_eval[rank][0]:
                if hand1_eval[rank][1] > hand2_eval[rank][1]:
                    return hand1
                elif hand1_eval[rank][1] < hand2_eval[rank][1]:
                    return hand2 
        ''' 
        #The rest of hands (SF, FK, FL, ST, TK, OP)
        
    #print("Same Hand")
    return -1
        
            
            
def find_best_hand(hole, community):
    total_cards = hole + community
    num_cards = len(total_cards)
    #pre-flop
    if (num_cards==2):
        return hole
    # flop
    elif(num_cards==5): 
        return total_cards
    #turn
    elif(num_cards==6): 
        holder = total_cards[0:5]
        for i in range(len(total_cards)-2, -1, -1):
            #print(i)
            #print(holder)
            card = total_cards[i]
            total_cards.remove(card)
            
            current_hand = copy.deepcopy(holder)
            checking_hand = copy.deepcopy(total_cards)
               
            holder = compare(current_hand, checking_hand)
            if holder == -1:
                holder = current_hand
            
            #print(total_cards)
            total_cards.insert(i, card)
        return holder
    #river
    elif(num_cards==7): 
        holder = total_cards[0:5]
        for i in range(len(total_cards)-1, 0, -1):
            card1 = total_cards[i]
            total_cards.remove(card1)
            for e in range(i-1, -1, -1):
                #print("i, e: " + str(i) + ", " + str(e))
                #print("e: " + str(e))
                #print(holder)
                
                card2 = total_cards[e]
                total_cards.remove(card2)
                
                #print(holder)
                #print(total_cards)
                current_hand = copy.deepcopy(holder)
                checking_hand = copy.deepcopy(total_cards)
                #print(checker)
                #print(current_hand)
                #print(checking_hand)
                holder = compare(current_hand, checking_hand)
                if holder == -1:
                    holder = current_hand
                #print(holder)
                total_cards.insert(e, card2)
            total_cards.insert(i, card1)
        return holder
            
    return num_cards
def translate(hand):
    your_hand = ""
    values = {14: 'Ace', 13:'King', 12:'Queen', 11:'Jack', 10:'Ten', 9:'Nine', 8:'Eight', 7:'Seven', 6:'Six', 5:'Five', 4: 'Four', 3:'Three', 2:'Two'}
    hand_eval = evaluate(copy.deepcopy(hand))
    if hand_eval[0]!=0:
        if hand_eval[0]==14:
            your_hand += "Royal Flush or an Ace High Straight Flush"
        else:
            your_hand += values[hand_eval[0]] + " High Straight Flush"
    elif hand_eval[2]!=[0,0]:
        your_hand += "Full House of " + values[hand_eval[2][0]] + "s over "+ values[hand_eval[2][1]] + "s"
    elif hand_eval[3]!=0:
        your_hand += values[hand_eval[3]] + " High Flush"
    elif hand_eval[4]!=0:
        your_hand += values[hand_eval[4]] + " High Straight"
    else:
        if hand_eval[1]!=0:
            your_hand += "Four-of-a-Kind of " + values[hand_eval[1]] + "s"
        if hand_eval[5]!=0:
            your_hand += "Three-of-a-Kind of " + values[hand_eval[5]] + "s"
        if hand_eval[6]!=[0,0]:
            your_hand += "Two Pair of " + values[hand_eval[6][0]] + "s and "+ values[hand_eval[6][1]] + "s"
        if hand_eval[7]!=0:
            your_hand += "Pair of " + values[hand_eval[7]] + "s"
        if len(hand_eval[8])!=0:
            if your_hand=="":
                your_hand += "High Card(s) "
                for i in range(len(hand_eval[8])-1):
                    your_hand += values[hand_eval[8][i]] + ", "
                your_hand += values[hand_eval[8][-1]]
            else:
                your_hand += " and High Card(s) "
                for i in range(len(hand_eval[8])-1):
                    your_hand += values[hand_eval[8][i]] + ", "
                your_hand += values[hand_eval[8][-1]]
    return your_hand     
def calculate_odds(deck, players_hands, curr_board):
    copy_deck = copy.deepcopy(deck)
    def helper():
        return 
    for i in range(5-len(curr_board)):
        print("Hello")
    for i in range(len(copy_deck)):
        #please fix this for preflop situations
        card = copy_deck[i]
        curr_board.append(card)
        temp_hands = []
        best_hand = []
        for e in range(len(players_hands)):
            temp_hands.append(find_best_hand(players_hands[e], curr_board))
        for e in range(len(temp_hands)-1):
            best_hand = compare(temp_hands[e], temp_hands[e+1])
        
        
        print(best_hand)
    
        curr_board.remove(card)
        

               
      
def main():
    deck = [('A', 'S'), ('K', 'S'), ('Q', 'S'), ('J', 'S'), ('T', 'S'), ('9', 'S'), ('8', 'S'), ('7', 'S'), ('6', 'S'), ('5', 'S'), ('4', 'S'), ('3', 'S'), ('2', 'D'), ('A', 'D'), ('K', 'D'), ('Q', 'D'), ('J', 'D'), ('T', 'D'), ('9', 'D'), ('8', 'D'), ('7', 'D'), ('6', 'D'), ('5', 'D'), ('4', 'D'), ('3', 'D'), ('2', 'D'), ('A', 'C'), ('K', 'C'), ('Q', 'C'), ('J', 'C'), ('T', 'C'), ('9', 'C'), ('8', 'C'), ('7', 'C'), ('6', 'C'), ('5', 'C'), ('4', 'C'), ('3', 'C'), ('2', 'C'), ('A', 'H'), ('K', 'H'), ('Q', 'H'), ('J', 'H'), ('T', 'H'), ('9', 'H'), ('8', 'H'), ('7', 'H'), ('6', 'H'), ('5', 'H'), ('4', 'H'), ('3', 'H'), ('2', 'H')]
    p1 = deal(deck, 2)
    p2 = deal(deck, 2)
    p3 = deal(deck, 2)
    p4 = deal(deck, 2)
    
    bh_p1 = []
    bh_p2 = []
    bh_p3 = []
    bh_p4 = []
    players_hands = [bh_p1, bh_p2, bh_p3, bh_p4]
    board = []
    ex1 = [('T', 'S'), ('J', 'D'), ('A', 'S'), ('K', 'S'), ('9', 'D'), ('Q', 'C'), ('9', 'D')]
    ex2 = [('A', 'S'), ('A', 'S'), ('A', 'S'), ('A', 'S'), ('K', 'C')]
    stages = ["Preflop:", "Flop", "Turn", "River"]
    for i in range(len(stages)):
        if i == 2:
            calculate_odds(deck, players_hands, board)
        print("\n\n"+stages[i])
        print(board)
        print("Player 1 Hand:")
        print(p1)
        bh_p1 = find_best_hand(p1, board)
        print("Player 2 Hand: ")
        print(p2)
        bh_p2 = find_best_hand(p2, board)
        print("Player 3 Hand: ")
        print(p3)
        bh_p3 = find_best_hand(p3, board)
        print("Player 4 Hand: ")
        print(p4)
        bh_p4 = find_best_hand(p4, board)
        
        if i == 0:
            board += deal(deck, 3)
        elif i < 3:
            board += deal(deck, 1)
        else:
            break
    better_hand = compare(compare(compare(bh_p1, bh_p2), bh_p3), bh_p4)   
    if (better_hand == bh_p1):
        print("Player 1 Wins with " + translate(better_hand))
    elif (better_hand == bh_p2):
        print("Player 2 Wins with " + translate(better_hand))
    elif (better_hand == bh_p3):
        print("Player 3 Wins with " + translate(better_hand))
    elif (better_hand == bh_p4):
        print("Player 4 Wins with " + translate(better_hand))
    else:
        print("Chop Pot")
        
    

    
    
    '''
    ev_ex1 = evaluate(ex1)
    ev_ex2 = evaluate(ex2)
    #print("Hole Cards")
    #print(ex1[0:2])
    #print("Board")
    #print(ex1[2:7])
    #print("Preflop: ")
    #print(find_best_hand(ex1[0:2], []))
    #print("Flop: ")
    #print(find_best_hand(ex1[0:2], ex1[2:5]))
    #print("Turn: ")
    #print(find_best_hand(ex1[0:2], ex1[2:6]))
    print("Your Hand: ")
    print(translate(ex2))
    #print("Example Hand #2: ")
    #print(ex2[0:2])
    #print("Better One: ")
    #print(compare(ev_ex1, ev_ex2))
    '''
    
    reshuffle_deck()
    
main()
    