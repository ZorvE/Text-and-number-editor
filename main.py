import tkinter as tk
import random as rng
import csv
import statistics

rng_sum = 0
statistics_window_open = False
extracted_numbers = []

root = tk.Tk()
root.geometry("400x600")
root.title("Text and number editor")

# generates a random number between 1 and 99
def rng_generate():
    rng_number = rng.randint(1, 99)
    global rng_sum
    rng_sum = rng_sum + rng_number
    label_text.set("The sum of the random numbers is: " + str(rng_sum))
    text_window.insert(1.0, str(rng_number) + "\n")

# clears the text window
def text_clear():
    text_window.delete(1.0, "end")

# printing the whats is in the text box on the commandline
def text_save():
    the_text = text_window.get(1.0, "end")
    text_file = open("text_source.txt", "w")
    text_file.write(the_text)
    print("Text saved!")
    text_file.close()

def text_import():
    text_reading = open("text_source.txt", "r")
    text_window.insert(1.0, text_reading.read())
    text_reading.close()

def rng_sum_set_to_0():
    global rng_sum
    rng_sum = 0
    label_text.set("The sum of the random numbers is: " + str(rng_sum))

def extract_numbers():
    text_from_window = text_window.get(1.0, "end")
    number_holder = ""
    for symbol in text_from_window:
        if symbol.isdigit():
            number_holder = number_holder + symbol
        else:
            if len(number_holder) > 0:
                extracted_numbers.append(int(number_holder))
                number_holder = ""
    number_file = open("number_source.scv", "w", newline="")
    writer = csv.writer(number_file)
    writer.writerow(extracted_numbers)
    number_file.close()

def statisticsWindow():
    global statistics_window_open
    if statistics_window_open == False:
        statistics_window_open = True
        statistics_window = tk.Toplevel()
        statistics_window.title("Number statistics")
        statistics_window.geometry("400x400")
        statistics_window.protocol("WM_DELETE_WINDOW", lambda: statisticsWindowClosing(statistics_window))

        number_reading = open("number_source.scv", "r")
        dummy = csv.reader(number_reading)
        number_list = list(dummy)
        inted_list = list(map(int, number_list[0]))

        median_text = tk.StringVar()
        median_text.set("The median value is " + str(round(statistics.median(inted_list))))
        median_label = tk.Label(statistics_window, textvariable=median_text)
        median_label.pack()
        mean_text = tk.StringVar()
        mean_text.set("The mean value is " + str(round(statistics.mean(inted_list))))
        mean_label = tk.Label(statistics_window, textvariable=mean_text)
        mean_label.pack()
        max_text = tk.StringVar()
        max_text.set("The highest value is " + str(max(inted_list)))
        max_label = tk.Label(statistics_window, textvariable=max_text)
        max_label.pack()
        low_text = tk.StringVar()
        low_text.set("The lowest value is " + str(min(inted_list)))
        low_label = tk.Label(statistics_window, textvariable=low_text)
        low_label.pack()

        number_reading.close()

def statisticsWindowClosing(win):
    global statistics_window_open
    statistics_window_open = False
    win.destroy()

label_text = tk.StringVar()
label_text.set("The sum of the random numbers will appear here.")
rng_label = tk.Label(root, textvariable=label_text)
rng_label.pack()
rng_button = tk.Button(root, text="Generate random numbers", command=rng_generate)
rng_button.pack()

rng_button_clear = tk.Button(root, text="Clear the sum of the random numbers", command=rng_sum_set_to_0)
rng_button_clear.pack()

text_window = tk.Text(root)
text_window.pack()

clear_button = tk.Button(text="Clear text", command=text_clear)
clear_button.pack()

save_button = tk.Button(text="Save text", command=text_save)
save_button.pack()

import_button = tk.Button(text="Import text", command=text_import)
import_button.pack()

extract_button = tk.Button(text="Extract numbers", command=extract_numbers)
extract_button.pack()

statistics_button = tk.Button(text="Number statistics", command=statisticsWindow)
statistics_button.pack()

root.mainloop()
