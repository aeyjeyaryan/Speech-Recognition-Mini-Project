import speech_recognition as sr 
import pyttsx3 
import datetime
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hi, Babe. How are you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Boss's Command: {query}\n")
        return query.lower()

    except Exception as e:
        print("Say that again please...")  
        return "None"

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()

        if 'give me a kiss' in query:
            speak("Muaaaah")
            # Load and display the image
            img_path = r'C:\Users\sahil\Downloads\55536b3b6b56d1389cf77a61d7bca7fe.jpg'
            img = mpimg.imread(img_path)
            plt.imshow(img)
            plt.axis('off')  # Turn off axis labels
            plt.show()
            break  # Exit the loop
