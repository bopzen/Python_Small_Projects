import tkinter as tk
from tkinter import messagebox
import threading
import time
import datetime
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from subprocess import CREATE_NO_WINDOW


def record():
    def job():
        global counter
        while True:
            try:
                driver.get("http://WEBSITE")
                element = driver.find_element(By.ID, "ELEMENT ID")
                element.click()

                text_box.insert(tk.END, f'Recording Data {counter} of {record_counter}...\n')
                text_box.see('end')

                wait = WebDriverWait(driver, 30)
                element_text = wait.until(EC.visibility_of_element_located((By.XPATH, 'XPATH')))
                data = element_text.text

                now = datetime.datetime.now()
                message = 'Data ' + now.strftime("%Y-%m-%d %H:%M:%S" + ': ' + data)
                text_box.insert(tk.END, f'{message}\n')
                text_box.see('end')

                file.write(message + "\n")
                counter += 1
            except:
                text_box.insert(tk.END, 'Recording failed. Trying again...\n')
                text_box.see('end')
                continue
            break

    global counter

    button_start.config(relief='sunken')
    text_box.insert(tk.END, '*** STARTING DATA RECORDER ***\n')
    text_box.see('end')

    record_interval = int(entry_interval.get())
    record_hours = float(entry_duration.get())
    record_minutes = int(record_hours * 60)
    record_counter = record_minutes // record_interval
    text_box.insert(tk.END, f'Record interval in minutes: {record_interval}\n')
    text_box.see('end')
    if record_hours % 1 == 0:
        text_box.insert(tk.END, f'Record duration in hours: {int(record_hours)}\n')
    else:
        text_box.insert(tk.END, f'Record duration in hours: {record_hours:.2f}\n')
    text_box.see('end')
    text_box.insert(tk.END, f'{record_counter} records will be saved in the file.\n\n')
    text_box.see('end')

    file_name = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_') + 'data.txt'
    text_box.insert(tk.END, f'Opening file {file_name}\n')
    text_box.see('end')
    file = open(file_name, 'w')

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_service = ChromeService('chromedriver')
    chrome_service.creationflags = CREATE_NO_WINDOW
    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)

    text_box.insert(tk.END, 'Opening website in the background...\n')
    text_box.see('end')
    text_box.insert(tk.END, 'Recording session will start soon...\n')
    text_box.see('end')

    counter = 1
    job()
    schedule.every(record_interval).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
        if counter > record_counter:
            break
        if not running:
            text_box.insert(tk.END, '\n*** PROCESS STOPPED MANUALLY! ***\nPlease restart the tool if you want to run a new record session.\n')
            text_box.see('end')
            break

    text_box.insert(tk.END, f'\nRecording finished and data saved in file {file_name}!\n')
    text_box.see('end')
    button_stop.config(relief='raised')
    tk.messagebox.showinfo('Message', f'Recording finished and data saved in file {file_name}')

    time.sleep(1)
    file.close()


def stop_record():
    global running
    button_start.config(relief='raised')
    button_stop.config(relief='sunken')
    text_box.insert(tk.END, 'Stopping the process, please wait...\n')
    text_box.see('end')
    running = False


running = True
counter = 1

window = tk.Tk()
window.title('Data Recorder')
window.geometry('425x525')
window.resizable(width=False,height=False)
window.iconbitmap(r'record.ico')

label_title = tk.Label(text='Data Recorder')
label_title.config(font=('Segoe UI', 18))
label_title.grid(row=1, column=1, padx=5, pady=5)

frame_input = tk.Frame()
label_interval = tk.Label(master=frame_input, text='Record Interval in Minutes')
label_interval.grid(row=2, column=1, padx=5, pady=5, sticky='w')
entry_interval = tk.Entry(master=frame_input)
entry_interval.grid(row=2, column=2, padx=5, pady=5)

label_duration = tk.Label(master=frame_input, text='Recording Duration in Hours')
label_duration.grid(row=3, column=1, padx=5, pady=5, sticky='w')
entry_duration = tk.Entry(master=frame_input)
entry_duration.grid(row=3, column=2, padx=5, pady=10)

frame_input.grid(row=2, column=1, padx=5, pady=10)

t = threading.Thread(target=record)
button_start = tk.Button(text='Start Recording', width=15, height=1, command=t.start)
button_start.grid(row=10, column=1, padx=5, pady=10)

button_stop = tk.Button(text='Stop', width=15, height=1, command=stop_record)
button_stop.grid(row=11, column=1, padx=5, pady=10)

frame_log = tk.Frame()
text_box = tk.Text(master=frame_log, width=67, height=20, font=('Segoe UI', 8))
text_box.grid(row=12, column=1, padx=5, pady=10)

frame_log.grid(row=12, column=1, padx=5, pady=10)

window.mainloop()
