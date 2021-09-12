import os
import sys
import datetime
import time

#Colours choosen by amlike
R = '\033[31m' #Red
Y = '\033[93m' #yellow
G = '\033[92m'  #green
rset = '\033[0m'  #clear
B = '\033[1;34m' #Blue
cyan = '\033[96m' #cyan
cy='\033[095m'  #cy
cya='\033[035m' #cya
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
cy='\033[095m'
cya='\033[035m'
# bak

led = "\033[1;32;41m"
bla ="\033[1;32;40m"
under = "\033[2;32;0m"


rows,columns=os.popen('stty size', 'r').read().split()
Colms =  int ((int (columns) + 16) / 2)
c = " " * Colms
cc = " " * (Colms-8)
hline = '#'*int(columns)

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.06)

os.system ("clear")
time.sleep(2)

#subprocess.call ('clear')
#introduction

os.system ("apt update && apt upgrade && apt install play-audio && pkg install play-audio && apt install wget && pkg install wget && apt install figlet && pkg install figlet && apt install python3 && pkg install python3 && apt install python")


os.system ("clear")

time.sleep(1)

print ()
delay_print(green+"T H I S   T O O L   I S   F O R    E D U C A T I O N A L    P U R P O S E S   O N L Y    I F   Y O U    M I S S    U S E   I T   D E V E L O P E R   I S   N O T    R E S P O N S I B L E    F O R   Y O U R   C O M M I T!!!!")
os.system ("play-audio .onyo.mp3")
      
time.sleep(2)
print("")
print("")

os.system ("mv .run.py run.py")

delay_print(B+"DO YOU WANT TO CONTINUE???")
delay_print(R+"\tY/N")
for i in range (5):
    co = input(" :")
    if co == "Y":
               os.system("clear")
               time.sleep(1)
               os.system ("python3 run.py")
                          
    elif co == "yes":
               os.system("clear")
               time.sleep(1)
               os.system ("python3 run.py")
    elif co == "y":
               os.system("clear")
               time.sleep(1)
               os.system ("python3 run.py")
    else:
              os.system("clear")
              time.sleep(1)
              os.system("figlet BYE 👍👋")
              print("")
              print(yellow+"TOOL INAENDA KU EXIT MAANA UMECHAGUA KU EXIT OR UMEENDIKA CHAGUO LISILO SASAHIH SO BYEEEE!!!!👍👋")
              print("")
              sys.exit(1)
