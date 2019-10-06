import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
    print(" Say anything ")
    audio=r.listen(source)
    print(" time over ")

try:
    print("text:"+r.recognize_google(audio))
    a=open("s.txt","a")
    a.write(r.recognize_google(audio))
    a.close()

except:
    pass
