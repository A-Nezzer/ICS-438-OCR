from receipt_parser import ReceiptParser
import os
import glob
import json

def parse_receipts(openai_key):
    parser = ReceiptParser(openai_key)

    script_directory = os.path.dirname(os.path.abspath(__file__))
    text_directory = os.path.join(script_directory, "text")
    json_directory = os.path.join(script_directory, "json")

    if not os.path.exists(text_directory):
        os.makedirs(text_directory)
        
    if not os.path.exists(json_directory):
        os.makedirs(json_directory)
        
    def receipt_json_from_file(path):
        with open(path, 'r') as file:
            content = file.read()
            return parser.receipt_json(content)

    def is_valid_json(json_string):
        try:
            json.loads(json_string)
            return True
        except json.JSONDecodeError:
            return False

    for filename in os.listdir(text_directory):
        file_path = os.path.join(text_directory, filename)
        print(f"{filename}")
        if os.path.isfile(file_path) and filename.endswith(".txt"):
            json_str = receipt_json_from_file(file_path)
            if is_valid_json(json_str):
                json_filename = filename.replace(".txt", ".json")
                json_obj = json.loads(json_str)
                with open(os.path.join(json_directory, json_filename), 'w') as json_file:
                    json.dump(json_obj, json_file)
                    print(f"Wrote to {json_filename}")
            else:
                print("Invalid JSON")
                
