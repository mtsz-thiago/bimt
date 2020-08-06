import re

from bimt.indexer.inverted_list import InvertedIndex
from sklearn.feature_extraction.text import TfidfTransformer

class VectorModel():

    def __init__(self, inverted_list):
        self.inverted_list = inverted_list
        self.eliminate_unwanted_tokens()
        self.tfidf_model = TfidfTransformer().fit(self.tokenized)
        self.tfidf = self.tfidf_model.transform(self.tokenized)


    def eliminate_unwanted_tokens(self):
        def keep_token(v):
            return (len(v) > 2) and (re.match("\w+",v) != None)

        tokens = self.inverted_list.vectorizer.get_feature_names()
        self.tokens_idx_to_drop = [i for i,v in enumerate(tokens) if keep_token(v)]
        self.tokenized = self.inverted_list.corps_tokenized[:,self.tokens_idx_to_drop]




    @staticmethod
    def get(inverted_list):
        return VectorModel(inverted_list)