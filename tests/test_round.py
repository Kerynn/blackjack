from lib.round import Round 

def test_deal_card():
  round = Round()
  card = round.deal_card()
  
  assert card in [11,2,3,4,5,6,7,8,9,10,10,10,10]