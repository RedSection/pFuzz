from reqparser       import HTTPReq
from reqsender       import sendit
from modules.exparse import getpayloads
from static.statics  import headersheetName
from static.statics  import headerspayloads
from static.statics  import genericcolmnName
from modules.headeroperations import headeroperation


def headervalue(myreq, head):
    head_value = "127.0.0.1"
    myreq.addheader(head, head_value)
    sendit(myreq)

    head_value = myreq.host
    myreq.addheader(head, head_value)
    sendit(myreq)

    myreq.delheader(head)


def changecontenttype(myreq, payload):
    if myreq.content_type is not None:
        new_contenttype = payload.split(":")[1]
        myreq.content_type = new_contenttype


def modifyheader():
    myreq = HTTPReq.getobj()
    getpayloads(headersheetName, genericcolmnName, headerspayloads)
    for payload in headerspayloads:
        if payload == '#exitme#':
            headeroperation(myreq)
            break
        else:
            if not "Content-Type" in payload:
                headervalue(myreq, payload)
            else:
                if myreq.content_type is not None:
                    changecontenttype(myreq, payload)
                    sendit(myreq)
