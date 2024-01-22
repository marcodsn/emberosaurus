import torch
from transformers import AutoModel, AutoTokenizer


class Ember:
    def __init__(self, model_name: str = "llmrails/ember-v1", device: str = "cpu"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name, device_map=device)

    def average_pool(self, last_hidden_states, attention_mask):
        last_hidden = last_hidden_states.masked_fill(
            ~attention_mask[..., None].bool(), 0.0
        )
        return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]

    def get_sentence_embedding(self, sentence: str):
        tokenized_sentence = self.tokenizer(
            [sentence], return_tensors="pt", padding=True, truncation=True
        )
        outputs = self.model(**tokenized_sentence)
        sentence_embedding = self.average_pool(
            outputs.last_hidden_state, tokenized_sentence["attention_mask"]
        )
        return sentence_embedding

    def get_word_embedding(self, word: str, sentence: str):
        tokenized_sentence = self.tokenizer(
            [sentence], return_tensors="pt", padding=True, truncation=True
        )
        outputs = self.model(**tokenized_sentence)

        word_ids = self.tokenizer.convert_tokens_to_ids(self.tokenizer.tokenize(word))
        mask = torch.isin(
            tokenized_sentence["input_ids"], torch.tensor(word_ids)
        ).bool()

        word_embedding = self.average_pool(outputs.last_hidden_state, mask)
        return word_embedding
