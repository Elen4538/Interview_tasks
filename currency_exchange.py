import xml.etree.ElementTree as ET
import re
import requests

"""
program converts "Венгерские форинты" в "Норвежскую крону"
via "Рубли" using current currency exchange here
'http://www.cbr.ru/scripts/XML_daily.asp'

"""
url = 'http://www.cbr.ru/scripts/XML_daily.asp'

try:
    response = requests.get(url)
    msg = response.content

except Exception as e:
    print('Connection failed, Error:', e)

tree = ET.fromstring(msg) 

for i in range(len(tree)):

    if tree[i][3].text == "Венгерских форинтов":

        ven_for = float(re.sub(r',','.',tree[i][4].text))/float(tree[i][2].text)
    
    if tree[i][3].text == "Норвежских крон":
        nor_kron = float(re.sub(r',','.',tree[i][4].text))/float(tree[i][2].text)

res = nor_kron / ven_for
    
print('Норвежская крона в венгерских форинтах через рубли составляет:', res)
