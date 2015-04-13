from gensim import corpora, models, similarities

documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]

# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in documents]

# remove words that appear only once
all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)

texts = [[word for word in text if word not in tokens_once] for text in texts]

dictionary = corpora.Dictionary(texts)
corp = [dictionary.doc2bow(text) for text in texts]

# extract 400 LSI topics; use the default one-pass algorithm
lsi = models.lsimodel.LsiModel(corpus=corp, id2word=dictionary, num_topics=400)

# print the most contributing words (both positively and negatively) for each of the first ten topics
lsi.print_topics(400)