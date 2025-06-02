import sys
import wave
import threading
import pyaudio
import time
import matplotlib.pyplot as mlp
import speech_recognition as sr
import numpy as np

stop_event = threading.Event()

def wait_for_enter():
    input("press enter to stop the recording")
    stop_event.set()

def spinner():
    spinner_chars = '|/-\\'
    i= 0
    while not stop_event.is_set():
        sys.stdout.write('\rrecording..'+spinner_chars[i%len(spinner_chars)])
        sys.stdout.flush()
        i = i+1
        time.sleep(0.1)
    sys.stdout.write("recording stopped!\n")


def until_enter_pressed():
    p = pyaudio.PyAudio()
    format = pyaudio.paInt16
    channels = 1
    frame_per_buffer = 1024
    rate = 16000
    stream = p.open(format = format , channels = channels , rate = rate , input = True, frames_per_buffer= frame_per_buffer)
    f1 = []
    threading.Thread(target = wait_for_enter).start()
    threading.Thread(target = spinner).start()

    while not stop_event.is_set():
        try:
            data = stream.read(frame_per_buffer)
            f1.append(data)
        except Exception as e :
            print(e)
            break
    stream.stop_stream()
    stream.close()

    sample_width = p.get_sample_size(format)
    p.terminate()

    audio_data = b''.join(f1)
    return audio_data , rate , sample_width

def save_audio(data , rate , width , filename="w.wav"):

    with wave.open(filename , "wb") as a:
         a.setnchannels(1)
         a.setsampwidth(width)
         a.setframerate(rate)
         a.writeframes(data)
    print(f"save {filename}")


#saving file and decoding file
def transcribe(data ,rate, width , filename = "transcript.txt"):
    r = sr.Recognizer()
    audio = sr.AudioData(data,rate,width)
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError :
        text = "couldn't recognize ur audio"
    except sr.RequestError as e:
        text = f"api error : {e}"
   
    with open(filename , "w") as f:
        f.write(text)

    print(f"save {filename}")

def wave_form(data,rate):
    samples = np.frombuffer(data,dtype = np.int16)
    time = np.linspace(0,len(samples)/rate , num = len(samples))

    mlp.plot(time,samples)
    mlp.title("audio wave form")
    mlp.ylabel("amlitude")
    mlp.xlabel("time taken")
    mlp.tight_layout()
    mlp.show()







def main():
    print("start speaking and press enter to stop\n")
    audio_data , rate , width = until_enter_pressed()
    save_audio(audio_data, rate , width)
    transcribe(audio_data , rate , width)
    wave_form(audio_data , rate)

main()



