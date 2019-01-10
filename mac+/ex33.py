i = 0
numbers =[]

while i < 6:
    print(f"At the top i is {i} ")
    numbers.append(i)
    
    i = i+ 1
    print("Nunber now: ", numbers)
    print("The numbers: ")
    
    
print("The number: ")

for num in numbers:
    print(num)