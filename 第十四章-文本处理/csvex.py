# -*- coding:utf-8 -*-

import csv
from distutils.log import warn as printf

DATA = (
    (9,"web Clients and Servers","base64, urllib"),
    (10,"web Programming:CGI & WSGI", "cgi, time, wsgiref"),
    (13,"web Services", "urllib, twython"),
)

printf("*** Writing csv data")

with open("bookdata.csv","w") as f:
    writer = csv.writer(f)
    for record in DATA:
        writer.writerow(record)

printf("*** Review of saved data")

with open("bookdata.csv","r") as f:
    reader = csv.reader(f)
    print(reader)
    for chap,title,modpkgs in reader:
        printf("Chapter %s: %r (featuring %s) " % (chap,title,modpkgs))
