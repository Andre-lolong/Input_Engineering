# ask the user to enter their fullname in incorrect casing
fullname = input("Enter your fullname in incorrect casing: ")

FULLNAME = fullname.swapcase() # reverse the casing

print(f"Your fullname: {FULLNAME}") # print the fullname of the user in reversed casing