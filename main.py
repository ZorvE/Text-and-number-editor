import tkinter as tk
import random as rng

rng_sum = 0

root = tk.Tk()
root.geometry("400x500")
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
def text_get():
    the_text = text_Window.get(1.0, "end")
    text_file = open("text_source.txt", "w")
    text_file.write(the_text)



label_Text = tk.StringVar()
label_Text.set("The sum of the random numbers will appear here.")
rng_Label = tk.Label(root, textvariable=label_Text)
rng_Label.pack()
rng_Button = tk.Button(root, text="Generate number", command=rng_generate)
rng_Button.pack()

text_Window = tk.Text(root)
text_Window.pack()

clear_Button = tk.Button(text="Clear text", command=text_clear)
clear_Button.pack()

get_Button = tk.Button(text="Get text", command=text_get)
get_Button.pack()

root.mainloop()
