from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
card = {}
to_learn = {}
# ----------------------------------------------------------------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    origin_data = pandas.read_csv("data/korean_words.csv")
    to_learn = origin_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global card, flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(to_learn)
    canvas.itemconfig(title, text="Korean", fill="black")
    canvas.itemconfig(word, text=card["Korean"], fill="black")
    canvas.itemconfig(canvas_img, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=card["English"], fill="white")


def learned_word():
    to_learn.remove(card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


# ----------------------------- UI ---------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 270, image=front_img)

title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

image1 = PhotoImage(file="images/wrong.png")
image2 = PhotoImage(file="images/right.png")
wrong_button = Button(image=image1, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_button = Button(image=image2, highlightthickness=0, command=learned_word)
right_button.grid(row=1, column=1)
next_card()

window.mainloop()
