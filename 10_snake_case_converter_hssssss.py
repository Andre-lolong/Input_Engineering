# ask the user for their fullname in incorrect casing
fullname = input("Enter your fullname in incorrect casing: ")

# convert to snake case
FULLNAME = fullname.title()
word = FULLNAME.split()
snake_cased_name = '_'.join(word)

# print the user's fullname in snake casing
print(f"Your name in snake case format is: {snake_cased_name}")