# File: airtable_sync.py

import requests
import json

# Replace with your own Airtable API key and base ID
AIRTABLE_API_KEY = "YOUR_AIRTABLE_API_KEY"
BASE_ID = "YOUR_BASE_ID"
TABLE_NAME = "ZoneRisk"  # Example: one of your 5 tables

AIRTABLE_ENDPOINT = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
HEADERS = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type": "application/json"
}

def get_airtable_data():
    response = requests.get(AIRTABLE_ENDPOINT, headers=HEADERS)
    if response.status_code == 200:
        records = response.json().get("records", [])
        return [{**r['fields'], 'id': r['id']} for r in records]
    else:
        print("Error:", response.text)
        return []

def update_zone_risk(record_id, new_risk):
    data = {
        "fields": {
            "Base Risk": new_risk
        }
    }
    url = f"{AIRTABLE_ENDPOINT}/{record_id}"
    response = requests.patch(url, headers=HEADERS, json=data)
    if response.status_code == 200:
        print(f"Updated risk for record {record_id}")
    else:
        print("Error:", response.text)
