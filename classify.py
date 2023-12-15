from vector_index import VectorIndex
import os
import json
import numpy as np

def _category(text, model, index):
    embedding = model.embedding(text)
    return index.search(np.array([embedding]))[0]

def _receipt_json_classifiables(receipt_json):
    merchant = receipt_json["ReceiptInfo"]["merchant"]
    item_objects = receipt_json["ReceiptInfo"]["ITEMS"]
    item_descriptions = map(lambda item_obj: item_obj["description"], item_objects)
    return {"merchant": merchant, "items": list(item_descriptions)}

def classify_receipt_from_json(receipt_data, model, index):
    classifiables = _receipt_json_classifiables(receipt_data)
    merchant_category = _category(classifiables["merchant"], model, index)
    items_categories = list(map(lambda item: _category(item, model, index), classifiables["items"]))
    return {"merchant": merchant_category, "items": items_categories}
    
def classify_all_receipts(model, index):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    json_directory = os.path.join(script_directory, "json")
    categorized_directory = os.path.join(script_directory, "categorized")
    if not os.path.exists(categorized_directory):
        os.makedirs(categorized_directory)
    for filename in os.listdir(json_directory):
        if filename.endswith('.json'):
            filepath = os.path.join(json_directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                categorized = classify_receipt_from_json(data, model, index)
                with open(os.path.join(categorized_directory, filename), 'w') as categorized_file:
                  json.dump(categorized, categorized_file)