from sys import argv

script, filename = argv

print(f"we're goning to erase {filename}.")
print("if you don't want that, hit CTRL-C (^C)")
print("if you do want that, hit RETRUN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("truncating the file. goodbye!")
target.truncate()

print("now i'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("now i'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally, we close it.")
target.close()