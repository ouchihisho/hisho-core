import MeCab
import sys

class Text:
    def __init__(self, string):
        tagger = MeCab.Tagger("-Ochasen")
        self.parsed = tagger.parse(string)

    
