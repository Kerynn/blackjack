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

  def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
      return "Your score is over 21. You lose!"
    elif user_score == computer_score:
      return "You tied with the computer!"
    elif computer_score == 0:
      return "The computer has a blackjack. You lose!"
    elif user_score == 0:
      return "You win with a blackjack!"
    elif user_score > 21:
      return "Your score is over 21. You lose!"
    elif computer_score > 21:
      return "The computer went over 21. You win!"
    elif user_score > computer_score:
      return "You win!"
    else: 
      return "You lose!"

  def play_game():
    user_cards = []
    computer_cards = []
    continue_play = True
    

