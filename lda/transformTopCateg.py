#Eliminate documents not related to top categories. using docTag, docText and topcategories files
# Output: finaText, cotaining documents only which are there in topcategories
# topdoctag: document to tag mapping for top categories

#Meanigful categories: 17257
import pickle

doctag = open('doctag.txt','r').read().replace('[','').replace(']','').replace('\'','').replace(',','').split("\n")[:-1]
topCategs1 = open('topcategories','r').read().replace('(','').replace(')','').replace('\'','').split("\n")[:-1]
topDocTag = open('topDocTag.txt','w')
oldText = open('docText','r').read().split('\n')
finalText = open('finalText','w')
topCategs = []
dt = {}
temp ={}
for j in oldText:
	temp[j.split(':')[0].strip()]=1

for i in topCategs1:
	topCategs.append(i.split(',')[0].strip())

for i in doctag:
	categs = ''
	for j in i.split(':')[1].strip().split(' '):
		if j.strip() in topCategs:
			categs += j.strip()+' '
	if(len(categs) > 0):
		if (temp.has_key(i.split(':')[0].strip())):
			dt[i.split(':')[0].strip()] = categs.strip()
			topDocTag.write(i.split(':')[0].strip()+':'+categs.strip()+'\n')

for i in oldText:
	if(dt.has_key(i.split(':')[0].strip())):
		finalText.write(i+'\n')

finalText.close()
topDocTag.close()
