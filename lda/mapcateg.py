# uses topDocTag.txt and topicdoc to create topictag which contains topic to tag mappings

import pickle

doctag = open('topDocTag.txt','r').read().replace('[','').replace(']','').replace('\'','').replace(',','').split("\n")[:-1]
topicdoc = open('topicDoc', 'r').read().split('\n')[:-1]
f = open('topictag','w')
dt = {}
td = {}
topictag = {}
for i in doctag:
	dt[i.split(':')[0].strip()] = i.split(':')[1].strip()

for i in topicdoc:
	td[i.split(':')[0].strip()] = i.split(':')[1].strip()

for i in td.keys():
	topictag[i] = dt[td[i]]
pickle.dump(topictag, f)
f.close()
