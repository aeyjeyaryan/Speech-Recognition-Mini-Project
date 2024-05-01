import speech_recognition as sr 
import pyttsx3 
import datetime
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os


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
        speak("Good Afternoon, babe")   

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
        print(f"Babe's Command: {query}\n")
        return query.lower()

    except Exception as e:
        print("Say that again please...")  
        return "None"

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()

        if 'give me a kiss' in query:
            kiss_dir = 'D:\KISS'
            sound = os.listdir(kiss_dir)
            print(sound)    
            os.startfile(os.path.join(kiss_dir, sound[0]))
            # Load and display the image
            img_path = r'C:\Users\sahil\Downloads\51e5db4c98038f075c3e752dfd03badf.jpg'
            img = mpimg.imread(img_path)
            plt.imshow(img)
            plt.axis('off')  #turning off the axix label
            plt.show()
            break   #exiting the loop


