import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()
#r.energy_threshold = 3333

def transcribeAudio():
    # Using microphone as source
    with sr.Microphone() as source:
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        print("Speak now...")
        # record the audio data from the user
        audio_data = r.listen(source)
        print("Recognizing...")

    # recognize speech using Google Speech Recognition
    #if audio_data:
        print('Invoking speech api......' )
        text = r.recognize_google(audio_data)
        #print('Results......' + text)
        return text


#transcribeAudio()
