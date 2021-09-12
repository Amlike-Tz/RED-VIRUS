import os
import sys
import subprocess
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
#48 black 47 white 46 cyan 45 pink 44 blue 43 njano  42 kijani
white = "\033[1;32;47m"
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

subprocess.call ('clear')
#introduction
time.sleep (2)
#print (G+hline)
print (R+"\t           x        x")
print (R+"\t             x "+R+ "■■ " +R+"x")
print (R+"\t             ■■■■■■")
print (R+"\t            ■■"+R+"▣"+R+"■■"+R+"▣"+R+"■■")
print (R+"\t           ■■■■■■■■■■")
print (R+"\t        ■■ ■■■■■■■■■■ ■■")
print (R+"\t      ■■■■ ■■■■■■■■■■ ■■■■")
print (R+"\t        ■■ ■■■■■■■■■■ ■■")
print (R+"\t           ■■■■■■■■■■")
print (R +"\t             ■■  ■■")
print (R+"\t             ■■  ■■")
print (yellow+"      "+R+"["+yellow+"Developer"+R+"]"+"  "+green+"  ➡➡➡➡➡➡"+yellow+"\t"+R+"["+yellow+"Amlike-Tz"+R+"]"+cyan+"")
#print (G+hline+cyan)
print (R+"\t        "+white+led+"  ||RED-VIRUS||   "+bla+"")
print (R+"\t        "+"      A.K.A   ")
print (R+"\t        "+white+"    ||Bad-Boys||  "+bla+"")
print ()
