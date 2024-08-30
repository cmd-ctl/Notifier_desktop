from tkinter import *
from tkinter import ttk
import threading
from datetime import datetime
import tkinter.messagebox as mb

# ----- tkinter interface -----
window = Tk()
window.wm_geometry("400x480")


HiTitle = (ttk.Label(window, text="Setup your notification"))
HiTitle.pack(side=TOP, pady=10)

ttk.Separator().pack(fill=X)

ntl = ttk.Label(window, text="Enter notification text")
ntl.pack(pady=10)
textField = Text(width=30, height=5)
textField.pack(pady=5)

ntml = ttk.Label(window, text="Enter the time to start\n(YYYY, MM, DD, HH, MM)")
ntml.pack(pady=10)
timeField = Entry(width=25)
timeField.pack(pady=5)

ttk.Button(window, text="Save", command=lambda: notification()).pack(pady=10)
ttk.Button(window, text="Exit", command=window.destroy).pack(padx=10, pady=5)

ttk.Separator().pack(fill=X)

textNote = Text(width=40, height=5)
textNote.pack(pady=5)


# ----- time count logic -----
def notification():
    t = threading.Thread(target=timeWait)   # start thread counting in background
    t.start()

def timeWait():
    try:
        text = textField.get(1.0, END)   # taking text data
        time = timeField.get()                  # taking time data
        textField.delete(1.0, END)        # clear text field

        takeTime = datetime.strptime(time, '%Y, %m, %d, %H, %M')  # time from input to vulnerable
        tf = takeTime.strftime("%Y-%m-%d %H:%M:%S")                       # format time
        tn = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if tf <= tn:
            mb.showerror("Ошибка", "Неверно указано время:\nУкажите дату в будущем")

        else:
            while True:             # start waiting loop
                tn = datetime.now().strftime("%Y-%m-%d %H:%M:%S")       # take current time
                if tf == tn:   # check if time-field time == current time -> do smth
                    textNote.insert(1.0, "Notification: \n Current time: " + str(tf) + " ---> " + text)   # insert text to 2nd field
                    print("Notification: \n Current time: " + str(tf) + " ---> " + text)          ## debug print
                    mb.showinfo("Информация", "Notification: \n Current time: " + str(tf) + " ---> " + text)   # pop-up notification
                    return True  # fin waiting loop

    except Exception as e:
        mb.showerror("Ошибка", str(e))

window.mainloop()