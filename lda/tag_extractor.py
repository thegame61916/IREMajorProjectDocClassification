import xml.sax	 
from collections import Counter
import matplotlib.pyplot as plot   
from copy import deepcopy     

        
tags=[]             #list of xml tags
labels=[]           #list of all labels
labeldict={}        #hash to labels mapping
titledict={}        #hash to title mapping
class XMLhandler(xml.sax.ContentHandler):
    def __init__(self):
        self.tags=[]            #list of all tags
        self.articlenumber=0
        self.content=""
        self.articlehash=""
        self.hash=""
    def startElement(self,name,attrs):      #runs at start of all tags (name)
        if name not in self.tags:
            self.tags.append(name)
            tags.append(name)
            self.content=""
    def endElement(self,name):
        if name=="hash":
            self.hash=self.content.strip()
            labeldict[self.hash]=[]
        if name=="name":
            labels.append(self.content.strip())
            labeldict[self.hash].append(self.content.strip())
        if name=="title":
            titledict[self.hash]=self.content.strip()
        self.content= ""
                                
    def characters(self,content):
        w = content.encode('utf-8').strip()
        if w > 0:
            self.content+= w + "\n"
            
            
#XML PARSING         
source = "tag-data.xml"       
parser = xml.sax.make_parser()
parser.setContentHandler(XMLhandler())
parser.parse(source)   

#NOTE in the xml file "css"  and "files" also come in the <hash>....</hash>, so i remove them manually
labeldict.pop("css")
labeldict.pop("files")

#TO TAKE LABELS WITH AT LEAST N OCCURENCES ONLY
N=100
freqs = Counter(labels)
pairs=sorted(freqs.items(), key=lambda item: item[1], reverse=True)
XY=zip(*pairs[:500])
plot.plot(range(len(XY[1])),XY[1])
index= zip(*pairs)[1].index(N-1) - 1

newpairs=pairs[:index+1]
newlabels=zip(*newpairs)[0]
newlabeldict=deepcopy(labeldict)



#REMOVE EXTRA LABELS FROM LABEL DICTIONARY (HASH-LABEL MAPPING)
#ALSO CHECK IF WE LOST ANY DOCUMENT; IN CASE A DOCUMENT HAS 0 LABELS

se=set(newlabels)
for i in labeldict:
    newlabeldict[i]=se.intersection(labeldict[i])
    if len(newlabeldict[i])==0:
        newlabeldict.pop(i)
        
#TURNS OUT WE LOST 31 DOCUMENTS
        
k=deepcopy(newlabeldict)
for i in newlabeldict:
    a= str(len(labeldict[i]))
    b=str(len(k[i]))
    if a==b:
        print str(len(labeldict[i])) + "--->" + str(len(k[i]))
print len(pairs)
for i in range(0,40):
	print pairs[i]
