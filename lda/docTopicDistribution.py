# Print distribution of topics for every document to predict which topic is best suited for a document. category of that document will be assigned to that topic. 
# Output: docTopicDistribution.txt, contains the topic distribution
# 		topicdoc, contains topic to the most relevant document mapping
import logging, gensim, bz2
import pickle

id2word = gensim.corpora.Dictionary.load_from_text('wiki_en_wordids.txt')
lda = gensim.models.ldamodel.LdaModel.load('ldaModel', mmap='r')
testData = open('finalText','r').read().split('\n')[:-1]
docTopic = open('docTopicDistribution.txt','w')
for test in testData:
	topic = [str(0) for i in range(25)]
	temp = test.split(':')
	docId = temp[0]
	temp1=''
	for i in temp[1:]:
		temp1 += i
	text = temp1 
	doc_bow = id2word.doc2bow(text.lower().split())
	doc_lda = lda[doc_bow]
	for i in doc_lda:
		topic[i[0]] = str(i[1])
	docTopic.write(temp[0] + ":" + ' '.join(topic) + '\n')
docTopic.close()

topicDist = open('docTopicDistribution.txt','r').read().split('\n')[:-1]
topicDoc = open('topicDoc', 'w')

for i in range(25):
	mx = 0
	mxDoc = ''
	for j in topicDist:
		pr = j.split(':')[1].strip().split(' ')
		if(float(pr[i]) >mx):
			mx = float(pr[i])
			mxDoc = j.split(':')[0].strip()
	topicDoc.write(str(i)+':'+mxDoc+'\n')
topicDoc.close()
