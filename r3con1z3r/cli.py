#!/usr/bin/env python
# coding: utf-8
# Author: Raji Abdulgafar
# GAPHY
# Twitter: @mrgaphy
# R3CON1Z3R v1.0.5
from __future__ import print_function, absolute_import
import sys, os
import requests, argparse

global R, B, C, W, Y, url, spinner


help_message = """%s
usage: r3con1z3r [-h] [-v] [-a] [-d DOMAIN]
"""

header_message = """
%s
 _____    ____     _____    ___    _   _   __   ______  ____    _____  
|  __ \  |___ \   / ____|  / _ \  | \ | | /_ | |___  / |___ \  |  __ \ 
| |__) |   __) | | |      | | | | |  \| |  | |    / /    __) | | |__) |
|  _  /   |__ <  | |      | | | | | . ` |  | |   / /    |__ <  |  _  / 
| | \ \   ___) | | |____  | |_| | | |\  |  | |  / /__   ___) | | | \ \ 
|_|  \_\ |____/   \_____|  \___/  |_| \_|  |_| /_____| |____/  |_|  \_\  
                                                            
         %sBy https://github.com/abdulgaphy - @mrgaphy%s    >|%s       #GAPHY %s
        """

# Banner Printing
def header():
    global header_message
    print(header_message%(R, B, R, C, W))

def print_help():
    """
    Print custom help message
    """
    global header_message, help_message, Y
    return header_message%(R, B, R, C, W) + "\n" + help_message%(Y)

# About r3con1z3r
def about():
    print(''' %s
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█                         R3CON1Z3R                            █
█                                                              █
█       A passive reconnaissance tool for Web information      █
█ gathering with an intuitive features, it provides a powerful █
█    environment in which OSINT web-based can be conducted.    █
█                                                              █
█                                                              █
█                       CONTRIBUTORS                           █
█                                                              █
█    1. DIRETNAN DOMNAN        https://github.com/deven96      █
█    2. SHUAIB OLADIGBOLU      https://github.com/sawzeeyy     █
█    3. NNAMDI                 https://github.com/nnamdei      █
█                                                              █
└══════════════════════════════════════════════════════════════┘     '''%(Y))

# parsing arguments
def parse_args():        
    parser = argparse.ArgumentParser(description='Example: r3con1z3r -d domain.com', usage=print_help())
  
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-v', '--version', action='version', version='r3con1z3r 1.0.5')
    parser.add_argument('-a', '--about', help='About the tools', action="store_true")
    parser.add_argument('-d', '--domain', help='Specify a domain name you want to gather information about')
    
    return parser.parse_args()
#handling requests
def requestHandler(request_type):
    """
    Handles request calls to the API
    """
    global R, B, C, W, Y, url, spinner

    core = "http://api.hackertarget.com"
    baseApi = "{0}/{1}/?q=".format(core, request_type) + url
    try:
        text = requests.get(baseApi).text
        return text
    except:
        # return an error message before exit script
        print('\n{}[+] Error generating report for {}{}{}'.format(Y, R, url, C))
        print('{}[!] Please check internet connection'.format(Y, C))
        spinner.terminate()
        sys.exit()
# Api : functionalities
def httpHeader():
	base = requestHandler(request_type="httpheaders")
	return base
def reverseHackTarget():
	base = requestHandler(request_type="reverseiplookup")
	return base
def traceRoute():
	base = requestHandler(request_type="mtr")
	return base
def whoIs():
	base = requestHandler(request_type="whois")
	return base
def dns():
	base = requestHandler(request_type="dnslookup")
	return base
def reverseDns():
	base = requestHandler(request_type="reversedns")
	return base
def geoIp():
	base = requestHandler(request_type="geoip")
	return base
def nmap():
	base = requestHandler(request_type="nmap")
	return base
def findSharedServer():
	base = requestHandler(request_type="findshareddns")
	return base
def pageLinks():
	base = requestHandler(request_type="pagelinks")
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
    global R, B, C, W, Y, url, spinner
    filename = url + '-r3con1z3r.html'
    spinner.start()
    with open(filename, 'w') as saveFile:
        saveFile.write(generateHTML())
    spinner.terminate()
    print('\n{}[+] HTML Report Successfully Generated{}'.format(Y, C))
    print('{}[+] File saved as {}{}{}'.format(Y, R, filename, C))
    print('{}[+] R3CON1Z3R Operation Completed!{}'.format(Y, W))

def gaphy():
	header()
	saveHTML()
	

def main():
    """
    Run main script
    """
    global R, B, C, W, Y, url, spinner
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    import spin
    R, B, Y, C, W = '\033[1;31m', '\033[1;37m', '\033[93m', '\033[1;30m', '\033[0m'
    args = vars(parse_args())
    
    
    # OS Compatibility : Coloring
   
    if sys.platform.startswith('win'):
        try:
            import win_unicode_console, colorama
            win_unicode_console.enable()
            colorama.init()
        except:
            print('[+] Error: Coloring libraries not installed')
            R, B, Y, C, W = '', '', '', '', ''
    
    if len(sys.argv) < 2 :
        header()
        print('{}Usage: r3con1z3r -d domain.com\n'.format(Y, C))
        print('{}Example: r3con1z3r -d google.com\n'.format(Y, C))
        print('{}[!] Please specify a domain'.format(Y, C))
        sys.exit()
    else:
        if args['about']:
            about()
        else: 
            url = args['domain']
            if  url[0:8] == 'https://':
                url = url.replace("https://","")
            elif url[0:7] == 'http://':
                url = url.replace("http://","")
            else:
                url = url
                
                # declare global spinner
                spinner = spin.create_spinner(before="Generating Report")
                gaphy()

if __name__=="__main__":
	main()
