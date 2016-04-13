# test all the documents whether we are able to predict any of the actual category for that doc.

import logging, gensim, bz2
import pickle
logging.basicConfig(filename= 'topics',format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

id2word = gensim.corpora.Dictionary.load_from_text('wiki_en_wordids.txt')
doctag = open('topDocTag.txt','r').read().replace('[','').replace(']','').replace('\'','').replace(',','').split("\n")[:-1]
dt= {}
for i in doctag:
	dt[i.split(':')[0].strip()] = i.split(':')[1].strip()

lda = gensim.models.ldamodel.LdaModel.load('ldaModel', mmap='r')
#lda.print_topics(26)
testData = open('finalText','r').read().split('\n')[:-1]
topictag = pickle.load(open("topictag",'r'))
matched = 0
for test in testData:
	temp = test.split(':')
	docId = temp[0]
	temp1=''
	for i in temp[1:]:
		temp1 += i
	text = temp1 
	doc_bow = id2word.doc2bow(text.lower().split())
	doc_lda = lda[doc_bow]
	categories = {}
	for i in doc_lda:
		for j in topictag[str(i[0])].split(' '):
			categories[j] = 1
	target = dt[docId].split(' ')
	for i in target:
		if(i in categories.keys()):
			matched += 1
			break
print matched
