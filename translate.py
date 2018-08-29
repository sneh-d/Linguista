import os
import sys
import requests
import unicodedata
import json

def translate(source_l, dest_l, data):
	if source_l=='':
		source= "auto"
	else:
		source = source_l
	dest = dest_l
	text = data
	URL = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=' + source + '&tl=' + dest + '&dt=t&q=' + text
	r = requests.get(url=URL)
	data = r.json()
	#webbrowser.open(url = URL, new = 2)
	fin_file = open("dest.txt", "w")
	oput = ""
	for result in data[0]:
		plainstring = unicodedata.normalize('NFKD', result[0]).encode('utf-8','ignore')
		oput+=plainstring
		fin_file.write(plainstring)
	return oput

"""def main():
    oput = translate('en', 'hi', 'I am Prachi')
    print("Translated text")
    print(oput)


if __name__ == '__main__':
    main()"""
