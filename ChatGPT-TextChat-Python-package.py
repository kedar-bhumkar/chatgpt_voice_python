import openai

import Text_To_Speech_Google as TTS
import Speech_recognizer as SR
import Constants as Q

#print('CHATGPT_PERSONALITY_MODE - ' , Q.CHATGPT_PERSONALITY_MODE)

messages = [
    Q.CHATGPT_SYSTEM_SETTINGS[Q.CHATGPT_PERSONALITY_MODE]
]
temperature = 0.1 if Q.CHATGPT_CREATIVITY_THRESHOLD == 'Low' else 0.5 if Q.CHATGPT_CREATIVITY_THRESHOLD == 'Medium' else 1.0


openai.api_key = Q.OPENAI_KEY

     
while True:
    
    message = input("\nUser : Press Enter for mic input")
    message = SR.transcribeAudio()
    #print ('transcribed text ', message )
    if message !='':
        messages.append({"role": "user", "content": message})
        #print('Set temperature =', temperature)
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", temperature = temperature, messages=messages)
    
    reply = chat.choices[0].message.content
    print("ChatGPT:")
    TTS.generate_and_play_speech(reply)
    messages.append({"role": "assistant", "content": reply})
          

