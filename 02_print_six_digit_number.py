# ask the user for number 1-1000
while True:
    try:
        num = input("Enter a number from 1 to 1000: ")
        if 1 <= int(num) <= 1000:
            num = num
            break
        else:
            print("The number you entered is not between 1 to 1000. Try again.\n")
    except ValueError:
        print("Enter a valid input.\n")
# check the digit
digit = len(num)
# add zeros to the beginning to match the six digit requirement for the input
for i in range(digit, 6):
    if digit == i:
        print("0" * (6-i) + (num))