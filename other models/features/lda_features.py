import pickle

[alllabels,testkeys,testdocs,testlabels,trainkeys,traindocs,trainlabels] = pickle.load(open("../data.pickle","r"))


print "load done"

f=open("docTopicDistribution.txt","r")
r=f.readlines()


vectordict={}
for i in r:
	s=i.split(":")
	#vectordict[s[0]]=[float(k) for k in s[1].strip().split(" ")]
	vectordict[s[0]]=s[1]
	
f=open("lda_vectors.txt","w")
for i in testkeys:
	f.write(vectordict[i])

for i in trainkeys:
	f.write(vectordict[i])

