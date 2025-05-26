import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Scope for Sheets and Drive
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# Authorize using the service account
import json
import os

json_creds = os.environ.get("GOOGLE_CREDS_B64")
if json_creds:
    parsed_creds = json.loads(json_creds)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(parsed_creds, scope)
else:
    raise Exception("GOOGLE_CREDS not found in environment")
client = gspread.authorize(creds)

# Open your sheet using the Google Sheet ID
# Example Sheet URL: https://docs.google.com/spreadsheets/d/1AyOganzN8k9KCixcSYR7bUMyik3_0cAksU99-V_qaUk/edit
SHEET_ID = "1bkh7E_SCd1rtvRxoL6trI--K2NnCzhldQXn8MxIDxR8"  # Replace with your actual Sheet ID
sheet = client.open_by_key(SHEET_ID).sheet1  # If using the first sheet

# Function to log a conversation
def log_conversation(data):
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [
            data.get("modality", "Chatbot"),
            now,
            data.get("phone", "NA"),
            data.get("outcome", "MISC"),
            data.get("room", "NA"),
            data.get("date", "NA"),
            data.get("time", "NA"),
            data.get("guests", "NA"),
            data.get("name", "NA"),
            data.get("summary", "No summary provided")
        ]
        sheet.append_row(row)
        return True
    except Exception as e:
        print("Error while logging:", e)
        return False

def log_post_call(data):
    try:
        sheet = client.open_by_key(SHEET_ID).worksheet("PostCallAnalysis")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([
            data.get("phone", "NA"),
            data.get("modality", "Chatbot"),
            data.get("intent", "Unknown"),
            data.get("success", "No"),
            data.get("issue", "NA"),
            data.get("summary", "No summary"),
            now
        ])
        return True
    except Exception as e:
        print("Post-call logging failed:", e)
        return False

import os, json
from oauth2client.service_account import ServiceAccountCredentials

import os, json, base64
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

try:
    # Decode Base64 env var to credentials.json
    encoded = os.environ.get("GOOGLE_CREDS_B64")
    if not encoded:
        raise Exception("GOOGLE_CREDS_B64 is not set")

    decoded = base64.b64decode(encoded)

    creds_path = os.path.join(os.path.dirname(__file__), "credentials.json")
    with open(creds_path, "wb") as f:
        f.write(decoded)

    with open(creds_path) as f:
        parsed_creds = json.load(f)

    creds = ServiceAccountCredentials.from_json_keyfile_dict(parsed_creds, scope)
    print("✅ Loaded credentials from base64 env and wrote to file")

except Exception as e:
    print(f"❌ Error loading Google credentials: {e}")
