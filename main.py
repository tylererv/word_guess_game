import speech_recognition as sr
import pyaudio
import librosa
import pyttsx3

recog = sr.Recognizer()


# Converts speech to text   ___
def textToSpeech(command) -> None:
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    engine.say(command)  # Queue the provided text (command) for speech synthesis
    engine.runAndWait()  # Process the queue and produce speech output


#
def recogUserAudio(listenDuration: float):
    with sr.Microphone() as source:

        # Wait a second to let recognizer adjust energy
        # threshold based on surrounding noise level
        recog.adjust_for_ambient_noise(source, duration=0.2)

        print("Say something...")
        # Listen for user input (source)
        userAudio = recog.listen(source, phrase_time_limit=listenDuration)

        return userAudio


def audioToText(audio):
    userText: str = None

    try:
        # Perform speech recognition using Google Web Speech API
        userText = recog.recognize_google(audio)
        userText = userText.lower()
        print(f"Did you say: | {userText} |")

    except sr.UnknownValueError:
        # Handle case where audio is not understandable
        print("Sorry, could not understand audio.")

    except sr.RequestError as e:
        # Handle case where Google API is unavailable or other errors occur
        print(f"Error: Could not request results from Google Speech Recognition service; {e}")

    return userText


def run() -> None:

    textToSpeech(audioToText(recogUserAudio(5)))


if __name__ == '__main__':
    run()
