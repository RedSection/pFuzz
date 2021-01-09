#!/usr/bin/python3

from os                 import path
from os                 import mkdir
from sys                import exit
from menu               import args
from time               import sleep
from static             import statics
from logging            import INFO
from logging            import basicConfig
from messages           import filenotfound
from messages           import tool_exit_message
from waflogger          import logstart
from waflogger          import logstop
from waflogger          import loginfo
from waflogger          import logwarn
from waflogger          import getcurrenttime
from reqsender          import sender
from reqparser          import HTTPReq
from reqparser          import parseheaders
from threading          import Thread
from modules.fuzzer     import fuzzmain
from modules.charfuzzer import charfuzzmain
from multiprocessing    import Process
from modules.manipulatingheaders import modifyheader


def controller(reqfile):
    if args.request is None:
        tool_exit_message()
        logstop()
        exit()

    if path.exists(reqfile):
        # other checks will be added.
        pass
    else:
        filenotfound(reqfile)
        logstop()
        exit()

    myreq = HTTPReq.generateobj()


def starts():
    if args.request is None:
        logwarn('The following arguments are required: --request/-r')
        print('The following arguments are required: --request/-r')
        logstop()
        tool_exit_message()
        exit()

    reqfile = args.request
    controller(reqfile)

    if args.proxy is not None:
        loginfo('Proxy [' + args.proxy + '] set by the user')
        statics.proxy = args.proxy
    else:
        loginfo('Proxy does not set by default')

    if args.ssl is not None:
        loginfo('SSL enabled by the user')
        statics.usessl = args.ssl
    else:
        loginfo('SSL disabled by default')

    if args.encode is True and args.full_encode is True:
        logwarn('URI/Body [space] and full encoding can not be used at the same time')
        tool_exit_message()
        exit()

    if args.encode is True:
        loginfo('URI/Body [space] encoding is enabled by the user')
        statics.encoding = args.encode
    else:
        loginfo('URI/Body [space] encoding is disabled by default')

    if args.full_encode is True:
        loginfo('URI/Body full encoding is enabled by the user')
        statics.fullencoding = args.full_encode
    else:
        loginfo('URI/Body full encoding is disabled by default')

    if args.output != "" and args.output is not None:
        if args.output == "terminal":
            loginfo('Output [terminal] is enabled by the user')
        elif path.isdir(args.output):
            loginfo('Output [folder] is enabled by the user')
            statics.outputFile = args.output + '/' + getcurrenttime() + '_outputs.txt'
        else:
            logwarn('Output [folder] is not found')
            mkdir(args.output)
            loginfo('Output [folder] is created')
            statics.outputFile = args.output + '/' + getcurrenttime() + '_outputs.txt'
            loginfo('Output [folder] is enabled by the user')
        statics.outputting = True
        statics.output     = args.output
    else:
        loginfo('Output is disabled by default')

    if args.output_details != "" and args.output_details is not None:
        if args.output_details == "terminal":
            loginfo('Output details [terminal] are enabled by the user')
        elif path.isdir(args.output_details):
            loginfo('Output details [folder] are enabled by the user')
            statics.outputReqdetail = args.output_details + '/' + getcurrenttime() + '_detailed_requests.txt'
            statics.outputResdetail = args.output_details + '/' + getcurrenttime() + '_detailed_responses.txt'
        else:
            logwarn('Output detail [folder] is not found')
            mkdir(args.output_details)
            loginfo('Output details [folder] are created')
            statics.outputReqdetail = args.output_details + '/' + getcurrenttime() + '_detailed_requests.txt'
            statics.outputResdetail = args.output_details + '/' + getcurrenttime() + '_detailed_responses.txt'
            loginfo('Output details [folder] are enabled by the user')
        statics.outputdetails   = True
        statics.output_details  = args.output_details
    else:
        loginfo('Output details are disabled by default')

    if args.fuzz is True:
        loginfo('Fuzzing module enabled by the user')
        statics.fuzzing = args.fuzz
        if args.delay is not None:
            loginfo('Fuzzing module delay sets "' + str(args.delay) + '" by the user')
            try:
                statics.reqdelay = int(args.delay)
            except:
                statics.reqdelay = float(args.delay)
        else:
            loginfo('Fuzzing module delay sets "0.05" by default')
    else:
        loginfo('Fuzzing module disabled by default')

    if args.manipulate is True:
        loginfo('Manipulating Headers module enabled by the user')
        statics.headers = args.manipulate
        if args.delay is not None:
            loginfo('Manipulating Headers module delay sets "' + str(args.delay) + '" by the user')
            try:
                statics.reqdelay = int(args.delay)
            except:
                statics.reqdelay = float(args.delay)
        else:
            loginfo('Manipulating Headers module delay sets "0.05" by default')
    else:
        loginfo('Manipulating Headers module disabled by default')

    if args.charfuzz is True:
        loginfo('Char Fuzzing module enabled by the user')
        statics.charfuzzing = args.charfuzz
        if args.delay is not None:
            loginfo('Char Fuzzing module delay sets "' + str(args.delay) + '" by the user')
            try:
                statics.reqdelay = int(args.delay)
            except:
                statics.reqdelay = float(args.delay)
        else:
            loginfo('Char Fuzzing module delay sets "0.05" by default')
    else:
        loginfo('Char Fuzzing module disabled by default')

    reqFile = open(reqfile, 'r')
    reqlist = reqFile.readlines()
    reqFile.close()

    if args.threads != "" and args.threads is not None:
        loginfo('Multi-threading [' + str(args.threads) + '] enabled by the user')
    else:
        args.threads = 1
        loginfo('Multi-threading disabled by default')

    for th in range(0, args.threads):
        loginfo('Sender module is starting')
        senderth = Thread(name='thread_'+str(th), target=sender)
        senderth.start()
        statics.threadList.append(senderth)

    loginfo('Parser module is starting')
    parseth = Thread(target=parseheaders, args=(reqlist,), )
    parseth.start()
    parseth.join()

    if statics.fuzzing is True:
        loginfo('Fuzzing module is starting')
        fuzzth = Thread(target=fuzzmain, )
        fuzzth.start()
        fuzzth.join()

    elif statics.charfuzzing is True:
        loginfo('Char Fuzzing module is starting')
        charfuzzth = Thread(target=charfuzzmain, )
        charfuzzth.start()
        charfuzzth.join()

    elif statics.headers is True:
        loginfo('Manipulating Headers module is starting')
        manheadersth = Thread(target=modifyheader, )
        manheadersth.start()
        manheadersth.join()

    else:
        print('No module selected by the user!')
        logwarn('No module selected by the user')
        statics.exitCall = True

    livecnt = 0
    while True:
        if statics.senderQ.qsize() == 0 and statics.exitCall is True:
            for th in statics.threadList:
                if th.is_alive():
                    th.join(1)
                livecnt += 1
        if livecnt == len(statics.threadList):
            break


if args.help is True:
    tool_exit_message()
    exit()

statics.logging = args.log
basicConfig(filename='logs/logfile.log', level=INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logstart()

engine = Process(target=starts, )
engine.start()
try:
    while True:
        sleep(2)
        if statics.senderQ.qsize() == 0:
            engine.join(timeout=2)
            break
except KeyboardInterrupt:
    logwarn('The process killed by the user')
    print('[WARNING]The process killed by the user!')
finally:
    try:
        engine.kill()
    except:
        engine.terminate()
    sleep(0.05)
    logstop()
