import streamlit as st
from backend import convert_speech_to_text  # Import the function from backend.py
from backend import convert_speech_to_text, text_to_speech

# Frontend UI layout
def main():
    st.title("Speech Translator")
    st.write("Select source and target languages:")
    source_language = st.selectbox("Source Language", ["English", "Hindi", "Bengali", "Telugu", "Marathi", "Tamil", "Urdu", "Gujarati", "Kannada", "Odia", "Malayalam", "Punjabi", "Assamese", "Maithili", "Santali", "Kashmiri", "Nepali", "Konkani", "Sindhi"])
    target_language = st.selectbox("Target Language", ["English", "Hindi", "Bengali", "Telugu", "Marathi", "Tamil", "Urdu", "Gujarati", "Kannada", "Odia", "Malayalam", "Punjabi", "Assamese", "Maithili", "Santali", "Kashmiri", "Nepali", "Konkani", "Sindhi"])

    
    # Convert source and target languages to language codes (e.g., 'en', 'hi', 'ta', 'te')
    source_code = get_language_code(source_language)
    target_code = get_language_code(target_language)

    if st.button("Start Recording"):
        translated_text = convert_speech_to_text(source_code, target_code)
        st.write("Translated Text:", translated_text)

        # Convert translated text to speech and save as audio file
        text_to_speech(translated_text, target_code)

        # Add play button to listen to the generated audio file 
        audio_file = open("translated_audio.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

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

# Run the frontend
if __name__ == "__main__":
    main()
