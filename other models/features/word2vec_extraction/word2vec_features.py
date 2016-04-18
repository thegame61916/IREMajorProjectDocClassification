import gensim
import pickle
import nltk
import numpy

Word2Vec=gensim.models.word2vec.Word2Vec
model=Word2Vec.load("model.en")
[alllabels,testkeys,testdocs,testlabels,trainkeys,traindocs,trainlabels] = pickle.load(open("../../data.pickle","r"))

documents=testdocs+traindocs
stop_word_list=open("english_stopwords.txt").read().split("\n")

#for tokenisation
for i in xrange(len(documents)):
	tokens=nltk.word_tokenize(documents[i])
	for j in xrange(len(tokens)):
		if tokens[j] in stop_word_list:
			tokens[j]=""
			continue
	if i%100==0:
		print i
	documents[i]=tokens

print "writing"
f=open("data.txt","w")
for i in documents:
	f.write(i)
	f.write("\n")
f.close()

w2vectors=[]
vector_len=200	#DEPENDS ON YOUR MODEL
for tokens in documents:
	lent=0
	i=documents.index(tokens)
	if i%1==0:
		print i
	avg = numpy.array(range(vector_len))*0
	for word in tokens:
		if word in model:
			lent=lent+1
			avg = avg + model[word]
	avg=avg/lent
	print lent
	w2vectors.append(avg)

f=open("word2vec_vectors.txt","w")
for i in w2vectors:
	f.write(" ".join(map(str,list(i))))
	f.write("\n")

f.close()

