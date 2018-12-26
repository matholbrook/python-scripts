#!/usr/bin/env python3

# global endpoint URL
baseUrl="http://api.open-notify.org/"

apiUrl="astros.json"
exec(open('restAPIget.py').read())

apiUrl="iss-now.json"
exec(open('restAPIget.py').read())
