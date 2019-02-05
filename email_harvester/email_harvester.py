import sys
import os, getopt
import subprocess
import re

def main(argv):
	domain = ''
	provider = ''

	try:
		opts, args = getopt.getopt(argv,"hd:p:",["domain=","provider="])
	except getopt.GetoptError:
		print ('test.py -d <domain> -p <provider>')
		print ('If you only input a domain, the program well check all the following sources:')
		print ("baidu, bing, bingapi, dogpile, google, googleCSE, googleplus, google-profiles, linkedin, pgp, twitter, vhost, virustotal, threatcrowd, crtsh, netcraft, yahoo")
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print ('test.py -d <domain> -p <provider>')
			sys.exit()
		elif opt in ("-d", "--domain"):
			domain = arg
		elif opt in ("-p", "--provider"):
			provider = arg
	
	if provider is '':
		one(domain)
	else:
		two(domain, provider)


def two(domain, provider):
	print('Domain:', domain)
	print('Provider:', provider)

	cmd = '/usr/bin/theharvester -d ' + domain + ' -b ' + provider

	print("SEARCHING...")

	with open("./outfile.txt", "wb", 0) as out:
		subprocess.run([cmd], stdout=out, check=True, shell=True)


def one(domain):
	print(domain)

	cmd = '/usr/bin/theharvester -d ' + domain + ' -b all'

	print("SEARCHING...")

	with open("./outfile.txt", "wb", 0) as out:
		subprocess.run([cmd], stdout=out, check=True, shell=True)

if __name__ == "__main__":
	main(sys.argv[1:])
