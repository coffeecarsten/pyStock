#!/usr/bin/python

import urllib
import re

symbolslist = ["fls:cph","aapl","novo-b.co","nzym-b.co","tdc.co","msft","dis","ko","vow.f","nesr.f","g4s.co","danske.co"]
######novo split jan 2, 2014 i 1/5
######apple split jun 9, 2014 i 1/7
########## g4s.co har jeg sat til 25 men det er ikke rigtigt. ved ikke hvad jeg kobte til.
#####danske bank er jo ikke relevant at regne paa... satte den bare til 180
orgpricelist= [316,86,159,163,43,25,98,37,183,57,25,180]
#styk=[]
i=0
####print "|    SYMB    |   BUY |   '%'     | "
while i<len(symbolslist):
    url = "https://www.google.com/finance?q="+symbolslist[i]
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="ref_(.+?)_l">(.+?)</span>'
    pattern = re.compile(regex)
    #pattern = re.compile(regex)
    price = re.findall(pattern,htmltext)
    print price
    i+=1
