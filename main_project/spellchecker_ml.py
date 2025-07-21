import os
import marisa_trie
import difflib

class MalayalamSpellChecker:
    def __init__(self):
        data_dir = os.path.join(os.path.dirname(__file__), 'data')
        rootwords_path = os.path.join(data_dir, 'ml_rootwords.txt')
        with open(rootwords_path, encoding='utf-8') as f:
            self.words = [x.strip() for x in f.readlines()]
        self.dictionary = set(self.words)

    def check(self, word):
        return word in self.dictionary

    def suggest(self, word, n=5):
        # Use difflib to get close matches
        return difflib.get_close_matches(word, self.words, n=n, cutoff=0.7)

    def check_and_generate(self, word):
        if self.check(word):
            return {'status': 1, 'suggestions': []}
        else:
            suggestions = self.suggest(word)
            if suggestions:
                return {'status': 0, 'suggestions': suggestions}
            else:
                return {'status': 2, 'suggestions': []} 