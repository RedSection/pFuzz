## What is pFuzz / pFuzz Nedir :question:

pFuzz is an advanced red teaming fuzzing tool which we developed for our research. It helps us to bypass web application firewall by using different methods at the same time.

pFuzz web uygulama araştırmaları için geliştirdiğimiz, gelişmiş bir fuzzing aracıdır. Farklı güvenlik uygulamaları üzerinde çeşitli saldırı yöntemlerinin denenmesi konusunda süreci hızlandırmak için geliştirilmiştir. 

## Description [EN]
pFuzz is a tool developed in the python language to have advanced fuzzing capability in web application research. Since the application has a modular structure, it has the ability to quickly add new found / to be found WAF bypassing methods to pFuzz and test it on all other WAFs. In addition to a modular structure, multi-threading, multi-processing and queue structures have been used to make the tool more flexible and the infrastructure has been created for future developments.

The tool is programmed so that a given request can be parsed and easily changed over an object. Thanks to this structure, those who will develop the application will be able to contribute easily and develop the tool in line with their own needs without changing the core structure of the application without having to learn.

---

**Note**: If you want to contribute to the development, you can do it not only developing pFuzz but also adding new modules.
Feel free to open new PR :)

---

## Açıklama [TR]
pFuzz, web uygulama araştırmalarında ileri düzey fuzzing kabiliyetine sahip olabilmek için python dilinde geliştirilmiş bir araçtır. Uygulama modüler bir yapıya sahip olduğu için yeni bulunan/bulunacak WAF atlatma yöntemlerinin pFuzz'a hızlıca eklenerek diğer tüm WAF’lar üzerinde de test edebilme yeteneğine sahiptir. Modüler bir yapının yanında, multi-threading, multi-processing, queue gibi yapılar kullanılarak aracın daha esnek bir yapıda olması sağlanmış ve ilerde yapılabilecek olan geliştirmeler için alt yapısı oluşturulmuştur.

Uygulama, verilen bir isteğin ayrıştırılarak bir nesne üzerinden kolaylıkla değiştirilebilmesi üzerine programlanmıştır. Bu yapı sayesinde uygulamayı geliştirecek kişiler uygulamanın çekirdek yapısını değiştirmeden ve öğrenmek zorunda kalmadan kolaylıkla katkıda bulunabilecek ve kendi ihtiyaçları doğrultusunda uygulamayı geliştirebilecektir.

---

**Not**: Geliştirme konusunda katkı yapmak istiyorsanız, bunu sadece çekirdek 'core' geliştirme olarak değil, aynı zamanda yeni modül ekleyerek de yapabilirsiniz.
Yeni PR'larınızı bekliyoruz :)

---


```
        _____                 
 _ __  |  ___|_   _  ____ ____
| '_ \ | |_  | | | ||_  /|_  /
| |_) ||  _| | |_| | / /  / / 
| .__/ |_|    \__,_|/___|/___|
|_|                           
```



## Developers :information_desk_person:
<table>
  <tr>
    <td align="center"><a href="https://emreovunc.com/"><img src="https://avatars.githubusercontent.com/u/15659223?v=3" width="100px;" alt=""/><br /><sub><b>Emre Övünç</b></sub></a><br/>
    <td align="center"><a href="https://mert.ninja/"><img src="https://avatars.githubusercontent.com/u/6993255?v=3" width="100px;" alt=""/><br /><sub><b>Mert Taşçı</b></sub></a><br/>
    <td align="center"><a href="https://evren.ninja/"><img src="https://avatars.githubusercontent.com/u/7601737?v=3" width="100px;" alt=""/><br /><sub><b>Evren Yalçın</b></sub></a><br/>
 </tr>
</table>

 
## Flow :clipboard:
 
 ![pFuzz](https://emreovunc.com/projects/pFuzz.png)
 

## Installation and Usage :books:
```
sudo pip3 install virtualenv
python3 -m venv myvenv
source myvenv/bin/activate
pip3 install -r requirements.txt
python3 pfuzz.py --help
```
#### Dependencies:
```
cffi==1.14.3
cryptography==3.1.1
numpy==1.19.2
pandas==1.1.3
pycparser==2.20
pyOpenSSL==19.1.0
python-dateutil==2.8.1
pytz==2020.1
six==1.15.0
xlrd==1.2.0
```
#### Usage
   - **Help**
   ```
   python3 pfuzz.py --help
   ```
   - **Manipulating Headers Module**
   ```
   python3 pfuzz.py -r request.txt -m
   ```
   - **Charfuzzing Module**
   ```
   python3 pfuzz.py -r request.txt -cf
   ```
   - **Fuzzing Module**
   ```
   python3 pfuzz.py -r request.txt -f
   ```
   - **Add proxy**
   ```
   python3 pfuzz.py -r request.txt -f --proxy 127.0.0.1:8080
   ```
   - **Add a delay between requests**
   ```
   python3 pfuzz.py -r request.txt -f -d 3
   ```
   - **Enable TLS/SSL connection**
   ```
   python3 pfuzz.py -r request.txt -f -s
   ``` 
   - **Enable logging**
   ```
   python3 pfuzz.py -r request.txt -f -l
   ```
   - **Enable payload encoding/full-encoding function**
   ```
   python3 pfuzz.py -r request.txt -f -e
   ```
   ```
   python3 pfuzz.py -r request.txt -f -fe
   ```
   - **Set multi-threads**
   ```
   python3 pfuzz.py -r request.txt -f -t 5
   ```
   - **Output to the terminal**
   ```
   python3 pfuzz.py -r request.txt -f -o terminal
   ```
   ```
   python3 pfuzz.py -r request.txt -f -od terminal
   ```
   - **Output to a file**
   ```
   python3 pfuzz.py -r request.txt -f -o ~/Desktop/
   ```
   ```
   python3 pfuzz.py -r request.txt -f -od ~/tmp/
   ```

## Help :computer:
```
              _____                 
       _ __  |  ___|_   _  ____ ____
      | '_ \ | |_  | | | ||_  /|_  /
      | |_) ||  _| | |_| | / /  / / 
      | .__/ |_|    \__,_|/___|/___|
      |_|
   ------------------------------------
   @EmreOvunc | @merttasci | @xsuperbug
   ------------------------------------
                 v0.2.4
   ------------------------------------

usage: pfuzz.py [-h] [--request REQUEST] [--proxy PROXY] [--log] [--ssl]
                 [--threads THREADS] [--output OUTPUT] [--delay TIME] 
                 [--output-details OUTPUT] [--full-encode] [--encode]
                 [--fuzz] [--charfuzz] [--manipulate] [--version]

optional arguments:
  --help/-h             show this help message and exit
  --proxy/-p    PROXY   proxy [IP:PORT]
  --log/-l              enable logging
  --ssl/-s              enable ssl
  --threads/-t  NUMBER  thread(s) number [default=1]
  --version/-v          show program's version number and exit
  
[Request Options]:  
  --request/-r  REQUEST request file
  --delay/-d    TIME    set a delay between requests [default=0.05]
  --encode/-e           encode space chars in uri/body
  --full-encode/-fe     encode all chars in uri/body
  
[Output Options]:
  --output/-o   OUTPUT  output important info [terminal/folder name]
  --output-details/-od OUTPUT
                        output all details [terminal/folder name]
                        
[Modules]:
  --fuzz/-f             run fuzzing module
  --charfuzz/-cf        run char fuzzing module
  --manipulate/-m       run manipulating headers module

Usage: python3 pfuzz.py -r req.txt --log -s --fuzz -d 1 --encode -o terminal --threads 2
Usage: python3 pfuzz.py -r req.txt -f -l --proxy 127.0.0.1:8080 --output-details ~/output
```


## Extras :loudspeaker:
#### How to Develop a New Module
- A python file that specifies the name of the module should be created inside **modules/** folder.
```
- modules
        - charfuzzer.py
        - exparse.py
        - fuzzer.py
        - headeroperations.py
        - manupilatingheaders.py
```
- You can use the parsed object like **myreq  = HTTPReq.getobj()**
```
from reqparser import HTTPReq
myreq  = HTTPReq.getobj()
```
  - It has many attributes derivated from **HTTPReq** class. You can them it in **reqparser.py.**
  ```
  ...
  myreq.uri
  myreq.body
  myreq.http
  myreq.referer
  myreq.origin
  myreq.host
  myreq.cookie
  ...
  ```
- If you want to get your payloads from the excel, you can use **getpayloads** methods coming from modules.exparse.

  - getpayloads(fuzzsheetName, genericcolmnName, fuzzingpayloads)
  ```
  from modules.exparse import getpayloads
  getpayloads(fuzzsheetName, genericcolmnName, fuzzingpayloads)
  ```

  - We set statics-objects like fuzzsheetName in statics.py that is under **static/** folder.
  ```
  # Fuzzing Module in static/statics.py
  fuzzsheetName   = 'Fuzzing'
  genericcolmnName = 'Payload'
  fuzzingpayloads = []
  ```
- Now, you can change/add/delete attributes whatever you want.
```
myreq.uri = tmpuri + payload
myreq.addheader(header, "127.0.0.1")
myreq.content_type = "text/html"
```
- To stop multi-threading, you should add **#exitme#** payload to the end of your payloads and set **statics.exitCall = True** to check whether queue is empty or not.
```
from modules.exparse import getpayloads
for payload in fuzzingpayloads:
if payload == '#exitme#':
    statics.exitCall = True
else:
    [OPERATIONS]
```

- When your object(request) is ready to be sent, you can use **sendit()** function to queue it.
```
from reqsender import sendit
sendit(myreq)
```
- If you need to change core functions in pFuzz, you can start a pull request or open an issue.

---

#### Some Important Functions to Develop New Modules
| Aim                                | Module/Class        | Function                    | Parameter(s)             |
| -------------                      |-------------        | -------------               | -------------            |
| To send a request                  |reqsender.py         | sendit()                    | object                   |
| To use a request object            |reqparser.py/HTTPReq | getobj()                    |     -                    |
| To add a custom header             |reqparser.py/HTTPReq | OBJECT.addheader()          | newHeadername,value      |
| To delete a header                 |reqparser.py/HTTPReq | OBJECT.delheader()          | headerName               |
| To change a header                 |reqparser.py/HTTPReq | OBJECT.changeheader()       |  headerName,newHeaderName |
| To get a payload from the file     |exparse.py           | getpayloads()               | sheetName,columnName     |
| To write a log info/debug/warning  |waflogger.py         | loginfo/logdebug/logwarn()  | logMessage               |

---

### What WAFs did we bypass?
- FortiWeb
- Cloudflare
- Sucuri
- Akamai
- Imperva
- F5 WAF
