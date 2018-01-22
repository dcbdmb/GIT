#!/usr/bin/python

import sys, getopt;
import os;
import json;
import requests;
import subprocess;
import urllib2;

def main(argv):
  username = ' '
  try:
     opts, args = getopt.getopt(argv,"hu:",["username="])
  except getopt.GetoptError:
     print 'creategit.py -u <username>'
     sys.exit(2)
  for opt, arg in opts:
     if opt == '-h':
        print 'test.py -u <username>'
        sys.exit()
     elif opt in ("-u","--username"):
        username = arg
  print 'username is:', username

  cwd = os.getcwd()
#  print 'cwd is:', cwd

#  data = {}
#  data['name'] = username
#  data['description'] = "this is a test"
#  data['private'] = false
#  data['has_issues'] = true
#  data['has_download'] = true
#  data['has_wiki'] = false

#  url = "curl -u https://api.github.com/users/repos -d " + json_data
#  print "the url:",url
#  os.system(url)
#  print "the command:",url,json_data
#  req = urllib2.Request(url, json_data)
#  response = urllib2.urlopen(req)
#  the_page = response.read()

#  subprocess.call(['curl',' -u','dcbdmb','https://api.github.com/users/repos','-d',json_data])
#  subprocess.call([url,json_data])
#  headers = {}
#  res = requests.post(url, data=json_data, headers=headers)

   
#  print curl -u user:username https://api.github.com/user/repos -d json_data
  json_string = r'''{"name": "marktest", "description": "trying to do via api", "private": false, "has_issues": true, "has_downloads": true, "has_wiki": false}'''
  url = "curl -u user:username https://api.github.com/user/repos -d " + json_string
  print url
  os.system(url)
#  os.system("curl -u dcbdmb https://api.github.com/user/repos -d \"{\"name\": \"marktest\", \"description\": \"trying to do via api\", \"private\": false, \"has_issues\": true, \"has_downloads\": true, \"has_wiki\": false}\"")


if __name__ == "__main__":
   main(sys.argv[1:])
