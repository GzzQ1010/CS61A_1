"""
Code that processes an iterator(via next) or iterable(via for or iter) make
few assumptions about the data itself
    1.changing the data representation from a list to a tuple, map object, 
    or dict_keys doesn't require rewriting code
    2.others are more likely to be able to use your code on their data
An iterator bundle together a sequence and a position within that sequence 
as one object
    1.Passing that object to another function always retains the position.
    2.useful for ensuring that each element of a squence is processed only once 
    limits the operations that can be performed on the sequence to only requesting next. 

"""

##Casino Blackjeck example
import random
points={'J':10,'Q':10,'K':10,'A':1}

def hand_score(hand):
    """Total score for a hand
    >>>hand_score(['A',3,6])
    20
    >>>hand_score(['A','J','A'])
    12
    """
    total=sum([points.get(card,card) for card in hand ])
    if total<=11 and 'A'in hand:
        return total+10
    return total

def shuffle_cards():
    deck=(['J','Q','K','A']+list(range(2,11)))*4
    random.shuffle(deck)
    return iter(deck)

def player_turn(up_card,cards,strategy,deck):
    while hand_score(cards)<=21 and strategy(up_card,cards):
        cards.append(next(deck))

def dealer_turn(cards,deck):
    while hand_score(cards)<17:
        cards.append(next(deck))

def blackjack(strategy, announce=print):
    """play a hand of casino blackjack"""
    deck=shuffle_cards()
    player_cards=[next(deck)]
    up_card=next(deck)
    player_cards.append(next(deck))
    hole_card=next(deck)
    player_turn(up_card,player_cards,strategy,deck)
    if hand_score(player_cards)>21:
        announce('Player goes bust with', player_cards,'against a',up_card)
        return -1 
    
    dealer_card=[up_card,hole_card]
    dealer_turn(dealer_card,deck)
    if hand_score(dealer_card)>21:
        announce('Dealer busts with', dealer_card)
        return 1
    else:
        announce('Player has', hand_score(player_cards),'and dealer has',
                 hand_score(dealer_card))
        diff=hand_score(player_cards)-hand_score(dealer_card)
        return max(-1,min(1,diff))

def basic_strategy(up_card,cards):
    if hand_score(cards)<=11:
        return True
    if up_card in [2,3,4,5,6]:
        return False 
    return hand_score(cards)<17
    