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

    for _ in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
    
    while continue_play:
      user_score = calclulate_score(user_cards)
      computer_score = calclulate_score(computer_cards)
      print(f"Your cards: {user_cards}, current score: {user_score}")
      print(f"Computer's first card: {computer_cards[0]}")

      if user_score > 21 or user_score == 0 or computer_score == 0:
        continue_play = False
      else:
        user_deal_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_deal_card == 'y':
          user_cards.append(deal_card())
        else:
          continue_play = False

    while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calclulate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    
      


