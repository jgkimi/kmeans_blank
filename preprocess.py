import re

class Preprocess(object):
    def __init__(self, texts):
        self.texts=texts#list of strings
        self.tokenized=[]
        self.cleaned=[]
        self.tf=list()
        self.df=dict()

    def remove_stopwords_punct(self, fn_stopwords='stopwords.txt'):
        """
        This function makes self.cleaned(a list of texts)
        which contains stopwords & punctuations-removed texts.
        """

        if not self.texts:
            print 'Error: Texts should be given first.'
            return 

        self.cleaned=[text.lower() for text in self.texts]
        self.cleaned=[re.sub('[,.?";:\-!@#$%^&*()]', '', text) for text in self.cleaned]

        if fn_stopwords:
            f_stopword=open(fn_stopwords, 'r')
            self.stopwords=set([line.strip() for line in f_stopword.readlines()])
            f_stopword.close()
            self.cleaned=[text.split() for text in self.cleaned]
            for i, text in enumerate(self.cleaned):
                self.cleaned[i]=" ".join([word for word in text if word not in self.stopwords])
    
    def tokenization(self, N=1):
        """
        This function tries to tokenize the texts in self.cleaned into
        'N'-sized pieces.

        RESULT should be contained by self.tokenized which is a list of lists of N-grams.
        """
        if not self.cleaned:
            print 'Calling the rmv function because we have not tokenized the texts yet. (Tokenization requires distillation on the texts.)'
            self.remove_stopwords_punct()
        
        self.tokenized=[text.split() for text in self.cleaned]
        #No matter what the method is, tokenization is nessesary.
        #1-gram(BOW): this is only needed.
        #More than 1: further processing is needed

        if N > 1:
            SOT='<SOT>' # start of text
            EOT='<EOT>' # end of text
            for text in self.tokenized:
                for i in range(N-1):
                    text.append(EOT)
            new_tokenized=[[] for text in self.tokenized]
            for i, text in enumerate(self.tokenized):
                for j, word in enumerate(text):
                    ngram=[]
                    '''
                    BLANK - hint: using 'for'.
                    *ngram should contain not only the current word, but also previous N-1 words.
                    '''
                    new_tokenized[i].append(" ".join(ngram)) # Replace a token with the ngram (str type)
            self.tokenized=new_tokenized
        #self.tokenized[text_idx][ngram_idx] is mapped to its ngram(str).

    def make_vectors(self, method='tf-idf'):
        """
        Given a list of texts, this function builds a dictionary('self.tf') that maps every word to its frequency(tf). Also, self.idf can be generated in tf-idf case. Finally, self.vectors is filled up.
        """

        for text in self.tokenized:#counting each ngram
            tf=dict()#term to freq for each text
            for ngram in text:
                try:
                    tf[ngram]+=1
                except KeyError:
                    tf[ngram]=1.0
            self.tf.append(tf)

            for unique_ngram in set(text):#if this text contains the n-gram at least once
                try:
                    self.df[unique_ngram]+=1
                except KeyError:
                    self.df[unique_ngram]=1.0
        #self.tf[text_idx][ngram] is mapped to its term frequency.
        #self.df[ngram] is mapped to its document frequency.
        if method=='tf-idf':
            '''
            BLANK - Calculate tf-idf using self.tf and self.df. Then, fill self.vectors up with the tf-idf.
            * tfidf[text_idx][ngram] should be mapped to its tf-idf.
            '''
        elif method=='tf':
            self.vectors=self.tf

    def get_vectors(self):
        return self.vectors
    
    def get_texts(self):
        return self.texts
