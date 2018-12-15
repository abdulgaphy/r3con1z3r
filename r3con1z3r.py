#!/usr/bin/env python
# coding: utf-8
# Author: Raji Abdulgafar
# GAPHY
# Twitter: @mrgaphy
# R3CON1Z3R v1.0
import sys
import requests


# OS Compatibility : Coloring
if sys.platform.startswith('win'):
    R, B, Y, C, W = '\033[1;31m', '\033[1;37m', '\033[93m', '\033[1;30m', '\033[0m'
    try:
        import win_unicode_console, colorama
        win_unicode_console.enable()
        colorama.init()
    except:
        print('[+] Error: Coloring libraries not installed')
        R, B, Y, C, W = '', '', '', '', ''
else:
    R, B, Y, C, W = '\033[1;31m', '\033[1;37m', '\033[93m', '\033[1;30m', '\033[0m'
# Banner Printing
def header():
    print('''%s
 _____    ____     _____    ___    _   _   __   ______  ____    _____  
|  __ \  |___ \   / ____|  / _ \  | \ | | /_ | |___  / |___ \  |  __ \ 
| |__) |   __) | | |      | | | | |  \| |  | |    / /    __) | | |__) |
|  _  /   |__ <  | |      | | | | | . ` |  | |   / /    |__ <  |  _  / 
| | \ \   ___) | | |____  | |_| | | |\  |  | |  / /__   ___) | | | \ \ 
|_|  \_\ |____/   \_____|  \___/  |_| \_|  |_| /_____| |____/  |_|  \_\  
                                                            
         %sBy https://github.com/abdulgaphy - @mrgaphy%s    >|%s       #GAPHY %s
        '''%(R, B, R, C, W))
    
if len(sys.argv) < 2 or len(sys.argv) > 2:
    header()
    print('{}Usage: python3 r3con1z3r.py [domain.com]\n'.format(Y, C))
    print('{}Example: python3 r3con1z3r.py google.com\n'.format(Y, C))
    print('{}[!] Please specify a domain'.format(Y, C))
    sys.exit()
else:
    url = str(sys.argv[1])

# Api : functionalities
def httpHeader():
	baseApi = "http://api.hackertarget.com/httpheaders/?q=" + url
	base = requests.get(baseApi).text
	return base
def reverseHackTarget():
	baseApi = "http://api.hackertarget.com/reverseiplookup/?q=" + url
	base = requests.get(baseApi).text
	return base
def traceRoute():
	baseApi = "http://api.hackertarget.com/mtr/?q=" + url
	base = requests.get(baseApi).text
	return base
def whoIs():
	baseApi = "http://api.hackertarget.com/whois/?q=" + url
	base = requests.get(baseApi).text
	return base
def dns():
	baseApi = "http://api.hackertarget.com/dnslookup/?q=" + url
	base = requests.get(baseApi).text
	return base
def reverseDns():
	baseApi = "http://api.hackertarget.com/reversedns/?q=" + url
	base = requests.get(baseApi).text
	return base
def geoIp():
	baseApi = "http://api.hackertarget.com/geoip/?q=" + url
	base = requests.get(baseApi).text
	return base
def nmap():
	baseApi = "http://api.hackertarget.com/nmap/?q=" + url
	base = requests.get(baseApi).text
	return base
def findSharedServer():
	baseApi = "http://api.hackertarget.com/findshareddns/?q=" + url
	base = requests.get(baseApi).text
	return base
def pageLinks():
	baseApi = "http://api.hackertarget.com/pagelinks/?q=" + url
	base = requests.get(baseApi).text
	return base	
# Generating reports in HTML format
def generateHTML():
	create = """<!DOCTYPE html>
<html>
<head>
  <title>R3C0N1Z3R Report</title>
</head>
<body>
 <center> <h1>R3C0N1Z3R Report - [{}]</h1></center>
 <strong>HTTP header information</strong>
	<pre>{}</pre>
    <strong>Trace Route</strong>
    <pre>{}</pre> 
  <strong>Whois Information</strong>
	<pre>{}</pre>
	<strong>DNS server record</strong>
	<pre>{}</pre>
	<strong><Nmap- running services/strong>
	<pre>{}</pre>
	<strong>Website on the same server</strong>
	<pre>{}</pre>
	<strong>Reverse IP Address</strong>
	<pre>{}</pre>
	<strong>Page Links</strong>
	<pre>{}</pre><hr>
	<center> All Rights Reserved &copy; <strong>R3CON1Z3R</strong></center>
 
</body>
</html>
    """.format(url,httpHeader(),traceRoute(),whoIs(),dns(),nmap(),findSharedServer(),reverseHackTarget(),pageLinks())	
	return create
# Saving the report
def saveHTML():
	saveFile = open(url + '.html', 'w')
	saveFile.write(generateHTML())
	saveFile.close()
	print('{}[+] HTML Report Successfully Generated{}'.format(Y, C))
	print('{}[+] File saved as {}{}.html{}'.format(Y, R, url, C))
	print('{}[+] R3CON1Z3R Operation Completed!{}'.format(Y, W))

def gaphy():
	header()
	saveHTML()
	

if __name__ == '__main__': gaphy()

