import urllib.parse
from ssl            import SSLError
from ssl            import SSLContext
from ssl            import wrap_socket
from ssl            import PROTOCOL_SSLv23
from ssl            import create_connection
from time           import sleep
from pickle         import dumps
from pickle         import loads
from static         import statics
from socket         import socket
from socket         import timeout
from socket         import gaierror
from socket         import AF_INET
from socket         import SOL_SOCKET
from socket         import SOCK_STREAM
from socket         import SO_REUSEADDR
from socket         import setdefaulttimeout
from OpenSSL        import SSL
from waflogger      import outputs
from waflogger      import loginfo
from waflogger      import logwarn
from waflogger      import detailedoutputs
from reqparser      import getheaderList


def extport(obj):
    try:
        return int(obj.host.split(':')[1])
    except:
        return 80


def concreq(obj):
    key  = statics.parseKey
    data = ""
    conFlag = 0
    if obj.method is not None and obj.uri is not None and obj.http is not None:
        conFlag += 1
        if statics.proxy != "" and statics.usessl is True:
            statics.tmpproxyData = "CONNECT " + obj.host + ":443 " + obj.http + "\r\n"
            statics.tmpproxyData += "Connection: close\r\n\r\n"
            data += obj.method + " " + obj.uri + " " + obj.http + "\r\n"
        elif statics.proxy != "" and statics.usessl is False:
            data += obj.method + " " + "http://" + obj.host + obj.uri + " " + obj.http + "\r\n"
        else:
            data += obj.method + " " + obj.uri + " " + obj.http + "\r\n"
    if obj.method is not None and conFlag == 0:
        if statics.proxy != "" and statics.usessl is True:
            statics.tmpproxyData = "CONNECT "
            data += obj.method + " "
        elif statics.proxy != "" and statics.usessl is False:
            data += obj.method + " " + "http://"
        else:
            data += obj.method + " "
    if obj.uri is not None and conFlag == 0:
        if statics.proxy != "" and statics.usessl is True:
            statics.tmpproxyData += obj.host + ":443 "
            data += obj.uri + " "
        elif statics.proxy != "" and statics.usessl is False:
            data += obj.host + obj.uri + " "
        else:
            data += obj.uri + " "
    if obj.http is not None and conFlag == 0:
        if statics.proxy != "" and statics.usessl is True:
            statics.tmpproxyData += obj.http + "\r\n"
            statics.tmpproxyData += "Connection: close\r\n\r\n"
            data += obj.http + "\r\n"
        elif statics.proxy != "" and statics.usessl is False:
            data += obj.http + "\r\n"
        else:
            data += obj.http + "\r\n"
    if obj.host is not None:
        if not key in obj.host:
            data += "Host: " + obj.host + "\r\n"
        elif key in obj.host:
            data += obj.host.split(key)[1] + ": " + obj.host.split(key)[0] + "\r\n"
    else:
        if not key in obj.test:
            data += "Host:" + obj.test + "\r\n"
        elif key in obj.test:
            data += obj.test.split(key)[1] + ":" + obj.test.split(key)[0] + "\r\n"
    if obj.user_agent is not None:
        if not key in obj.user_agent:
            data += "User-Agent: " + obj.user_agent + "\r\n"
        elif key in obj.user_agent:
            data += obj.user_agent.split(key)[1] + ": " + obj.host.user_agent(key)[0] + "\r\n"
    if obj.im is not None:
        if not key in obj.im:
            data += "-IM: " + obj.im + "\r\n"
        elif key in obj.im:
            data += obj.im.split(key)[1] + ": " + obj.im.split(key)[0] + "\r\n"
    if obj.accept is not None:
        if not key in obj.accept:
            data += "Accept: " + obj.accept + "\r\n"
        elif key in obj.accept:
            data += obj.accept.split(key)[1] + ": " + obj.accept.split(key)[0] + "\r\n"
    if obj.accept_charset is not None:
        if not key in obj.accept_charset:
            data += "Accept-Charset: " + obj.accept_charset + "\r\n"
        elif key in obj.accept_charset:
            data += obj.accept_charset.split(key)[1] + ": " + obj.accept_charset.split(key)[0] + "\r\n"
    if obj.accept_encoding is not None:
        if not key in obj.accept_encoding:
            data += "Accept-Encoding: utf-8\r\n"
        elif key in obj.accept_encoding:
            data += obj.accept_encoding.split(key)[1] + ": " + obj.accept_encoding.split(key)[0] + "\r\n"
    if obj.accept_language is not None:
        if not key in obj.accept_language:
            data += "Accept-Language: " + obj.accept_language + "\r\n"
        elif key in obj.accept_language:
            data += obj.accept_language.split(key)[1] + ": " + obj.accept_language.split(key)[0] + "\r\n"
    if obj.accept_datetime is not None:
        if not key in obj.accept_datetime:
            data += "Accept-Datetime: " + obj.accept_datetime + "\r\n"
        elif key in obj.accept_datetime:
            data += obj.accept_datetime.split(key)[1] + ": " + obj.accept_datetime.split(key)[0] + "\r\n"
    if obj.access_control_req_method is not None:
        if not key in obj.access_control_req_method:
            data += "Access-Control-Request-Method: " + obj.access_control_req_method + "\r\n"
        elif key in obj.access_control_req_method:
            data += obj.access_control_req_method.split(key)[1] + ": " + obj.access_control_req_method.split(key)[0] + "\r\n"
    if obj.access_control_req_headers is not None:
        if not key in obj.access_control_req_headers:
            data += "Access-Control-Request-Headers: " + obj.access_control_req_headers + "\r\n"
        elif key in obj.access_control_req_headers:
            data += obj.access_control_req_headers.split(key)[1] + ": " + obj.access_control_req_headers.split(key)[0] + "\r\n"
    if obj.authorization is not None:
        if not key in obj.authorization:
            data += "Authorization: " + obj.authorization + "\r\n"
        elif key in obj.authorization:
            data += obj.authorization.split(key)[1] + ": " + obj.authorization.split(key)[0] + "\r\n"
    if obj.referer is not None:
        if not key in obj.referer:
            data += "Referer: " + obj.referer + "\r\n"
        elif key in obj.referer:
            data += obj.referer.split(key)[1] + ": " + obj.referer.split(key)[0] + "\r\n"
    if obj.content_type is not None:
        if not key in obj.content_type:
            data += "Content-Type: " + obj.content_type + "\r\n"
        elif key in obj.content_type:
            data += obj.content_type.split(key)[1] + ": " + obj.content_type.split(key)[0] + "\r\n"
    if obj.content_length is not None:
        if not key in obj.content_length:
            data += "Content-Length: " + obj.content_length + "\r\n"
        elif key in obj.content_length:
            data += obj.content_length.split(key)[1] + ": " + obj.content_length.split(key)[0] + "\r\n"
    if obj.cookie is not None:
        if not key in obj.cookie:
            data += "Cookie: " + obj.cookie + "\r\n"
        elif key in obj.cookie:
            data += obj.cookie.split(key)[1] + ": " + obj.cookie.split(key)[0] + "\r\n"
    if obj.connection is not None:
        if not key in obj.connection:
            data += "Connection: " + obj.connection + "\r\n"
        elif key in obj.connection:
            data += obj.connection.split(key)[1] + ": " + obj.connection.split(key)[0] + "\r\n"
    if obj.origin is not None:
        if not key in obj.origin:
            data += "Origin: " + obj.origin + "\r\n"
        elif key in obj.origin:
            data += obj.origin.split(key)[1] + ": " + obj.origin.split(key)[0] + "\r\n"
    if obj.upgrade is not None:
        if not key in obj.upgrade:
            data += "Upgrade: " + obj.upgrade + "\r\n"
        elif key in obj.upgrade:
            data += obj.upgrade.split(key)[1] + ": " + obj.upgrade.split(key)[0] + "\r\n"
    if obj.upgrade_insecure_requests is not None:
        if not key in obj.upgrade_insecure_requests:
            data += "Upgrade-Insecure-Requests: " + obj.upgrade_insecure_requests + "\r\n"
        elif key in obj.upgrade_insecure_requests:
            data += obj.upgrade_insecure_requests.split(key)[1] + ": " + obj.upgrade_insecure_requests.split(key)[0] + "\r\n"
    if obj.via is not None:
        if not key in obj.via:
            data += "Via: " + obj.via + "\r\n"
        elif key in obj.via:
            data += obj.via.split(key)[1] + ": " + obj.via.split(key)[0] + "\r\n"
    if obj.warning is not None:
        if not key in obj.warning:
            data += "Warning: " + obj.warning + "\r\n"
        elif key in obj.warning:
            data += obj.warning.split(key)[1] + ": " + obj.warning.split(key)[0] + "\r\n"
    if obj.dnt is not None:
        if not key in obj.dnt:
            data += "DNT: " + obj.dnt + "\r\n"
        elif key in obj.dnt and not key in obj.dnt:
            data += obj.dnt.split(key)[1] + ": " + obj.dnt.split(key)[0] + "\r\n"
    if obj.x_requested_with is not None:
        if not key in obj.x_requested_with:
            data += "X-Requested-With: " + obj.x_requested_with + "\r\n"
        elif key in obj.x_requested_with:
            data += obj.x_requested_with.split(key)[1] + ": " + obj.x_requested_with.split(key)[0] + "\r\n"
    if obj.x_csrf_token is not None:
        if not key in obj.x_csrf_token:
            data += "X-CSRF-Token: " + obj.x_csrf_token + "\r\n"
        elif key in obj.x_csrf_token:
            data += obj.x_csrf_token.split(key)[1] + ": " + obj.x_csrf_token.split(key)[0] + "\r\n"
    if obj.expiresself is not None:
        if not key in obj.expiresself:
            data += "Expires: " + obj.expiresself + "\r\n"
        elif key in obj.expiresself:
            data += obj.expiresself.split(key)[1] + ": " + obj.expiresself.split(key)[0] + "\r\n"
    if obj.date is not None:
        if not key in obj.date:
            data += "Date: " + obj.date + "\r\n"
        elif key in obj.date:
            data += obj.date.split(key)[1] + ": " + obj.date.split(key)[0] + "\r\n"
    if obj.expect is not None:
        if not key in obj.expect:
            data += "Expect: " + obj.expect + "\r\n"
        elif key in obj.expect:
            data += obj.expect.split(key)[1] + ": " + obj.expect.split(key)[0] + "\r\n"
    if obj.forwarded is not None:
        if not key in obj.forwarded:
            data += "Forwarded: " + obj.forwarded + "\r\n"
        elif key in obj.forwarded:
            data += obj.forwarded.split(key)[1] + ": " + obj.forwarded.split(key)[0] + "\r\n"
    if obj.reqfrom is not None:
        if not key in obj.reqfrom:
            data += "From: " + obj.reqfrom + "\r\n"
        elif key in obj.reqfrom:
            data += obj.reqfrom.split(key)[1] + ": " + obj.reqfrom.split(key)[0] + "\r\n"
    if obj.if_match is not None:
        if not key in obj.if_match:
            data += "If-Match: " + obj.if_match + "\r\n"
        elif key in obj.if_match:
            data += obj.if_match.split(key)[1] + ": " + obj.if_match.split(key)[0] + "\r\n"
    if obj.if_modified_since is not None:
        if not key in obj.if_modified_since:
            data += "If-Modified-Since: " + obj.if_modified_since + "\r\n"
        elif key in obj.if_modified_since:
            data += obj.if_modified_since.split(key)[1] + ": " + obj.if_modified_since.split(key)[0] + "\r\n"
    if obj.if_none_match is not None:
        if not key in obj.if_none_match:
            data += "If-None-Match: " + obj.if_none_match + "\r\n"
        elif key in obj.if_none_match:
            data += obj.if_none_match.split(key)[1] + ": " + obj.if_none_match.split(key)[0] + "\r\n"
    if obj.if_range is not None:
        if not key in obj.if_range:
            data += "If-Range: " + obj.if_range + "\r\n"
        elif key in obj.if_range:
            data += obj.if_range.split(key)[1] + ": " + obj.if_range.split(key)[0] + "\r\n"
    if obj.if_unmodified_since is not None:
        if not key in obj.if_unmodified_since:
            data += "If-Unmodified-Since: " + obj.if_unmodified_since + "\r\n"
        elif key in obj.if_unmodified_since:
            data += obj.if_unmodified_since.split(key)[1] + ": " + obj.if_unmodified_since.split(key)[0] + "\r\n"
    if obj.max_forwards is not None:
        if not key in obj.max_forwards:
            data += "Max-Forwards: " + obj.max_forwards + "\r\n"
        elif key in obj.max_forwards:
            data += obj.max_forwards.split(key)[1] + ": " + obj.max_forwards.split(key)[0] + "\r\n"
    if obj.pragma is not None:
        if not key in obj.pragma:
            data += "Pragma: " + obj.pragma + "\r\n"
        elif key in obj.pragma:
            data += obj.pragma.split(key)[1] + ": " + obj.pragma.split(key)[0] + "\r\n"
    if obj.proxy_authorization is not None:
        if not key in obj.proxy_authorization:
            data += "Proxy-Authorization: " + obj.proxy_authorization + "\r\n"
        elif key in obj.proxy_authorization:
            data += obj.proxy_authorization.split(key)[1] + ": " + obj.proxy_authorization.split(key)[0] + "\r\n"
    if obj.range is not None:
        if not key in obj.range:
            data += "Range: " + obj.range + "\r\n"
        elif key in obj.range:
            data += obj.range.split(key)[1] + ": " + obj.range.split(key)[0] + "\r\n"
    if obj.te is not None:
        if not key in obj.te:
            data += "TE: " + obj.te + "\r\n"
        elif key in obj.te:
            data += obj.te.split(key)[1] + ": " + obj.te.split(key)[0] + "\r\n"
    if obj.cache_control is not None:
        if not key in obj.cache_control:
            data += "Cache-Control: " + obj.cache_control + "\r\n"
        elif key in obj.cache_control:
            data += obj.cache_control.split(key)[1] + ": " + obj.cache_control.split(key)[0] + "\r\n"

    headerList = getheaderList()
    if len(obj.__dict__) != len(headerList):
        for head in obj.__dict__:
            detectnewheader = 0
            found = 0
            for header in headerList:
                if "-" in header:
                    newhead = ""
                    for leng in range(0, len(header.split('-'))):
                        if leng != int(len(header.split('-')) - 1):
                            newhead += header.split('-')[leng] + "_"
                        else:
                            newhead += header.split('-')[leng]
                else:
                    newhead = header
                if head.lower() == newhead.lower():
                    found = 1
                    break
                else:
                    detectnewheader += 1
            if detectnewheader == len(headerList) and found == 0 and getattr(obj, head) is not None and head != "body":
                data += head + ":" + " " + getattr(obj, head) + "\r\n"

    data += "\r\n"
    if obj.body is not None:
        data += obj.body
    return data.encode('utf-8')


def extresult(res):
    try:
        if res != "" or res is not None:
            try:
                resline = res.decode('utf-8', 'ignore')
                code = resline.split('\r')[0]
            except UnicodeDecodeError:
                resline = str(res)
                code = resline.split('\x5c\x72\x5c\x6e')[0]
            finally:
                loginfo('Response: ' + code.split(' ')[1])
                return code, resline
        else:
            loginfo("Response did not come")
    except:
        logwarn('Connection could not be established')


def socketconnect(s, host, port):
    loginfo('Socket is created [' + host + ":" + str(port) + ']')
    s.connect((host, port))
    loginfo('Socket connected to [' + host + ":" + str(port) + ']')


def socketsslconnect(s, host, port):
    if port == 80:
        port = 443
    loginfo('SSL Socket is created [' + host + ":" + str(port) + ']')
    try:
        sslSocket = wrap_socket(s)
        sslSocket.check_hostname = False
        sslSocket.connect((host, port))
    except SSLError:
        conn = create_connection((host, port))
        context = SSLContext(PROTOCOL_SSLv23)
        sslSocket = context.wrap_socket(conn, server_hostname=host)
    except gaierror:
        host = host.strip()
        try:
            sslSocket = wrap_socket(s)
            sslSocket.check_hostname = False
            sslSocket.connect((host, port))
        except:
            conn = create_connection((host, port))
            context = SSLContext(PROTOCOL_SSLv23)
            sslSocket = context.wrap_socket(conn, server_hostname=host)
    finally:
        loginfo('SSL Socket connected to [' + host + ":" + str(port) + ']')
    return sslSocket


def verifyconn(conn, cert, errun, depth, ok):
    return True


def sendit(obj):
    statics.senderQ.put(dumps(obj))


def fullencode(obj):
    if obj.body is not None:
        obj.body = urllib.parse.quote(obj.body)
    if obj.uri is not None:
        obj.uri  = urllib.parse.quote(obj.uri)


def spaceencode(obj):
    if obj.body is not None:
        obj.body = obj.body.replace(" ", "+")
    if obj.uri is not None:
        obj.uri  = obj.uri.replace(" ", "+")


def sender():
    while True:
        if statics.senderQ.qsize() != 0:
            sleep(statics.reqdelay)
            obj = loads(statics.senderQ.get())
            if statics.encoding is True:
                spaceencode(obj)
            elif statics.fullencoding is True:
                fullencode(obj)

            s = socket(AF_INET, SOCK_STREAM)
            s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 2)
            if statics.usessl is not True and statics.proxy == "":
                setdefaulttimeout(3)

            try:
                if statics.usessl is True:
                    if statics.proxy != "":
                        port = int(statics.proxy.split(":")[1])
                        rawrequest = concreq(obj)
                        socketconnect(s, statics.proxy.split(":")[0], port)
                        s.send(statics.tmpproxyData.encode())
                        s.recv(4096)
                        ctx = SSL.Context(SSL.SSLv23_METHOD)
                        ctx.set_verify(SSL.VERIFY_PEER, verifyconn)
                        ss = SSL.Connection(ctx, s)
                        ss.set_connect_state()
                        ss.do_handshake()
                        ss.send(rawrequest)
                        responsex = ss.recv(4096)
                        with open('textfile.txt', 'a') as f:
                            for ch in responsex:
                                f.write('{}\n'.format(ord(ch)))
                        result, allresults = extresult(responsex)
                        if result is not None and allresults is not None:
                            statics.responses.append((result, allresults))
                        ss.shutdown()
                        ss.close()
                    else:
                        port = extport(obj)
                        if obj.host is not None:
                            if ":" in obj.host:
                                sslSocket = socketsslconnect(s, obj.host.split(":")[0], port)
                            else:
                                sslSocket = socketsslconnect(s, obj.host, port)
                        else:
                            if ":" in obj.test:
                                sslSocket = socketsslconnect(s, obj.test.split(":")[0], port)
                            else:
                                sslSocket = socketsslconnect(s, obj.test, port)
                        loginfo(obj.method + " " + obj.uri + " " + obj.http)
                        rawrequest = concreq(obj)
                        sslSocket.send(rawrequest)
                        result, allresults = extresult(sslSocket.recv(4096))
                        if result is not None and allresults is not None:
                            statics.responses.append((result, allresults))
                        sslSocket.close()
                else:
                    if statics.proxy != "":
                        port = int(statics.proxy.split(":")[1])
                        socketconnect(s, statics.proxy.split(":")[0], port)
                        loginfo(obj.method + " " + obj.uri + " " + obj.http)
                        rawrequest = concreq(obj)
                        s.send(rawrequest)
                    else:
                        port = extport(obj)
                        try:
                            if ":" in obj.host and "\t" not in obj.host:
                                socketconnect(s, obj.host.split(":")[0], port)
                            elif "\t" in obj.host:
                                socketconnect(s, obj.host.strip().split(":")[0], port)
                            else:
                                socketconnect(s, obj.host, port)
                        except:
                            try:
                                if ":" in obj.test:
                                    socketconnect(s, obj.test.split(":")[0], port)
                                else:
                                    socketconnect(s, obj.test, port)
                            except TypeError:
                                pass
                        loginfo(obj.method + " " + obj.uri + " " + obj.http)
                        rawrequest = concreq(obj)
                        try:
                            s.sendall(rawrequest)
                        except timeout:
                            pass

                    try:
                        result, allresults = extresult(s.recv(4096))
                        if result is not None and allresults is not None:
                            statics.responses.append((result, allresults))
                    except timeout:
                        pass
                    s.close()

                if statics.outputting is True:
                    outputs(obj, result)

                if statics.outputdetails is True:
                    detailedoutputs(obj, allresults)

                loginfo('Socket is closed')

            except ConnectionRefusedError:
                logwarn('Connection is refused [' + obj.host + ']')

        elif statics.exitCall is True:
            exit()
