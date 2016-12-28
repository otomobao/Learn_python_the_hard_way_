#ask user to input filename
print "Type the filename again:"
#give the input value to the variable
file_again = raw_input(">")

#open the file and give the value to variable
txt_again = open(file_again)

#print the file content
print txt_again.read()
