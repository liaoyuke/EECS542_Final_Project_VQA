import urllib2
import json
from get_commonsense import *

word  = "placeholder"
while word != "exit":
	word = raw_input("Enter the Word: ")
	get_commonsense(word, 50)
	#print word