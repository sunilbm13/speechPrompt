import streamlit as st
import speech_recognition as sr
from googletrans import Translator
import os
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
    tts = gTTS(translated_text, lang=target_language)
    tts.save("translated_audio.mp3")