# Learns the lda model saves it in file ldaModel and saves the topics with word probabilities in 'topics' file

import logging, gensim, bz2
import pickle
logging.basicConfig(filename= 'topics',format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

id2word = gensim.corpora.Dictionary.load_from_text('wiki_en_wordids.txt')
mm = gensim.corpora.MmCorpus('wiki_en_tfidf.mm')

lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=25, update_every=1, chunksize=10000, passes=1)
lda.print_topics(25)
lda.save('ldaModel')


