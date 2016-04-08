from stem import *

word  = "placeholder"
while word != "exit":
	word = raw_input("Enter the Word: ")
	res = stem(word)
	print res