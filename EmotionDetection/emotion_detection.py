import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

def emotion_detector(text_to_analyze):
    api_url = "https://api.meaningcloud.com/sentiment-2.1"
    api_key = os.getenv('API_KEY')
    params = {
        'key': api_key,
        'lang': 'en',  # Language of the text
        'txt': text_to_analyze,
    }
    try:
        response = requests.post(api_url, data=params)
        if response.status_code == 200:
            sentiment_info = response.json()
            return sentiment_info
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return response
    except requests.exceptions.RequestException as e:
        print(f"exception {e}: {type(e)}")
