from transformer_model import TransformerModel
import json
import os
import numpy as np
from vector_index import VectorIndex

def train(model):
    def process_category_files(directory):
        embeddings = []
        categories = []
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                category = filename.split(".")[0]
                file_path = os.path.join(directory, filename)
                with open(file_path, 'r') as file:
                    for line in file:
                        text = line.strip()
                        if text:
                            embedding = model.embedding(text)
                            embeddings.append(embedding)
                            categories.append(category)
        return np.array(embeddings, dtype=np.float32), categories

    script_directory = os.path.dirname(os.path.abspath(__file__))
    categories_directory = os.path.join(script_directory, "categories")

    embeddings, categories = process_category_files(categories_directory)

    return VectorIndex(embeddings, categories)