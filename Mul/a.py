import logging
from gensim.corpora import WikiCorpus
logging.info("Love Live!")
wiki_corpus = WikiCorpus('zhwiki-20190520-pages-articles-multistream.xml.bz2',dictionary={})
texts_num = 0
with open("wiki_texts.txt",'w',encoding='utf-8') as output:
    for text in wiki_corpus.get_texts():
        output.write(''.join(text)+'\n')
        texts_num += 1
        if texts_num % 10000 == 0:
            logging.info("Processed %d articles" % texts_num)
