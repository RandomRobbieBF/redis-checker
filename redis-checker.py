#!/usr/bin/env python
#
# 
#
# redis-checker.py - Finding Exposed Redis Services
#
# By @RandomRobbieBF
# 
#

import requests
import sys
import argparse
import os.path
import redis
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
session = requests.Session()


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=False ,default="",help="URL to test")
parser.add_argument("-f", "--file", default="",required=False, help="File of urls")
parser.add_argument("-p", "--proxy", default="",required=False, help="Proxy for debugging")
parser.add_argument("-P", "--port", default=6379,required=False, help="Default Port")
parser.add_argument("-s", "--ssl", default=False,required=False, help="Use SSL")


args = parser.parse_args()
IP = args.url
urls = args.file
PORT = args.port
SSL = args.ssl

if args.proxy:
	http_proxy = args.proxy
	os.environ['HTTP_PROXY'] = http_proxy
	os.environ['HTTPS_PROXY'] = http_proxy
	
	

            
           

def test_url(IP,PORT,SSL):
	try:
		user_connection = redis.Redis(host=IP, port=PORT, decode_responses=True,socket_timeout=2,ssl=SSL)
		user_connection.ping()
		text_file = open("redis.txt", "a+")
		text_file.write(""+IP+"\n")
		text_file.close()
		print("Host: "+IP+" Port:"+str(PORT)+" Connection Confirmed")
	except Exception as e:
		print(e)
		pass

			
			
				


if urls:
	if os.path.exists(urls):
		with open(urls, 'r') as f:
			for line in f:
				IP = line.replace("\n","")
				PORT = 16379
				try:
					print("Testing "+IP+"")
					test_url(IP,PORT,SSL)
				except KeyboardInterrupt:
					print ("Ctrl-c pressed ...")
					sys.exit(1)
				except Exception as e:
					print('Error: %s' % e)
					pass
		f.close()
	

else:
	test_url(IP,PORT,SSL)
