import pyttsx3
import speech_recognition as sr
import Units.music as mp
import Units.weather as wt

A = wt.get_weather("London, GB")
print(f"At {A.hr_time_got} temp was {A.temp} C.")



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