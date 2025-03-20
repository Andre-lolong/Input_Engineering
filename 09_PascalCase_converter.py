# Ask the user for their fullname in incorrect casing
fullname = input("Enter your fullname in incorrect casing: ")

# Convert to pascal case
FULLNAME = fullname.title()
word = FULLNAME.split()
pascal_cased_name = ''.join(word)

print(f"Your fullname in pascal casing is: {pascal_cased_name}")