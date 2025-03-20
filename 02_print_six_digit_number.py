# ask the user for number 1-1000
while True:
    try:
        num = input("Enter a number from 1 to 1000: ")
        if 1 <= int(num) <= 1000:
            num = num
            print(num)
            break
        else:
            print("The number you entered is not between 1 to 1000. Try again.\n")
    except ValueError:
        print("Enter a valid input.")
# check the digit
digit = len(num)
print(digit)
# add zeros to the beginning to match the six digit requirement for the input