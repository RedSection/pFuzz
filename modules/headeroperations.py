from static    import statics
from reqsender import sendit


def addfirstline(myreq):
    tmpmethod = myreq.method
    myreq.method = "\r\n" + myreq.method
    sendit(myreq)

    myreq.method = tmpmethod


def writelowercasemethod(myreq):
    tmpmethod = myreq.method
    myreq.method = myreq.method.lower()
    sendit(myreq)

    myreq.method = tmpmethod


def tabsbeforemethod(myreq):
    tmpmethod = myreq.method
    myreq.method = "\t" + myreq.method
    sendit(myreq)

    myreq.method = tmpmethod


def hostlowercase(myreq):
    tmphost = myreq.host
    myreq.host = myreq.host.lower()
    sendit(myreq)

    myreq.host = tmphost


def removehostspace(myreq):
    tmphost = myreq.host
    myreq.host = None
    myreq.test = tmphost
    sendit(myreq)

    myreq.test = None
    myreq.host = tmphost


def hostwithtab(myreq):
    tmphost = myreq.host
    myreq.host = "\t" + myreq.host
    sendit(myreq)

    myreq.host = tmphost


def headeroperation(myreq):
    addfirstline(myreq)
    writelowercasemethod(myreq)
    tabsbeforemethod(myreq)
    hostlowercase(myreq)
    removehostspace(myreq)
    hostwithtab(myreq)

    statics.exitCall = True
