from shutdown import *
import pyttsx3

def PlayResponse(audio):
    print(audio)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    en_voice_id = "com.apple.speech.synthesis.voice.Alex"
    engine.setProperty('voice', en_voice_id)
    engine.say(audio)
    engine.runAndWait()
    
if __name__ == '__main__':
    PlayResponse("System about to Sleep... Could you Please switch off the Mouse")
    PlayResponse("Thank you..Good Bye..")
    hibernate(force=False)