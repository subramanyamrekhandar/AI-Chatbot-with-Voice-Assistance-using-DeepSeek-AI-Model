# AI Chatbot with Voice Assistance

## Overview
This project is an AI-powered chatbot with voice assistance, built using **DeepSeek AI** on **Groq API** and a **Streamlit UI**. The chatbot allows users to interact via text or voice input and receive responses using an AI model.

## Features
- **Text-based chatbot interaction**
- **Voice input using speech recognition**
- **Voice output using text-to-speech (TTS)**
- **Uses DeepSeek AI model via Groq API**
- **Simple web-based UI using Streamlit**

## Installation

### Prerequisites
Ensure you have Python 3.9 installed on your system.

### Install Dependencies
Run the following command to install the required Python libraries:
```bash
pip install groq streamlit requests speechrecognition pyttsx3 python-dotenv PyAudio streamlit_option_menu
```

## Environment Variables
Create a `.env` file in the project root directory and add your Groq API key:
```
GROQ_API_DeepSeek_Model_KEY=your_groq_api_key_here
```

## Running the Application
To start the chatbot application, run:
```bash
streamlit run app.py
```

## Usage
1. Navigate to `http://localhost:8501` in your browser.
2. Use the **Home** page for general information.
3. On the **Assistant** page:
   - Type a message and click **Send** to receive a text response.
   - Click **🎤 Speak** to use voice input and get an AI-generated response.

## File Structure
```
├── app.py              # Main application file
├── .env                # Environment variables file
├── README.md           # Project documentation
```

## Future Improvements
- Add session memory for conversation history
- Improve UI/UX with better design elements
- Support multiple AI models

## License
This project is open-source under the MIT License.

---

Let me know if you need modifications or additional details! 🚀

