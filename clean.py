# -*- coding: latin-1 -*-
import os
import codecs
from gensim import corpora, models, similarities
from gensim.models import hdpmodel, ldamodel
from itertools import izip
from nltk.corpus import stopwords

os.system("pdftotext -layout test.pdf output.txt")

with open("output.txt") as myfile:
    raw="".join(line.rstrip() for line in myfile)


raw= raw.decode('utf-8')
document=''' '''
for str in raw:
	document=document+str
# documents=raw

documents=[document]

# print documents

stoplist = set(stopwords.words("english"))
# stoplist = set('by is his as was with at it for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in documents]



# remove words that appear only once
all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once]
         for text in texts]

# print texts

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# I can print out the topics for LSA
lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
corpus_lsi = lsi[corpus]

# for l,t in izip(corpus_lsi,corpus):
#   print l,"#",t
# print

res=""
for topic in lsi.show_topics(1,5):
  res= res+ topic

print res
