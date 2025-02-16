# Import necessary libraries
import os
from dotenv import load_dotenv
import base64
from groq import Groq
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
import subprocess
import platform
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Load API keys from .env
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
ELEVENLABS_API_KEY = st.secrets["ELEVENLABS_API_KEY"]

# Step 1: Encode image to base64
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

# Step 2: Analyze image with query using Groq API
def analyze_image_with_query(query, model, encoded_image):
    client = Groq(api_key=GROQ_API_KEY)
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
    ]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )
    return chat_completion.choices[0].message.content

# Step 3: Text-to-Speech with gTTS
def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)
    play_audio(output_filepath)

# Step 4: Text-to-Speech with ElevenLabs
def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    play_audio(output_filepath)

# Helper function to play audio based on OS
def play_audio(output_filepath):
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        st.error(f"An error occurred while trying to play the audio: {e}")

# Step 5: Record audio from microphone (Not directly supported in Streamlit, so we'll skip this for now)
# Instead, allow users to upload an audio file.
def transcribe_with_groq(stt_model, audio_filepath):
    client = Groq(api_key=GROQ_API_KEY)
    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=stt_model,
            file=audio_file,
            language="en"
        )
    return transcription.text

# Streamlit App
def main():
    st.title("🤖✨Multimodal AI Application")

    # Image Upload Section
    st.header("Step 1: Analyze an Image🖼️📷")
    uploaded_image = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        encoded_image = encode_image(uploaded_image)
        query = "Is there something wrong with my face?"
        model = "llama-3.2-90b-vision-preview"
        if st.button("Analyze Image"):
            analysis_result = analyze_image_with_query(query, model, encoded_image)
            st.write("Image Analysis Result:", analysis_result)

    # Text-to-Speech Section
    st.header("Step 2: Convert Text to Speech🎙️🎤")
    input_text = st.text_input("Enter text to convert to speech", value="Hi, this is AI with Avinash!")
    tts_choice = st.selectbox("Choose TTS engine", ["gTTS", "ElevenLabs"])
    output_filepath = "output.mp3"
    if st.button("Generate Speech"):
        if tts_choice == "gTTS":
            text_to_speech_with_gtts(input_text, output_filepath)
        elif tts_choice == "ElevenLabs":
            text_to_speech_with_elevenlabs(input_text, output_filepath)
        st.success(f"Speech generated! Saved to {output_filepath}")
        st.audio(output_filepath)

    # Speech-to-Text Section
    st.header("Step 3: Transcribe Audio🎚️🎛️")
    uploaded_audio = st.file_uploader("Upload an audio file for transcription", type=["mp3", "wav"])
    if uploaded_audio:
        with open("uploaded_audio.mp3", "wb") as f:
            f.write(uploaded_audio.read())
        st.success("Audio file saved locally.")
        stt_model = "whisper-large-v3"
        if st.button("Transcribe Audio"):
            transcription = transcribe_with_groq(stt_model, "uploaded_audio.mp3")
            st.write("Transcription:", transcription)

if __name__ == "__main__":
    main()
