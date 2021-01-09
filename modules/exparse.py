from pandas         import ExcelFile
from waflogger      import loginfo
from static.statics import excelFile


def excelfile():
    try:
        excel = ExcelFile(excelFile)
        return excel
    except:
        loginfo('[-] ' + str(excelFile) + ' file could not found')


def getpayloads(sheetName, columnName, arr):
    exc = excelfile()
    try:
        sheet = exc.parse(sheetName)
        try:
            for data in sheet[columnName]:
                arr.append(data)
        except:
            loginfo('[-] ' + str(columnName) + ' could not found')
    except:
         loginfo('[-] ' + str(sheetName) + ' could not found')
