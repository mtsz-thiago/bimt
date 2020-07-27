from bimt.query.cfg import config
from bimt.query import corpus as bimt_corpus

from sklearn.feature_extraction.text import TfidfVectorizer

class ProcessQuery:

    def __init__(self):
        pass

    def __call__(self, query_input):
        print("method to override")


class TFIDF(ProcessQuery):

    def __init__(self, corpus):
        super().__init__()
        self.vectorizer = TfidfVectorizer().fit(corpus)

    def __call__(self, query_input):
        return self.vectorizer.transform(query_input)

    @staticmethod
    def get():
        queries_xml = bimt_corpus.parse_query_file()
        parsed_corpus = bimt_corpus.get_text_corpus_from_queries(queries_xml)
        return TFIDF(parsed_corpus)