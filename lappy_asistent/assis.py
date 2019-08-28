import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voices', voice[0].id)


def speak(audio):
 engine.say(audio)
 engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
       speak("Good Morning")
    elif hour>=12 and hour<18:
       speak("Good Afternoon")
    else:
       speak("Good Evening")

    speak("I am Your Assistant Madam.Please tell me how may I help you")

def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,)
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that Again Please...")
        return "None"
    return query

if __name__ =='__main__':

    WishMe()
    while True:
      query = takeCommand().lower()

      if 'wikipedia' in query:
          speak('Searching Wikipedia...')
          query = query.replace("Wikipeadia", "  ")
          results = wikipedia.summary(query,sentences=2)
          speak("According to Wikipedia")
          print(results)
          speak(results)

      elif 'open youtube'in query:
          webbrowser.open("youtube.com")

      elif 'open google' in query:
          webbrowser.open("google.com")

      elif 'open stackoverflow' in query:
          webbrowser.open("stackoverflow.com")

      elif 'play music' in query:
          music_dir = 'D:\\personal\\music'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[5]))

      elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Mam,the time is {strTime}")

      elif 'open gmail' in query:
          webbrowser.open("gmail.com")