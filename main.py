import tkinter as tk
import random as rng

rng_sum = 0
statisticsWindowOpen = False

root = tk.Tk()
root.geometry("400x600")
root.title("Text and number editor")


# generates a random number between 1 and 99
def rng_generate():
    rng_number = rng.randint(1, 99)
    global rng_sum
    rng_sum = rng_sum + rng_number
    label_Text.set("The sum of the random numbers is: " + str(rng_sum))
    text_Window.insert(1.0, str(rng_number) + "\n")

# clears the text window
def text_clear():
    text_Window.delete(1.0, "end")

# printing the whats is in the text box on the commandline
def text_save():
    the_text = text_Window.get(1.0, "end")
    text_file = open("text_source.txt", "w")
    text_file.write(the_text)
    print("Text saved!")
    text_file.close()

def text_import():
    text_reading = open("text_source.txt", "r")
    text_Window.insert(1.0, text_reading.read())
    text_reading.close()

def rng_sum_set_to_0():
    global rng_sum
    rng_sum = 0
    label_Text.set("The sum of the random numbers is: " + str(rng_sum))

def extract_numbers():
    text_From_Window = text_Window.get(1.0, "end")
    print(text_From_Window)
    for symbol in text_From_Window:
        print(symbol, symbol.isdigit())

def statisticsWindow():
    global statisticsWindowOpen
    if statisticsWindowOpen == False:
        statisticsWindowOpen = True
        statisticsWindow = tk.Toplevel()
        statisticsWindow.title("Number statistics")
        statisticsWindow.geometry("400x400")
        statisticsWindow.protocol("WM_DELETE_WINDOW", lambda: statisticsWindowClosing(statisticsWindow))

def statisticsWindowClosing(win):
    global statisticsWindowOpen
    statisticsWindowOpen = False
    win.destroy()

label_Text = tk.StringVar()
label_Text.set("The sum of the random numbers will appear here.")
rng_Label = tk.Label(root, textvariable=label_Text)
rng_Label.pack()
rng_Button = tk.Button(root, text="Generate random numbers", command=rng_generate)
rng_Button.pack()

rng_Button_Clear = tk.Button(root, text="Clear the sum of the random numbers", command=rng_sum_set_to_0)
rng_Button_Clear.pack()

text_Window = tk.Text(root)
text_Window.pack()

clear_Button = tk.Button(text="Clear text", command=text_clear)
clear_Button.pack()

save_Button = tk.Button(text="Save text", command=text_save)
save_Button.pack()

import_Button = tk.Button(text="Import text", command=text_import)
import_Button.pack()

extract_Button = tk.Button(text="Extract numbers", command=extract_numbers)
extract_Button.pack()

statisticsButton = tk.Button(text="Number statistics", command=statisticsWindow)
statisticsButton.pack()

#soring out numbers from text
extracted_numbers = []

root.mainloop()
