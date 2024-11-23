import pyaudio
import wave
import threading
from django.conf import settings
import os

# Global variable to handle the recording process
frames = []
is_recording = False
stream = None
p = None

# Path where the recording will be saved
AUDIO_FILE_PATH = os.path.join(settings.BASE_DIR, 'recorded_audio.wav')

def start_recording():
    global is_recording, stream, p, frames
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)
    is_recording = True
    frames = []
    
    def record():
        while is_recording:
            data = stream.read(1024)
            frames.append(data)
    
    threading.Thread(target=record).start()

def stop_recording():
    global is_recording, stream, p, frames
    is_recording = False
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    # Save the recorded audio to a file
    with wave.open(AUDIO_FILE_PATH, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))

    print(f"Recording saved to {AUDIO_FILE_PATH}")
