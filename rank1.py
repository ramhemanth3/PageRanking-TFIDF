import sys
import csv
import pandas as pd
import nltk
from nltk.corpus import stopwords
from export import *
#import pymysql
from functools import reduce
from collections import defaultdict
import math

#con = pymysql.connect(host='localhost', port=3306, user='team1', passwd='test623', db='rdbidf1')
import sqlite3
con = sqlite3.connect('rdbidf1')
N=5

with open('Falcon2.txt', 'r') as myfile:
       text=myfile.read().replace('\n', '')
       text=text.replace(',','')
       text=text.replace(';','')
       text = text.lower()	   
myfile.close()
       
    
with open('greed2.txt', 'r') as myfile:
       textr=myfile.read().replace('\n', '')
       textr=textr.replace(',','')
       textr=textr.replace(';','')
       textr = textr.lower()	   
myfile.close()
with open('Alaudeen2.txt', 'r') as myfile:
       text3=myfile.read().replace('\n', '')
       text3=text3.replace(',','')
       text3=text3.replace(';','')
       text3 = text3.lower()	   
myfile.close()
with open('alibaba2.txt', 'r') as myfile:
       text4=myfile.read().replace('\n', '')
       text4=text4.replace(',','')
       text4=text4.replace(';','')
       text4 = text4.lower()	   
myfile.close()
with open('banished2.txt', 'r') as myfile:
       text5=myfile.read().replace('\n', '')
       text5=text5.replace(',','')
       text5=text5.replace(';','')
       text5 = text5.lower()	   
myfile.close()
with con:
      cur = con.cursor()
      cur.execute('SELECT * FROM qryselected;')
      rows = cur.fetchone()
      fp = open('qury.csv', 'w')
      myFile = csv.writer(fp)
      myFile.writerows(rows)
      fp.close()
      con.commit()
data2 = ' ';
with open('qury.csv', 'r') as myfile1:
       text2=myfile1.read().replace('\n', '')
       text2=text2.replace(',','')
       text2=text2.replace(';','')
       text2 = text2.lower()	   
       data2 = text2.split()
print(data2)
print("Stop word are as follows:")
print(stopwords.words('english'))
#print(data2)

#with open('kywrd1.csv', 'w') as f:
  #sys.stdout = f
print("Keyword statistics from Falcon File are as follows:")
list1 = [stopwords.words('english')]
for temp in data2:
    if (temp not in list1):
      if (text.count(temp) > 0):    
        list1.append(temp)
        print(temp,text.count(temp))

print("Keyword statistics from Greediness File are as follows:")
list1 = [stopwords.words('english')]
for temp in data2:
    if (temp not in list1):
      if (textr.count(temp) > 0):    
        list1.append(temp)
        print(temp,textr.count(temp))
print("Keyword statistics from Alaudeen File are as follows:")
list1 = [stopwords.words('english')]
for temp in data2:
    if (temp not in list1):
      if (text3.count(temp) > 0):    
        list1.append(temp)
        print(temp,text3.count(temp))
print("Keyword statistics from Alibaba File are as follows:")
list1 = [stopwords.words('english')]
for temp in data2:
    if (temp not in list1):
      if (text4.count(temp) > 0):    
        list1.append(temp)
        print(temp,text4.count(temp))
print("Keyword statistics from Banished File are as follows:")

list1 = [stopwords.words('english')]
for temp in data2:
    if (temp not in list1):
      if (text5.count(temp) > 0):    
        list1.append(temp)
        print(temp,text5.count(temp))

totext = str(text)+str(textr)+str(text2)+str(text3)+str(text4)+str(text5)
totext=totext.replace(',','')
totext=totext.replace(';','')
totext=totext.replace(':','')
totext=totext.replace('"','')
totext=totext.replace('.',' ')
totext1 = totext.split()
#print(totext)
list2 = ['in','a','the','there','not','of','and','an','nor','yet','it','to','on','or','that','one','about','half','our','than','he','is','like','most','his','best','when','by','own','certainlythis',
'would','last','for','no','such','however','soon','have','before','can','even','out','into','from','their','from','alongthe','they','all','whom','this','j','r','has','himself','at','its',
'all','be','will','time','so','below','under','why','are','you','we','said','do','must','only','if',"i'd",'then','could','her',"i'm","who's",'who','there?','-','my','i','what','where','now',
'your','u','s','may','him','them','else','end','each','been','never','any','again',"'ll","they'll",'ask','there!','as','gu','just']
list1 = [stopwords.words('english')] + list2
ld1 = 0.0
ld2 = 0.0
ld3 = 0.0
ld4 = 0.0
ld5 = 0.0
lq = 0.0
simco1 = 0.0
simco2 = 0.0
simco3 = 0.0
simco4 = 0.0
simco5 = 0.0
for temp in totext1:
    if (temp not in list1):  
        list1.append(temp)
        m = totext.count(temp)
        print(temp,m,math.log((float(N)/float(m)),2))
        if (temp in text):
          ld1 = ld1 + math.log((float(N)/float(m)),2) ** 2
        if (temp in textr):
          ld2 = ld2 + math.log((float(N)/float(m)),2) ** 2
        if (temp in text3):
          ld3 = ld3 + math.log((float(N)/float(m)),2) ** 2
        if (temp in text4):
          ld4 = ld4 + math.log((float(N)/float(m)),2) ** 2
        if (temp in text5):
          ld5 = ld5 + math.log((float(N)/float(m)),2) ** 2
        if (temp in data2):
          n = text2.count(temp)
          d1 = text.count(temp)
          d2 = textr.count(temp)
          d3 = text3.count(temp)
          d4 = text4.count(temp)
          d5 = text5.count(temp)
          dt = d1+d2+d3+d4+d5
          print(temp,(float(n)/float(dt)*math.log((float(N)/float(m)),2)))
          lq = lq + math.log((float(N)/float(m)),2) ** 2
          if (temp in text):
            simco1 = simco1 + math.log((float(N)/float(m)),2)*math.log((float(N)/float(m)),2)
          if (temp in textr):
            simco2 = simco2 + math.log((float(N)/float(m)),2)*math.log((float(N)/float(m)),2)
          if (temp in text3):
            simco3 = simco3 + math.log((float(N)/float(m)),2)*math.log((float(N)/float(m)),2)
          if (temp in text4):
            simco4 = simco4 + math.log((float(N)/float(m)),2)*math.log((float(N)/float(m)),2)
          if (temp in text5):
            simco5 = simco5 + math.log((float(N)/float(m)),2)*math.log((float(N)/float(m)),2)
ld1 = math.sqrt(ld1)
ld2 = math.sqrt(ld2)
ld3 = math.sqrt(ld3)
ld4 = math.sqrt(ld4)
ld5 = math.sqrt(ld5)
lq = math.sqrt(lq)
simco1 = simco1/ld1
simco2 = simco2/ld2
simco3 = simco3/ld3
simco4 = simco4/ld4
simco5 = simco5/ld5
print(simco1,simco2,simco3,simco4,simco5)



#print("keywords statistics file is generated")

#pip3 install nltk
#python
#>>import nltk
#>>nltk.download()
#pip3 install export


