from sys import argv # takes in arguments

script, arg = argv # the varibales that taking the values
n = int(arg) # typecast a string into an int

for i in range( 1, n ): # a for loop that happens as many times as the number of n
    if n//i == i and n%i == 0: # checks if its a you can square root the number and its positive
        print(n//i) # prints out the square root
        exit(0) # if statement is rrue then exist the program
        
print(False) # if loop is down and nothing is correct then print out false



# programs square roots numbers.