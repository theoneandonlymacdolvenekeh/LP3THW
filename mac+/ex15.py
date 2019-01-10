from sys import argv
script, filname = argv 

txt = open(filname)

print(f"Here's your file {filename}.")
print(txt.read())

print("Type the filename again.")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())