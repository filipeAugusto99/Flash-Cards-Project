from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

flip_timer = None
current_card = {}
to_learn = {}

# Create New Flash Cards
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global flip_timer, current_card

    if flip_timer is not None:
        window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)

    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=current_card["French"])
    canvas.itemconfig(create_image, image=card_front_img)

    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=current_card["English"])
    canvas.itemconfig(create_image, image=card_back_img)


def is_known():
    global current_card
    to_learn.remove(current_card)

    data_save = pandas.DataFrame(to_learn)
    data_save.to_csv("data/words_to_learn.csv", index=False)

    next_card()


# UI SETUP
window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Create Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
create_image = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(
    400, 150,
    text="Title",
    font=("Arial", 40, "italic")
)

word_text = canvas.create_text(
    400, 263,
    text=f"word",
    font=("Arial", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# Create Buttons
# RIght Button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

# Wrong Button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
