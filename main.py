import random
import pyttsx3
import speech_recognition as sr

def created():
    speak("My name is VEE AI. I am created by Varun of Second Chance.")

def take_cmd():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print('Recognizing...')
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print('Sorry, I could not understand. Please try again.')
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def listen():
    while True:
        command = take_cmd()
        if command is not None:
            return command

# speak
engine = pyttsx3.init('sapi5')   
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    speak("Hello! How are you?")
    speak("My name is Varun AI.")
    speak("what you want to play")
    print("Hello! How are you?")
    print("My name is Varun AI.")
    print("what you want to play")

def math():
    i1 = random.randint(10, 100)
    i3 = random.randint(10, 100)
    speak("Get a paper and pencil.")

    speak(f"What is {i1} plus {i3}?")
    print(f"What is {i1} plus {i3}?")
    user_answer = int(listen())

    if user_answer == i1 + i3:
        speak("Congratulations! You got this.")
    else:
        speak("Wrong! Try again.")
        speak(f"The correct answer is {i1 + i3}.")
        print(f"The correct answer is {i1 + i3}.")

# Add your general knowledge questions here
qdic = {
    "What is the largest ocean in the world?": "Pacific Ocean",
    "What is the highest mountain in the world?": "Mount Everest",
    "What is the longest river in the world?": "Nile River",
    "What is the world's most populous country?": "China",
    "What is the official language of India?": "Hindi",
    "What is the national currency of India?": "Indian Rupee",
    "What is the national animal of India?": "Tiger",
    "What is the national bird of India?": "Peacock",
    "What is the national flower of India?": "Lotus",
    "What is the national sport of India?": "Hockey",
    "When did India gain independence from British rule?": "August 15, 1947",
}

def gk(question_dict):
    for question, answer in question_dict.items():
        speak(question)
        user_ans = listen().lower().strip()

        if user_ans == answer.lower().strip():
            speak("Correct!")
        elif user_ans == "exit":
            break
        else:
            speak("Incorrect. Try again.")

if __name__ == "__main__":
    greet()
    while True:
        query = listen()

        if "math" in query or "mate" in query:
            math()
        elif "general" in query or "journal" in query:
            gk(qdic)
        elif "created" in query:
            created()
        elif "run" in query:
            speak("i loved to play with you ")
            break
        else:
            speak("Could you please say it again?")


