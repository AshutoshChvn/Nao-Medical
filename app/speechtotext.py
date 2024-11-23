from django.core.files.storage import FileSystemStorage
from pydub import AudioSegment
import speech_recognition as sr
from django.conf import settings
import os

def transcribe_audio(request):
    if request.method == 'POST':
        request_file = request.FILES.get('document')

        fs = FileSystemStorage()
        uploaded = False
        transcript = None

        if request_file:
            if request_file.name.endswith(('.wav', '.mp3')):

                filename = fs.save(request_file.name, request_file)
                uploaded = True

                if uploaded:
                    file_path = fs.path(filename)

                    if not file_path.endswith('.wav'):
                        audio = AudioSegment.from_file(file_path)
                        wav_path = file_path.split('.')[0] + '.wav'
                        audio.export(wav_path, format='wav')
                        file_path = wav_path

                    r = sr.Recognizer()

                    with sr.AudioFile(file_path) as source:
                        audio_listened = r.record(source)

                        try:
                            # Perform speech recognition on the audio
                            transcript = r.recognize_google(audio_listened)
                        except sr.UnknownValueError:
                            transcript = "Sorry, I couldn't understand the audio."
                        except sr.RequestError as e:
                            transcript = f"Sorry, there was an error with the speech recognition service: {e}"

        return transcript
