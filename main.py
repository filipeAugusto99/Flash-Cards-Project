from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

def generate_random_word(list):
    list_of_words_for_learning = []

    for word in list:
        list_of_words_for_learning.append(word["French"])

    choice_a_word = random.choice(list_of_words_for_learning)

    return choice_a_word

def random_word():
    canvas.itemconfig(word_text, text=f"{generate_random_word(list_of_dict)}")


# Create New Flash Cards
data = pandas.read_csv("data/french_words.csv")

list_of_dict = data.to_dict(orient='records')


# UI SETUP
window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Create Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(
    400, 150,
    text="French",
    font=("Arial", 40, "italic")
)

word_text = canvas.create_text(
    400, 263,
    text=f"{generate_random_word(list_of_dict)}",
    font=("Arial", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)


# Create Buttons
    # RIght Button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=random_word)
right_button.grid(column=1, row=1)

    # Wrong Button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=random_word)
wrong_button.grid(column=0, row=1)


window.mainloop()