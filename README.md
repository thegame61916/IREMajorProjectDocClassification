prereq: gensim, numpy, slkearn.
for word2vec : word2vec model to be stored as "model.en", in features/word2vec_extraction

#for data
uploaded here:
https://drive.google.com/file/d/0B6UrE1zfRs68Rm9kM2ZyOFBkbEk/view?usp=sharing
has a "docdict.pickle" stores a dictonary mapping from document_ids to documents
and tag-data.xml

#for running LDA
1. Download the data from http://nlp.uned.es/social-tagging/wiki10+/. Download both the files: wiki10+_tag-data.tar.gz and wiki10+_documents.tar.bz2 and extract both.
2. Create a file containing docuemnt texts in format "docID: text" using all the docs in wiki10+_documents.tar.bz2. Name it as "docText". Create a mapping doc to tag and save it in "doctag.txt".
3. Run "python tag_extractor.py". Copy the top 25 tags from output to a file "topcategories". Now run "python transformTopCateg.py".
4. Now run "python createXML.py" and compress the output file "new.xml" in bz2 format. Name it as "wiki.tar.bz2".
5. Install gensim from https://radimrehurek.com/gensim/install.html and run script "python -m gensim.scripts.make_wiki wiki.tar.bz2 wiki_en"
6. Extract the contents of file "wiki_en_wordids.text.bz2". Now run "python lda.py". It'll generate all the topics in file "topics". Open the file and remove all other logs except the topics.
7. Run "python createQueryFile.py"
8. Run "python "docTopicDistribution.py"
9. Run "python mapcateg.py".
10. Now open "queries" file and "topictag" file. Manually check which topic is matched to which query and keep on the best category in "topictag" file for that paricular topic. Remove others.
11. Run "python ldaTest.py" to check the accuracy of learnt model.
12. To test any random text. Write it in file "test" and run "python testRandom.py".

#for "OTHER MODELS"
place docdict.pickle and tag-data.xml in the folder other models

	
##running the vector based models
run cross_validation.py to create a dump "data.pickle" with the data in following manner
[alllabels,testkeys,testdocs,testlabels,trainkeys,traindocs,trainlabels] 
alllabels is list/set of all labels considerd, current code only top 25 considered
where test is possibly of 5000 documents and train with around 15000
keys is the list of hashes, i.e.  the document names
docs are list of documents in the order in which keys are stored
labels are list of set of labels (each document is multi-labeled) in the same order as corresponding keys

###Feature Extraction
once data.pickle is ready, generate vectors, by running either 
features/tf_idf_features.py     
features/word2vec_extraction/word2vec_features.py       
features/doc2vec_extraction/doc2vec_train.py    

once feature extraction is done 
edit the variable in this file, for example for tf-idf
vector_source="tf_idf_vectors.txt"

###Classification
then to run the classifier, open python shell in the features folder:

  >>>from classifiers import *  
  >>>print accuracy

#other links

Github webpage link: http://ravitejatv.github.io/IREMajorProjectDocClassification/

Youtube video link: https://www.youtube.com/watch?v=N4DimsHMu4g&feature=youtu.be

Presentation slideshare link: http://www.slideshare.net/MohitSharma634/wikipedia-document-classification-60966086

Dropbox link to ppt,report and video https://www.dropbox.com/sh/6dfbi9l568fn5hw/AABknCo7PfnnUlzOkyRVciAVa?dl=0

Tags :Wikipedia, Document Classification, Word2Vec, Doc2Vec, LDA, Topic Modeling, tf-idf, Information Retrieval Extraction, Machine Learning, gensim, Latent Dirichlet allocation, SVM, Natural Language Processing, Stochastic Gradient Design, wiki, Information Retrieval and Extraction Course', IIIT-H, Major Project, Pattern Recognition, sklearn
