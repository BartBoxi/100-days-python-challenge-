print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))

if percentage == 10:
  print("Your tip is 10%")
elif percentage == 12:
  print("Your tip is 12%")
elif percentage == 15:
  print("Your tip is 15%")
else:
  print(f'Your tip is" {percentage} "%"')

tip = (percentage / 100) * (bill)

print(f'Then your tip should be {tip}')
