import json

def categorize_receipt(receipt):
    merchant = receipt['ReceiptInfo']['merchant']
    total = receipt['ReceiptInfo'].get('total', 0)

    print(f"Merchant: {merchant}")
    print(f"Total: ${total:.2f}")

    if 'ITEMS' in receipt:
        items = receipt['ITEMS']
        for item in items:
            description = item['description']
            quantity = item['quantity']
            unit_price = item['unitPrice']
            total_price = item['totalPrice']

            print(f"  - {description} (Quantity: {quantity}, Unit Price: ${unit_price:.2f}, Total Price: ${total_price:.2f})")

    print("\n")

# Provided JSON data
json_data = '''
[
    {
        "ReceiptInfo": {
            "merchant": "Longs Drugs",
            "address": "4211 WAIALAE AVE",
            "city": "HONOLULU",
            "state": "HI",
            "phoneNumber": "808.732.0781",
            "tax": 0.77,
            "total": 17.24,
            "receiptDate": "JULY 3, 2023",
            "receiptTime": "2:48 PM"
        },
        "ITEMS": [
            {
                "description": "CFRIO SF PEG BAG 3Z",
                "quantity": 1,
                "unitPrice": 4.59,
                "totalPrice": 4.59,
                "discountAmount": 0
            },
            {
                "description": "CFRIO SF PEG BAG 3Z",
                "quantity": 1,
                "unitPrice": 4.59,
                "totalPrice": 4.59,
                "discountAmount": 0
            },
            {
                "description": "CFRIO SF PEG BAG 3Z",
                "quantity": 1,
                "unitPrice": 4.59,
                "totalPrice": 4.59,
                "discountAmount": 0
            },
            {
                "description": "CR GYSR SPR WTR 33.8",
                "quantity": 1,
                "unitPrice": 1.29,
                "totalPrice": 1.29,
                "discountAmount": 0
            },
            {
                "description": "BOTTLE DEPOSIT",
                "quantity": 1,
                "unitPrice": 0.05,
                "totalPrice": 0.05,
                "discountAmount": 0
            },
            {
                "description": "HI CONTAINER FEE",
                "quantity": 1,
                "unitPrice": 0.01,
                "totalPrice": 0.01,
                "discountAmount": 0
            },
            {
                "description": "CR GYSR SPR WTR 33.8",
                "quantity": 1,
                "unitPrice": 1.29,
                "totalPrice": 1.29,
                "discountAmount": 0
            },
            {
                "description": "BOTTLE DEPOSIT",
                "quantity": 1,
                "unitPrice": 0.05,
                "totalPrice": 0.05,
                "discountAmount": 0
            },
            {
                "description": "HI CONTAINER FEE",
                "quantity": 1,
                "unitPrice": 0.01,
                "totalPrice": 0.01,
                "discountAmount": 0
            }
        ]
    },
    {
        "ReceiptInfo": {
            "merchant": "Halal Gyro Kabob House",
            "address": "240 EAST DELAWARE AVENUE",
            "city": "NEWARK",
            "state": "DE",
            "phoneNumber": "4439937029",
            "tax": 0.00,
            "total": 16.09,
            "receiptDate": "06-Jul-2023",
            "receiptTime": "7:57:49P",
            "paymentMethod": "CONTACTLESS",
            "cardType": "VISA",
            "cardNumber": "**** **** **** 2130",
            "referenceID": "318700509347",
            "authorizationID": "02779D",
            "merchantID": "********3889",
            "AID": "A0000000031010",
            "athNtwkNm": "VISA",
            "onlineLink": "https://clover.com/p/GD5PY93HP0HMM",
            "cloverID": "TEXFAZ7ZA34GM"
        },
        "ITEMS": [
            {
                "description": "#18. Lamb Salad",
                "quantity": 1,
                "unitPrice": 13.99,
                "totalPrice": 13.99,
                "discountAmount": 0.00
            }
        ]
    },
    {
        "ReceiptInfo": {
            "merchant": "Panda Express #2150",
            "address": "Honolulu, HI",
            "phoneNumber": "(808)956-7229",
            "total": 12.67,
            "receiptDate": "6/9/2023",
            "receiptTime": "11:02:50 AM",
            "paymentMethod": "Visa",
            "cardType": "VISA",
            "cardNumber": "XXXX-XXXX-XXXX-9212",
            "authorizationID": "060248",
            "EMV": "Contactless",
            "APL": "VISA DEBIT",
            "AID": "A0000000031010"
        },
        "ITEMS": [
            {
                "description": "1 Plate",
                "quantity": 1,
                "unitPrice": 10.60,
                "totalPrice": 10.60,
                "discountAmount": 0.00
            },
            {
                "description": "FRIED RICE-1/2",
                "quantity": 1,
                "unitPrice": 1.50,
                "totalPrice": 1.50,
                "discountAmount": 0.00
            },
            {
                "description": "STR BN CKN BRST",
                "quantity": 1,
                "unitPrice": 0.00,
                "totalPrice": 0.00,
                "discountAmount": 0.00
            },
            {
                "description": "ORANGE CKN",
                "quantity": 1,
                "unitPrice": 0.00,
                "totalPrice": 0.00,
                "discountAmount": 0.00
            },
            {
                "description": "1 XTRA ENTREE",
                "quantity": 1,
                "unitPrice": 1.50,
                "totalPrice": 1.50,
                "discountAmount": 0.00
            },
            {
                "description": "VEG SPRING <UNKNOWN>",
                "quantity": 1,
                "unitPrice": 0.00,
                "totalPrice": 0.00,
                "discountAmount": 0.00
            }
        ]
    },
    {
        "ReceiptInfo": {
            "merchant": "H MART",
            "website": "http://www.hmart.com",
            "address": "458 Keawe st, Honolulu, 96813"
            
        }
    }
]
'''

# Convert JSON data to Python objects
receipts = json.loads(json_data)

# Categorize and print information for each receipt
for receipt in receipts:
    categorize_receipt(receipt)


