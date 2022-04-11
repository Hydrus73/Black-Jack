import os
import random
import time
def makeDeck(): # Makes the deck
  deck = []
  for i in range(1, 14):
    for x in range(1, 5):
      if x == 1:
        suit = ' of Hearts'
      elif x == 2:
        suit = ' of Diamonds'
      elif x == 3:
        suit = ' of Spades'
      elif x == 4:
        suit = ' of Clubs'
      value = i
      if i == 11:
        value = 'Jack'
      elif i == 12:
        value = 'Queen'
      elif i == 13:
        value = 'King'
      elif i == 1:
        value = 'Ace'
      deck.append(str(value) + suit)
  return deck
def clear(): # clears the screen
  os.system('clear')
def rand(deck):
  return random.randint(0, len(deck)-1)
def printCards(cards1, num): # prints the cards
  thing = []
  for i in range(0, len(cards1)):
    thing.append(cards1[i])
    if thing[i].split(' of ')[1].lower() == 'spades' or thing[i].split(' of ')[1].lower() == 'clubs':
      thing[i] = '\033[36m' + thing[i] + '\033[32m'
    else:
      thing[i] = '\033[31m' + thing[i] + '\033[32m'
  cards = ''
  if num == 1:
    for i in range(0, len(cards1)):
      if len(cards1) != 2:
        if i != len(cards1) - 1:
          cards += ' the ' + thing[i] + ','
        else:
          cards += ' and the ' + thing[i] + '.'
      else:
        if i != len(cards1) - 1:
          cards += ' the ' + thing[i]
        else:
          cards += ' and the ' + thing[i] + '.'
    print('Your cards are' + cards)
  elif num == 2:
    cards += ' the ' + thing[0] + '.'
    print('One of the house\'s cards is' + cards)
  elif num == 3:
    for i in range(0, len(cards1)):
      if len(cards1) != 2:
        if i != len(cards1) - 1:
          cards += ' the ' + thing[i] + ','
        else:
          cards += ' and the ' + thing[i] + '.'
      else:
        if i != len(cards1) - 1:
          cards += ' the ' + thing[i]
        else:
          cards += ' and the ' + thing[i] + '.'
    print('The house\'s cards were' + cards)
def getHitOrStay(num, total, total2): # gets if you and the house want to hit or stay
  if num == 1:
    while True:
      hitOrStay = input('Will you hit or stay?\n').lower()
      if hitOrStay == 'hit' or hitOrStay == 'stay':
        break
      else:
        clear()
        printCards(houseCards, 2)
        printCards(playerCards, 1)
        print("Your total is now " + str(total) + ".")
        print('Invalid Input.')
    return hitOrStay
  else:
    if total < total2 and total <= 21 and total2 > 16 and total2 <= 21 and random.randint(1, 3) <= 2 or total <= 15:
      return "hit"
    elif total <= 21 and total2 > 21:
      if random.randint(1, 10) <= 3:
        return 'hit'
      else:
        return 'stayed'
    else:
      return "stayed"
def getTotals(cards, total): # gets the total value for the hand
  x = 0
  cardy = []
  bob = []
  for i in range(0, len(cards)):
    if cards[i].split(" of ")[0].lower() == "ace":
      bob.append(cards[i])
    else:
      cardy.append(cards[i])
  for y in bob:
    cardy.append(y)
  for card in cardy:
    try:
      x += int(card.split(" of ")[0])
    except:
      if card.split(" of ")[0].lower() != "ace":
        x += 10
      else:
        if x + 11 <= 21:
          x += 11
        else:
          x += 1
  return x
def sleep(): # sleeps
  time.sleep(2)
def winner(houseCards, playerCards, houseTotal, playerTotal, num): # writes the stuff at the end and who won
  printCards(houseCards, 3)
  if num == 1:
    sleep()
  printCards(playerCards, 1)
  if num == 1:
    sleep()
  if houseTotal > 21:
    print("The house's total was " + str(houseTotal) + ", so the house busted.")
  else:
    print("The house's total was " + str(houseTotal) + ".")
  if num == 1:
    sleep()
  if playerTotal > 21:
    print("Your total was " + str(playerTotal) + ", so you busted.")
  else:
    print("Your total was " + str(playerTotal) + ".")
  if num == 1:
    sleep()
  if playerTotal > 21 and houseTotal <= 21:
    print("\033[31mThe house won.")
  elif playerTotal <= 21 and houseTotal > 21:
    print("\033[34mYou won!")
  elif playerTotal == houseTotal:
    print("\033[31mThe house won.")
  elif playerTotal <= 21 and houseTotal < playerTotal:
    print("\033[34mYou won!")
  elif houseTotal <= 21 and houseTotal > playerTotal:
    print("\033[31mThe house won.")
  elif houseTotal < playerTotal:
    print("\033[31mYou both busted, but the house won because it was the closest to 21.")
  elif houseTotal > playerTotal:
    print("\033[34mYou both busted, but you won because you were the closest to 21!")
clear()
input("\033[32mWelcome to Black Jack.\nPress enter to start...\n")
while True: # runs all the code
  playerCards = [] # the next part of code sets up the deck and hands
  houseCards = []
  playerTotal = 0
  houseTotal = 0
  deck = makeDeck()
  clear()
  x = rand(deck)
  playerCards.append(deck[x])
  del deck[x]
  x = rand(deck)
  playerCards.append(deck[x])
  del deck[x]
  x = rand(deck)
  houseCards.append(deck[x])
  del deck[x]
  x = rand(deck)
  houseCards.append(deck[x])
  del deck[x]
  printCards(houseCards, 2)
  printCards(playerCards, 1)
  playerTotal = getTotals(playerCards, 0)
  houseTotal = getTotals(houseCards, 0)
  print("Your total is " + str(playerTotal) + ".")
  while True: # does the player's move
    yellow = getHitOrStay(1, playerTotal, 0)
    if yellow == "stay":
      clear()
      printCards(houseCards, 2)
      printCards(playerCards, 1)
      playerTotal = getTotals(playerCards, playerTotal)
      break
    else:
      x = rand(deck)
      clear()
      playerCards.append(deck[x])
      del deck[x]
      printCards(houseCards, 2)
      printCards(playerCards, 1)
      playerTotal = getTotals(playerCards, playerTotal)
      print("Your total is now " + str(playerTotal) + ".")
      if playerTotal > 21:
        clear()
        printCards(houseCards, 2)
        printCards(playerCards, 1)
        playerTotal = getTotals(playerCards, playerTotal)
        break
  print("Your total is " + str(playerTotal) + ".")
  while True: # does the house's move
    if getHitOrStay(2, houseTotal, playerTotal) == "hit":
      time.sleep(1)
      print("The house hit.")
      x = rand(deck)
      houseCards.append(deck[x])
      del deck[x]
      houseTotal = getTotals(houseCards, houseTotal)
    else:
      time.sleep(1)
      print("The house stayed.")
      break
  time.sleep(2)
  clear()
  winner(houseCards, playerCards, houseTotal, playerTotal, 1)
  while True: # asks to play again
    again = input("\033[32mWould you like to play again?\n").lower()
    if again == "y" or again == "yes" or again == "no" or again == "n":
      break
    else:
      clear()
      winner(houseCards, playerCards, houseTotal, playerTotal, 0)
      print("\033[32mInvalid Input.")
  if again == "no" or again == "n":
    break
clear()
winner(houseCards, playerCards, houseTotal, playerTotal, 0)
