from gtts import gTTS
import playsound
import os

def speak(text):
    print('cosmic: '+ text)
    #chuyển text thành văn bản qua API của google
    tts = gTTS(text=text, lang='vi', slow=False)
    #sau khi gửi âm thanh về lưu lại dưới tên sound.mp3
    tts.save('sound.mp3')
    #phát file sound.mp3
    playsound.playsound('sound.mp3', True)
    #xóa file sound.mp3
    os.remove('sound.mp3')
