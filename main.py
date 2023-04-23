import speech_recognition as sr
import pyttsx3
import os
import wikipedia
import time
import pyaudio
import pyautogui

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define the voice assistant function
def voice_assistant():
    # Set up the speech recognition
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Use Google Speech Recognition to convert audio to text
    try:
        command = r.recognize_google(audio).lower()
        print("You said:", command)
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return
    except sr.RequestError:
        print("Sorry, speech service is not available.")
        return

    # Perform different tasks based on user input
    if "open" in command:
        if "chrome" in command:
            os.system("start chrome")
        elif "notepad" in command:
            os.system("start notepad")
        elif "word" in command:
            os.system("start winword")
        else:
            print("Sorry, I cannot open that application.")
    elif "close" in command:
        if "chrome" in command:
            os.system("taskkill /f /im chrome.exe")
        elif "notepad" in command:
            os.system("taskkill /f /im notepad.exe")
        elif "word" in command:
            os.system("taskkill /f /im winword.exe")
        else:
            print("Sorry, I cannot close that application.")

    elif "take a screenshot" in command:
        # Take a screenshot of the current screen
        screenshot = pyautogui.screenshot()
        # Save the screenshot as an image file
        screenshot.save("screenshot.png")

    elif "search" in command:
        query = command.split("search")[-1]
        results = wikipedia.summary(query, sentences=2)
        print(results)
        engine.say(results)
        engine.runAndWait()
    elif "shutdown" in command:
        print("Shutting down...")
        engine.say("Shutting down...")
        engine.runAndWait()
        time.sleep(2)
        os.system("shutdown /s /t 1")
    else:
        print("Sorry, I cannot perform that task.")

# Run the voice assistant function
while True:
    voice_assistant()