import pickle
import random
from sklearn import linear_model
from sklearn.naive_bayes import MultinomialNB


#dockeys

[alllabels,testkeys,testdocs,testlabels,trainkeys,traindocs,trainlabels] = pickle.load(open("../data.pickle","r"))


def read(filename):
	f=open(filename)
	a=f.readlines()
	v=[]
	for i in a:
		v.append([float(k) for k in i.strip().split(" ")])
	f.close()
	return v

def compare(a,b):
	return len([i for i, j in zip(a, b) if i == j])*100.0/len(a)

def most_common(lst):
    return max(set(lst), key=lst.count)


#vector_source="word2vec_extraction/word2vec_vectors.txt"
vector_source="tf_idf_vectors.txt"
vectors=read(vector_source)

#MAKING TEST TRAIN TESTLABELS TRAINLABELS 
#others ready
test=vectors[0:5000]
train=vectors[5000:len(vectors)]


#classification for each label
accuracy={}
model={}
output={}
for label in alllabels:
	#create a binaryclassifier from trainlabel and testlabel
	test_binary_labels=[1 if label in testlabels[i] else 0 for i in xrange(len(testlabels))]
	#1 means label is there, 0 means it isnt there
	train_binary_labels=[1 if label in trainlabels[i] else 0 for i in xrange(len(trainlabels))]

	#FOR SVM
	clfsvm = linear_model.SGDClassifier()
	clfsvm.fit(train,train_binary_labels)
	output1=clfsvm.predict(test)


	#FOR NAIVE BAYES'
	#clfbayes = MultinomialNB()
	#clfbayes.fit(train,train_binary_labels)
	#output2=clfbayes.predict(test)
	
	#also for comparison also storing, what if all labels belong to  one, for that
	a=most_common(train_binary_labels)
	output3=[a]*len(test)	#HIGHLY NAIVE PREDICTION
	output2=output3
	#compare output and test_bianry_labels
	accuracy[label]=[compare(output1,test_binary_labels),compare(output3,test_binary_labels)]

	#model[label]=[clfsvm,clfbayes]
	model[label]=[clfsvm]
	output[label]=[output1,output2]
	print label

pickle.dump([accuracy,output,model],open("results.pickle","w"))


"""
with tf_idf 1000
{'wiki': [53.08, 57.24], 'art': [94.54, 91.88], 'reference': [70.68, 70.44], 'people': [92.9, 89.72], 'culture': [91.38, 91.18], 'books': [95.56, 92.88], 'design': [93.24, 92.56], 'politics': [94.34, 91.86], 'technology': [93.18, 93.18], 'psychology': [94.7, 93.82], 'interesting': [89.72, 89.72], 'wikipedia': [84.92, 84.92], 'research': [84.6, 84.6], 'religion': [96.72, 94.38], 'music': [98.06, 92.9], 'math': [96.24, 93.86], 'development': [94.34, 93.96], 'theory': [94.22, 94.22], 'philosophy': [93.48, 91.0], 'article': [90.34, 90.34], 'language': [94.82, 92.56], 'science': [89.08, 86.72], 'programming': [92.98, 89.88], 'history': [83.54, 81.22], 'software': [94.0, 92.22]}


500
tf=
{'wiki': [49.52, 57.24], 'art': [94.28, 91.88], 'reference': [70.52, 70.44], 'people': [91.98, 89.72], 'culture': [91.2, 91.18], 'books': [95.04, 92.88], 'design': [93.22, 92.56], 'politics': [94.12, 91.86], 'technology': [93.18, 93.18], 'psychology': [94.42, 93.82], 'interesting': [89.72, 89.72], 'wikipedia': [84.92, 84.92], 'research': [84.6, 84.6], 'religion': [95.84, 94.38], 'music': [97.06, 92.9], 'math': [96.04, 93.86], 'development': [94.04, 93.96], 'theory': [94.22, 94.22], 'philosophy': [93.16, 91.0], 'article': [90.34, 90.34], 'language': [94.74, 92.56], 'science': [88.88, 86.72], 'programming': [92.46, 89.88], 'history': [84.38, 81.22], 'software': [93.04, 92.22]}

with lda
{'wiki': [43.48, 57.24, 57.24], 'art': [91.88, 91.88, 91.88], 'reference': [70.44, 70.44, 70.44], 'people': [89.72, 89.72, 89.72], 'culture': [91.18, 91.18, 91.18], 'books': [92.88, 92.88, 92.88], 'design': [92.56, 92.56, 92.56], 'politics': [91.86, 91.86, 91.86], 'technology': [93.18, 93.18, 93.18], 'psychology': [93.82, 93.82, 93.82], 'interesting': [89.72, 89.72, 89.72], 'wikipedia': [84.92, 84.92, 84.92], 'research': [84.6, 84.6, 84.6], 'religion': [94.38, 94.38, 94.38], 'music': [92.9, 92.9, 92.9], 'math': [93.86, 93.86, 93.86], 'development': [93.96, 93.96, 93.96], 'theory': [94.22, 94.22, 94.22], 'philosophy': [91.0, 91.0, 91.0], 'article': [90.34, 90.34, 90.34], 'language': [92.56, 92.56, 92.56], 'science': [86.6, 86.72, 86.72], 'programming': [89.88, 89.88, 89.88], 'history': [81.22, 81.22, 81.22], 'software': [92.22, 92.22, 92.22]}


with doc2vec
d2v=
{
'wiki' : [50.04, 57.24],
'art' : [94.14, 91.88],
'reference' : [69.32, 70.44],
'people' : [91.86, 89.72],
'culture': [90.56, 91.18],
'books':[94.72, 92.88],
'design':[92.28, 92.56],
'politics':[93.56, 91.86],
'technology':[92.32, 93.18],
'psychology':[95.46, 93.82],
'interesting':[89.48, 89.72],
'wikipedia':[83.58, 84.92],
'research':[82.06, 84.6],
'religion':[96.84, 94.38],
'music':[97.74, 92.9],
'math':[96.56, 93.86],
'development':[93.74, 93.96],
'theory':[94.28, 94.22],
'philosophy':[93.18, 91.0],
'article':[90.32, 90.34],
'language':[94.44, 92.56],
'science':[89.12, 86.72],
'programming':[93.38, 89.88],
'history':[81.76, 81.22],
'software':[92.82, 92.22]
}

with word2vec
w2v=
{
'wiki' : [43.12, 57.24],
'art' : [92.42, 91.88],
'reference' : [70.48, 70.44],
'people' : [89.9, 89.72],
'culture': [91.18, 91.18],
'books':[93.24, 92.88],
'design':[92.56, 92.56],
'politics':[94.2, 91.86],
'technology':[93.18, 93.18],
'psychology':[93.92, 93.82],
'interesting':[89.72, 89.72],
'wikipedia':[84.92, 84.92],
'research':[84.6, 84.6],
'religion':[94.76, 94.38],
'music':[97.26, 92.9],
'math':[95.56, 93.86],
'development':[93.96, 93.96],
'theory':[94.22, 94.22],
'philosophy':[93.0, 91.0],
'article':[90.34, 90.34],
'language':[94.22, 92.56],
'science':[88.62, 86.72],
'programming':[90.58, 89.88],
'history':[84.78, 81.22],
'software':[92.42, 92.22]
}



import matplotlib.pyplot as plot   
tags=d2v.keys()
d=[d2v[i] for i in tags]
t=[tf[i] for i in tags]
w=[w2v[i] for i in tags]



dd,=plot.plot(xrange(len(d)-1),zip(*d)[0][1:],label="doc2vec")
rr,=plot.plot(xrange(len(d)-1),zip(*d)[1][1:],label="maxclass")
tt,=plot.plot(xrange(len(d)-1),zip(*t)[0][1:],label="tf-idf")
ww,=plot.plot(xrange(len(d)-1),zip(*w)[0][1:],label="word2vec")
plot.legend([dd,rr,tt,ww], ['doc2vec' , 'maxclass','tf-idf','word2vec'])
plot.xlabel("tags")
plot.ylabel("accuracies")
plot.show()

wiki ,art , reference ,people ,culture,books,design , politics , technology , psychology , interesting , wikipedia , research , religion , music , math , development , theory , philosophy , article , language , science , programming , history , software
"""

