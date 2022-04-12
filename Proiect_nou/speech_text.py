import sys
from threading import Thread

import speech_recognition as sr
import pyttsx3
from pyttsx3 import engine


def speechToText(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["success"] = False
        response["error"] = "Unable to recognize speech"
    return response


def textToSpeech(myText):
    engine = pyttsx3.init()
    engine.say(myText)
    engine.runAndWait()


def functieSpeech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    engine = pyttsx3.init()
    action = 'Can I help you?'
    print(action)
    textToSpeech(action)
    quitFlag = True
    while (quitFlag):
        text = speechToText(recognizer, microphone)
        if not text["success"] and text["error"] == "API unavailable":
            print("ERROR: {}\nclose program".format(text["error"]))
            break

        while not text["success"]:
            print("I didn't catch that. What did you say?\n")
            text = speechToText(recognizer, microphone)

        if (text["transcription"].lower() == "exit"):
            quitFlag = False
            sys.exit(0)

        print(text["transcription"].lower())
        textToSpeech(text["transcription"].lower())


def threadFunctionSpeech():
    thread = Thread(target=functieSpeech)
    thread.start()


if __name__ == '__main__':
    threadFunctionSpeech()
