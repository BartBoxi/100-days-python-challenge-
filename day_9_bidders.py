from replit import clear
#HINT: You can call clear() to clear the output in the console.

#print logo
from art import logo
print(logo)

#What is your name? 
#What is your bid 
#Are they any other bidders? Type yes or no 
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
  bidder_name = input("What is your name?: ")
  bidder_value = int(input("What is your bid? $"))
  bids[bidder_name] = bidder_value
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()


    
