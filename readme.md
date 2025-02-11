# Hindi-Speaking AI Career Counseling Mentor

This repository contains the source code for a **Hindi-speaking AI career counseling mentor** built using **Twilio** for voice interactions and **Groq's LLaMA models** for generating AI responses. The bot provides personalized career guidance to students in Hindi, making it accessible and user-friendly.

## 🚀 Features

- **Voice-Based Interaction**: Users can speak in Hindi, and the bot will respond using Twilio's **Polly.Aditi** voice.
- **AI-Powered Career Guidance**: Uses Groq's LLaMA models to generate intelligent and contextual responses.
- **Twilio Integration**: Handles incoming calls, processes speech input, and delivers responses.
- **Flask Backend**: Manages the API endpoints and processes speech responses.
- **ngrok for Public URL**: Exposes the local Flask server to Twilio for real-time interaction.

---

## 🛠 Tech Stack

- **Twilio**: Voice call handling and speech recognition
- **Groq's LLaMA Models**: AI-generated career counseling responses
- **Flask**: Backend API for handling calls and responses
- **ngrok**: Exposing local server to the internet

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/rugvedp/VoiceBot.git
cd VoiceBot
```

### 2️⃣ Install Dependencies
```bash
pip install flask twilio groq
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add:
```
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_number
MY_PHONE_NUMBER=your_phone_number
GROQ_API_KEY=your_groq_api_key
```

### 4️⃣ Start ngrok
```bash
ngrok http 5000
```
Copy the provided HTTPS URL and update `ngrok_url` in `app.py`.

### 5️⃣ Run the Flask Server
```bash
python app.py
```

---

## 📞 Twilio Configuration
1. Log in to [Twilio Console](https://www.twilio.com/console).
2. Go to **Phone Numbers** → **Manage Numbers** → Select your number.
3. Under **Voice & Fax**, set the Webhook for incoming calls to your `ngrok_url/voice`.

---

## 🏃‍♂️ How It Works
1. **User Calls Twilio Number** → The call is routed to the Flask server.
2. **Twilio Gathers Speech Input** → The user speaks in Hindi.
3. **AI Generates a Response** → The speech is processed and sent to Groq for response generation.
4. **Bot Speaks Back** → Twilio's Polly voice synthesizes the AI response and plays it back to the user.
5. **Continuous Conversation** → The loop continues for further queries.

---

## 🤖 API Endpoints

### `/voice` (POST)
- Handles incoming Twilio voice calls.
- Prompts user to speak their career query.

### `/process_voice` (POST)
- Captures speech input and sends it to Groq.
- Returns AI-generated response as speech.

### `/static/<filename>` (GET)
- Serves static files like pre-recorded responses if needed.

---

## 🔥 Future Enhancements
- **Multi-language Support**: Expand to other Indian languages.
- **Improved NLP**: Fine-tune AI responses for better accuracy.
- **User Session Management**: Maintain conversation history.

---

## 💡 Contributing
Pull requests are welcome! Feel free to fork this repo and suggest improvements.

1. **Fork the repo**
2. **Create a new branch** (`git checkout -b feature-name`)
3. **Commit changes** (`git commit -m "Added new feature"`)
4. **Push to branch** (`git push origin feature-name`)
5. **Create a Pull Request**

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact
For any queries or collaborations, reach out:
- **GitHub**: [your-username](https://github.com/rugvedp)
- **LinkedIn**: [Your Profile](https://linkedin.com/in/rugvedp)

Happy coding! 🚀

