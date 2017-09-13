import random 
from preprocess import Preprocess

def similarity(v1, v2, measure='cos'):
    sim=0.
    if measure=='cos':
        dot=0.
        magv1=0.
        magv2=0.
        for key in v1.keys():
            magv1+=v1[key]**2
            try:
                dot+=(v1[key]*v2[key])
            except KeyError:
                continue
        for key in v2.keys():
            magv2+=v2[key]**2
        
        sim=dot/(magv1 * magv2+ 0.00000000001)
    return sim

class KMeansClustering(object):
    def __init__(self, vectors, k):
        self.centers = random.sample(vectors, k)#init of centers using random.sample()
        for i in range(k):
            self.centers[i]=self.centers[i].copy()
        self.clusters = [[] for c in self.centers]#A cluster has a list that contains indices of the texts that are in the cluster.
        self.vectors = vectors
    def update_clusters(self):
        self.clusters = [[] for c in self.centers]
        for i, vector in enumerate(self.vectors):
            '''
            BLANK - hint: Use similarity(vector, center) to get a value (cosine similarity) of them.
            '''
            self.clusters[sim_to_center.index(mxvalue)].append(i)
    def update_centers(self):
        new_centers = []
        len_cluster=len(cluster)
        for cluster in self.clusters:#for each cluster among k
            new_center=dict()
            for ci in cluster:#for each index of vectors(dict)
            '''
            BLANK - hint: Calculate mean of vectors in the current cluster ci.
            '''
            for axis in new_center.keys():
                new_center[axis]=new_center[axis]/len_cluster
            new_centers.append(new_center)
        if new_centers==self.centers: # In no change case,
            return False
        else:
            return True

    def start(self):
        self.update_clusters()
        while self.update_centers():# M-step
            self.update_clusters()# E-step
    
    def get_clusters(self):
        return self.clusters

def print_clusters(texts, clusters):
    for i in range(len(clusters)):
        print
        print 'Group '+str(i)+': '
        print '========\n'
        print '\n-----\n'.join([texts[ci] for ci in clusters[i]])

    print

def main():
    corpus_fn='corpus.txt'
    stopwords_fn='stopwords.txt'
    num_clusters=2
    cls_method='kmeans'
    tok_ngram=1 #BOW is the same as unigram(1-gram)
    vec_method='tf-idf'

    fr_corp=open(corpus_fn, 'r')
    texts=fr_corp.readlines()
    fr_corp.close()

    '''
    A phase of checks on variables
    '''
    assert num_clusters <= len(texts)
    assert (cls_method=='kmeans')
    assert (type(tok_ngram) == int and tok_ngram>=1)
    assert (vec_method=='tf-idf' or vec_method=='tf')

    '''
    Step 1. Preprocessing
    '''
    prep=Preprocess(texts)
    prep.remove_stopwords_punct(stopwords_fn) # 1. Remove stop words and punctuations
    prep.tokenization(N=tok_ngram)   # 2. Tokenization
    prep.make_vectors(method=vec_method) # 3. Calculation of tf-idf to make vectors


    '''
    Step 2. Clustering
    '''    
    if cls_method=='kmeans':
        clusters=KMeansClustering(prep.get_vectors(), k=num_clusters)
        clusters.start() # 4. Clustering
        print_clusters(prep.get_texts(), clusters.get_clusters())

if __name__=='__main__':
    main()
