import streamlit as st
# from backend import convert_speech_to_text  # Import the function from backend.py
# from backend import convert_speech_to_text, text_to_speech
from backend import convert_speech_to_text, text_to_speech, get_language_code


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
        audio_filename = text_to_speech(translated_text, target_code)
        st.write("Audio File Name:", audio_filename)  # Add this line to print the filename

        # Add play button to listen to the generated audio file 
        audio_file = open(audio_filename, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")


# Run the frontend
if __name__ == "__main__":
    main()
