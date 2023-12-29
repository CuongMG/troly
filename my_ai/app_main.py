from library import *

url = 'https://tro-ly-ao-c6d33-default-rtdb.firebaseio.com/.json'
json = {
  "esp_get": {
    "blue": 0,
    "yellow": 0
  }
}

def wiki_search(you):
    wikipedia.set_lang('Vi')
    try:
        info = wikipedia.summary(you).split('\n')
        speak(info[0].split('.')[0])
        for i in info[1:]:
            #speak('bạn có muốn nghe thêm không')
            return 'bạn có muốn nghe thêm không'
            ans = hear()
            if 'có' not in ans:
                break
            #speak(i)
            return i

        #speak('cảm ơn bạn đã lắng nghe, bạn muốn giúp gì khác không')
        return 'cảm ơn bạn đã lắng nghe, bạn muốn giúp gì khác không'
    except:
        #speak('mình không tìm được thông tin bạn nói, bạn cần gì khác không')
        return 'mình không tìm được thông tin bạn nói, bạn cần gì khác không'
def playgame():
    webbrowser.open('https://poki.com/')
    time.sleep(1)
    #speak('đây là 1 web chơi game trực tuyến')
    return 'đây là 1 web chơi game trực tuyến'

def now_day(you):
    if 'nhiệt độ' in you:
        response = requests.get(url=url)
        if response.status_code == 200:
            data = response.json()
            txt = data['esp_patch']['temperature']
            a = 'nhiệt độ là {} độ c'.format(txt)
            return a
    if 'độ ẩm' in you:
        response = requests.get(url=url)
        if response.status_code == 200:
            data = response.json()
            txt = data['esp_patch']['humidity']
            a = 'độ ẩm là {} phần trăm'.format(txt)
            return a
    now = datetime.datetime.now()
    if 'giờ' in you:
        h = now.strftime('%H h, %M phút, %S giây')
        #speak(h)
        return h
    else:
        return 'mình chưa nghe được bạn nói, bạn nói lại được không?'

    if 'ngày' in you:
        d = now.strftime('hôm nay là ngày %d, tháng %m, năm %Y')
        #speak(d)
        return d
    else:
        return 'mình chưa nghe được bạn nói, bạn nói lại được không?'

def open_web(you):
    if 'facebook' in you:
        webbrowser.open('https://www.facebook.com/')
        time.sleep(1)
        #speak('facebook đã được mở')
        return 'facebook đã được mở'
    if 'zalo' in you:
        webbrowser.open('https://chat.zalo.me/')
        time.sleep(1)
        #speak('zalo đã được mở')
        return 'zalo đã được mở'
    if 'youtube' in you:
        webbrowser.open('https://www.youtube.com/')
        time.sleep(1)
        #speak('youtube đã được mở')
        return 'youtube đã được mở'

#speak('xin chào mọi người mình là trợ lý ảo cosmic')

def main(you):

    while True:
#        global you
#        you = hear()


        if you == None:
            #speak('mình chưa nghe được bạn nói, bạn nói lại được không?')
            return 'mình chưa nghe được bạn nói, bạn nói lại được không?'
        elif 'xin chào' in you:
            #speak('chào bạn')
            return 'chào bạn'
        elif 'chủ tịch' in you and 'đầu tiên' in you and 'việt nam' in you:
            #speak('là chủ tịch hồ chí minh')
            return 'là chủ tịch hồ chí minh'
        elif 'con người' in you:
            speak('mình chỉ là một trợ lý ảo')
            return 'mình chỉ là một trợ lý ảo'
        elif 'tìm kiếm' in you and 'thông tin' in you:
            return wiki_search(you)
        elif 'mở' in you and 'word' in you:
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word')
        elif 'mở' in you:
            return open_web(you)
        elif 'giải trí' in you or 'game' in you:
            return playgame(you)
        elif 'hôm nay' in you or 'bây giờ' in you:
            return now_day(you)
        elif 'nhiệt độ' in you:
            response = requests.get(url=url)
            if response.status_code == 200:
                data = response.json()
                txt = data['esp_patch']['temperature']
                a = 'nhiệt độ là {} độ c'.format(txt)
                return a
        elif 'độ ẩm' in you:
            response = requests.get(url=url)
            if response.status_code == 200:
                data = response.json()
                txt = data['esp_patch']['humidity']
                a = 'độ ẩm là {} phần trăm'.format(txt)
                return a
        elif 'bật' in you:
            if 'xanh' in you:
                json['esp_get']['blue'] = 1
                content = requests.put(url=url, json=json)
                #speak('led xanh đã được bật')
                return 'led xanh đã được bật'
            else:
                return 'mình chưa nghe được bạn nói, bạn nói lại được không?'
            if 'vàng' in you:
                json['esp_get']['yellow'] = 1
                content = requests.put(url=url, json=json)
                #speak('led vàng đã được bật')
                return 'led vàng đã được bật'
            else:
                return 'mình chưa nghe được bạn nói, bạn nói lại được không?'
        elif 'tắt' in you:
            if 'xanh' in you:
                json['esp_get']['blue'] = 0
                content = requests.put(url=url, json=json)
                #speak('led xanh đã được tắt')
                return 'led xanh đã được tắt'
            else:
                return 'mình chưa nghe được bạn nói, bạn nói lại được không?'
            if 'vàng' in you:
                json['esp_get']['yellow'] = 0
                content = requests.put(url=url, json=json)
                #speak('led vàng đã được tắt')
                return 'led vàng đã được tắt'
            else:
                return 'mình chưa nghe được bạn nói, bạn nói lại được không?'
        elif 'tạm biệt' in you:
            #speak('hẹn gặp lại bạn sau')
            return 'hẹn gặp lại bạn sau'
            break
        else:
            return 'Xin lỗi, tôi không hiểu câu của bạn. Bạn có thể nói lại không?'

if __name__ == '__main__':
    main()