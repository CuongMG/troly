import sys
import tkinter as tk
from tkinter.font import Font
from PIL import Image, ImageTk
from tkinter import ttk
from threading import Thread
from hear import *
from app_main import *
import threading
from uart import *


root = tk.Tk()
root.title('virtual assistant')
root.attributes('-topmost', True)

root.resizable(width=False, height=False)


def finish():

    exit_event.set()
    root.quit()

    time.sleep(1) # wait for other threads

    sys.exit()
def update_data():
  data = get_h_t()

  cosmic_temper.config(text=f"{data[0]}\u00B0C")
  cosmic_humi.config(text=f"{data[1]}\u0025")

  root.after(1000, update_data) # gọi lại sau 1s
def cosmic_hear_def():
    speak('xin chào mọi người mình là trợ lý ảo cosmic')
    #while True:  # Lắng nghe liên tục
    while not exit_event.is_set():
        """global exit_event
        if exit_event.is_set():
            return"""

        ans = hear()
        if ans == None:
            result = 'mình chưa nghe được bạn nói, bạn nói lại được không?'
        if ans:
            root.after(0, cosmic_hear.delete, "1.0", tk.END)  # Xóa nội dung cũ
            root.after(0, cosmic_hear.insert, tk.END, ans)  # Chèn câu mới

            result = main(ans)  # Xử lý câu nói và trả về kết quả


            root.after(0, cosmic_speak.delete, "1.0", tk.END)  # Xóa nội dung cũ
            root.after(0, cosmic_speak.insert, tk.END, result)  # Chèn kết quả
        speak(result)
        if "tạm biệt" in ans:
            finish_thread.start()

        """if "tạm biệt" in ans:
            exit_event.set()

            #thread1.join()
            root.quit()

            listener_thread.join()
            sys.exit()"""
def listener():

    cosmic_hear_def()

exit_event = threading.Event()
#listener_thread = Thread(target=listener)
#listener_thread.start()
finish_thread = Thread(target=finish)

thread1 = Thread(target=cosmic_hear_def)
thread1.start()


app_width = 1000
app_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

my_font = Font(family='Brush Script MT', size=20, weight='bold', slant='italic')

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

img_load = Image.open(r"C:\Users\TieuCuong\OneDrive\Pictures\bg.jpg").resize([app_width, app_height],)
img = ImageTk.PhotoImage(image=img_load)

my_canvas = tk.Canvas(main_frame, width=app_width, height=app_height, bd=0, highlightthickness=0)
my_canvas.pack(fill=tk.BOTH, expand=True)
my_canvas.create_image(0, 0, image=img, anchor=tk.NW)

my_canvas.create_text(400, 50, text='Cosmic chatbot', font=('Helvetica', 40), fill='white')

my_canvas.create_text(150, 100, text='cosmic hear', font=my_font, fill='white')
my_canvas.create_text(150, 300, text='cosmic speak', font=my_font, fill='white')

my_canvas.create_text(850, 100, text='temperature', font=my_font, fill='white')
my_canvas.create_text(850, 300, text='humidity', font=my_font, fill='white')

ans = 'xin chào mọi người mình là trợ lý ảo cosmic'
cosmic_hear = tk.Text(main_frame, font=my_font, bd=0, wrap=tk.WORD)
cosmic_hear_text = my_canvas.create_window(100, 130, anchor=tk.NW, width=600, height=150, window=cosmic_hear)

cosmic_speak = tk.Text(main_frame, font=my_font, bd=0, wrap=tk.WORD)
cosmic_speak.insert(tk.END, ans)
cosmic_speak_text = my_canvas.create_window(100, 330, anchor=tk.NW, width=600, height=150, window=cosmic_speak)

cosmic_temper = tk.Label(main_frame, text='', width=10, font=my_font, bd=0)
#cosmic_temper.insert(tk.END, ans)
cosmic_temper_entry = my_canvas.create_window(775, 150, anchor=tk.NW, window=cosmic_temper)

cosmic_humi = tk.Label(main_frame, text='',  width=10, font=my_font, bd=0)
#cosmic_humi.insert(tk.END, ans)
cosmic_humi_entry = my_canvas.create_window(775, 350, anchor=tk.NW, window=cosmic_humi)

x_hear_scrollbar = ttk.Scrollbar(cosmic_hear, orient=tk.HORIZONTAL, command=my_canvas.xview)
x_hear_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
y_hear_scrollbar = ttk.Scrollbar(cosmic_hear, orient=tk.VERTICAL, command=my_canvas.yview)
y_hear_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

x_speak_scrollbar = ttk.Scrollbar(cosmic_speak, orient=tk.HORIZONTAL, command=my_canvas.xview)
x_speak_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
y_speak_scrollbar = ttk.Scrollbar(cosmic_speak, orient=tk.VERTICAL, command=my_canvas.yview)
y_speak_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


my_canvas.configure(xscrollcommand=x_hear_scrollbar.set, yscrollcommand=y_hear_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox(tk.ALL)))

my_canvas.configure(xscrollcommand=x_speak_scrollbar.set, yscrollcommand=y_speak_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox(tk.ALL)))

update_data()
root.mainloop()

