def f(player1, player2):
  def sumCards(cards):
    _sum = 0

    for i in cards:
      if i == "A" or i == "K" or i == "Q" or i == "J" or i == "T":
        _sum += 10
      else:
        _sum += int(i)

    return _sum

  return True if sumCards(player1) > sumCards(player2) else False
