import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to listen to the user's voice command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""

# Function to respond to commands
def respond(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        now = datetime.datetime.now()
        speak(f"The current time is {now.strftime('%I:%M %p')}")
    elif "date" in command:
        today = datetime.date.today()
        speak(f"Today's date is {today.strftime('%B %d, %Y')}")
    elif "search" in command:
        speak("What do you want to search for?")
        query = listen()
        if query:
            url = f"https://www.google.com/search?q={query}"
            speak(f"Searching for {query}")
            webbrowser.open(url)
    else:
        speak("Sorry, I don't understand that command.")

# Main function
def main():
    speak("Hi, I am your voice assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            if "exit" in command or "quit" in command:
                speak("Goodbye!")
                break
            respond(command)

if __name__ == "__main__":
    main()
