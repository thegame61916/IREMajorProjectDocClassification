# output the tag for text provided in test file

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
testData = open('test','r').read()
topictag = pickle.load(open("topictag",'r'))
matched = 0
doc_bow = id2word.doc2bow(testData.lower().split())
doc_lda = lda[doc_bow]
categories = {}
for i in doc_lda:
	for j in topictag[str(i[0])].split(' '):
		categories[j] = 1
print categories.keys()
