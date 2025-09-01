import os
import datetime
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
to_number = os.getenv("TO_NUMBER")
from_number = os.getenv("FROM_NUMBER")
whatsapp_from = os.getenv("WHATSAPP_FROM")
whatsapp_to = os.getenv("WHATSAPP_TO")

client = Client(account_sid, auth_token)

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

# The new function to check the time and call the appropriate reminder
def run_scheduled_task():
    now_utc = datetime.datetime.utcnow()
    day_of_week = now_utc.weekday()  # Monday is 0 and Sunday is 6
    hour = now_utc.hour
    minute = now_utc.minute

    # Sunday 7:30 AM IST (02:00 UTC)
    if day_of_week == 6 and hour == 2 and minute == 0:
        every_sun_leetcode_7_30am()
    
    # Wednesday 7:30 PM IST (14:00 UTC)
    elif day_of_week == 2 and hour == 14 and minute == 30:
        every_wed_codechef_7_30pm()

    # Saturday 7:30 PM IST (14:00 UTC)
    elif day_of_week == 5 and hour == 14 and minute == 30:
        every_sat_leetcode_7_30pm()

    # Saturday 10:00 AM IST (04:30 UTC)
    elif day_of_week == 5 and hour == 4 and minute == 30:
        every_sat_codechef_10am()

    # Thursday 7:30 PM IST (14:00 UTC)
    elif day_of_week == 3 and hour == 14 and minute == 30:
        every_thurs_naukri_7_30pm()
    
    else:
        print("No scheduled task to run at this time.")

# This line ensures the function is called when the script is run
if __name__ == "__main__":
    run_scheduled_task()