import requests
import json

def fetch_tomtom_traffic(api_key, lat, lon):
    url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point={lat}%2C{lon}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'currentSpeed': data['flowSegmentData']['currentSpeed'],
            'freeFlowSpeed': data['flowSegmentData']['freeFlowSpeed'],
            'confidence': data['flowSegmentData']['confidence']
        }
    else:
        print(f"Error fetching data for {lat}, {lon}")
        return None
