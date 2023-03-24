import speech_recognition as sr
import cryptocode
import pyodbc

recognizer = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    audio = recognizer.listen(source)

text = recognizer.recognize_ibm(audio, language = 'ES')

cryp = cryptocode.encrypt(text)
print(f'Has dicho: {cryp}')

uncryp = cryptocode.decrypt(cryp)
print(f'\nSin nada:  {uncryp}')

def validacion(cryp):
    if cryp == "hola":
        c = print("Acceso correcto")
        return c
    else:
        i = print("Acceso incorrecto")
        return i