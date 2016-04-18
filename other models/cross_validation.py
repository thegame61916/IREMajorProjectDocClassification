import random
import pickle

from tag_extractor import newlabeldict as labeldict,newlabels as alllabels
from doc_extractor import docdict

print "importing done"

#DIVIDE IN TEST AND TRAN with labels


#SOME DOCUMENTS ANURAG EXTRACTED BUT NOT THERE IN TAG DICT I CREATED , HENCE REMOVE THEM
for i in docdict.keys():
    if i not in labeldict:  #all those documents in docdict for whom i dont have label
        del docdict[i]

for i in labeldict.keys():
    if i not in docdict:    #all those document in labeldict for whom i dont have documents
        del labeldict[i]

assert len(labeldict) == len(docdict)

dockeys=labeldict.keys() #THIS ORDER IS IMPORTANT

#Random shuffle
random.shuffle(dockeys)

#take first 5000 as test
testkeys=dockeys[0:5000]
trainkeys=dockeys[5000:len(dockeys)]

#check whether alltestlabels are in alltrainlabels
testlabels=set()
for i in testkeys:
	testlabels.update(labeldict[i])

trainlabels=set()
for i in trainkeys:
	trainlabels.update(labeldict[i])

assert set(testlabels)==set(trainlabels)==set(alllabels)
#if assertion fails then do again shuffle

#if assertion passed, now get train, test, trainlabels, trainlabels
	
	#Testing data
testdocs=[docdict[i] for i in testkeys]
testlabels=[labeldict[i] for i in testkeys]

	#Training data
traindocs=[docdict[i] for i in trainkeys]
trainlabels=[labeldict[i] for i in trainkeys]

#DUMP EVERYTHING
print "starting storing"
pickle.dump([dockeys,testdocs,testlabels,traindocs,trainlabels],open("data.pickle","w"))
print "storing done"

