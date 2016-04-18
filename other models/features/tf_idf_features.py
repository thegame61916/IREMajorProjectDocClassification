# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:55:25 2016

@author: anves_000
"""

#EACH VECTORISZER FILE loads from ../data.pickle



import nltk
import pickle
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

[alllabels,testkeys,testdocs,testlabels,trainkeys,traindocs,trainlabels] = pickle.load(open("../data.pickle","r"))

stemmer=PorterStemmer()
stop_word_list=open("english_stopwords.txt").read().split("\n")


print "load done"
V={}
k=0

def tokenise(strings):    #to include stemming , is it "tokenize"?, i dont care
    r=nltk.word_tokenize(strings)
    for i in xrange(len(r)):
        r[i]=stemmer.stem(r[i])
    return r


#ORDER : TEST + TRAIN 

#MAIN ORDER IN WHICH VECTORS AND LABELS WILL BE STORED
docvalues=testdocs + traindocs
vectorizer = TfidfVectorizer(tokenizer=tokenise, stop_words='english', max_features = 500, sublinear_tf = True,min_df=1,lowercase=True)
a=vectorizer.fit_transform(docvalues) #notice order in a and order in dockeys same
pickle.dump(a,open("tf_idf_matrix.pickle","w"))
matrix=a.todense()
f=open("tf_idf_vectors.txt","w")

for i in matrix:
    l=i.tolist()[0]
    f.write(' '.join(map(str,l)))
    f.write("\n")
    
f.close()
#vectors stored
#storing labels




"""
   
 
for i in docdict:
    k=k+1
    if k%100==0:
        print k
    #PRE_PROCESSING
    docdict[i]=nltk.word_tokenize(docdict[i].lower())   #case folding and Tokenisation
    for j in xrange(len(docdict[i])):
        word=docdict[i][j]
        if word in stop_word_list:              #Stop word removal
            docdict[i][j]=""
            continue
        docdict[i][j]=stemmer.stem(word)       #STemming
"""
