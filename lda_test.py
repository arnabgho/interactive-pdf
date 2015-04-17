#!/usr/bin/python
# -*- coding: latin-1 -*-
from gensim import corpora, models, similarities
from gensim.models import hdpmodel, ldamodel
from itertools import izip
from nltk.corpus import stopwords
# documents = ["Human machine interface for lab abc computer applications",
#               "A survey of user opinion of computer system response time",
#               "The EPS user interface management system",
#               "System and human system engineering testing of EPS",
#               "Relation of user perceived response time to error measurement",
#               "The generation of random binary unordered trees",
#               "The intersection graph of paths in trees",
#               "Graph minors IV Widths of trees and well quasi ordering",
#               "Graph minors A survey"]

documents=[''' Casino Royale is the first novel by the British author Ian Fleming. Published in 1953, it is the first James Bond book, and it paved the way for a further eleven novels and two short story collections by Fleming, followed by numerous continuation Bond novels by other authors.

The story concerns the British secret agent James Bond, gambling at the casino in Royale-les-Eaux to bankrupt Le Chiffre, the treasurer of a French union and a member of the Russian secret service. Bond is supported in his endeavours by Vesper Lynd, a member of his own service, as well as Felix Leiter of the CIA and René Mathis of the French Deuxième Bureau. Fleming used his wartime experiences as a member of the Naval Intelligence Division, and the people he met during his work, to provide plot elements; the character of Bond also reflected many of Fleming's personal tastes. Fleming wrote the draft in early 1952 at his Goldeneye estate in Jamaica while awaiting his marriage. He was initially unsure whether the work was suitable for publication, but was assured by his friend, the novelist William Plomer, that the novel had promise.

Within the spy storyline, Casino Royale deals with themes of Britain's position in the world, particularly the relationship with the US in light of the defections to the Soviet Union of the British traitors Guy Burgess and Donald Maclean. The book was given broadly positive reviews by critics at the time and sold out in less than a month after its UK release on 13 April 1953, although US sales upon release a year later were much slower.

Since publication Casino Royale has appeared as a comic strip in a British national newspaper, The Daily Express. It has been also adapted for the screen three times, a 1954 episode of the CBS television series Climax! with Barry Nelson as an American Bond, a 1967 film version with David Niven playing "Sir James Bond", and a 2006 film in the Eon Productions film series starring Daniel Craig as James Bond. ''']
# remove common words and tokenize
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

for topic in lsi.show_topics(1,10):
  print topic