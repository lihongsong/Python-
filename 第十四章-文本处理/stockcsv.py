# -*- coding:utf-8 -*-

from time import ctime
from urllib.request import urlopen
import csv

TICs = ("yhoo","dell","cost","abde","intc")
URL = "http://quote.yahoo.com/d/quotes.csv?s=%s&f=sllclp2"

print("\nPrices quoted as of : %s PDT\n " % ctime())
print("TOCKER","PRICE","CHANGE",r"%AGE")

print("----- ---- ----- ----")

with urlopen(URL % ",".join(TICs)) as u:

    print(u.read().decode("utf-8"))

    reader = csv.reader(u.read().decode("utf-8"))

    print(reader)
    # for tick, price, chg, pct in reader:
    #     print(tick.ljust(7), ("%.2f" % round(float(price), 2)).rjust(6) , chg.rjust(6), pct.rstrip().rjust(6))
