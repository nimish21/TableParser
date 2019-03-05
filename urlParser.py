#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pandas as pd 
from bs4 import BeautifulSoup

#'''
tableId = "tablaDatos"
outputfile = "file.csv"
url = 'http://www.knowafest.com/college-fests/upcomingfests'
#url = 'http://www.knowafest.com/college-fests/featured-events'
#'''


def parser(_url,_tableid,_outputFile):
	try:
		response = requests.get(_url)
		soup = BeautifulSoup(response.content, "html.parser")
		table = soup.find("table", id = _tableid )
		allrows = table.findAll('tr')
		data = ['|'.join([td.findNext(text=True) for td in tr.findAll("td")]) for tr in allrows]
		head = ['|'.join([th.findNext(text=True) for th in tr.findAll("th")]) for tr in allrows]
		newArray = []
		head = head[0].split('|')
		newArray.append(head)
		for row in data:
			column = row.split('|')
			newArray.append(column) 		
		dataframe = pd.DataFrame(newArray).to_csv(_outputFile, index=False)
		return True
	except :
		return False


if(parser(url,tableId,outputfile)):
	print("Successfully Saved into " + str(outputfile))
else:
	print("Failed to Parse HTML")
	