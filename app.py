import os

from groq import Groq
import streamlit as st
import requests
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
from streamlit_option_menu import option_menu

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_DeepSeek_Model_KEY")

# Initialize Groq Client
client = Groq(api_key=api_key)

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get chatbot response from DeepSeek model via Groq API
def get_chat_response(user_input):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": user_input}],
        model="deepseek-r1-distill-llama-70b",
    )
    return chat_completion.choices[0].message.content if chat_completion.choices else "Error: Unable to fetch response"

# Speech-to-text function
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Could not understand"
        except sr.RequestError:
            return "Error with speech recognition service"

# Streamlit UI
st.set_page_config(page_title="AI Chatbot", layout="wide")
st.title("🤖 AI Chatbot with Voice Assistance")

# Sidebar for navigation
# menu = st.sidebar.radio("Navigation", ["Home", "Assistant"])
with st.sidebar:
    menu = option_menu(
        menu_title="Main Menu",
        options=["Home", "Assistant"],
        icons=["house", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

if menu == "Home":
    st.header("Welcome to AI Chatbot")
    st.write("This chatbot uses DeepSeek AI on Groq API for responses.")
    st.write("Use voice or text input to interact with the chatbot.")

elif menu == "Assistant":
    st.header("Chat Assistant")
    user_input = st.text_input("Enter your message:")
    
    if st.button("Send"):
        if user_input:
            response = get_chat_response(user_input)
            st.write("💬 Bot:", response)
            speak(response)
        else:
            st.warning("Please enter a message.")
    
    if st.button("🎤 Speak"):
        spoken_text = recognize_speech()
        st.write("🎙 You said:", spoken_text)
        if spoken_text:
            response = get_chat_response(spoken_text)
            st.write("💬 Bot:", response)
            speak(response)

# Run using: streamlit run app.py
