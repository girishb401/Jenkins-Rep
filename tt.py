from tabulate import tabulate
from netmiko import ConnectHandler
import time
# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
from prettytable import PrettyTable

F5_LTM = {
    'device_type': 'f5_ltm',
    'ip':   '10.1.0.2',
    'username': 'root',
    'password': 'default',
    'port' : '22'         # optional, defaults to 22
   }

net_connect = ConnectHandler(**F5_LTM)

#output = net_connect.find_prompt()

#o1=net_connect.config_mode() 

#output2 = net_connect.send_command("tmsh \n")
#print (" Collecting F5 Version ")
o12 = str("=============================F5 LTM Version=============================")
output12 = net_connect.send_command(' show sys version')

int0 = output12.index('12.')
Vr = (output12[int0: int0 + 8])
str1= str("F5 LTM Version")
#print str1+Vr

#print ( "Collecting F5 Hardware ")

o1234 = str("=============================F5 LTM Hardware=============================")
output1234 = net_connect.send_command('  show sys license  ')
int1 = output1234.index('Registration')
#print outp
str2= str("F5 Chassis SN ")
hw = (output1234[int1: int1+50])
#print hw

#print ( "Collecting F5 time")
o123 = str("=============================F5 LTM clock=============================")
output123 = net_connect.send_command(' show sys clock ')
str3= str("F5 clock")
int2 = output123.find('Sun')
#print outp
clk = (output123[int2: int2 + 90])
print clk

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("f5.bgmka@gmail.com", "gsyfojpjkvrqqmhl")
 
# message to be sent
message = ("This is an auto-genarated mail from Girish's Python Lab")

#subject = "A"

Print_table = tabulate([[str2, hw],[str1, Vr],[str3,clk]],headers=['Iteams', '\t deatils'],tablefmt='orgtbl')
#rint Print_table + "\n\n\n"

t = PrettyTable(['Iteams', 'Details'])
t.add_row([str1,Vr])
t.add_row([str2, hw])
t.add_row([str3, clk])
#rint t

from texttable import Texttable
t = Texttable()
t.add_rows([['Iteams', 'Details'], [str1, Vr], [str2, hw],[str3, clk]])
po= t.draw()

print po


#otabody=(Print_table + t)

print ("sending the mail")

BODY = '\r\n'.join(["From: user_me@gmail.com",
       "To: f5.bgmka@gmail.com",
      "Subject: AUTO GENARATED MAIL",
       '', message+ "\n\n" + po])
	   
	  # message+ "\n\n" +"\n\n" + o12 +"\n " + output12 + "\n\n\n"+ o1234+ "\n"+ output1234 + "\n\n" + o123 + "\n\n" + "\n" + "\n\n" ])
	   
s.sendmail("f5.bgmka@gmail.com", "f5.bgmka@gmail.com", BODY)
 

print ('Mail sent successfully')
# terminating the session
s.quit()

