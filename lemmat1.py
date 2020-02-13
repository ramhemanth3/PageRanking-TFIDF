import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
  
lemmat = WordNetLemmatizer() 

list2 = ['in','a','the','there','not','of','and','an','nor','yet','it','to','on','or','that','one','about','half','our','than','he','is','like','most','his','best','when','by','own','certainlythis',
'would','last','for','no','such','however','soon','have','before','can','even','out','into','from','their','from','alongthe','they','all','whom','this','j','r','has','himself','at','its',
'all','be','will','time','so','below','under','why','are','you','we','said','do','must','only','if',"i'd",'then','could','her',"i'm","who's",'who','there?','-','my','i','what','where','now',
'your','u','s','may','him','them','else','end','each','been','never','any','again',"'ll","they'll",'ask','there!','as','gu','just','was']
list1 = [stopwords.words('english')] + list2

with open('urlx1.txt', 'r') as myfile:
       text=myfile.read().replace('\n', '')
       text=text.replace(',','')
       text=text.replace(';','')
       text = text.lower()
       data1 = text.split()	   
myfile.close()

print("Following are the lemmatized words fo the given file :")
for temp in data1:
    if (temp not in list1):
      list1.append(temp)
      lemtemp = lemmat.lemmatize(temp)
      if (temp != lemtemp):    
        print(temp,lemtemp)
