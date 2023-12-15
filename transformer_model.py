from transformers import BertModel, BertTokenizer
import torch
import numpy as np


class TransformerModel:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')

    def embedding(self, text):
        tokenized = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**tokenized)
            return outputs.last_hidden_state[:, 0, :].squeeze().numpy()