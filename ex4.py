cars = 100
spcae_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * spcae_in_a_car
average_passengers_per_car = passengers / cars_driven
#average_passengers_per_car2 = car_pool_capacity / passengers
#average_passengers_per_car2 = carpool_capacity / passengers

print "There are", cars, "cars availabe."
print "There are only", drivers, "drivers availabe."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
#print "We need to test about", average_passengers_per_car2, "in each car."
print "Hey %s there." % "you"
