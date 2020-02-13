from bs4 import BeautifulSoup as Soup
import re, urllib, nltk,sys
import urllib.request
from urllib.request import urlopen, Request
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,}
#url1 = str(sys.argv[1]) 
url1 = 'http://www.english-for-students.com/banished-son-saves-his-brothers.html'
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
html = urllib.request.urlopen(url).read() #make the request to the url
soup = Soup(html) #using Soup on the responde read
for script in soup(["script", "style"]): #You need to extract this <script> and <style> tags
    script.extract() #strip them off
text = soup.getText() #this is the method that I had like 40 min problems
text = text.encode('utf-8') #make sure to encode your text to be compatible
#raw = nltk.clean_html(document)
#print(text.encode('utf-8'))
print(text)
'''

#pip3 install html2text
#pip3 install beutifulsoup4
#pip3 install html5lib

