import random

class Round:
  def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card 

def calclulate_score(current_hand):
  total_score = sum(current_hand)
  if total_score == 21 and len(current_hand) == 2:
    total_score = 0
  if 11 in current_hand and total_score > 21:
    current_hand.remove(11)
    current_hand.append(1)
  return total_score
