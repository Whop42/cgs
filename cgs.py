import requests
from colorama import init
from colorama import Fore
import urllib3
import sys

init()

APP_VERSION = "0.2.1"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def request_info(inst, pop_num, password, verification):
    load_student_headers = {
        #"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "User-Agent": "YourMom/69.420 (Michealsoft Binbows TN 12.993; Win64; x64; rv:1.1) MichealsoftLedge/1100110011",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://cgslab.com/genetics/index.html?22328",
        "DNT": "1",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }
    return requests.get(
                        "https://www.cgslab.com/c/loadPopulation.cgi?verif5322=" + str(verification) + "&stuPasswd=" + str(password) + "&inst=" + str(inst) + "&popNum=" + str(pop_num),
                        verify = False,
                        headers = load_student_headers)

def parse_info(content):
    print("\n##############################\n\ncontent:")
    for i in content:
        if "Cross:" in i:
            content.remove(i)

    content_values = []
    extras = []
    for i in content:
        content_values.append(i.split("=")[1])

    output = [
        ["Population Name: ", content_values[2]],
        ["Easy Mode: ", content_values[9]],
        ["Organism: ", content_values[4]]
    ]

    for i in content:
        if "t1m=" in i:
            output.append(["Trait 1 Mode: ", i.split("=")[1]])
        elif "t1n=" in i:
            output.append(["Trait 1 Name: ", i.split("=")[1]])
        elif "t1d=" in i:
            output.append(["Trait 1 Dominant: ", i.split("=")[1]])
        elif "t1h=" in i:
            output.append(["Trait 1 Heterozygous: ", i.split("=")[1]])
        elif "t1r=" in i:
            output.append(["Trait 1 Recessive: ", i.split("=")[1]])
        elif "t1n=" in i:
            output.append(["Trait 1 Name: ", i.split("=")[1]])
        elif "li=" in i:
            output.append(["???: ", i.split("=")[1]])
        elif "t2m=" in i:
            output.append(["Trait 2 Mode: ", i.split("=")[1]])
        elif "t2n=" in i:
            output.append(["Trait 2 Name: ", i.split("=")[1]])
        elif "t2d=" in i:
            output.append(["Trait 2 Dominant: ", i.split("=")[1]])
        elif "t2h=" in i:
            output.append(["Trait 2 Heterozygous: ", i.split("=")[1]])
        elif "t2r=" in i:
            output.append(["Trait 2 Recessive: ", i.split("=")[1]])
        elif "t2n=" in i:
            output.append(["Trait 2 Name: ", i.split("=")[1]])
        elif "t3m=" in i:
            output.append(["Trait 3 Mode: ", i.split("=")[1]])
        elif "t3n=" in i:
            output.append(["Trait 3 Name: ", i.split("=")[1]])
        elif "t3d=" in i:
            output.append(["Trait 3 Dominant: ", i.split("=")[1]])
        elif "t3h=" in i:
            output.append(["Trait 3 Heterozygous: ", i.split("=")[1]])
        elif "t3r=" in i:
            output.append(["Trait 3 Recessive: ", i.split("=")[1]])

    for i in output:
        print("    " + i[0] + i[1])

print("\n##############################\n    cgs_breaker [" + APP_VERSION + "]")
print("for educational purposes only\n##############################\n")
# detect auto mode
if "--auto" in sys.argv or "-a" in sys.argv:
    args = sys.argv[2]
    print("\nargs: " + args)
    args = args.split(":")
    print(parse_info(str(request_info(args[0], args[1], args[2], args[3]).content).split("&")))
elif "--help" in sys.argv or "-h" in sys.argv:
    print("""
          breaker mode:
              1. find your verification # and inst
              code (if you know what you are doing,
              this should be easy) ex. ver123 or ver626
              2. open cgs
              3. go to the population you want to use
              4. start this script, enter info
              4a. if you get an error, most likely your
                  info was bad
              5. profit
          
          help:
            shows this page
        
          educational purposes only, i am not responsible
          for any bad things you do with this, nor do i
          condone them in any way. 
          DO NOT USE THIS TO CHEAT.
          """)
else:
    # ask for creds and get info, print it
    print(parse_info(str(request_info(input("inst code: "), input("pop num: "), input("password: "), input("verification # (ex. ver123): ")).content).split("&")))

print("\n##############################")
