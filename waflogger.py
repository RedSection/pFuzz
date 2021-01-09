from static     import statics
from logging    import info
from datetime   import datetime


def getcurrenttime():
    time = str(datetime.now()).split(' ')[1].split(":")[0] + "_" + \
           str(datetime.now()).split(' ')[1].split(":")[1] + "_" + \
           str(datetime.now()).split(' ')[1].split(":")[2].split('.')[0]
    return time


def outputs(obj, result):
    if not obj.host is None:
        if statics.usessl is True:
            try:
                msg = '[https://' + obj.host + ']' + " " + '[' + obj.method + " " + obj.uri + ']' + " " + '[' + result.split("b'")[1] + ']'
            except:
                msg = '[https://' + obj.host + ']' + " " + '[' + obj.method + " " + obj.uri + ']' + " " + '[' + result + ']'
        else:
            msg = '[http://' + obj.host + ']' + " " + '[' + obj.method + " " + obj.uri + ']' + " " + '[' + result + ']'

        if statics.outputFile == "":
            print(msg)
        else:
            try:
                file = open(statics.outputFile, 'a')
            except IOError:
                logdebug(statics.outputFile + 'got an error')
            finally:
                file.write(msg + "\n")
                file.close()


def detailedoutputs(obj, result):
    from reqsender import concreq
    if statics.outputReqdetail == "" and statics.outputResdetail == "":
        print('[REQUEST #'  + str(statics.outputFlag) + ']')
        print(concreq(obj).decode())
        print('[RESPONSE #' + str(statics.outputFlag) + ']')
        print(result)
        print('##################################')
    else:
        try:
            filereq = open(statics.outputReqdetail, 'a')
            fileres = open(statics.outputResdetail, 'a')
        except IOError:
            logdebug(statics.outputReqdetail + 'got an error')
            logdebug(statics.outputResdetail + 'got an error')
        finally:
            filereq.write('[REQUEST #' + str(statics.outputFlag) + ']' + "\n")
            filereq.write(concreq(obj).decode() + "\n")
            filereq.write('##################################\n')
            filereq.close()
            fileres.write('[RESPONSE #' + str(statics.outputFlag) + ']' + "\n")
            fileres.write(result + "\n")
            fileres.write('##################################\n')
            filereq.close()
    statics.outputFlag += 1


def logstart():
    if statics.logging is True:
        info('#####################################')
        info('[INFO] pFuzz is starting...')


def logstop():
    if statics.logging is True:
        info('[INFO] pFuzz is stopping...')
        info('#####################################')


def loginfo(msg):
    if statics.logging is True:
        info('[INFO] ' + msg + '...')


def logdebug(msg):
    if statics.logging is True:
        info('[DEBUG] ' + msg + '.')


def logwarn(msg):
    if statics.logging is True:
        info('[WARNING] ' + msg + '!')

