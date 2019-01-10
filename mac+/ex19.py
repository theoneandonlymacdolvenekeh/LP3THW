def cheese_and_crackers(cheese_count, box_of_crackers):
    print(f"you have {box_of_cracker} boxes of crackers!")
    print(f"you have {cheese_count} dheese!")
    print("man that's enough for a party!")
    print("get a blanket.\n")
    
    
print("we can just give the funtion number directly:")
cheese_and_crackers(20, 30)



print("or, we can use veriales from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("and we can even do math inside too")
cheese_and_crackers(10 + 20, 5 + 6)


print("and we can combine the two, veriable and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)