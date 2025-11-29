import sounddevice as sd
import wavio
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

# Text-to-Speech Engine Initialization
def talk(text):
    import pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()  

def record_audio(filename="input.wav", duration=5, fs=44100):
    try:
        print("Listening...")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished
        wavio.write(filename, recording, fs, sampwidth=2)
        return filename
    except Exception as e:
        talk(f"Recording error: {e}")
        return None

def listen():
    recognizer = sr.Recognizer()
    audio_file = record_audio()

    if audio_file is None:
        return ""

    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print("You said:", command)
            return command
    except sr.UnknownValueError:
        talk("Sorry, I didn't understand that.")
    except sr.RequestError:
        talk("Sorry, the speech recognition service is not available.")
    except Exception as e:
        talk(f"Error recognizing audio: {e}")

    return ""

def run_assistant():
    command = listen()

    if "hello" in command:
        talk("Hello there! How can I help you?")
    
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is {time}")
    
    elif "date" in command:
        date = datetime.datetime.now().strftime('%A, %B %d, %Y')
        talk(f"Today is {date}")
    
    elif "search for" in command:
        search_query = command.replace("search for", "").strip()
        talk(f"Searching the web for {search_query}")
        pywhatkit.search(search_query)

    elif "thank you" in command:
        talk("No worries at all!\nIt was my pleasure!\nI'm happy to assist you!")
        exit()
    
    elif "exit" in command or "stop" in command :
        talk("No worries at all!\nIt was my pleasure!\nI'm happy to assist you!")
        exit()
    
    else:
        talk("Sorry, I didn't understand. Try saying something else.")

# Main loop
if __name__ == "__main__":
    while True:
        run_assistant()