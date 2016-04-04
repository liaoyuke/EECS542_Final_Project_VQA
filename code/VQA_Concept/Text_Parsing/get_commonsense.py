import urllib2
import json

def get_commonsense(word, limit):
	str = 'http://conceptnet5.media.mit.edu/data/5.4/c/en/' + word
	response = urllib2.urlopen(str)
	data = json.load(response)
	data_len = len(data["edges"])
	if limit < data_len:
		data_len = limit

	for i in range (0, data_len ):
		data_ex = data["edges"][i]["uri"]
		splited_str = data_ex.split(",")
		obj1 = splited_str[1].split("/")[3]
		obj2 = splited_str[2].split("/")[3]
		if obj1 != word :
			rst = obj1
		if obj2 != word :
			rst = obj2
		final_rst = rst.replace("_", " ")
		print(final_rst)

