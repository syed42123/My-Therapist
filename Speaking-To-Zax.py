import openai
import sounddevice as sd
import numpy as np
from scipy.io import wavfile
import tempfile
import pyttsx3
from google.cloud import texttospeech
from google.cloud import texttospeech_v1
import pygame
import os

class VoiceAssistant:
    def __init__(self):
        #API KEY
        openai.api_key = "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"

        # Initialize the assistant's history
        self.history = [
                {"role": "system", "content": "You are an empathetic and supportive online therapist whose name is Zax. Your goal is to provide guidance, understanding, and coping strategies to users who express their thoughts and feelings. Engage in a conversation with the user, ask open-ended questions, offer validation, and suggest healthy ways to manage their emotions. Begin the conversation. Ensure you ask one question at a time, remember you are the therapist"}
            ]
    def listen(self):
        #Recording
        print("Listening...")
        # Record the audio
        duration = 5
        fs = 44100  # Sample rate

        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
        sd.wait()

        # Save the NumPy array to a temporary wav file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav_file:
            wavfile.write(temp_wav_file.name, fs, audio)

            # Use the temporary wav file in the OpenAI API
            transcript = openai.Audio.transcribe("whisper-1", temp_wav_file)

        print(f"User: {transcript['text']}")
        return transcript['text']
    def think(self, text):
        #Generate a response
        self.history.append({"role": "user", "content": text})
        #GPT TIme
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.history,
            temperature=0.8,
            frequency_penalty = 0,
            max_tokens = 150
        )
        # Extract the assistant's response from the API response
        message = dict(response.choices[0])['message']['content']
        self.history.append({"role": "system", "content": message})
        print('Assistant: ', message)
        return message

    def speak(self, text):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'tidal-timer-396506-34c26ca533e1.json'
        client = texttospeech_v1.TextToSpeechClient()

        synthesis_input = texttospeech_v1.SynthesisInput(text=text)

        voice1 = texttospeech_v1.VoiceSelectionParams(
            language_code ='en-UK',
            ssml_gender = texttospeech_v1.SsmlVoiceGender.FEMALE
        )

        voice2 = texttospeech_v1.VoiceSelectionParams(
            name = 'fr-CA-Wavenet-A',
            language_code ='fr-CA',
            ssml_gender = texttospeech_v1.SsmlVoiceGender.FEMALE
        )

        audio_config = texttospeech_v1.AudioConfig(
            audio_encoding=texttospeech_v1.AudioEncoding.MP3
        )

        response = client.synthesize_speech(
            input=synthesis_input,
            voice = voice1,
            audio_config=audio_config
        )
        #creating mp3 file
        with open('audio_file.mp3', 'wb') as output:
            output.write(response.audio_content)

        #playing the mp3 file
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('audio_file.mp3')
        pygame.mixer.music.play()

        # Let the audio play for a while
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.quit()


if __name__ == "__main__":
    assistant = VoiceAssistant()

    while True:
        text = assistant.listen()

        if "goodbye" in text.strip().lower():
            print("Assistant: Goodbye! Have a great day!")
            assistant.speak("Goodbye! Have a great day!")
            break

        response = assistant.think(text)
        assistant.speak(response)
