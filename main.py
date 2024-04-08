import queue
import threading

from RealtimeSTT import AudioToTextRecorder
from RealtimeTTS import TextToAudioStream, SystemEngine
import os

if __name__ == '__main__':

    engine = SystemEngine()
    stream = TextToAudioStream(engine=engine)

    print("Initializing RealtimeSTT test...")

    def clear_console():
        os.system('clear' if os.name == 'posix' else 'cls')


    text_queue = queue.Queue()
    stream_lock = threading.Lock()
    def process_text(text):
        print(text)
        text_queue.put(text)


    def play_text():
        while True:
            text = text_queue.get()
            with stream_lock:
                stream.feed(text)
                while stream.is_playing():
                    pass
                stream.play_async(buffer_threshold_seconds=0.1)



    text_thread = threading.Thread(target=play_text, daemon=True)
    text_thread.start()

    recorder_config = {
        'spinner': False,
        'language': 'en',
        'enable_realtime_transcription': True,
        'post_speech_silence_duration': 0.1,
        'realtime_model_type': 'tiny.en',
    }

    recorder = AudioToTextRecorder(**recorder_config)

    clear_console()
    print("Say something...", end="", flush=True)

    while True:
        recorder.text(process_text)