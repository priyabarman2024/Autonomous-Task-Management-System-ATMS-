import datetime
from googleapiclient.discovery import build
from google.oauth2 import service_account

class GoogleCalendar:
    def __init__(self, credentials_file):
        self.credentials_file = credentials_file
        self.service = None
        self.authenticate()

    def authenticate(self):
        # Authenticate using the service account credentials
        creds = service_account.Credentials.from_service_account_file(
            self.credentials_file, 
            scopes=["https://www.googleapis.com/auth/calendar"]
        )
        # Build the service object to interact with the Google Calendar API
        self.service = build('calendar', 'v3', credentials=creds)

    def create_event(self, event_details):
        # Use the service to create an event in Google Calendar
        event = self.service.events().insert(
            calendarId='primary', 
            body=event_details
        ).execute()
        print(f"Event created: {event['summary']} on {event['start']['dateTime']}")
