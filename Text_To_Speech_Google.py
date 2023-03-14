from google.cloud import texttospeech
import os
import playsound
import random as R
import Constants as Q


# set up Google Cloud Text-to-Speech API credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = Q.GOOGLE_SYSTEM_USER

# function to generate speech from text input and play it
def generate_and_play_speech(text_input):
    print (text_input)
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text_input)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name = "en-US-Neural2-E" if Q.VOICE_GENDER == 'Female' else  "en-US-Neural2-D",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE if Q.VOICE_GENDER == 'Female' else  texttospeech.SsmlVoiceGender.MALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    # save audio content to temporary file
    extNo = str(R.randrange(0, 101, 2))   
    fileName = os.path.dirname(__file__) +  "\\temp" + extNo + ".mp3"
    #print('fileName ', fileName )
    with open(fileName, "wb") as f:
        f.write(response.audio_content)

    # play temporary file
    playsound.playsound(fileName)

    # delete temporary file
    os.remove(fileName)

# example usage
text_input = Q.WELCOME_SPEECH
generate_and_play_speech(text_input)
