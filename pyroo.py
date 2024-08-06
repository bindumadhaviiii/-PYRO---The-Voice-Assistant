import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia  # Importing wikipedia module
import webbrowser
import os

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def respond(audio):
    print(f"Pyro: {audio}")  # Print the response for debugging
    engine.say(audio)
    engine.runAndWait()

def introduction():
    respond("Hello! I’m Pyro, your friendly assistant. I can help with various tasks and entertain you with interactive stories.")

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        respond("Good Morning!")
    elif hour >= 12 and hour < 18:
        respond("Good Afternoon!")
    else:
        respond("Good Evening!")
    respond("How can I assist you today?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def interactive_story():
    respond("Welcome to the interactive story!")
    respond("You find yourself in a dark forest. There are two paths ahead: a narrow path to the left and a wide path to the right.")
    
    while True:
        choice = input("Which path will you take? (left/right): ").strip().lower()
        
        if choice == "left":
            respond("You take the narrow path and encounter a wise old man who gives you a magical amulet. You feel empowered!")
            break
        elif choice == "right":
            respond("You take the wide path and discover a hidden treasure chest filled with gold. You feel rich!")
            break
        else:
            respond("Invalid choice. Please choose 'left' or 'right'.")

def main():
    introduction()
    wish_me()
    
    while True:
        query = take_command().lower()
        print(f"Debug: Received command: {query}")

        if 'hi' in query or 'hello' in query:
            respond("Hi there! How can I assist you today?")
        
        elif 'bye' in query or 'goodbye' in query:
            respond("Goodbye! Have a great day!")
            break
        
        elif 'story' in query:
            interactive_story()
        
        elif 'joke' in query:
            respond("Why did the scarecrow win an award? Because he was outstanding in his field!")
        
        elif 'wikipedia' in query:
            respond('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            respond("According to Wikipedia")
            respond(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        
        elif 'play music' in query:
            music_dir = 'F:\\Music'  # Update the path as needed
            songs = os.listdir(music_dir)
            respond(f"Playing {songs[0]}")
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"The time is {strTime}")
        
        elif 'open visual studio' in query:
            codePath = "C:\\Users\\om\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Update the path as needed
            os.startfile(codePath)

        else:
            respond("Sorry, I didn't understand that command. You can ask me to tell a story, a joke, or more.")

if __name__ == "__main__":
    main()
