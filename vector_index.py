import faiss

class VectorIndex:
    def __init__(self, vectors, vector_categories):
        d = len(vectors[0])
        nb = len(vectors)
        nlist = max(1, int(nb / 10))
        quantizer = faiss.IndexFlatL2(d)
        index = faiss.IndexIVFFlat(quantizer, d, nlist, faiss.METRIC_L2)
        index.train(vectors)
        index.add(vectors)
        index.nprobe = 5
        self.index = index
        self.vector_categories = vector_categories
    
    def _vote(self, indices):
        index_categories = [self.vector_categories[i] for i in indices]
        chosen_category = max(set(index_categories), key=index_categories.count)
        return chosen_category
        
    
    def search(self, vectors):
        k = 5
        all_indices = self.index.search(vectors, k)[1]
        categories = [self._vote(indices) for indices in all_indices]
        return categories