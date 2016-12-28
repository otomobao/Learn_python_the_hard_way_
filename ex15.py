#import argument module
from sys import argv

#give the value of arguments to variables
script, filename = argv

#give the value of file object to variable
txt = open(filename)

#print the filename
print "Here's your file %r:" %filename
#print file content
print txt.read()
txt.close()

#ask user to input filename
print "Type the filename again:"
#give the input value to the variable
file_again = raw_input(">")

#give the value of file object to variable
txt_again = open(file_again)

#print the file content
print txt_again.read()
txt_again.close()

#in terminal: f = open('ex15_sample.txt') print f.read()
