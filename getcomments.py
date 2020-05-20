#!/usr/bin/python3
#
# getcomments.py
#
# Check web pages for hidden comments
#
# NOTE: This is not another spider/brute force script
# We will check files with 200 status from gobuster or ffuf
#
# This program can be redistributed and/or modified under the terms of the
# GNU General Public License, either version 3 of the License, or (at your
# option) any later version.
#
# Author: vaccine - https://jellyfishsizzle.xyz
# Version: v1.3

import requests
from requests.exceptions import Timeout
import argparse
import re
import os.path
from bs4 import BeautifulSoup, Comment
from colorama import Fore, Style
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument("file", help="ffuf or gobuster output")
parser.add_argument("host", help="Host/IP")
args = parser.parse_args()

fname = args.file
host = args.host

def get_files():
  try:
    with open(fname) as infile:
      reg = re.compile('[\w,-]+\.\w{3,4}.*Status:\s200')
      matches = []

      for line in infile:
        if reg.findall(line):
          matches += line.strip("/").split(" ", 1)[:1]
      infile.close()
      return(sorted(set(matches)))

  except IOError:
    print(colored("[-] Unable to locate file", 'red'))
    exit(1)


def find_cmnts(my_list):
  for f in my_list:
    try:
      r = requests.get(host + "/" + f, timeout=2)
    except Timeout:
      print(colored("[-] Unable to connect to host", 'red'))
    else:
      soup = BeautifulSoup(r.text, 'html.parser')
      scomments = soup.findAll(text=lambda text:isinstance(text, Comment))
      bcomments = soup.findAll(text=re.compile('<--[\s\S]*?-->'))
      mcomments = soup.findAll(text=re.compile('<!--[\s\S]*?-->'))
      comments = scomments + bcomments + mcomments

      if comments:
        print(" ")
        print(colored("[+] " + host + "/" + f, 'green'))
        for c in comments:
          print(c.strip().lstrip("<--").rstrip("-->"))

def main():
  my_list = get_files()
  find_cmnts(my_list)

if __name__ == "__main__":
  main()
