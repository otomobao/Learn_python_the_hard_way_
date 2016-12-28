my_name = 'Zed A. Shaw'
my_age = 35 #not a lie
my_height = 74 # inches
my_height_cm = my_height * 2.54 # cm
my_weight = 180 # lbs
my_weight_kg = my_weight * 0.4536 #kg
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee" % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
#print "If I add %s, %s, and %s I get %s." % (
    #my_age, my_height, my_weight, my_age + my_height + my_weight)
#print "If I add %s, %s, and %s I get %s." % (
    #my_eyes, my_teeth, my_hair, my_eyes + my_teeth + my_hair)

#print "If I add %d, %d, and %d I get %d." % (
    #my_eyes, my_teeth, my_hair, my_eyes + my_teeth + my_hair)
    #This doesn't work
print "He's %d cm tall." % my_height_cm
#print "He's %f cm tall." % my_height_cm
print "He's %d pounds heavy." % my_weight_kg
#print "He's %f pounds heavy." % my_weight_kg
