import sys
import urllib.request
import re

REVVY_FTP = ['alftp', 
'apache', 
'cerberus', 
'complete', 
'crush ftp', 
'eft ftp', 
'free ftp', 
'glftp', 
'IIS', 
'muddle ftpd', 
'pro ftp', 
'public file ftp', 
'pure ftp', 
'raiden ftp', 
'slim ftp', 
'vsftp', 
'wu ftp']

ALL_FTP = '''
##FTP##
ALFTP
Apache FTP 
Cerberus FTP
Complete FTP
CrushFTP
EFT Server
glFTP
IIS
Muddle FTP
Pro FTP
Publicfile
Pure FTP
Raiden FTP
Slim FTP
vsFTP (Very Secure)
Wu FTP
'''

#ALL_SSH = '''
##SSH##
#Cop SSH
#Dropbear
#GoAnywhere Services
#LSH
#OpenSSH
#Pragma Fortress SSH
#Tectia SSh
#WinSSH
#'''

REV_ASCII = '''
    ____                       
   / __ \___ _   ___   ____  __
  / /_/ / _ \ | / / | / / / / /
 / _, _/  __/ |/ /| |/ / /_/ / 
/_/ |_|\___/|___/ |___/\__, /  
                      /____/ 
'''


def fetch_and_find(page, prefix, shift, length):
	page = urllib.request.urlopen(page)
	text = page.read().decode("utf8")
	where = text.find(prefix)
	start = where + shift
	end = start + length
	return(text[start:end])





if len(sys.argv) == 1:
		print('''Revvy. A revision number parser
Usage: ./revvy.py [OPTIONS]...<ARGUMENT>...

  -h, --help			show help
  -l, --list <SERVICE>	list specified service software (eg ./revvy.py -L ftp)
  -s, --search <NAME>	search software by name			
  -a, --all 			show all available service and revision numbers
  -r, --ascii 			print fantastic Revvy ASCII art
  -v, --version			show version
''')

		sys.exit()

if sys.argv[1].startswith('-'):
	option = sys.argv[1][1:]
	# fetch sys.argv[1] but without the first two characters
	if option == 'v':
		print('''#============================================================
#
#          FILE:  revvy
#
#         USAGE:  ./revvy [OPTIONS]...<ARGUMENT>...
#
#   DESCRIPTION:  
#
#       OPTIONS:  ---
#  REQUIREMENTS:  Python 3.x
#          BUGS:  Still in POC Testing.
#         NOTES:  Development of this tool is still in progress.
#        AUTHOR:  Pekk0, AWB
#       COMPANY:  ---
#       VERSION:  0.10a
#       CREATED:  1/27/12 01:42:08 PST
#      REVISION:  ---
#============================================================
''')
		sys.exit()
	elif option == 'h':
		print('''Revvy. A revision number parser
Usage: ./revvy.py [OPTIONS]...<ARGUMENT>...

  -h, --help			show help
  -l, --list <SERVICE>	list specified service software (eg ./revvy.py -l ftp)
  -s, --search <NAME>	search software by name			
  -a, --all 			show all available service and revision numbers
  -r, --ascii 			print fantastic Revvy ASCII art
  -v, --version			show version
''')
		sys.exit()
	elif option == 'r':
		print(REV_ASCII)
		sys.exit()
	elif option == 'a':
		print(ALL_FTP)
		sys.exit()
	elif option == 'l':
		try:
			option = sys.argv[1][1:]
			if sys.argv[2] == 'ftp':
				print(ALL_FTP)
			else:
				print("Revvy does not have revision numbers for %s yet." %sys.argv[2])
				sys.exit()
		except IndexError:
			print('Error: You need to specify what kind of software (SSH, FTP...')
			sys.exit()

	elif option == 's' or '-search':
		option = sys.argv[2:]
		#while len(sys.argv[2]) >= 0: 
		#	print("No software selected.")
		#	sys.exit()
		for i in REVVY_FTP:
			low_search = sys.argv[2].lower()
			revision = "Current revision for"
			if low_search == 'alftp' :
				print(revision, "ALFTP is", fetch_and_find("http://www.altools.com/ALTools/ALFTP/Version-History.aspx", 'g>#', 13, 5))
				sys.exit()
			elif low_search == 'apache':
				print(revision, "Apache FTP is", fetch_and_find("http://mina.apache.org/ftpserver/downloads.html", 'se">Apa', 21, 6))
				sys.exit()
			elif low_search == 'cerberus':
				print(revision, "Cerberus is", fetch_and_find("http://www.cerberusftp.com/download/", 'h4>', 14, 3))
				sys.exit()
			elif low_search == 'complete':
				print(revision, "Complete ftp is", fetch_and_find("http://www.enterprisedt.com/products/completeftp/history.html", '">V', 2, 13))
				sys.exit()
			elif low_search == 'crush':
				print(revision, "Crush ftp is", fetch_and_find("http://www.crushftp.com/download.html", 'g>Crus', 11, 5))
				sys.exit()
			elif low_search == 'eft':
				print(revision, "EFT FTP is", fetch_and_find("http://www.globalscape.com/eft/whatsnew.aspx", '<h2>E', 15, 5))
				sys.exit()
			elif low_search == 'free':
				print(revision, "Free ftp is", fetch_and_find("http://www.freesshd.com/?ctt=download", '<h1>Cur', 133, 6))
				sys.exit()
			elif low_search == 'glftp':
				print(revision, "glFTP is", fetch_and_find("http://www.glftpd.dk", 'z">gl', 11, 4))
				sys.exit()
			elif low_search == 'iis':
				print(revision, "IIS is", fetch_and_find("http://www.iis.net/overview", 'n">E', 16, 3))
				sys.exit()
			elif low_search == 'muddle':
				print(revision, "Muddle FTP is", fetch_and_find("https://savannah.nongnu.org/news/?group=muddleftpd", '56"><s', 12, 5))
				sys.exit()
			elif low_search == 'pro':
				print(revision, "Pro FTP is", fetch_and_find("http://www.proftpd.org/", '1>Cur', 42, 5))
				sys.exit()
			elif low_search == 'public':
				print(revision, "Public File is", fetch_and_find("http://cr.yp.to/publicfile/install.html", 'gz">pu', 15, 4))
				sys.exit()
			elif low_search == 'pure':
				print(revision, "Pure FTP is", fetch_and_find("http://www.pureftpd.org/project/pure-ftpd", '<li>Lat', 21, 6))
				sys.exit()
			elif low_search == 'raiden':
				print(revision, "Raiden FTP is", fetch_and_find("http://www.raidenftpd.com/en/download.html", 'er</s', 12, 15))
				sys.exit()
			elif low_search == 'slim':
				print(revision, "Slim FTP is", fetch_and_find("http://www.crushftp.com/download.html", 'g>Crus', 11, 5))
				sys.exit()
			elif low_search == 'vs':
				print(revision, "vsFTP is", fetch_and_find("https://security.appspot.com/vsftpd.html", '<li>vs', 11, 6))
				sys.exit()
			elif low_search == 'wu':
				print(revision, "Wu FTP is", fetch_and_find("http://wu-ftpd.therockgarden.ca", '.gz">cu', 42, 5))
				sys.exit()
			else:
				print("No software found for %s " %sys.argv[2])
				sys.exit()
