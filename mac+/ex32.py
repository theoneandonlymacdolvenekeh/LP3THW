the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pear', 'apricots']
change = [1, 'pennies', 2, 'dines', 3, 'quarters']


# this frist kind of for-loop goes through a list 
for fruit in fruits:
    print(f"A fruits type: {fruits}")
    
    
# also we can go through mixed lists too 
# notice have to {} since we don't know what's in it
for i in change:
    print(f"I got {i}")
    
# we can also build lists, frist start with an empty one
elements = []

# then use the range funtion to do 0 to 5 counts
for i in range(0,6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)
    
# now we can print theb out too
for i in elements:
    print(f"Elements was: {i}")