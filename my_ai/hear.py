#module hear
import speech_recognition as sr

def hear():
    print('dang nghe...')
    #lưu lại class Recognizer() vào biến r
    r = sr.Recognizer()
    #source = sr.Microphone()
    #mở một Microphone với tên source, sau khi tắt with as thì tắt Microphone
    with sr.Microphone() as source:
        print('toi: ', end='')
        #lưu lại câu nói của mình dưới file âm thanh
        audio = r.listen(source, phrase_time_limit=3)
        try:
            text = r.recognize_google(audio, language='vi-VN')
            print(text)
            return str(text).lower()
        except:
            return None
