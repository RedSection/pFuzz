from argparse import ArgumentParser

parser = ArgumentParser(add_help=False)
parser.add_argument('--help',    '-h',  help='show this help message and exit', action='store_true'           )
parser.add_argument('--proxy',   '-p',  help='proxy [IP:PORT]'                                                )
parser.add_argument('--log',     '-l',  help='enable logging',    action='store_true'                         )
parser.add_argument('--ssl',     '-s',  help='enable ssl',        action='store_true'                         )
parser.add_argument('--threads', '-t',  help='thread(s) number [default=1]', type=int                         )
request_opts = parser.add_argument_group('[Requests Options]'                                                 )
request_opts.add_argument('--request',      '-r',  help='request file',                                       )
request_opts.add_argument('--delay',        '-d',  help="set a delay between requests [default=0.05]"         )
request_opts.add_argument('--encode',       '-e',  help="encode space chars in uri/body",  action='store_true')
request_opts.add_argument('--full-encode',  '-fe', help="encode all chars in uri/body"  ,  action='store_true')
output_opts = parser.add_argument_group('[Output Options]'                                                    )
output_opts.add_argument('--output',         '-o' , help='output type [terminal/folder name]'                 )
output_opts.add_argument('--output-details', '-od', help='outputting more details [terminal/folder name]'     )
modules = parser.add_argument_group('[Modules]'                                                               )
modules.add_argument('--fuzz',        '-f',  help="run fuzzing module", action='store_true'                   )
modules.add_argument('--charfuzz',    '-cf', help="run char fuzzing module", action='store_true'              )
modules.add_argument('--manipulate',  '-m',  help="run manipulating headers module", action='store_true'      )
parser.add_argument('--version', '-v', action='version',  version='pFuzz Advanced Fuzzing Tool v0.2.4\n\
                                                                 @EmreOvunc\n\
                                                                 @merttasci\n\
                                                                 @xsuperbug'                                  )
parser.epilog = "Usage: python3 pfuzz.py -r req.txt -l -s -p 127.0.0.1:8080 --fuzz -e --delay 0.5 -o terminal"

args = parser.parse_args()
