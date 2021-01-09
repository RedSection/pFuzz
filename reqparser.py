from difflib        import SequenceMatcher
from waflogger      import loginfo
from waflogger      import logdebug
from static.statics import parseKey
from static.statics import headerFile


class HTTPReq:
    def __init__(self):
        self.im                         = None
        self.accept                     = None
        self.accept_charset             = None
        self.accept_encoding            = None
        self.accept_language            = None
        self.accept_datetime            = None
        self.access_control_req_method  = None
        self.access_control_req_headers = None
        self.authorization              = None
        self.cache_control              = None
        self.connection                 = None
        self.content_length             = None
        self.content_type               = None
        self.cookie                     = None
        self.date                       = None
        self.expect                     = None
        self.forwarded                  = None
        self.reqfrom                    = None
        self.host                       = None
        self.if_match                   = None
        self.if_modified_since          = None
        self.if_none_match              = None
        self.if_range                   = None
        self.if_unmodified_since        = None
        self.max_forwards               = None
        self.method                     = None
        self.origin                     = None
        self.pragma                     = None
        self.proxy_authorization        = None
        self.range                      = None
        self.referer                    = None
        self.te                         = None
        self.uri                        = None
        self.http                       = None
        self.user_agent                 = None
        self.upgrade                    = None
        self.upgrade_insecure_requests  = None
        self.via                        = None
        self.warning                    = None
        self.dnt                        = None
        self.x_requested_with           = None
        self.x_csrf_token               = None
        self.expiresself                = None
        self.body                       = None
        self.test                       = None
        self.result                     = None

    # Request object
    def generateobj():
        global myreq
        myreq = HTTPReq()

    def getobj():
        return myreq

    def addheader(self, newheader, newvalue):
        self.__dict__[newheader] = newvalue

    def delheader(self, oldheader):
        self.__dict__[oldheader.lower()] = None
        self.__dict__[oldheader] = None

    def changeheader(self, header, newvalue):
        self.__dict__[header.lower()] = self.__dict__[header.lower()] + parseKey + newvalue


def getheaderList():
    headerfile = open(headerFile, 'r')
    headerList = []
    for header in headerfile:
        headerList.append(header.strip())
    return headerList


def getdiffratio(header, objattr):
    newobj = ""

    if objattr == "reqfrom":
        newobj = "FROM"

    if newobj == "":
        newobj = objattr

    return objattr, SequenceMatcher(None, header.upper(), newobj.upper()).ratio()


def extbody(line, lastpart):
    if myreq.body is None:
        myreq.body = ""

    if myreq.content_type is not None:
        if "multipart" in myreq.content_type and lastpart != 0:
            line += "\n"

    myreq.body += line


def extmethods(line):
    myreq.method = line.split(' ')[0].strip()
    myreq.uri    = line.split(' ')[1].strip()
    myreq.http   = line.split(' ')[2].strip()


def concobj(myreq, data, objattr):
    if "-" in objattr:
        newobj = ""
        for leng in range(0, len(objattr.split('-'))):
            if leng != int(len(objattr.split('-')) - 1):
                newobj += objattr.split('-')[leng] + "_"
            else:
                newobj += objattr.split('-')[leng]
    else:
        newobj = objattr

    setattr(myreq, newobj.lower(), data)


def parseheaders(usrreqlist):
    loginfo('Header parsing module is running')
    headers = getheaderList()

    methodFlag  = 0
    payloadFlag = 0

    for line in usrreqlist:

        if payloadFlag != 0:
            if line == usrreqlist[-1]:
                extbody(line.strip(), 0)
            else:
                extbody(line.strip(), 1)

        if line == "\n":
            payloadFlag += 1

        methodFlag += 1

        if methodFlag == 1:
            extmethods(line)

        else:
            for header in headers:
                checkpart = line.split(' ')[0]

                if ":" in checkpart:
                    checkpart = checkpart[:-1]

                objattr, rate = getdiffratio(header, checkpart)

                if objattr != myreq.content_type and objattr == "Content-Type" and myreq.content_type is not None:
                    rate = 0

                if rate == 1:
                    logdebug('Header [' + objattr + '] is found in the request')

                    if len(line.split(":")) == 2:
                        data = line.split(":")[1].strip()
                        concobj(myreq, data, objattr)
                    else:
                        newline = ""

                        for leng in range(0, len(line.split(':'))):
                            if leng != 0:
                                if leng != len(line.split(':'))-1:
                                    newline += line.split(":")[leng].strip() + ":"
                                else:
                                    newline += line.split(":")[leng].strip()

                        concobj(myreq, newline, objattr)
