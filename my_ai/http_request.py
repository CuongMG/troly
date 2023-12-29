import requests

from library import *

url = 'https://tro-ly-ao-c6d33-default-rtdb.firebaseio.com/.json'
json = {
  "esp_get": {
    "blue": 0,
    "yellow": 0
  }
}

def wiki_search():
    wikipedia.set_lang('Vi')
    try:
        info = wikipedia.summary(you).split('\n')
        speak(info[0].split('.')[0])
        for i in info[1:]:
            speak('bạn có muốn nghe thêm không')
            ans = hear()
            if 'có' not in ans:
                break
            speak(i)

        speak('cảm ơn bạn đã lắng nghe, bạn muốn giúp gì khác không')
    except:
        speak('mình không tìm được thông tin bạn nói, bạn cần gì khác không')
def playgame():
    webbrowser.open('https://poki.com/')
    time.sleep(1)
    speak('đây là 1 web chơi game trực tuyến')

def now_day():
    now = datetime.datetime.now()
    if 'giờ' in you:
        h = now.strftime('%H h, %M phút, %S giây')
        speak(h)
    if 'ngày' in you:
        d = now.strftime('hôm nay là ngày %d, tháng %m, năm %Y')
        speak(d)
def open_web():
    if 'facebook' in you:
        webbrowser.open('https://www.facebook.com/')
        time.sleep(1)
        speak('facebook đã được mở')
    if 'zalo' in you:
        webbrowser.open('https://chat.zalo.me/')
        time.sleep(1)
        speak('zalo đã được mở')
    if 'youtube' in you:
        webbrowser.open('https://www.youtube.com/')
        time.sleep(1)
        speak('youtube đã được mở')

speak('xin chào mọi người mình là trợ lý ảo cosmic')

def main():
    while True:
        global you
        you = hear()

        if you == None:
            speak('mình chưa nghe được bạn nói, bạn nói lại được không?')
        elif 'xin chào' in you:
            speak('chào bạn')
        elif 'chủ tịch' in you and 'đầu tiên' in you and 'việt nam' in you:
            speak('là chủ tịch hồ chí minh')
        elif 'con người' in you:
            speak('mình chỉ là một trợ lý ảo')
        elif 'tìm kiếm' in you and  'thông tin' in you:
            wiki_search()
        elif 'mở' in you and 'word' in you:
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word')
        elif 'mở' in you:
            open_web()
        elif 'giải trí' in you or 'game' in you:
            playgame()
        elif 'hôm nay' in you or 'bây giờ' in you:
            now_day()
        elif 'nhiệt độ' in you:
            response = requests.get(url=url)
            if response.status_code == 200:
                data = response.json()
                txt = data['esp_patch']['temperature']
                speak(f'nhiệt độ là {txt} độ c')
        elif 'độ ẩm' in you:
            response = requests.get(url=url)
            if response.status_code == 200:
                data = response.json()
                txt = data['esp_patch']['humidity']
                speak(f'độ ẩm là {txt} phần trăm')
        elif 'bật' in you:
            if 'xanh' in you:
                json['esp_get']['blue'] = 1
                content = requests.patch(url=url, json=json)
                speak('led xanh đã được bật')
            if 'vàng' in you:
                json['esp_get']['yellow'] = 1
                content = requests.patch(url=url, json=json)
                speak('led vàng đã được bật')
        elif 'tắt' in you:
            if 'xanh' in you:
                json['esp_get']['blue'] = 0
                content = requests.patch(url=url, json=json)
                speak('led xanh đã được tắt')
            if 'vàng' in you:
                json['esp_get']['yellow'] = 0
                content = requests.patch(url=url, json=json)
                speak('led vàng đã được tắt')
        elif 'tạm biệt' in you:
            speak('hẹn gặp lại bạn sau')
            break

if __name__ == '__main__':
    main()