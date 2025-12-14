# airtable_sync.py

import requests
import json

# === CONFIGURE THESE VALUES ===
AIRTABLE_API_KEY = 'your_airtable_api_key'
BASE_ID = 'your_base_id'
TABLE_NAME = 'PatrolLogs'

# Airtable API URL
AIRTABLE_ENDPOINT = f'https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}'

# Headers
HEADERS = {
    'Authorization': f'Bearer {AIRTABLE_API_KEY}',
    'Content-Type': 'application/json'
}

def upload_patrol_decision(hour, zone, decision, risk_score):
    record = {
        "fields": {
            "Hour": hour,
            "Zone": zone,
            "Decision": decision,
            "RiskScore": risk_score
        }
    }
    response = requests.post(AIRTABLE_ENDPOINT, headers=HEADERS, data=json.dumps(record))
    if response.status_code == 200 or response.status_code == 201:
        print(f"✅ Uploaded decision for hour {hour}")
    else:
        print(f"❌ Failed to upload: {response.status_code}, {response.text}")

# Example call
# upload_patrol_decision(0, 'A', 'Move to B', 7.5)
