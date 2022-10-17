from logo import logo
from replit import clear
import os

bid = {}
bidding_finished = True

print(logo)

def highest_bidder(bid_record):
  for i in bid_record:
    max = 0
    if bid_record[i] > max:
      max = bid [i]
      bidder = i

  print(f"The winner is {bidder} with the highest bid of ₹{max}")

while bidding_finished:

  name = input("What is your name?: ")

  bid[name] = int(input("What is your bid?: ₹"))

  other_bid = input("Is there any other bidder?: ")

  other_bid.lower()

  if other_bid =='no' or other_bid =='n':
    bidding_finished = False
    clear()
    highest_bidder(bid)

  elif other_bid =='yes' or other_bid =='y':
    os.system('clear')
