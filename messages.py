def tool_exit_message():
    print(
"""
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
"""
)


def filenotfound(file):
    print('[ERROR] <' + file + '> file not found!')
