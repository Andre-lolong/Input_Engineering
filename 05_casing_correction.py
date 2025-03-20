# ask the user for fullname with incorrect casing
fullname = input("Enter your fullname in incorrect casing: ")

FULLNAME = fullname.title() # correct the casing

print(f"Your fullname: {FULLNAME}") # print the fullname with correct casing
