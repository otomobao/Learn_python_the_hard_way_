#import argument module
from sys import argv

#give the value of arguments to variables
script, filename = argv

#open the file and give the value to variable
txt = open(filename)

#print the filename
print "Here's your file %r:" %filename
#print file content
print txt.read()
