import speech_recognition as sr

Listen = sr.Recognizer()


with sr.Microphone() as source:
    print("listening...")
    voice = Listen.listen(source)
    command = Listen.recognize_google(voice)
    print(command)