import streamlit as st
import openai
import speech_recognition as sr

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Function to convert speech to text using ChatGPT API
def speech_to_text(audio_content, language):
    prompt = f"Convert the following speech to text: \n\n{audio_content}\n\nLanguage: {language}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=300,
        n=1,
    )
    return response.choices[0].text.strip()

# Streamlit app
def main():
    st.title("Multilingual Speech to Text App")

    # Language selection dropdown
    language = st.selectbox("Select Language", ["English", "Spanish", "French"])

    # Speak button for recording speech
    speak_button = st.button("Speak your query 🎤")

    # Speech-to-text conversion button
    convert_button = st.button("Convert to Text 📝")

    # Placeholder for speech content
    speech_content = ""

    if speak_button:
        st.info("Speak into your microphone and hold the button.")
        
        # Speech recognition using SpeechRecognition library
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        with microphone as source: 
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=10)

        try:
            st.success("Speech captured successfully!")
            speech_content = recognizer.recognize_google(audio)
            st.info(f"Captured Speech: {speech_content}")
        except sr.UnknownValueError:
            st.warning("Speech not recognized. Please try again.")
        except sr.RequestError as e:
            st.error(f"Error with the speech recognition service; {e}")

    if convert_button and speech_content:
        st.info("Converting speech to text...")
        text_result = speech_to_text(speech_content, language)
        st.success(f"Text Result ({language}): {text_result}")

if __name__ == "__main__":
    main()

