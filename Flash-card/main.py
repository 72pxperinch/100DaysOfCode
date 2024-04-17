from tkinter import *
import pandas
import random
import os 

script_dir = os.path.dirname(__file__)
toLearn = os.path.join(script_dir, 'data/words_to_learn.csv')
fWords = os.path.join(script_dir, 'data/french_words.csv')
cardFront = os.path.join(script_dir, 'images/card_front.png')
cardBack = os.path.join(script_dir, 'images/card_back.png')
crossIMG = os.path.join(script_dir, 'images/wrong.png')
checkIMG = os.path.join(script_dir, 'images/right.png')


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pandas.read_csv(toLearn)
except FileNotFoundError:
    print("File 'data/words_to_learn.csv' not found. Reading from 'data/french_words.csv' instead.")
    original_data = pandas.read_csv(fWords)
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    print("File 'data/words_to_learn.csv' is empty. No data to parse.")
    original_data = pandas.read_csv(fWords)
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv(toLearn, index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file=cardFront)
card_back_img = PhotoImage(file=cardBack)
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file=crossIMG)
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file=checkIMG)
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()


