import pyttsx3
import speech_recognition as sr
import Units.music as mp
import Units.weather as wt

wt.get_weather("Sevenoaks, GB", False)
#mp.play_anti_flag()

#settings = numpy.load()
#engine = pyttsx3.init()
#engine.say("Hello world!")
#engine.save_to_file("The quick brown fox jumped over the green bat. He was on fire.","out.wav")
#engine.runAndWait()

#r = sr.Recognizer()
#file = sr.AudioFile("out.wav")
#with file as source:
    #audio = r.record(source)
    #result = r.recognize_google(audio)
    #print(result)