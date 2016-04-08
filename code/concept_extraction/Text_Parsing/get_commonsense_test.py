import urllib2
import json
from get_commonsense import *

word  = "placeholder"
while word != "exit":
	word = raw_input("Enter the Word: ")
	rst = get_commonsense(word, 20)
	print rst;