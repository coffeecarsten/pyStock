#!/usr/bin/python

import urllib
import re

print "Content-type:text/html\r\n\r\n"
print "<head><title>test</title></head>"
print "<html>"
print "<body>"
print '<table border="1">'
print "<tr>"
print "<td>SYMB</td>"
print "<td>pris</td>"
print "<td>procent</td>"
print "</tr>"

symbolslist = ["fls.co","aapl","novo-b.co","nzym-b.co","tdc.co","msft","dis","ko","vow.f","nesr.f","g4s.co","danske.co"]
######novo split jan 2, 2014 i 1/5
######apple split jun 9, 2014 i 1/7
########## g4s.co har jeg sat til 25 men det er ikke rigtigt. ved ikke hvad jeg kobte til.
#####danske bank er jo ikke relevant at regne paa... satte den bare til 180
orgpricelist= [316,86,159,163,43,25,98,37,183,57,25,180]
#styk=[]
i=0
####print "|	SYMB	|	BUY	|	'%'		| "
while i<len(symbolslist):
	url = "https://finance.yahoo.com/q;_ylt=AsYRfIsgdDn56eKmf2ut2k4nv7gF?uhb=uhb2&fr=uh3_finance_vert_gs_ctrl1_e&type=2button&s=" +symbolslist[i] +"%2C"
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	regex = '<span id="yfs_l84_' +symbolslist[i] +'">(.+?)</span>'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)
	price1 = ', '.join(price)
	price2 = float(price1)
	procent = ((price2 - orgpricelist[i]) / price2)*100
	print "<tr>"
	print "<td>",symbolslist[i],"</td>"
	print "<td>",price2,"</td>"
	print "<td>",procent,"</td>"
	print "</tr>"
	i+=1
print "test"
print '</table>'
print "</body>"
print "</html>"

