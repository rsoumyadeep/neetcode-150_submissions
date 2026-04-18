import datetime
import os.path
import re
import json

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# ---------------- CONFIG ----------------
SCOPES = ['https://www.googleapis.com/auth/calendar']
MD_FILE = '../problems.md'
PROCESSED_FILE = 'processed.json'

# ---------------- AUTH ----------------
def get_calendar_service():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)

# ---------------- PARSE MARKDOWN ----------------
def parse_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Matches:
    # ## 18-04-2026
    # - Problem 1
    # - Problem 2
    pattern = r'## (\d{2}-\d{2}-\d{4})\n((?:- .+\n)+)'
    matches = re.findall(pattern, content)

    data = []
    for date_str, problems_block in matches:
        problems = [
            p.strip('- ').strip()
            for p in problems_block.strip().split('\n')
        ]
        data.append((date_str, problems))

    return data

# ---------------- DATE PARSER ----------------
def parse_date(date_str):
    return datetime.datetime.strptime(date_str, "%d-%m-%Y")

# ---------------- PROCESSED TRACKING ----------------
def load_processed():
    try:
        with open(PROCESSED_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_processed(data):
    with open(PROCESSED_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_key(date_str, problem):
    return f"{date_str}::{problem}"

# ---------------- CREATE EVENTS ----------------
def create_event(service, summary, event_date, recurrence=None):
    event = {
        'summary': summary,
        'start': {'date': event_date.strftime('%Y-%m-%d')},
        'end': {'date': event_date.strftime('%Y-%m-%d')},
        'reminders': {
            'useDefault': False,
            'overrides': [{'method': 'email', 'minutes': 60}]
        }
    }

    if recurrence:
        event['recurrence'] = recurrence

    service.events().insert(calendarId='primary', body=event).execute()

def create_events(service, date_str, problem):
    base_date = parse_date(date_str)

    # spaced repetition intervals
    intervals = [0, 1, 3, 7]

    for i in intervals:
        event_date = base_date + datetime.timedelta(days=i)
        create_event(service, f"Revise: {problem}", event_date)

    # weekly repetition after day 7
    weekly_start = base_date + datetime.timedelta(days=7)

    create_event(
        service,
        f"Revise Weekly: {problem}",
        weekly_start,
        recurrence=['RRULE:FREQ=WEEKLY']
    )

# ---------------- MAIN ----------------
def main():
    service = get_calendar_service()
    data = parse_md(MD_FILE)

    processed = load_processed()

    new_count = 0

    for date_str, problems in data:
        for problem in problems:
            key = get_key(date_str, problem)

            if key in processed:
                continue

            print(f"Scheduling: {problem} ({date_str})")
            create_events(service, date_str, problem)

            processed[key] = True
            new_count += 1

    save_processed(processed)

    print(f"\nDone. {new_count} new problems scheduled.")

# ---------------- RUN ----------------
if __name__ == '__main__':
    main()
