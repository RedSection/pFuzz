from static          import statics
from reqparser       import HTTPReq
from reqsender       import sendit
from modules.exparse import getpayloads
from static.statics  import fuzzsheetName
from static.statics  import fuzzingpayloads
from static.statics  import genericcolmnName


def fuzzmain():
    myreq  = HTTPReq.getobj()
    tmpuri = myreq.uri
    getpayloads(fuzzsheetName, genericcolmnName, fuzzingpayloads)
    for payload in fuzzingpayloads:
        if payload == '#exitme#':
            statics.exitCall = True
        else:
            myreq.uri = tmpuri + payload
            sendit(myreq)
