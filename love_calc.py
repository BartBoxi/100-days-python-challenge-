# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1=name1.lower()
lower_case_name2=name2.lower()

true_love = (lower_case_name1.count("t") + lower_case_name2.count("t"))
true_love = true_love + (lower_case_name1.count("r") + lower_case_name2.count("r"))
true_love = true_love + (lower_case_name1.count("u") + lower_case_name2.count("u"))
true_love = true_love + (lower_case_name1.count("e") + lower_case_name2.count("e"))


love_count = (lower_case_name1.count("l") + lower_case_name2.count("l"))
love_count = love_count + (lower_case_name1.count("o") + lower_case_name2.count("o"))
love_count = love_count + (lower_case_name1.count("v") + lower_case_name2.count("v"))
love_count = love_count + (lower_case_name1.count("e") + lower_case_name2.count("e"))

result = str(true_love) + str(love_count)

result = int(result)

if result < 10 or result > 90:
    print(f'Your score is {result}, you go together like coke and mentos.')
elif result >= 40 and result < 50:
    print(f'Your score is {result}, you are alright together.')
else:
    print(f'Your score is {result}.')



