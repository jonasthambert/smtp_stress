#!/usr/bin/env python2.7
#
# SMTP and email stress testing tool
# Jonas Thambert
#
# 

import smtplib
import threading

def prompt(prompt):
    return raw_input(prompt).strip()

def print_logo():
    print '...................................'
    print '.                                 .'
    print '.          SMTP stresser          .'
    print '.     with threading support      .'
    print '.        by Jonas Thambert        .'
    print '.                                 .'
    print '...................................'

def send_email(fromaddr, toaddr, relay, msg):
 try:
   server = smtplib.SMTP(relay)
   server.sendmail(fromaddr, toaddr, msg)
   server.quit()
 except Exception, error:
   print "Unable to send e-mail: '%s'." % str(error)
 
# void main() {printf "hello world";};
def main():

# Print logo
 print_logo()

# Take input from CLI
 fromaddr = prompt("From: ")
 toaddr  = prompt("To: ").split()
 subject = prompt("Subject: ")
 numbs = int(prompt("Number of emails to send: "))
 relay = prompt("SMTP server to use: ")
 stress = prompt("Use threading to stress server [y/n]: ")
 print "Enter message, end with ^D (Unix) or ^Z (Windows):"

# Create the msg and add headers
 msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % (fromaddr, ", ".join(toaddr), subject))

# Email body
 while 1:
    try:
        line = raw_input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

# Print whats going to be done
 print "Message length is " + repr(len(msg))
 print ("Numbers of emails to send: %d" % (numbs))

# Let's start sending some emails..
 threads = []
 count = 0
 while (numbs > 0):
   numbs = numbs - 1
   count = count + 1 
   print ("Sending Email Number: %d" % (count))
   if stress == "y":
    t = threading.Thread(target=send_email, args=(fromaddr, toaddr, relay, msg,))
    threads.append(t)
    t.start()
   else:
    send_email(fromaddr, toaddr, relay, msg)

# Print last output to terminal
 if stress == "y":
  print "All threads spawned, lets wait until they finish and we get prompt back..."
 else:
  print "done.."

if __name__=='__main__':
	main()
