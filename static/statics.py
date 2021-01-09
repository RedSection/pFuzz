from queue                    import PriorityQueue
from multiprocessing.managers import SyncManager


class MyManager(SyncManager):
    pass


def Manager():
    m = MyManager()
    m.start()
    return m


# Statics
headerFile      = 'static/headers'
methodFile      = 'static/methods'
excelFile       = 'static/waf_bypass_db.xlsx'
proxy           = ''
output          = ''
outputFile      = ''
outputdetail    = ''
outputReqdetail = ''
outputResdetail = ''
outputFlag      = 1
tmpproxyData    = ''
threadList      = []
responses       = []
parseKey        = "#pFuzz#"
# System variables
exitCall        = False
encoding        = False
fullencoding    = False
# Modules
outputdetails   = False
outputting      = False
logging         = False
usessl          = False
fuzzing         = False
charfuzzing     = False
headers         = False
genericcolmnName = 'Payload'
reqdelay        = 0.05
# Fuzzing Module
fuzzsheetName   = 'Fuzzing'
fuzzingpayloads = []
charfuzzsheetName   = 'CharFuzzing'
charfuzzingpayloads = []
# Modifying Headers Module
headersheetName = 'Headers'
typeccolmnName  = 'Type'
headerspayloads = []
# Sender Module
MyManager.register("PriorityQueue", PriorityQueue)
m         = Manager()
senderQ   = m.PriorityQueue(maxsize=15000)