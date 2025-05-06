**🇷🇼 Kinyarwanda Voice Assistant**

A mini voice assistant built with Python that listens to speech in Kinyarwanda, processes the input, and responds using synthesized speech.
It uses speech recognition, simple intent matching, and text-to-speech — making it ideal for demonstrating conversational AI in low-resource languages.

**✨ Features**

- 🎙️ **Automatic Speech Recognition (ASR)** using SpeechBrain
- 🧠 **Natural Language Processing (NLP)** with pretrained KinyaRoberta or keyword matching
- 🔊 **Text-to-Speech (TTS)** using `gTTS` (Swahili is used as a workaround for Kinyarwanda)
- 📁 Option to choose between microphone input or pre-recorded .wav audio files
- 🗣️ Responds to basic questions in Kinyarwanda
- 🖥️ Simple terminal interface — say `"rekera aho"` to exit

**Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Musi-si/kinyarwanda_voice_assistant.git
   cd kinyarwanda_voice_assistant

2. **Set up virtual environment (optional but recommended)**:
   
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

   ```bash
   choco install ffmpeg

4.  **Usage (run)**:
   ```bash
   python main.py