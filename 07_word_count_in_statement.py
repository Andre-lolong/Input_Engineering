# ask the user to enter any statement
sentence = input("Enter any statement you want: ")

# count each word
word = sentence.split()
word_count = len(word)

# print how many words are used in the 
print(f'You have used {word_count} in your statement "{sentence}"')