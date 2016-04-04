import sys
sys.path.append("../lib")
import en

def stem(word):
	result = en.verb.infinitive(word)
	if len(result) is 0:
		result = en.noun.singular(word)
	return result