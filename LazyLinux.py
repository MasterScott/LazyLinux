from os import system
from time import sleep
def choose:
   print "Select An Option:"
   print "1. Spoof/Spam Email"
option = input(">")
while option != 1:
  print"INVALID OPTION"
  choose()
 if option == 1:
   print "You need a STMP server. \n If you don't have one, I suggest STMP2GO.com\n\n\n"
   
