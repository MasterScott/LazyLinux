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
   os.system('apt-get install sendemail -y')
   print "You need a STMP server. \n If you don't have one, I suggest STMP2GO.com\n\n\n"
   print ('If you want to set any of these variables as default, edit the code in "LazyLinux.py"')
   sleep(3)
   stmpserver = raw_input("stmp server(example:stmp.stmp2go.com): ")
   stmppass = raw_input("stmp server password: ")
   spoof = raw_input ("Send From(Can be false): ")
   sendto = raw_input("Victim: ")
   sub = raw_input("Subject: ")
   mes = raw_input("Message: ")
   os.system('sendemail -f '+spoof+' -t '+sendto+' -s '+sub+' -m '+mes+'
