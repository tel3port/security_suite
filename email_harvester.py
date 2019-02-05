import sys
import os
import subprocess
import re

print('Argument One:', sys.argv[1])
print('Argument Two:', sys.argv[2])

domain = sys.argv[1]
provider = sys.argv[2]

"""
os.system(cmd)
"""

cmd = '/usr/bin/theharvester -d ' + domain + ' -b ' + provider

with open("./email_harvester/outfile.txt", "wb", 0) as out:
	subprocess.run([cmd], stdout=out, check=True, shell=True)

    