from flask import Flask, request, Response, send_from_directory
from twilio.twiml.voice_response import VoiceResponse, Gather
from twilio.rest import Client
from groq import Groq
import os

# Initialize Flask
app = Flask(__name__)

AUDIO_DIR = "static"
os.makedirs(AUDIO_DIR, exist_ok=True)

# Twilio Credentials (Replace with yours)
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
MY_PHONE_NUMBER = os.getenv('MY_PHONE_NUMBER')

twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Initialize the Groq client
client = Groq(api_key=os.getenv('GROQ_API_KEY'))  # Add your API key here
ngrok_url = os.getenv('NGROK_URL')  # Replace with your ngrok URL

# Messages for Groq conversation context
messages = [
    {
        "role": "system",
        "content": """You are a highly knowledgeable and professional mentor female voice assistant who can solve any query regarding to career choice. Provide insightful, personalized, and practical guidance to students regarding their career and academic path. Focus on delivering clear, concise, expert advice using natural, conversational language suitable for Hindi translation and speech.  Be encouraging and supportive. Keep responses short and to the point. Start with the greeting and flow should be human-like. Behave like you are his friend and guide."""
    }
]

@app.route("/voice", methods=['POST'])
def voice():
    """Handles incoming voice calls from Twilio."""
    response = VoiceResponse()
    response.say("Namaste, aap kaise hai?", voice="Polly.Aditi", language="hi-IN" )
    gather = Gather(input="speech", action="/process_voice", method="POST", language="hi-IN", speechTimeout="auto")
    gather.say("कृपया अपनी समस्या बताएं।", voice="Polly.Aditi", language="hi-IN")
    response.append(gather)
    return Response(str(response), content_type='text/xml')

@app.route("/process_voice", methods=['POST'])
def process_voice():
    """Processes user Hindi speech input, generates a response, and returns a spoken reply."""
    response = VoiceResponse()
    speech_text = request.form.get("SpeechResult", "")

    if not speech_text:
        response.say("मुझे आपकी आवाज़ सुनाई नहीं दी, कृपया फिर से बोलें।", voice="Polly.Aditi", language="hi-IN")
        response.redirect("/voice")  # Retry input
        return Response(str(response), content_type='text/xml')

    print(f"User said: {speech_text}")

    # Generate AI response using Groq
    ai_response = generate_response(speech_text)
    print(f"AI response: {ai_response}")

    # Stream the response back to the user
    response.say(ai_response, voice="Polly.Aditi", language="hi-IN" )

    # Continue the conversation
    gather = Gather(input="speech", action="/process_voice", method="POST", language="hi-IN", speechTimeout="auto")
    response.append(gather)
    return Response(str(response), content_type='text/xml')

def generate_response(prompt):
    """Uses Groq to generate AI responses in Hindi based on conversation context."""
    messages.append({"role": "user", "content": prompt})

    try:
        ai_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Replace with your preferred Groq model
            messages=messages,
            max_tokens=32768,
            temperature=0.5,
            n=1
        )
        res = ai_response.choices[0].message.content.strip()
        #print(res)
        messages.append({"role": "system", "content": res})
        return res
    except Exception as e:
        print(f"Error generating response: {e}")
        return "मुझे क्षमा करें, मैं आपकी सहायता नहीं कर सकता।"


def make_call():
    try:
        call = twilio_client.calls.create(
            url=f'{ngrok_url}/voice',  # URL to the TwiML response
            to=MY_PHONE_NUMBER,  # Replace with the user's phone number
            from_=TWILIO_PHONE_NUMBER  # Your Twilio phone number
        )
        print(f"Call SID: {call.sid}")
    except Exception as e:
        print(f"Error making call: {e}")

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serves static files like audio WAV files."""
    return send_from_directory("static", filename)  

if __name__ == "__main__":
    make_call()
    app.run(host='0.0.0.0', port=5000)