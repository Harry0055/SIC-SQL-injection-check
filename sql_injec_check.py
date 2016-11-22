#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, time
from termcolor import colored
print colored("\n+===========================================================================+", 'blue')
print colored("| SIC - Simple SQL Webapp Injection Checking script                            |", 'blue')
print colored("| Author: Harry6666                                                            |", 'blue')
print colored("| Usage: Just run it and let it head you :)                                    |", 'blue') 
print colored("+===========================================================================+\n", 'blue')
time.sleep(1.5)
print colored("\n|  [WARNING] must be like .php(asp/aspx)?id=  |\n", 'yellow' )
time.sleep(1.5)
url = raw_input("url(with protocol): ")
initial = "'"
print "Testing "+ url
first = requests.post(url+initial)
if "mysql" in first.text.lower():
  print "Injectable MySQL detected"
elif "native client" in first.text.lower():
  print "Injectable MSSQL detected"
elif "syntax error" in first.text.lower():
  print "Injectable PostGRES detected"
elif "ORA" in first.text.lower():
  print "Injectable Oracle detected"
else:
  print "Not Injectable Oops J J"
