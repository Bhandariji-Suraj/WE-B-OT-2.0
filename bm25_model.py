from rank_bm25 import BM25Okapi
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

class BM25Model:
    def __init__(self, summaries, links):
        """
        Initialize BM25 model with summaries and corresponding links.
        """
        self.links = links
        tokenized_corpus = [word_tokenize(summary.lower()) for summary in summaries]
        self.bm25 = BM25Okapi(tokenized_corpus)

    def search(self, query, top_n=5):
        """
        Search the corpus for the query and return top N results.
        """
        tokenized_query = word_tokenize(query.lower())
        scores = self.bm25.get_scores(tokenized_query)
        sorted_indices = scores.argsort()[-top_n:][::-1]
        results = [{"link": self.links[i], "score": scores[i]} for i in sorted_indices]
        return results
