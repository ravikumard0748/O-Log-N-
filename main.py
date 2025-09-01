import os
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

load_dotenv()

# Load credentials
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
to_number = os.getenv("TO_NUMBER")            # Your phone number
from_number = os.getenv("FROM_NUMBER")        # Twilio number
whatsapp_from = os.getenv("WHATSAPP_FROM")    # Twilio WhatsApp number
whatsapp_to = os.getenv("WHATSAPP_TO")        # Your WhatsApp number

client = Client(account_sid, auth_token)

# Base message
BASE_MESSAGE = """ 
Ravi, You have a contest today. Kindly check the schedule and prepare.\n
uttratha da dei onnume panna mudiayathu apram pathuko \n
enna vela irrunthalum poi podu da de \n
Travel la irrutha phone coding podu da dei \n
mn mn mn mn mn define who you are \n
"""

def send_whatsapp(msg):
    message = client.messages.create(
        from_=whatsapp_from,
        body=msg,
        to=whatsapp_to
    )
    print("WhatsApp Message SID:", message.sid)

def make_call():
    response = VoiceResponse()
    response.say("Intha phone yaaru attend pannalum sari. Thoongitu irukura Raviya ellupunga. Avanukku oru contest irruku ippo.")
    call = client.calls.create(
        to=to_number,
        from_=from_number,
        twiml=str(response)
    )
    print("Call SID:", call.sid)

# Scheduled tasks
def every_sun_leetcode_7_30am():
    make_call()

def every_sat_leetcode_7_30pm():
    msg = BASE_MESSAGE + "Leetcode: https://leetcode.com/profile/account/"
    send_whatsapp(msg)

def every_wed_codechef_7_30pm():
    msg = BASE_MESSAGE + "CodeChef: https://www.codechef.com/users/ravikumard"
    send_whatsapp(msg)

def every_sat_codechef_10am():
    msg = BASE_MESSAGE + "CodeChef: https://www.codechef.com/users/ravikumard"
    send_whatsapp(msg)

def every_thurs_naukri_7_30pm():
    msg = BASE_MESSAGE + "Naukri/Code360: https://www.naukri.com/code360/contests"
    send_whatsapp(msg)
