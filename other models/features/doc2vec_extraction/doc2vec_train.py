import gensim, logging
import codecs
import sys
import nltk
from nltk.stem.porter import PorterStemmer
import pickle
[alllabels,testkeys,testdocs,testlabels,trainkeys,traindocs,trainlabels] = pickle.load(open("../../data.pickle","r"))

stop_word_list=open("english_stopwords.txt").read().split("\n")
stemmer=PorterStemmer()
#FOR TRAINING
"""

documents=testdocs+traindocs
#for tokenizing first 
for i in xrange(len(documents)):
	tokens=nltk.word_tokenize(documents[i])
	for j in xrange(len(tokens)):
		if tokens[j] in stop_word_list:
			tokens[j]=""
			continue
		tokens[j]=stemmer.stem(tokens[j])
	if i%100==0:
		print i
	documents[i]=" ".join(tokens)



#tokenization done
print "tokenization done"
print "writing"
f=open("data.txt","w")
for i in documents:
	f.write(i)
	f.write("\n")
f.close()



class LabeledLineSentence(object):
    def __init__(self, filename):
        self.filename = filename
    def __iter__(self):
        for lid, line in enumerate(codecs.open(self.filename,encoding='utf-8')):
            yield gensim.models.doc2vec.LabeledSentence(words=line.split(), tags=[lid])

def model_generator(filename,lang_tag):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    #textfile = codecs.open(filename,encoding='utf-8')
    lines = LabeledLineSentence(filename)
    for line in lines:
    	print line
    model = gensim.models.doc2vec.Doc2Vec(lines, size=300, window=4, min_count=0, workers=4)
    #try:
    #    print model.docvecs['0']
    #except:
    #    print model.docvecs[0]
    model.save('model.'+lang_tag)

model_generator("data.txt","en")

"""

#once traines
print "begin modeling doc2vec"
model=gensim.models.doc2vec.Doc2Vec.load("model.en")
vectors=model.docvecs

f=open("doc2vec_vectors.txt","w")
for i in vectors:
	f.write(" ".join(map(str,list(i))))
	f.write("\n")

f.close()


