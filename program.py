import random as rd

class Password:

    def __init__(self, max_length, min_length):
        self.max_length = max_length
        self.min_length = min_length
        self.password = ""

    def create_pass(self):
        length = rd.randint(self.min_length, self.max_length)
        for x in range(length):
            self.password += rd.choice(allsq)


upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters = "abcdefghijklmnopqrstuvwxyz"
symbols = "(){}[]<>,.?/';\\+=-_!`~^$%#@*&"
digits = "0123456789"

digitBool, lowerBool, upperBool, symBool = True, True, True, True

while True:
    digit = input("Does the password have number (Yes or No): ")
    if digit == "Yes" or digit == "yes":
        break
    elif digit == "No" or digit == "no":
        digitBool = False
        break
    else:
        print("Invalid input. Please try again")
        continue

while True:
    lower = input("Does the password have lowercase letters (Yes or No): ")
    if lower == "Yes" or lower == "yes":
        break
    elif lower == "No" or lower == "no":
        lowerBool = False
        break
    else:
        print("Invalid input. Please try again")
        continue

while True:
    upper = input("Does the password have uppercase letters (Yes or No): ")
    if upper == "Yes" or upper == "yes":
        break
    elif upper == "No" or upper == "no":
        upperBool = False
        break
    else:
        print("Invalid input. Please try again")
        continue

while True:
    sym = input("Does the password have symbols (Yes or No): ")
    if sym == "Yes" or sym == "yes":
        break
    elif sym == "No" or sym == "no":
        symBool = False
        break
    else:
        print("Invalid input. Please try again")
        continue

allsq = ""

if digitBool:
    allsq += digits
if lowerBool:
    allsq += lower_letters
if upperBool:
    allsq += upper_letters
if symBool:
    allsq += symbols

while True:
    max = int(input("Insert the maximum length of the password: "))
    min = int(input("Insert the minimum length of the password: "))
    if min > max:
        print("Minimum length has to be smaller or equal to maximum length. Please try again.")
        continue
    break

pw1 = Password(max, min)
pw1.create_pass()
print(f"Your password is:\n{pw1.password}")

input("Enter any key to quit: ")

