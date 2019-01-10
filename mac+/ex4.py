cars = 100
# i decalare and intialize the veriable cars and set its value to be 100
space_in_a_car = 40
# i declare and intaiize the variable space_in_a_car and set its value to 40 
drivers = 30
# i declare and initailize the veriable drivers and set its value to 30
passenger = 90
# i declare and intialize the veriable passenger and set the value to 90
cars_not_driven = cars - drivers
# i declare and intailize the veriable cars_not_driven and set its value to cars - drivers 
cars_driven = drivers
# i dreclate and intailize the verable cars_driven and set its value to drivers
carpool_capacity = cars_driven * space_in_a_car
# i declare and imtialize the veriable carpool_capacity and set the value  to cars_driven * space_in_car
average_passenger_per_car = passenger / cars_driven
# i declare and intialize the veriable average_passenger_per_car and set the value to passenger / cars_driven


print("these are", cars, "cars available.")
print("there will be", drivers, "empty cars today.")
print("There will be", cars_not_driven, "empty cars today.")
print("we can transport", carpool_capacity, 'people today.')
print("we have", passenger, "to carpool today.")
print("we need to put about", average_passenger_per_car, "in each car.")
