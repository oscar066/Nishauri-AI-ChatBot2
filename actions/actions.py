# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted, SlotSet
from rasa_sdk.executor import CollectingDispatcher

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Provide a message to the user
        dispatcher.utter_message(text="I am passing you to a human. Please hold on.")

        # Retrieve the contact information
        contact_info = "You can reach out to the human at the following contact number: 0719696313"

        # Send the contact information to the user
        dispatcher.utter_message(text=contact_info)
        
        # Assume there's a function to call customer service
        # Pass the tracker so that the agent has a record of the conversation between the user and the bot for context

        #call_customer_service(tracker)
     
        # Pause the tracker so that the bot stops responding to user input
        return [ConversationPaused(), UserUtteranceReverted()]





# Appointment booking Action         

class AppointmentBooking(Action):
    def name(self) -> Text:
        return "action_appointment_booking"

    def run(self, dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        day = tracker.get_slot("day")
        date = tracker.get_slot("date")

        # Logic to process the appointment booking and store the details

        appointment_details = f"Appointment booked for {name} on {day}, {date}."
        
        dispatcher.utter_message(text=appointment_details)

        return []

# # Setting up Medication reminder action

# class SetMedicationReminder(Action):
#     def name(self) -> Text:
#         return "action_set_medication_reminder"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         medication = tracker.get_slot("medication")
#         time = tracker.get_slot("time")

#         # Logic to set medication reminder and store the details

#         reminder_message = f"A reminder has been set for you to take {medication} at {time}."

#         dispatcher.utter_message(text=reminder_message)

#         return []

# # Advanced setting up medical reminders 

# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.types import DomainDict
# from googleapiclient.discovery import build
# from google.oauth2 import service_account

# # Path to your Google service account credentials JSON file
# SERVICE_ACCOUNT_FILE = "/path/to/your/service_account_credentials.json"

# class SetMedicationReminder(Action):
#     def name(self) -> Text:
#         return "action_set_medication_reminder"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         medication = tracker.get_slot("medication")
#         time = tracker.get_slot("time")

#         # Authenticate and build the Google Calendar service
#         credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=["https://www.googleapis.com/auth/calendar"])
#         service = build("calendar", "v3", credentials=credentials)

#         # Logic to create a medication reminder event in the user's calendar
#         event = {
#             "summary": "Medication Reminder",
#             "description": f"Take {medication} at {time}.",
#             "start": {
#                 "dateTime": "YYYY-MM-DDT" + time + ":00",
#                 "timeZone": "UTC"
#             },
#             "end": {
#                 "dateTime": "YYYY-MM-DDT" + time + ":00",
#                 "timeZone": "UTC"
#             },
#             "reminders": {
#                 "useDefault": False,
#                 "overrides": [
#                     {"method": "popup", "minutes": 15}
#                 ]
#             }
#         }

#         # Insert the event into the user's calendar
#         calendar_id = "primary"  # or specify the calendar ID of the user's specific calendar
#         event = service.events().insert(calendarId=calendar_id, body=event).execute()

#         reminder_message = f"A medication reminder has been set for you to take {medication} at {time}."
#         dispatcher.utter_message(text=reminder_message)

#         return []

