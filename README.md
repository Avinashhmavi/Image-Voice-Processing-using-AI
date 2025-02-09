### 🤖😎Multimodal AI Application

Welcome to the **Multimodal AI Application**, a powerful tool that combines image analysis, text-to-speech (TTS), and speech-to-text (STT) capabilities into one seamless interface. Built with modern AI technologies, this app allows you to interact with images, generate lifelike speech, and transcribe audio effortlessly.

## Table of Contents
1. [Features](#features)
2. [Pre-Installation Steps](#pre-installation-steps)
3. [How to Run the App](#how-to-run-the-app)
4. [Application Workflow](#application-workflow)
5. [Dependencies](#dependencies)
6. [Contributing](#contributing)
7. [License](#license)

---

## Features

### 1. **Image Analysis**
   - Analyze uploaded images using advanced AI models.
   - Ask specific questions about the image (e.g., "Is there something wrong with my face?").
   - Powered by **Groq API** for state-of-the-art vision models.

### 2. **Text-to-Speech (TTS)**
   - Convert text into natural-sounding speech.
   - Choose between two TTS engines:
     - **gTTS**: Google Text-to-Speech for simple and reliable voice generation.
     - **ElevenLabs**: High-quality, customizable voices for professional-grade audio output.

### 3. **Speech-to-Text (STT)**
   - Transcribe uploaded audio files into text.
   - Utilizes **Groq API's Whisper model** for accurate transcription.

### 4. **Cross-Platform Audio Playback**
   - Automatically detects your operating system (macOS, Windows, Linux) and plays generated audio files seamlessly.

### 5. **Streamlit Interface**
   - A clean, intuitive web-based interface powered by **Streamlit**.
   - Easy-to-use file uploaders, buttons, and interactive elements for a smooth user experience.

---

## Pre-Installation Steps

Before running the application, ensure you have the following prerequisites installed:

### 1. **Python Environment**
   - Install Python 3.8 or higher from [python.org](https://www.python.org/downloads/).

### 2. **Install Dependencies**
   - Clone this repository:
     ```bash
     git clone https://github.com/your-repo/multimodal-ai-app.git
     cd multimodal-ai-app
     ```
   - Create a virtual environment (optional but recommended):
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
   - Install the required libraries:
     ```bash
     pip install -r requirements.txt
     ```

### 3. **Environment Variables**
   - Create a `.env` file in the root directory of the project and add your API keys:
     ```plaintext
     GROQ_API_KEY=your_groq_api_key_here
     ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
     ```
   - Replace `your_groq_api_key_here` and `your_elevenlabs_api_key_here` with your actual API keys.

### 4. **System Tools**
   - Ensure you have the following tools installed based on your operating system:
     - **macOS**: `afplay` (pre-installed).
     - **Windows**: PowerShell (pre-installed).
     - **Linux**: Install `aplay`, `mpg123`, or `ffplay` for audio playback:
       ```bash
       sudo apt-get install alsa-utils mpg123 ffmpeg
       ```

---

## How to Run the App

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open the provided local URL in your browser (e.g., `http://localhost:8501`).
3. Follow the instructions in the app interface to analyze images, generate speech, or transcribe audio.

---

## Application Workflow

### Step 1: Analyze an Image
   - Upload an image file (JPEG, PNG).
   - Enter a query related to the image.
   - Click "Analyze Image" to get insights from the AI model.

### Step 2: Convert Text to Speech
   - Enter the text you want to convert into speech.
   - Select a TTS engine (`gTTS` or `ElevenLabs`).
   - Click "Generate Speech" to create and play the audio file.

### Step 3: Transcribe Audio
   - Upload an audio file (MP3, WAV).
   - Click "Transcribe Audio" to convert the audio into text.

---

## Dependencies

The application relies on the following Python libraries:

| Library          | Purpose                          |
|------------------|----------------------------------|
| `streamlit`      | Web interface                   |
| `groq`           | Image analysis and STT          |
| `gtts`           | Text-to-Speech (Google TTS)     |
| `elevenlabs`     | High-quality TTS                |
| `speech_recognition` | Speech recognition utilities |
| `pydub`          | Audio processing                |
| `dotenv`         | Load environment variables      |

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Contributing

We welcome contributions to improve this project! Here’s how you can help:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request on GitHub.

---


## Description

The **Multimodal AI Application** is more than just a tool—it's your gateway to exploring the limitless possibilities of artificial intelligence. Whether you're diagnosing issues in images, creating lifelike voiceovers, or transcribing interviews, this app empowers you to do it all with ease. With its sleek Streamlit interface and robust backend powered by cutting-edge AI models, this application is designed to inspire creativity and efficiency.

Unlock the power of AI today—analyze, speak, and listen like never before!

---
