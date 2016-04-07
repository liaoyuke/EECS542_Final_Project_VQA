from get_keywords import *

sentence  = "placeholder"
while sentence != "exit":
	sentence = raw_input("Enter the Sentence: ")
	print get_keywords(sentence)