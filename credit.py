from cs50 import get_int

# This program checks if credit card is valid and what's the type of card.
# It can detect Visa, Mastercard and American Express cards.


# 1.Getting card number from user and checking it's lenght.
#   Checking lenght of card number. Accepted lenght: 13, 15, 16.
while (True):
    card_number = input("Please enter card number here: ")
    if len(card_number) in [13, 15, 16] and card_number.isdigit():
        break
    elif card_number.isdigit():
        break


# 2.Checking card with Luhn's Algorithm.
rcard_nr = card_number[::-1]


number_of_digits = len(card_number)
sum_of_odds = 0
sum_of_evens = 0


# 2.1.Sum of every second digit multiplied by 2.
# Calculating multiplication of every other digit by 2,
# starting with the number's second-to-last digit
# and then adding those products’ digits together.

for i in range(1, number_of_digits, 2):
    if int(rcard_nr[i]) * 2 > 9:
        sum_of_odds += 1 + (int(rcard_nr[i]) * 2) % 10
    else:
        sum_of_odds += int(rcard_nr[i]) * 2

# 2.2.Sum of the rest of digits.
for i in range(0, number_of_digits, 2):
    sum_of_evens += int(rcard_nr[i])


# 2.3.Calculating total sum.
total_sum = sum_of_odds + sum_of_evens


# 2.4.Checking if card number is valid.
if total_sum % 10 == 0:
    # 3.Checking card type.
    if int(card_number[0]) == 4 and number_of_digits in [13, 16]:
        print("VISA")
    elif number_of_digits == 15 and int(card_number[0]) == 3 and int(card_number[1]) in [4, 7]:
        print("AMEX")
    elif number_of_digits == 16 and int(card_number[0]) == 5 and int(card_number[1]) in [1, 2, 3, 4, 5]:
        print("MASTERCARD")
else:
    print("INVALID")