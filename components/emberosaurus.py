import spacy
import torch
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from itertools import chain


class Emberosaurus:
    def __init__(self, ember_model):
        self.ember = ember_model
        self.nlp = spacy.load("en_core_web_trf")
        self.lemmatizer = WordNetLemmatizer()

    def _get_synonyms(self, word, pos):
        nltk.download("wordnet", quiet=True)
        synonyms = set(
            chain.from_iterable(
                [w.lemma_names() for w in wordnet.synsets(word, pos=pos)]
            )
        )
        lemmatized_word = self.lemmatizer.lemmatize(word, pos=pos)
        synonyms.discard(lemmatized_word)
        return list(synonyms)

    def _spacy_to_nltk_pos(self, spacy_pos):
        mapping = {"ADJ": "a", "ADV": "r", "NOUN": "n", "VERB": "v"}
        return mapping.get(spacy_pos, None)

    def ranked_synonyms(self, sentence, word):
        doc = self.nlp(sentence)
        word_pos = self._spacy_to_nltk_pos(
            [token.pos_ for token in doc if token.text == word][0]
        )
        synonyms = self._get_synonyms(word, word_pos)

        # original_embedding = self.ember.get_sentence_embedding(sentence)
        original_embedding = self.ember.get_word_embedding(sentence, word)
        similarity_scores = {}

        for synonym in synonyms:
            modified_sentence = sentence.replace(word, synonym)
            # modified_embedding = self.ember.get_sentence_embedding(modified_sentence)
            modified_embedding = self.ember.get_word_embedding(
                sentence, modified_sentence
            )
            similarity = torch.cosine_similarity(
                original_embedding, modified_embedding, dim=1
            )
            similarity_scores[synonym] = similarity.item()

        ranked = sorted(
            similarity_scores.items(), key=lambda item: item[1], reverse=True
        )

        return ranked
