#for data
uploaded here:
https://drive.google.com/file/d/0B6UrE1zfRs68Rm9kM2ZyOFBkbEk/view?usp=sharing
has a "docdict.pickle" stores a dictnary from document_ids to documents
and the original tag-data.xml

#for "OTHER MODELS"
place docdict.pickle and tag-data.xml in the folder other models
prereq: gensim, numpy, slkearn.
	for word2vec : word2vec model to be stored as "model.en", in features/word2vec_extraction
	
#running the vector based models
run cross_validation.py to create a dump "data.pickle" with the data in following manner
[alllabels,testkeys,testdocs,testlabels,trainkeys,traindocs,trainlabels] 
alllabels is list/set of all labels considerd, current code only top 25 considered
where test is possibly of 5000 documents and train with around 15000
keys is the list of hashes, i.e.  the document names
docs are list of documents in the order in which keys are stored
labels are list of set of labels (each document is multi-labeled) in the same order as corresponding keys

#
once data.pickle is ready, generate vectors, by running either 
features/tf_idf_features.py
features/word2vec_extraction/word2vec_features.py
features/doc2vec_extraction/doc2vec_train.py

once feature extraction is done 
edit the variable in this file, for exaample for tf-idf
	vector_source="tf_idf_vectors.txt"

then to run the classifier, open python shell:

from classifiers import *
print accuracy
