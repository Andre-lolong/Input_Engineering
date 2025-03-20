# ask the user for their fullname with several spaces in the beginning
fullname = input("Enter your fullname with several space characters at the beginning: ")
full_name = fullname.strip() # remove the indentation

print(f"Fullname: {full_name}") # print the fullname