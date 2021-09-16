import speech_recognition as sr

r = sr.Recognizer()

audio = 'filename.wav'


with sr.AudioFile(audio) as source: 
    print ('say')

    audio = r.record(source)
    print('done')

try:
    text = r.recognizer_google(audio)
    print(text)


except Exception as e:
    print(e)