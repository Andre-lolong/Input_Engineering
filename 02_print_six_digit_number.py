# ask the user for number 0 to 1000
while True:
    try:
        num = int(input("Enter a number from 0 to 1000: "))
        if 0 <= int(num) <= 1000:
            num = num
            break
        else:
            print("The number you entered is not between 0 to 1000. Try again.\n")
    except ValueError:
        print("Enter a valid input.\n")

# add zeros to the beginning to match the six digit requirement for the input
new_num = (f"{num:06}")
print(new_num)