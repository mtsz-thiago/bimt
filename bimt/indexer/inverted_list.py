from bimt.indexer.cfg import config
from tqdm import tqdm
# from bimt.query import corpus as bimt_corpus

import xml.etree.ElementTree as ET
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from scipy.sparse import coo_matrix

def parse_corpus_xml(root):
    record_list_tags = root.findall('RECORD')
    data = []
    for record_tag in tqdm(record_list_tags):
        abstract_element = record_tag.find("ABSTRACT")
        if abstract_element != None:
            doc_identifier = record_tag.find("RECORDNUM").text
            doc_text = record_tag.find("ABSTRACT").text
            data.append({"doc_identifier": doc_identifier, "doc_text": doc_text})
    return data    

def read_corpus(file_paths):
    corpus_json_data = []
    for fp in file_paths:
        root = ET.parse( fp).getroot()
        corpus_json = parse_corpus_xml(root)
        corpus_json_data.extend(corpus_json)
    
    return corpus_json_data

class InvertedIndex():

    def __init__(self, corpus):
        self.corpus_df = pd.DataFrame(corpus)
        self.corps_tokenized = self.tokenize(self.corpus_df)
        self.create_inverted_list_df(self.corps_tokenized)
        self.write_fo_file(config["DEFAULTS"]["ESCREVA"])

    def tokenize(self, corpus):
        self.vectorizer = CountVectorizer().fit(corpus["doc_text"])
        return self.vectorizer.transform(corpus["doc_text"])

    def create_inverted_list_df(self, tokenized):
        cx = coo_matrix(tokenized)

        tokens = self.vectorizer.get_feature_names()
        num_features = len(tokens)

        self.inv_index = { k:[] for k in tokens }

        for doc_idx, token_idx, token_freq in zip(cx.row, cx.col, cx.data):
            self.inv_index[tokens[token_idx]].extend([doc_idx]*token_freq)

    def write_fo_file(self, path):
        lines = [f"{k};{self.inv_index[k]}\n" for k in self.inv_index.keys()]
        with open(path, "w") as f:
            f.writelines(lines)
        f.close()

    @staticmethod
    def get():
        to_read = config["DEFAULTS"]["LEIA"]
        corpus = read_corpus(to_read)

        return InvertedIndex(corpus)
