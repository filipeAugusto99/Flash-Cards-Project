from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"


# UI SETUP
window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Create Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_img)
canvas.grid(column=0, row=0, columnspan=2)


# Create Buttons
    # RIght Button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=1, row=1)

    # Wrong Button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)

# Texts Positions Labels
    # Language i want learn
language_want = Label(text="French", bg="white", font=('Arial', 40, 'italic'))
language_want.place(x=320, y=100)


    # text learn
text_learn = Label(text="trouve", bg="white", font=('Arial', 60, 'bold'))
text_learn.place(x=280, y=200)

window.mainloop()