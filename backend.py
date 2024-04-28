import streamlit as st
import speech_recognition as sr
from googletrans import Translator
import os
import datetime
from gtts import gTTS

# Initialize SpeechRecognizer and Translator
recognizer = sr.Recognizer()
translator = Translator()

# Define backend function to convert speech to text and translate 
def convert_speech_to_text(source_language, target_language):
    with sr.Microphone() as source:
        st.write("Speak now...")
        audio_data = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_data, language=source_language)
            st.write("Original Speech Text:", text)
            translated_text = translator.translate(text, dest=target_language).text
            return translated_text
        except sr.UnknownValueError:
            return "Unable to recognize speech"
        except sr.RequestError as e:
            return "Could not request results; {0}".format(e)

# Define backend function to convert translated text to speech and save as audio file
def text_to_speech(translated_text, target_language):
    # Create a directory named "Audio" if it doesn't exist
    if not os.path.exists("Audio"):
        os.makedirs("Audio")
    
    # Generate a timestamp for the filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Generate the filename with the timestamp and target language code
    filename = f"Audio/{timestamp}_{target_language}.mp3"

    try:
    # Convert text to speech and save as audio file
        tts = gTTS(translated_text, lang=target_language)
        tts.save(filename)
        return filename  # Return the filename if conversion is successful
    except Exception as e:
        print(f"Error occurred during text-to-speech conversion: {e}")
        return None  # Return None if conversion fails

# Define a function to map language names to language codes
def get_language_code(language):
    language_mapping = {
        "English": "en",
        "Kannada": "kn",
        "Hindi": "hi",
        "Bengali": "bn",
        "Telugu": "te",
        "Marathi": "mr",
        "Tamil": "ta",
        "Urdu": "ur",
        "Gujarati": "gu",
        "Kannada": "kn",
        "Odia": "or",
        "Malayalam": "ml",
        "Punjabi": "pa",
        "Assamese": "as",
        "Maithili": "mai",
        "Santali": "sat",
        "Kashmiri": "ks",
        "Nepali": "ne",
        "Konkani": "kok",
        "Sindhi": "sd"
        # Add more languages and their codes as needed
    }
    return language_mapping.get(language, "en")  # Default to English if language not found