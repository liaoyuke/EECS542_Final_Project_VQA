
import urllib2
import json
from get_common_sense import *

word  = "placeholder"
while word != "exit":
	word = raw_input("Enter the Word: ")
	GetCommonSense(word, 50)
	#print word