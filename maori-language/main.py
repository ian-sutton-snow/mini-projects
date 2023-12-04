from tkinter import *

import pandas as pd
import random
import os.path

BACKGROUND_COLOR = "#B1DDC6"
SHOW_WORD_TIME = 2000
WORDS_TO_LEARN_FILE = "data/words_to_learn.csv"
# Load the language data
# If we have used this programme before then there may be a smaller set of words to learn
# as some we may have said that we already know
if os.path.exists(WORDS_TO_LEARN_FILE):
  language_data = pd.read_csv(WORDS_TO_LEARN_FILE)
else:
  language_data = pd.read_csv("data/maori_words.csv")
language_words = language_data.to_dict(orient="records")

current_card = {}
english_word = ''
maori_word = ''

def next_card():
    global current_card
    global english_word
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(language_words)
    maori_word = current_card["Maori"]
    english_word = current_card["English"]
    canvas.itemconfig(card_bg_image, image=card_front_image)
    canvas.itemconfig(card_title, text="Maori", fill="black")
    canvas.itemconfig(card_word,  text=maori_word, fill="black")
    flip_timer = window.after(SHOW_WORD_TIME, func=flip_card_to_show_english_word)

def flip_card_to_show_english_word():
    canvas.itemconfig(card_bg_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word,  text=english_word, fill="white")

def add_history_record(word_is_known):
    if not word_is_known:
        return
    # If we know this word then remove it from the language list so we don't keep asking it
    language_words.remove(current_card)
    print(len(language_words))

    # # Do we have any record for this word already? If so fetch it, if not then start one
    # history_record_for_word = history_record[maori_word]
    data = pd.DataFrame(language_words)
    data.to_csv(WORDS_TO_LEARN_FILE, index=False)

def word_is_known():
    add_history_record(word_is_known=True)
    next_card()

# def word_is_unknown():
# #    add_history_record(guess_was_correct=False)
#     next_card()

window = Tk()
window.title("Flash card language app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(SHOW_WORD_TIME, func=flip_card_to_show_english_word)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image  = PhotoImage(file="images/card_back.png")
card_bg_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word =  canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=1, columnspan=2)

correct_image = PhotoImage(file="images/right.png")
wrong_image   = PhotoImage(file="images/wrong.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=word_is_known)
wrong_button   = Button(image=wrong_image,   highlightthickness=0, command=next_card)

correct_button.grid(row=2, column=1)
wrong_button.grid(row=2, column=2)

next_card()
window.mainloop()