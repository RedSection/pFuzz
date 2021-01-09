from re 			 import findall
from static          import statics
from reqparser       import HTTPReq
from reqsender       import sendit
from modules.exparse import getpayloads
from static.statics  import genericcolmnName
from static.statics  import charfuzzsheetName
from static.statics  import charfuzzingpayloads
import urllib.parse

def charfuzzmain():
	myreq  = HTTPReq.getobj()
	tmpuri = myreq.uri
	getpayloads(charfuzzsheetName, genericcolmnName, charfuzzingpayloads)
	for payload in charfuzzingpayloads:
		if payload == '#exitme#':
			statics.exitCall = True
		else:
			myreq.uri = tmpuri + "?param=valuex" + str(payload) + "aaaavaluey"
			sendit(myreq)
	
	while True:
		if len(statics.responses) == len(charfuzzingpayloads)-1:
			break

	for response in statics.responses:
		matched = findall(r'valuex(.*?)valuey', response[1])
		try:
			if matched[0] == '<aaaa' or urllib.parse.unquote(matched[0]) == '<aaaa':
				print("WAF bypassed via " + matched[0] + " char.")
		except:
			pass
