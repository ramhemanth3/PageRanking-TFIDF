from bs4 import BeautifulSoup as Soup
import re, urllib, nltk,sys
import urllib.request
from urllib.request import urlopen, Request
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,}
url1 = str(sys.argv[1]) 
#url = 'http://www.english-for-students.com/alaudeen-and-the-magical-lamp.html'
request=urllib.request.Request(url1,None,headers) #The assembled request
response = urllib.request.urlopen(request)
text = response.read()
soup = Soup(text) #using Soup on the responde read
for script in soup(["script", "style"]): #You need to extract this <script> and <style> tags
    script.extract() #strip them off
text = soup.getText() #this is the method that I had like 40 min problems
text = text.encode('utf-8') #make sure to encode your text to be compatible
print(text)

'''
from bs4 import BeautifulSoup
import json

with open('test.html','r',encoding='utf8') as file:
    content = file.read()
soup = BeautifulSoup(content)
text = soup.find('p').text    # Unicode string!

items = {'text':text}

with open('out.json','w',encoding='utf8') as out:
    json.dump(items,out,ensure_ascii=False)

with open('out.json','r',encoding='utf8') as file:
    data = json.load(file)

print(data)
'''
#Ref:https://stackoverflow.com/questions/45651482/python-beautifulsoup-creating-weird-xe2-unicode-characters-when-written-to-file
#pip3 install html2text
#pip3 install beutifulsoup4
#pip3 install html5lib

