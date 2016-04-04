import urllib2
import json

def get_commonsense(word, limit):
	result_list = []
	limit = limit / 2 
	str1 = 'http://conceptnet5.media.mit.edu/data/5.4/search?end=/c/en/' + word + '&start=/c/en'
	str2 = 'http://conceptnet5.media.mit.edu/data/5.4/search?start=/c/en/' + word + '&end=/c/en'
	response1 = urllib2.urlopen(str1)
	response2 = urllib2.urlopen(str2)
	data1 = json.load(response1)
	data2 = json.load(response2)
	data = dict(data1.items() + data2.items())
	data_len = len(data["edges"])
	if limit * 2 < data_len:
		data_len = limit * 2

	for i in range (0, data_len ):
		data_ex = data["edges"][i]["uri"]
		splited_str = data_ex.split(",")
		obj1 = splited_str[1].split("/")[3]
		obj2 = splited_str[2].split("/")[3]
		rst = None
		if obj1 != word :
			rst = obj1
		if obj2 != word :
			rst = obj2
		if rst is None :
			continue
		final_rst = rst.replace("_", " ")
		result_list.append(final_rst)
		print(final_rst)

