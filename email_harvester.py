import os

domain = input("Enter a domain: ")

cmd = 'theharvester -d ' + domain + ' -b pgp'
os.system(cmd)