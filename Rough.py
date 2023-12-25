import random
import pyttsx3
import speech_recognition as sr

def created():
    speak("My name is VEE AI i am created by Varun of second chance")    


def take_cmd():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        global query
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
        global a
        command = take_cmd()
        if command is not None:
            a = command
            break


# speak
engine = pyttsx3.init('sapi5')   
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("varun")
#print(voices)
def greet():
    speak(f"Hello how are you ")
    speak("my name is varun AI ")
    
def math():
    i1 = random.randint(10,100)
    i2 = random.randint(10,100)
    i3 = random.randint(10,100)
    i4 = random.randint(10,100)
    print("get a paper and pencil ")
    
    ques1 = int(input(f'{i1} + {i3} = '))
    if ques1 == i1 + i3 :
        speak("Congratulation you got this !!! ")
    else:
        speak("Wrong ! Try Again")
        print(i1 + i3 , "is the corret answer ")
    
    
    ques2 = int(input(f'{i2} + {i4} = '))
    if ques2 == i2 + i4 :
        speak("Congratulation you got this !!! ")
    else :
        speak("Wrong ! Try Again")
        speak(i2 + i4 , "is the corret answer ")
        # speak(f"wrong answer{i2 + i4} is correct answer")
    
    
    ques3 = int(input(f'{i3} + {i4} = '))
    if ques3 == i3 + i4 :
        speak("Congratulation you got this !!! ")
    else :
        speak("Wrong ! Try Again")
        print(i3 + i4 , "is the corret answer ")
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
        user_ans = input(question + " ").lower().strip()
        
        if user_ans == answer.lower().strip():
            speak("Correct!")
        elif user_ans == "exit".lower().strip():
            break
        else:
            speak("Incorret , Try again ")
           
if __name__ == "__main__":
    greet()
    listen()
    while True:
        if "math" in query.strip().lower() or "mathe" in query.stripe().lower() or "mate" in query.stripe().lower():
            math()
        elif "general" in query.strip().lower() or "genral" in query.strip().lower():
            gk(qdic)
        elif "created" in query.strip().lower():
                created()
        else :
            speak("Could you please say it again ")

