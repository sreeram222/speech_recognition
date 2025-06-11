# This script uses the SpeechRecognition library to recognize speech from an audio file.
import speech_recognition as sr

def recognize_speech_from_microphone():#to recognize speech from microphone
    recognizer= sr.Recognizer()# create a recognizer instance
    mic=sr.Microphone()# create a microphone instance
    # Adjust the recognizer sensitivity to ambient noise

    while True:
        try:
            with mic as source:
                print("please speak something")
                audio = recognizer.listen(source) # listen for the first phrase and extract it into audio data
                print("Recognizing...")
                text = recognizer.recognize_google(audio)# recognize speech using Google Web Speech API
                print(f"You said: {text}")
                # return text
                if text.lower() == "stop":# if user says "stop"
                    print("Exiting the program.")
                    break# exit the loop if user says "exit"
        except sr.UnknownValueError:# if speech is unintelligible
            print("Sorry, I did not understand that. Please try again.")# prompt user to try again
        except sr.RequestError as e:
            print(f"Could not request results; {e}. Please check your internet connection.")# handle request errors
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")# handle other exceptions
            
recognize_speech_from_microphone()# call the function to recognize speech from microphone
